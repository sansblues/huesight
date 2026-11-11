"""Scores the replies and compares every variation of a drawing with its original (thesis, Study Design, Analysis).

Run: uv run study/analyze.py <set>
Reads data/<set>/manifest.jsonl and data/<set>/replies/<model>.jsonl, and writes
data/<set>/results.md, data/<set>/parsed.csv (every reply with its parsed answer) and
data/<set>/replies_to_code.csv (every distinct reply text once, with how often it occurred).

For the pilot's parser check, copy replies_to_code.csv to hand_coding.csv and fill its hand_coded column
with yes, no, a number or invalid. Identical texts always get the same code, so coding each distinct text
once checks every reply. The script only reads hand_coding.csv, so rerunning it never loses the hand
coding, and results.md lists every disagreement with the parser.
"""

import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np

from generate import Bands, Distances, ImagePx, Limit, Tasks

Data = Path(__file__).resolve().parent.parent / "data"
# T1 to T3 ask about the colors and are analyzed together; T4, the control, asks about an edge and is
# analyzed on its own.
ColorTasks = ("T1", "T2", "T3")
TaskSets = {"color tasks": ColorTasks, "control": ("T4",)}
# Each recoloring comes with an edited twin in the same palette: the reassigned tab10 palette (52
# CIEDE2000 units between its closest colors) pairs with the original palette edited, and every
# close palette "d<distance>" with "d<distance>-edited".
Recolorings = ("reassigned",) + tuple(f"d{d}" for d in Distances)
Ladder = Recolorings[1:]  # the six controlled palettes, which the code calls the ladder
Conditions = ("original", "repeat") + tuple(c for r in Recolorings for c in (r, "edited" if r == "reassigned" else f"{r}-edited")) + ("no_image",)
Invalid = -1.0  # a reply without a valid answer line, or truncated: counts as wrong, and as a changed answer
Missing = math.nan  # no reply after all retries: the drawing drops out of comparisons that need it
# The three comparisons with the original at each distance: how many more answers a recoloring changes
# than a repeat of the original does, and the accuracy on the recolored and on the edited drawing minus
# the accuracy on the original.
Measures = ("answer change", "accuracy, recolored", "accuracy, edited")
Margin = 0.05  # H1: a recoloring changes fewer than this share of answers more than a repeat does
Resamples = 100_000
Seed = 0
Level = 0.05
# A bound this close to a threshold counts as touching it, so floating-point noise cannot decide a tie.
Tie = 1e-9
# The names of the models in the report, by the name of their replies file.
ModelNames = {"claude": "Claude Opus 5.5", "qwen": "Qwen3.8-27B", "gpt": "GPT-6.1 Sol", "gemini": "Gemini 3.8 Flash"}


def main():
    name = sys.argv[1] if len(sys.argv) == 2 else None
    folder = Data / str(name)
    if name is None or not (folder / "manifest.jsonl").exists():
        sys.exit("usage: uv run study/analyze.py pilot|main")
    items = [json.loads(line) for line in (folder / "manifest.jsonl").read_text().splitlines()]
    reply_files = sorted((folder / "replies").glob("*.jsonl"))
    if not reply_files:
        sys.exit(f"no replies in {folder / 'replies'}")
    sets = [s for s, tasks in TaskSets.items() if any(item["task"] in tasks for item in items)]
    tests = comparisons(len(reply_files), len(sets))
    report = [f"# Results: {name}", "", f"{len(items)} drawings. Differences are in percentage points (pp). Each has a 95% "
              f"interval and one corrected for the set's {tests} comparisons (models x task sets x distances x measures = "
              f"{len(reply_files)} x {len(sets)} x {len(Recolorings)} x {len(Measures)}): percentile intervals of "
              f"{Resamples:,} resamples of the drawings. Decisions use the corrected interval; the margin for answer "
              f"change is {Margin * 100:g} pp. The sign test is exact and two-sided; its corrected level is {Level / tests:.2g}.", ""]
    rows = []
    for path in reply_files:
        replies = first_replies(path)
        tables = answer_tables(items, replies)
        report += model_report(path.stem, tables, items, replies, tests)
        rows += parsed_rows(path.stem, items, replies)
    distinct = distinct_replies(rows)
    report += hand_coding_report(distinct, sum(r["reply"] is None for r in rows), folder / "hand_coding.csv")
    (folder / "results.md").write_text("\n".join(report) + "\n")
    write_csv(folder / "parsed.csv", rows)
    write_csv(folder / "replies_to_code.csv", distinct)
    print(f"wrote results.md, parsed.csv and replies_to_code.csv in {folder}")


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def score(task, reply):
    """The answer in a reply, or Invalid when the model did not finish normally (truncated or blocked)."""
    return parse(task, reply["text"]) if reply["stop"] == "done" else Invalid


def parse(task, text):
    """The answer in a reply's text, or Invalid. The answer must stand alone on the first or the last
    non-empty line, because models sometimes explain before or after it (seen in the pilot). If both
    lines hold answers that differ, or neither holds one, the reply is invalid."""
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if not lines:
        return Invalid
    answers = {parse_line(task, lines[0]), parse_line(task, lines[-1])} - {Invalid}
    return answers.pop() if len(answers) == 1 else Invalid


def parse_line(task, line):
    """Accepts only the requested form: "yes" or "no" for T1, T3 and T4, a whole number for T2. Ignores case,
    surrounding whitespace, asterisks on either side (markdown bold or italics, paired or not) and a
    final period inside and/or outside them."""
    answer = line.strip().removesuffix(".").strip().strip("*").strip().removesuffix(".").strip().lower()
    if task == "T2":
        return float(answer) if re.fullmatch(r"[0-9]+", answer) else Invalid
    return {"yes": 1.0, "no": 0.0}.get(answer, Invalid)


def first_replies(path):
    """query id -> the first successful reply; failed attempts are skipped."""
    replies = {}
    for line in path.read_text().splitlines():
        reply = json.loads(line)
        if reply["ok"] and reply["query_id"] not in replies:
            replies[reply["query_id"]] = reply
    return replies


def answer_tables(items, replies):
    """Per task of the set: the correct answers and each condition's parsed answers, one entry per item."""
    tables = {}
    for task in [t for t in Tasks if any(item["task"] == t for item in items)]:
        task_items = [item for item in items if item["task"] == task]
        answers = {}
        for condition in Conditions:
            values = []
            for item in task_items:
                reply = replies.get(f"{item['id']}-{condition}")
                values.append(Missing if reply is None else score(task, reply))
            answers[condition] = np.array(values)
        tables[task] = {
            "truth": np.array([encode(item["answer"]) for item in task_items]),
            "truth_edited": np.array([encode(item["edited_answer"]) for item in task_items]),
            "answers": answers,
        }
    return tables


def encode(answer):
    return {"yes": 1.0, "no": 0.0}.get(answer, answer) * 1.0


def edited_twin(recoloring):
    return "edited" if recoloring == "reassigned" else f"{recoloring}-edited"


def is_edited(condition):
    return condition == "edited" or condition.endswith("-edited")


def comparisons(models, task_sets):
    """How many comparisons with the original a set makes: the family of the Bonferroni correction."""
    return models * task_sets * len(Recolorings) * len(Measures)


def differences(table):
    """Per comparison with the original, one value per drawing: the drawing's outcome on the variation
    minus its outcome on the original; NaN where a needed reply is missing.

    Answer change, r: 1 if the answer to the recolored drawing differs from the answer to the original,
    minus 1 if the answer to the repeat does. Accuracy, c: 1 if the answer to the variation c is correct,
    minus 1 if the answer to the original is."""
    a = table["answers"]

    def changed(condition):
        other = a[condition]
        differs = (a["original"] != other) | (a["original"] == Invalid) | (other == Invalid)
        return np.where(np.isnan(a["original"]) | np.isnan(other), np.nan, differs * 1.0)

    original = accuracy_values(table, "original")
    values = {}
    for r in Recolorings:
        values[f"answer change, {r}"] = changed(r) - changed("repeat")
        values[f"accuracy, recolored, {r}"] = accuracy_values(table, r) - original
        values[f"accuracy, edited, {r}"] = accuracy_values(table, edited_twin(r)) - original
    return values


def bootstrap(per_task, resamples=Resamples, seed=Seed):
    """The mean of each comparison over the drawings of the given tasks, and its bootstrap distribution.

    per_task holds, for each task, the output of differences. Each resample draws every task's drawings
    with replacement, as many as the task has, so a resample keeps the study's number of drawings per task.
    All comparisons share the resampled drawings. A drawing without a value for a comparison (a missing
    reply) is left out of that comparison's mean, in the estimate and in every resample.
    Returns name -> (estimate, number of drawings, resample means)."""
    names = list(per_task[0])
    values = np.concatenate([np.column_stack([task[name] for name in names]) for task in per_task])
    known = ~np.isnan(values)
    filled = np.where(known, values, 0.0)
    sizes = [len(next(iter(task.values()))) for task in per_task]
    rng = np.random.default_rng(seed)
    means = []
    chunk = 10_000
    for start in range(0, resamples, chunk):
        size = min(chunk, resamples - start)
        rows = np.arange(size)[:, None]
        # How often each drawing occurs in each resample: n draws with replacement among a task's n drawings.
        counts = np.concatenate([np.bincount((rng.integers(0, n, (size, n)) + rows * n).ravel(), minlength=size * n).reshape(size, n)
                                 for n in sizes], axis=1).astype(float)
        means.append((counts @ filled) / (counts @ known))
    means = np.concatenate(means)
    return {name: (float(filled[:, i].sum() / known[:, i].sum()), int(known[:, i].sum()), means[:, i])
            for i, name in enumerate(names)}


def interval(means, level=Level):
    """The percentile interval of a bootstrap distribution: the range that leaves out level / 2 of the
    resample means on each side. The bounds are resample means, never interpolated between two of them, so
    an interval never excludes a value that the stated share of resamples reached."""
    return (float(np.quantile(means, level / 2, method="lower")), float(np.quantile(means, 1 - level / 2, method="higher")))


def decision(name, low, high, margin=Margin):
    """What a comparison's corrected interval says. Answer change (H1): supported if the interval lies
    below the margin, rejected if it lies above, inconclusive otherwise. Accuracy (H2): a drop if the
    interval lies below zero, a rise if above, no change otherwise. A bound at the threshold touches it."""
    if name.startswith("answer change"):
        return "supported" if high < margin - Tie else "rejected" if low > margin + Tie else "inconclusive"
    return "drop" if high < -Tie else "rise" if low > Tie else "no change"


def sign_test(values):
    """The exact two-sided sign test of no difference: among the drawings whose value is not zero, how
    likely a split at least as uneven as the observed one is if each were as likely positive as negative.
    It checks a decision that rests on few drawings, where percentile intervals are too narrow."""
    values = values[~np.isnan(values)]
    up, down = int((values > 0).sum()), int((values < 0).sum())
    n, k = up + down, min(up, down)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n) if n else 1.0


def analyze_tasks(tables, tasks, tests, margin=Margin):
    """Every comparison of one task set: name -> its estimate, number of drawings, 95% interval,
    interval corrected for `tests` comparisons (Bonferroni), decision, bootstrap distribution, and
    whether the exact sign test also finds a difference at the corrected level."""
    per_task = [differences(tables[task]) for task in tasks]
    results = {}
    for name, (estimate, n, means) in bootstrap(per_task).items():
        corrected = interval(means, Level / tests)
        p = sign_test(np.concatenate([task[name] for task in per_task]))
        results[name] = {"estimate": estimate, "n": n, "interval": interval(means), "corrected": corrected,
                         "decision": decision(name, *corrected, margin), "means": means,
                         "sign test": p, "sign test agrees": p < Level / tests}
    return results


def baseline_check(tables, items):
    """Per task: accuracy on the original and without the image, the gain with its 95% interval, and the
    bar, the accuracy reachable without reading what the task asks about. The bar is the share of the most
    common correct answer; in T3 it is at least the accuracy of answering from the edges alone
    (structure_only_accuracy), and in T4 that of answering from the positions alone (proximity_only_accuracy)."""
    rows = {}
    for task, table in tables.items():
        truth = table["truth"]
        bar = max(Counter(truth.tolist()).values()) / len(truth)
        if task == "T3":
            bar = max(bar, structure_only_accuracy([item for item in items if item["task"] == "T3"]))
        if task == "T4":
            bar = max(bar, proximity_only_accuracy([item for item in items if item["task"] == "T4"]))
        original, blind_correct = accuracy_values(table, "original"), accuracy_values(table, "no_image")
        gain, n, means = bootstrap([{"gain": original - blind_correct}])["gain"] if (~np.isnan(blind_correct)).any() else (math.nan, 0, None)
        blind = table["answers"]["no_image"]
        blind = blind[~np.isnan(blind)]
        rows[task] = {"original": float(np.nanmean(original)),
                      "no image": float(np.nanmean(blind_correct)) if len(blind) else math.nan,
                      "gain": (gain, *interval(means)) if n else (math.nan,) * 3, "n": n, "bar": bar,
                      "invalid without image": (int((blind == Invalid).sum()), len(blind))}
    return rows


def structure_only_accuracy(t3_items):
    """The share of T3 items a reader blind to color answers correctly by saying yes exactly when u has two
    or more neighbors: in the generated items, u's degree is not independent of the answer."""
    hits = 0
    for item in t3_items:
        degree = sum(item["u"] in edge for edge in item["edge_list"])
        hits += (degree >= 2) == (item["answer"] == "yes")
    return hits / len(t3_items)


def proximity_only_accuracy(t4_items):
    """The share of T4 items a reader blind to edges answers correctly by saying yes exactly when u and v
    are closer than some cutoff, with the best cutoff for these items: nodes joined by an edge sit closer."""
    distances = [(math.dist(item["positions"][item["u"]], item["positions"][item["v"]]), item["answer"] == "yes")
                 for item in t4_items]
    return max(sum((d <= cutoff) == joined for d, joined in distances) for cutoff, _ in distances) / len(distances)


def model_report(model, tables, items, replies, tests):
    tokens = [r["output_tokens"] for r in replies.values() if r.get("output_tokens") is not None]
    lines = [f"## {ModelNames.get(model, model)}", ""]
    if tokens:
        lines += [f"Output tokens per reply, reasoning included: mean {np.mean(tokens):.0f}, median {np.median(tokens):.0f}.", ""]
    lines += [f"Answers changed on the repeat: {pct(float(np.mean([repeat_flips(t) for t in tables.values()])))} (mean over tasks).", "",
              "### Baseline check", "",
              "| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |",
              "| --- | --- | --- | --- | --- | --- |"]
    for task, row in baseline_check(tables, items).items():
        invalid, asked = row["invalid without image"]
        gain, low, high = row["gain"]
        lines.append(f"| {task} | {pct(row['original'])} | {pct(row['no image'])} | {points(gain)} [{points(low)}, {points(high)}], "
                     f"n = {row['n']} | {pct(row['bar'])} | {invalid} of {asked} |")
    lines += ["", "Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.", ""]
    sets = {name: analyze_tasks(tables, tasks, tests) for name, tasks in TaskSets.items() if all(t in tables for t in tasks)}
    for name, results in sets.items():
        lines += comparison_tables(f"{name.capitalize()} ({', '.join(TaskSets[name])})", results)
    for task in tables:
        lines += comparison_tables(f"{task} alone (descriptive)", analyze_tasks(tables, (task,), tests), decisions=False)
    lines += other_margins(sets) + missing_as_wrong(tables, sets, tests)
    lines += default_answers(tables) + invalid_kinds(items, replies) + yes_rates(tables)
    lines += error_directions(tables) + ["### Accuracy per condition and task", "",
              "| Condition | " + " | ".join(tables) + " |", "| --- |" + " --- |" * len(tables)]
    for condition in Conditions:
        lines.append(f"| {condition} | " + " | ".join(accuracy_cell(table, condition) for table in tables.values()) + " |")
    lines += ["", "Cells: accuracy, then invalid and missing replies.", ""]
    lines += hue_analysis(tables, items) + middle_color_analysis(tables, items)
    lines += spatial_analysis(tables, items) + error_analysis(tables, items) + token_analysis(items, replies)
    return lines + (shared_color_analysis(tables, items) if "T4" in tables else [])


def comparison_tables(title, results, decisions=True):
    """One table per measure: a row per distance with the estimate, its 95% interval and, where the
    comparison decides something, the corrected interval, the decision and the exact sign test's p."""
    lines = [f"### {title}", ""]
    for measure in Measures:
        lines += [f"| {measure.capitalize()} | Difference (pp) | 95% interval |" + (" Corrected interval | Decision | Sign test p |" if decisions else "") + " n |",
                  "| --- | --- | --- |" + (" --- | --- | --- |" if decisions else "") + " --- |"]
        for r in Recolorings:
            row = results[f"{measure}, {r}"]
            cells = [points(row["estimate"]), span(row["interval"])] + ([span(row["corrected"]), row["decision"], f"{row['sign test']:.2g}"] if decisions else [])
            lines.append(f"| {distance_name(r)} | " + " | ".join(cells) + f" | {row['n']} |")
        lines.append("")
    return lines


def other_margins(sets):
    """Descriptive: H1 under other margins than the study's, read off the same corrected intervals."""
    lines = ["### H1 under other margins (descriptive)", "",
             "| Task set | Margin | " + " | ".join(distance_name(r) for r in Recolorings) + " |", "| --- | --- |" + " --- |" * len(Recolorings)]
    for name, results in sets.items():
        for margin in (0.025, 0.05, 0.10):
            cells = [decision("answer change", *results[f"answer change, {r}"]["corrected"], margin) for r in Recolorings]
            lines.append(f"| {name} | {margin * 100:g} pp | " + " | ".join(cells) + " |")
    return lines + [""]


def missing_as_wrong(tables, sets, tests):
    """Sensitivity: the decisions that change when every missing reply counts as invalid, so as wrong and
    as a changed answer, instead of dropping its drawing from the comparison."""
    missing = sum(int(np.isnan(a).sum()) for table in tables.values() for a in table["answers"].values())
    if not missing:
        return []
    worst = {task: {**table, "answers": {c: np.where(np.isnan(a), Invalid, a) for c, a in table["answers"].items()}}
             for task, table in tables.items()}
    changed = []
    for name, before in sets.items():
        after = analyze_tasks(worst, TaskSets[name], tests)
        changed += [f"- {name}, {key}: {before[key]['decision']} becomes {after[key]['decision']} "
                    f"({points(after[key]['estimate'])} {span(after[key]['corrected'])})"
                    for key in before if before[key]["decision"] != after[key]["decision"]]
    return ["### Missing replies counted as wrong and as changed answers (sensitivity)", "",
            f"{missing} replies are missing. " + ("Decisions that change:" if changed else "No decision changes."), "", *changed, ""]


def distance_name(recoloring):
    return "52 (reassigned)" if recoloring == "reassigned" else recoloring.removeprefix("d")


def points(share):
    """A difference of two shares in percentage points, without a negative zero."""
    text = f"{100 * share:.1f}"
    return "-" if math.isnan(share) else text.lstrip("-") if float(text) == 0 else text


def span(bounds):
    return f"[{points(bounds[0])}, {points(bounds[1])}]"


def invalid_kinds(items, replies):
    """Descriptive: invalid replies by kind, with and without the image: truncated, blocked, or a finished
    reply with no answer line (which, without the image, is mostly a request for the image)."""
    counts = {"with image": Counter(), "without image": Counter()}
    for item in items:
        for condition in Conditions:
            reply = replies.get(f"{item['id']}-{condition}")
            if reply is None or score(item["task"], reply) != Invalid:
                continue
            kind = {"truncated": "truncated", "blocked": "blocked"}.get(reply["stop"], "no answer line")
            counts["without image" if condition == "no_image" else "with image"][kind] += 1
    lines = ["### Invalid replies by kind (descriptive)", "",
             "| Drawing | No answer line | Truncated | Blocked |", "| --- | --- | --- | --- |"]
    for where, c in counts.items():
        lines.append(f"| {where} | {c['no answer line']} | {c['truncated']} | {c['blocked']} |")
    return lines + [""]


def yes_rates(tables):
    """Descriptive: in T1 and T3, on the ladder palettes, how often the model says yes when the correct
    answer is yes (hits) and when it is no (false alarms), recolored and edited drawings together. Reading
    two colors as one raises false alarms only; a general tendency to say yes raises both."""
    lines = ["### Yes answers by correct answer on the controlled palettes (descriptive)", "",
             "| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |", "| --- | --- | --- | --- | --- |"]
    for r in Ladder:
        cells = []
        for task in ("T1", "T3"):
            answers = np.concatenate([tables[task]["answers"][r], tables[task]["answers"][edited_twin(r)]])
            truths = np.concatenate([tables[task]["truth"], tables[task]["truth_edited"]])
            valid = ~np.isnan(answers) & (answers != Invalid)
            for target in (1.0, 0.0):
                chosen = valid & (truths == target)
                cells.append(pct(float((answers[chosen] == 1.0).mean())) if chosen.any() else "-")
        lines.append(f"| {r} | " + " | ".join(cells) + " |")
    return lines + ["", "Cells: share of valid answers that are yes.", ""]


def default_answers(tables):
    """Descriptive: the answers a model gives without the image, its default when it cannot see; a model
    that says yes by default could make false yes answers look like colors read as one."""
    lines = ["### Answers without the image (descriptive)", "",
             "| Task | Valid replies | Yes, or mean count |", "| --- | --- | --- |"]
    for task in tables:
        a = tables[task]["answers"]["no_image"]
        valid = a[~np.isnan(a) & (a != Invalid)]
        if len(valid) == 0:
            value = "-"
        elif task == "T2":
            value = f"{np.mean(valid):.1f}"
        else:
            value = pct(float(np.mean(valid)))
        lines.append(f"| {task} | {len(valid)} | {value} |")
    return lines + [""]


def error_directions(tables):
    """Exploratory: the direction of errors on the ladder, as a table (see error_direction_counts)."""
    lines = ["### Error directions on the controlled palettes (exploratory)", "",
             "| Recoloring | False yes or overcount | False no or undercount | Invalid |", "| --- | --- | --- | --- |"]
    for r, counts in error_direction_counts(tables).items():
        lines.append(f"| {r} | {counts['toward one color']} | {counts['toward two colors']} | {counts['invalid']} |")
    return lines + [""]


def error_direction_counts(tables, tasks=ColorTasks):
    """Per ladder recoloring, wrong answers on the recolored and edited drawings of the given tasks by
    direction. A false
    yes (T1, T3) or an overcount (T2) is consistent with two colors read as one ("toward one color"), a
    false no or an undercount with one color read as two. The direction is observed; the cause is not,
    since counting, label or edge errors can point the same way."""
    directions = {}
    for r in Ladder:
        counts = Counter()
        for task in tasks:
            for condition, target in ((r, tables[task]["truth"]), (edited_twin(r), tables[task]["truth_edited"])):
                a = tables[task]["answers"][condition]
                for answer, truth in zip(a, target):
                    if np.isnan(answer) or answer == truth:
                        continue
                    if answer == Invalid:
                        counts["invalid"] += 1
                    elif (task == "T2" and answer > truth) or (task != "T2" and truth == 0.0):
                        counts["toward one color"] += 1
                    else:
                        counts["toward two colors"] += 1
        directions[r] = counts
    return directions


def accuracy_values(table, condition):
    a = table["answers"][condition]
    target = table["truth_edited"] if is_edited(condition) else table["truth"]
    return np.where(np.isnan(a), np.nan, (a == target) * 1.0)


def repeat_flips(table):
    a = table["answers"]
    present = ~np.isnan(a["original"]) & ~np.isnan(a["repeat"])
    changed = (a["original"] != a["repeat"]) | (a["original"] == Invalid) | (a["repeat"] == Invalid)
    return float(changed[present].mean()) if present.any() else math.nan


def accuracy_cell(table, condition):
    values = accuracy_values(table, condition)
    a = table["answers"][condition]
    return f"{pct(float(np.nanmean(values)))} ({int((a == Invalid).sum())} inv, {int(np.isnan(a).sum())} miss)"


def hue_analysis(tables, items):
    """Exploratory: accuracy on each ladder distance by hue center, as a table (see hue_accuracy)."""
    lines = ["### Accuracy by base hue (exploratory)", "",
             "| Base hue | " + " | ".join(Ladder) + " |", "| --- |" + " --- |" * len(Ladder)]
    for center, row in hue_accuracy(tables, items).items():
        lines.append(f"| {center} | " + " | ".join(pct(row[r]) if row[r] is not None else "-" for r in Ladder) + " |")
    return lines + [""]


def hue_accuracy(tables, items):
    """Per hue center and ladder recoloring, accuracy pooling the recolored and the edited drawing (None
    without answers); the edit flips the answer, so each hue center gets yes and no answers equally often."""
    centers = sorted({item["hue_center"] for item in items})
    accuracy = {}
    for center in centers:
        accuracy[center] = {}
        for r in Ladder:
            values = []
            for task in ColorTasks:
                task_items = [item for item in items if item["task"] == task]
                for condition in (r, edited_twin(r)):
                    correct = accuracy_values(tables[task], condition)
                    values += [c for item, c in zip(task_items, correct) if item["hue_center"] == center and not np.isnan(c)]
            accuracy[center][r] = float(np.mean(values)) if values else None
    return accuracy


def middle_color_analysis(tables, items):
    """Exploratory: T2 accuracy on each ladder distance by u's color. The middle color of a ladder
    palette has an adjacent color on both sides, an outer color on one side only, so a model that
    confuses adjacent colors should miscount more often when u's color is the middle one."""
    task_items = [item for item in items if item["task"] == "T2"]
    middle = np.array([item["palette_position"][item["groups"][item["u"]]] == 1 for item in task_items])
    lines = ["### T2 accuracy by the position of u's color in the controlled palette (exploratory)", "",
             "| u's color | " + " | ".join(Ladder) + " | Items |", "| --- |" + " --- |" * (len(Ladder) + 1)]
    for name, rows in (("middle", middle), ("outer", ~middle)):
        cells = []
        for r in Ladder:
            values = np.concatenate([accuracy_values(tables["T2"], c)[rows] for c in (r, edited_twin(r))])
            cells.append(pct(float(np.nanmean(values))) if (~np.isnan(values)).any() else "-")
        lines.append(f"| {name} | " + " | ".join(cells) + f" | {int(rows.sum())} |")
    return lines + ["", "Each cell pools the recolored and the edited drawing.", ""]


def spatial_analysis(tables, items):
    """Exploratory: T1 accuracy by how far apart u and v sit in the drawing. For people, colors are
    harder to tell apart the farther apart they are (Brychtova and Coltekin, 2017). Counts only the T1
    drawings where u and v have adjacent, different colors: the plain drawing of a no item and the
    edited drawing of a yes item. Distances are in pixels, split into thirds."""
    task_items = [item for item in items if item["task"] == "T1"]
    scale = ImagePx / (2 * Limit)  # pixels per layout unit
    distance = np.array([math.dist(item["positions"][item["u"]], item["positions"][item["v"]]) * scale for item in task_items])
    cuts = np.quantile(distance, [1 / 3, 2 / 3])
    third = np.searchsorted(cuts, distance, side="right")
    no_item = tables["T1"]["truth"] == 0.0
    lines = ["### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)", "",
             "Drawings where u and v have adjacent, different colors of a controlled palette.", "",
             "| Distance between u and v | " + " | ".join(Ladder) + " | Items |", "| --- |" + " --- |" * (len(Ladder) + 1)]
    for k in range(3):
        rows = third == k
        cells = []
        for r in Ladder:
            plain = accuracy_values(tables["T1"], r)[rows & no_item]
            edited = accuracy_values(tables["T1"], edited_twin(r))[rows & ~no_item]
            values = np.concatenate([plain, edited])
            cells.append(pct(float(np.nanmean(values))) if (~np.isnan(values)).any() else "-")
        label = f"{distance[rows].min():.0f} to {distance[rows].max():.0f} px"
        lines.append(f"| {label} | " + " | ".join(cells) + f" | {int(rows.sum())} |")
    return lines + [""]


def error_analysis(tables, items):
    """Exploratory: accuracy on the ladder drawings (recolored and edited, every distance) by drawing
    features. On tab10 every model is near 100%, so failures show only on the ladder."""
    rows = []
    for task in ColorTasks:
        task_items = [item for item in items if item["task"] == task]
        ladder = np.array([accuracy_values(tables[task], c) for r in Ladder for c in (r, edited_twin(r))])
        for i, item in enumerate(task_items):
            values = ladder[:, i][~np.isnan(ladder[:, i])]
            rows.append({
                "task": task, "nodes": item["nodes"], "edge band": item["band"],
                "crossings": crossing_bin(item["crossings"]), "edited node degree": min(item["edited_node_degree"], 5),
                "accuracy": float(values.mean()) if len(values) else None,
            })
    lines = ["### Accuracy on the controlled palettes by properties of the drawing (exploratory)", ""]
    for factor in ("nodes", "edge band", "crossings", "edited node degree"):
        lines += [f"| {factor} | Accuracy | Items |", "| --- | --- | --- |"]
        # Bands in the generator's order; numbers by the leading one, so the crossing bins read 0, 1-2, 3-5, 6+.
        levels = Bands if factor == "edge band" else sorted({row[factor] for row in rows},
                                                            key=lambda level: int(re.match(r"\d+", str(level)).group()))
        for level in levels:
            group = [row["accuracy"] for row in rows if row[factor] == level and row["accuracy"] is not None]
            lines.append(f"| {level} | {pct(float(np.mean(group))) if group else '-'} | {len(group)} |")
        lines.append("")
    return lines


def token_analysis(items, replies):
    """Exploratory and correlational: accuracy on the ladder drawings (recolored and edited) by the
    reply's output tokens, reasoning included, in quartiles of this model's ladder replies. Harder
    drawings may draw longer reasoning, so this cannot show whether reasoning helps."""
    tokens, correct = [], []
    for item in (item for item in items if item["task"] in ColorTasks):
        for r in Ladder:
            for condition in (r, edited_twin(r)):
                reply = replies.get(f"{item['id']}-{condition}")
                if reply is None or reply.get("output_tokens") is None:
                    continue
                truth = encode(item["edited_answer"] if is_edited(condition) else item["answer"])
                tokens.append(reply["output_tokens"])
                correct.append(score(item["task"], reply) == truth)
    if not tokens:
        return []
    tokens, correct = np.array(tokens), np.array(correct)
    edges = np.quantile(tokens, [0, 0.25, 0.5, 0.75, 1])
    quartile = np.minimum(np.searchsorted(edges, tokens, side="right") - 1, 3)
    lines = ["### Accuracy on the controlled palettes by output tokens (exploratory)", "",
             "| Output tokens | Accuracy | Replies |", "| --- | --- | --- |"]
    for q in range(4):
        rows = quartile == q
        if rows.any():
            lines.append(f"| {tokens[rows].min()} to {tokens[rows].max()} | {pct(float(correct[rows].mean()))} | {int(rows.sum())} |")
    return lines + ["", "Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.", ""]


def shared_color_analysis(tables, items):
    """Exploratory: T4 yes answers by edge and shared color, as a table (see shared_color_rates)."""
    lines = ["### T4 yes answers by edge and shared color (exploratory)", "",
             "| Palette | No edge, shared color | No edge, other colors | Edge, shared color | Edge, other colors |",
             "| --- | --- | --- | --- | --- |"]
    for palette, rates in shared_color_rates(tables, items).items():
        lines.append(f"| {palette} | " + " | ".join("-" if rate is None else pct(rate) for rate in rates.values()) + " |")
    return lines + ["", "Cells: share of valid answers that are yes. tab10 pools the original, reassigned and edited drawings.", ""]


SharedCells = ((False, True), (False, False), (True, True), (True, False))  # (edge, shared color)


def shared_color_rates(tables, items):
    """Per palette, the share of valid T4 answers that are yes in each cell of SharedCells (None
    without answers). The edit switches whether u and v share a color, never the edge, so a model
    whose reading of edges follows the colors says yes more often when they share one."""
    task_items = [item for item in items if item["task"] == "T4"]
    shared = np.array([item["groups"][item["u"]] == item["groups"][item["v"]] for item in task_items])
    edge = tables["T4"]["truth"] == 1.0
    palettes = [("tab10", ("original", "reassigned", "edited"))] + [(r, (r, edited_twin(r))) for r in Ladder]
    rates = {}
    for name, conditions in palettes:
        answers = np.concatenate([tables["T4"]["answers"][c] for c in conditions])
        same = np.concatenate([shared != is_edited(c) for c in conditions])
        joined = np.tile(edge, len(conditions))
        valid = ~np.isnan(answers) & (answers != Invalid)
        rates[name] = {}
        for cell in SharedCells:
            chosen = valid & (joined == cell[0]) & (same == cell[1])
            rates[name][cell] = float((answers[chosen] == 1.0).mean()) if chosen.any() else None
    return rates


def crossing_bin(count):
    return "0" if count == 0 else "1-2" if count <= 2 else "3-5" if count <= 5 else "6+"


def pct(x):
    return "-" if isinstance(x, float) and math.isnan(x) else f"{100 * x:.1f}%"


def distinct_replies(rows):
    """Every distinct (task, stop, reply text) once, most frequent first, for hand coding."""
    counts = Counter((r["task"], r["stop"], r["reply"]) for r in rows if r["reply"] is not None)
    parsed = {(r["task"], r["stop"], r["reply"]): r["parsed"] for r in rows if r["reply"] is not None}
    return [{"task": task, "stop": stop, "reply": reply, "count": n, "parsed": parsed[(task, stop, reply)], "hand_coded": ""}
            for (task, stop, reply), n in sorted(counts.items(), key=lambda kv: (kv[0][0], -kv[1]))]


def hand_coding_report(distinct, missing, path):
    """Compares the hand coding in hand_coding.csv, if it exists, with the parser, text by text."""
    if not path.exists():
        return []
    with open(path, newline="") as f:
        coded = {(r["task"], r["stop"], r["reply"]): r["hand_coded"].strip().lower()
                 for r in csv.DictReader(f) if r["hand_coded"].strip()}
    parsed = {(r["task"], r["stop"], r["reply"]): r["parsed"] for r in distinct}
    uncoded = set(parsed) - set(coded)
    disagree = [key for key, value in coded.items() if key in parsed and hand_answer(value) != parsed[key]]
    passes = not uncoded and not disagree and not missing
    lines = ["## Parser against hand coding", "",
             f"{len(set(parsed) & set(coded))} of {len(parsed)} distinct replies hand coded, {len(uncoded)} not yet; "
             f"{len(disagree)} disagree with the parser; {missing} queries have no reply. "
             f"The parser check {'passes' if passes else 'does not pass yet'}.", ""]
    lines += [f"- {task}, {stop}: {reply[:80]!r}: hand coded {coded[(task, stop, reply)]}, parsed {parsed[(task, stop, reply)]}"
              for task, stop, reply in disagree]
    return lines + [""]


def hand_answer(value):
    """A hand-coded answer in the parser's encoding: yes, no, invalid or a number."""
    words = {"yes": 1.0, "no": 0.0, "invalid": Invalid}
    return words[value] if value in words else float(value)


def parsed_rows(model, items, replies):
    rows = []
    for item in items:
        for condition in Conditions:
            reply = replies.get(f"{item['id']}-{condition}")
            rows.append({
                "model": model, "query_id": f"{item['id']}-{condition}", "task": item["task"],
                "reply": None if reply is None else reply["text"],
                "stop": None if reply is None else reply["stop"],
                "parsed": None if reply is None else score(item["task"], reply),
            })
    return rows


if __name__ == "__main__":
    main()
