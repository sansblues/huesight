import json
import math

import numpy as np
import pytest

import analyze
import generate
from analyze import Invalid, Missing


def test_parse_accepts_only_the_requested_form():
    assert analyze.parse("T1", " Yes.\n") == 1.0
    assert analyze.parse("T3", "**no**") == 0.0
    assert analyze.parse("T2", "4") == 4.0
    assert analyze.parse("T2", "7.") == 7.0
    assert analyze.parse("T1", "**yes**.") == analyze.parse("T1", "**yes.**") == analyze.parse("T1", "**yes**") == 1.0
    assert analyze.parse("T1", "Yes, they do.") == Invalid


def test_parse_reads_an_answer_that_stands_alone_on_the_first_or_last_line():
    assert analyze.parse("T1", "B is blue and D is green, so they differ.\n\nNo") == 0.0
    assert analyze.parse("T2", "Orange nodes: D and C.\n\n**2**") == 2.0
    assert analyze.parse("T3", "No\n\nNode H is connected to E, G and A, none of which share its color.") == 0.0
    assert analyze.parse("T3", "Yes\n\nNode K is green, and so is G.\n\n**Yes**") == 1.0
    assert analyze.parse("T1", "Yes\n\nOn second thought:\n\nNo") == Invalid
    assert analyze.parse("T2", "Let me count.\n5\nThat is my answer.") == Invalid
    assert analyze.parse("T2", "four") == Invalid
    assert analyze.parse("T2", "yes") == Invalid
    assert analyze.parse("T1", "") == Invalid


def test_a_truncated_or_blocked_reply_is_invalid_whatever_its_text():
    assert analyze.score("T1", {"text": "yes", "stop": "done"}) == 1.0
    assert analyze.score("T1", {"text": "yes", "stop": "truncated"}) == Invalid
    assert analyze.score("T1", {"text": "yes", "stop": "blocked"}) == Invalid


def table(original, repeat, reassigned, edited, truth, truth_edited, **other):
    """Every recoloring answers like `reassigned` and every edited twin like `edited`, unless a condition
    is given by name in `other` (for example d10=[...])."""
    answers = {"original": original, "repeat": repeat, "no_image": [Missing] * len(truth)}
    for r in analyze.Recolorings:
        answers[r] = reassigned
        answers[analyze.edited_twin(r)] = edited
    answers.update({name.replace("_edited", "-edited"): values for name, values in other.items()})
    return {"truth": np.array(truth, float), "truth_edited": np.array(truth_edited, float),
            "answers": {c: np.array(v, float) for c, v in answers.items()}}


def test_an_invalid_reply_counts_as_a_changed_answer_even_against_another_invalid_reply():
    t = table(original=[Invalid, 1], repeat=[Invalid, 1], reassigned=[1, 1],
              edited=[0, 0], truth=[1, 1], truth_edited=[0, 0])
    # Drawing 1 changed under the recoloring and on the repeat, so the two cancel; drawing 2 changed in neither.
    assert analyze.differences(t)["answer change, reassigned"].tolist() == [0.0, 0.0]
    assert analyze.differences(t)["accuracy, recolored, reassigned"].tolist() == [1.0, 0.0]


def test_answer_change_is_the_change_under_the_recoloring_minus_the_change_on_the_repeat():
    t = table(original=[1, 1, 1], repeat=[1, 0, 1], reassigned=[0, 1, 1],
              edited=[0, 0, 0], truth=[1, 1, 1], truth_edited=[0, 0, 0])
    assert analyze.differences(t)["answer change, reassigned"].tolist() == [1.0, -1.0, 0.0]


def test_accuracy_is_scored_against_the_edited_answer_on_an_edited_drawing():
    # Drawing 1 follows the edit, drawing 2 misses it, drawing 3 was already wrong on the original.
    t = table(original=[1, 1, 0], repeat=[1, 1, 0], reassigned=[1, 1, 0],
              edited=[0, 1, 0], truth=[1, 1, 1], truth_edited=[0, 0, 0])
    assert analyze.differences(t)["accuracy, edited, reassigned"].tolist() == [0.0, -1.0, 1.0]


def test_a_missing_reply_drops_the_drawing_from_comparisons_that_need_it():
    t = table(original=[1, 1], repeat=[1, 1], reassigned=[1, 1], d20=[Missing, 1],
              edited=[0, 0], truth=[1, 1], truth_edited=[0, 0])
    values = analyze.differences(t)
    assert math.isnan(values["answer change, d20"][0]) and math.isnan(values["accuracy, recolored, d20"][0])
    assert values["answer change, d14"].tolist() == [0.0, 0.0]


def test_a_model_that_merges_colors_fails_on_recolored_and_edited_drawings_alike():
    # At d3 a model merges the adjacent colors, so it answers "yes" to every T1 drawing.
    n = 100
    truth = [1] * 50 + [0] * 50
    edited_truth = [0] * 50 + [1] * 50
    merged = table(original=truth, repeat=truth, reassigned=truth, edited=edited_truth, truth=truth,
                   truth_edited=edited_truth, d3=[1] * n, d3_edited=[1] * n)
    values = analyze.differences(merged)
    assert np.mean(values["answer change, d3"]) == 0.5
    assert np.mean(values["accuracy, recolored, d3"]) == np.mean(values["accuracy, edited, d3"]) == -0.5


def test_the_bootstrap_estimate_is_the_mean_over_the_drawings_with_a_value():
    estimate, n, means = analyze.bootstrap([{"x": np.array([1.0, 0.0, math.nan, -1.0, 1.0])}], resamples=100)["x"]
    assert (estimate, n, len(means)) == (0.25, 4, 100)


def test_the_bootstrap_is_reproducible_and_matches_the_standard_error_of_a_mean():
    values = np.array([1.0] * 90 + [0.0] * 810)
    first = analyze.bootstrap([{"x": values}], resamples=20_000)["x"][2]
    second = analyze.bootstrap([{"x": values}], resamples=20_000)["x"][2]
    assert (first == second).all()
    assert first.std() == pytest.approx(math.sqrt(0.1 * 0.9 / 900), rel=0.03)
    low, high = analyze.interval(first)
    assert low == pytest.approx(0.1 - 1.96 * 0.01, abs=0.002) and high == pytest.approx(0.1 + 1.96 * 0.01, abs=0.002)


def test_every_resample_keeps_each_tasks_number_of_drawings():
    # One task is all ones, the other all zeros: only an unstratified resample could move the mean.
    means = analyze.bootstrap([{"x": np.ones(30)}, {"x": np.zeros(10)}], resamples=1_000)["x"][2]
    assert (means == 0.75).all()


def test_comparisons_share_the_resampled_drawings():
    values = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 1.0])
    results = analyze.bootstrap([{"x": values, "y": 1 - values}], resamples=1_000)
    assert np.allclose(results["x"][2] + results["y"][2], 1)


def test_an_interval_without_any_difference_has_no_width():
    means = analyze.bootstrap([{"x": np.zeros(300)}], resamples=1_000)["x"][2]
    assert analyze.interval(means) == (0.0, 0.0)


def test_interval_bounds_are_resample_means_and_never_exclude_a_value_the_resamples_reached():
    means = np.array([-0.2] * 3 + [0.0] * 97)
    assert analyze.interval(means, 0.05) == (-0.2, 0.0)   # 3% of the resamples lie at -0.2
    assert analyze.interval(means, 0.10) == (0.0, 0.0)


def test_h1_is_supported_below_the_margin_rejected_above_it_and_inconclusive_across_it():
    assert analyze.decision("answer change, d10", -0.01, 0.04) == "supported"
    assert analyze.decision("answer change, d10", 0.03, 0.08) == "inconclusive"
    assert analyze.decision("answer change, d10", 0.07, 0.17) == "rejected"
    assert analyze.decision("answer change, d10", 0.03, 0.08, margin=0.10) == "supported"


def test_a_bound_exactly_at_the_margin_is_not_below_it_even_after_floating_point_rounding():
    upper = float(np.mean([0.0, 0.15, 0.0]))  # 0.049999999999999996
    assert upper < analyze.Margin
    assert analyze.decision("answer change, d10", 0.0, upper) == "inconclusive"


def test_accuracy_drops_only_when_the_interval_lies_below_zero():
    assert analyze.decision("accuracy, edited, d7", -0.023, -0.001) == "drop"
    assert analyze.decision("accuracy, edited, d7", -0.013, 0.0) == "no change"
    assert analyze.decision("accuracy, recolored, d7", 0.001, 0.02) == "rise"


def test_a_model_that_reads_everything_right_shows_no_change_at_any_distance():
    n = 300
    right = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n)
    results = analyze.analyze_tasks({task: right for task in analyze.Tasks}, analyze.ColorTasks, tests=84)
    assert {row["decision"] for name, row in results.items() if name.startswith("answer change")} == {"supported"}
    assert {row["decision"] for name, row in results.items() if name.startswith("accuracy")} == {"no change"}
    assert results["accuracy, edited, d3"]["n"] == 900


def test_a_loss_at_one_distance_shows_at_that_distance_only():
    n = 300
    wrong_at_d10 = [0] * 60 + [1] * (n - 60)
    t = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n,
              truth_edited=[0] * n, d10=wrong_at_d10)
    results = analyze.analyze_tasks({task: t for task in analyze.Tasks}, analyze.ColorTasks, tests=84)
    assert results["answer change, d10"]["estimate"] == pytest.approx(0.2)
    assert (results["answer change, d10"]["decision"], results["accuracy, recolored, d10"]["decision"]) == ("rejected", "drop")
    assert (results["answer change, d7"]["decision"], results["accuracy, edited, d10"]["decision"]) == ("supported", "no change")


def test_the_corrected_interval_is_wider_than_the_95_percent_interval():
    n = 300
    some_wrong = [0] * 30 + [1] * (n - 30)
    t = table(original=[1] * n, repeat=[1] * n, reassigned=some_wrong, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n)
    row = analyze.analyze_tasks({task: t for task in analyze.Tasks}, ("T1",), tests=84)["answer change, d10"]
    assert row["corrected"][0] < row["interval"][0] < row["estimate"] < row["interval"][1] < row["corrected"][1]


def test_the_sign_test_is_exact_and_two_sided():
    assert analyze.sign_test(np.array([-1.0] * 9 + [0.0] * 891)) == 2 * 0.5 ** 9
    assert analyze.sign_test(np.array([-1.0] * 30 + [1.0] * 7 + [math.nan])) == pytest.approx(1.9e-4, rel=0.05)
    assert analyze.sign_test(np.array([1.0, -1.0])) == analyze.sign_test(np.zeros(5)) == 1.0


def test_a_drop_on_nine_drawings_passes_the_interval_but_not_the_sign_test():
    n = 300
    right = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n)
    nine = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n,
                 d7_edited=[1] * 9 + [0] * (n - 9))
    row = analyze.analyze_tasks({"T1": nine, "T2": right, "T3": right}, analyze.ColorTasks, tests=84)["accuracy, edited, d7"]
    assert row["decision"] == "drop" and not row["sign test agrees"]


def test_the_family_counts_every_comparison_of_the_main_study():
    assert analyze.comparisons(models=2, task_sets=2) == 84


def test_the_report_counts_a_missing_edited_reply_in_that_comparison_only():
    items, _ = generate.make_items("pilot", seed=3, items_per_task=20)
    replies = {}
    for item in items:
        for condition in analyze.Conditions:
            answer = item["edited_answer"] if analyze.is_edited(condition) else item["answer"]
            replies[f"{item['id']}-{condition}"] = {"text": str(answer), "stop": "done", "ok": True}
    del replies[next(f"{i['id']}-d10-edited" for i in items if i["task"] == "T1")]
    tables = analyze.answer_tables(items, replies)
    results = analyze.analyze_tasks(tables, analyze.ColorTasks, tests=42)
    assert (results["accuracy, recolored, d10"]["n"], results["accuracy, edited, d10"]["n"]) == (60, 59)
    report = "\n".join(analyze.model_report("m", tables, items, replies, tests=42))
    assert "1 replies are missing. No decision changes." in report


def test_hand_coding_is_compared_with_the_parser_text_by_text(tmp_path):
    rows = [{"task": "T1", "stop": "done", "reply": "Yes", "parsed": 1.0},
            {"task": "T1", "stop": "done", "reply": "Yes", "parsed": 1.0},
            {"task": "T1", "stop": "done", "reply": "No, they differ.", "parsed": Invalid},
            {"task": "T2", "stop": "done", "reply": "4", "parsed": 4.0}]
    distinct = analyze.distinct_replies(rows)
    assert [r["count"] for r in distinct] == [2, 1, 1]
    (tmp_path / "hand_coding.csv").write_text("task,stop,reply,hand_coded\nT1,done,Yes,yes\nT1,done,\"No, they differ.\",no\nT2,done,4,4\n")
    report = "\n".join(analyze.hand_coding_report(distinct, 0, tmp_path / "hand_coding.csv"))
    assert "3 of 3 distinct replies hand coded" in report and "1 disagree" in report and "they differ" in report


def test_a_blank_hand_coding_sheet_does_not_pass(tmp_path):
    distinct = analyze.distinct_replies([{"task": "T1", "stop": "done", "reply": "Yes", "parsed": 1.0}])
    (tmp_path / "hand_coding.csv").write_text("task,stop,reply,hand_coded\nT1,done,Yes,\n")
    report = "\n".join(analyze.hand_coding_report(distinct, 0, tmp_path / "hand_coding.csv"))
    assert "0 of 1 distinct replies hand coded" in report and "does not pass yet" in report


def test_the_report_runs_end_to_end_on_a_generated_set(tmp_path, monkeypatch):
    items, _ = generate.make_items("pilot", seed=3, items_per_task=10)
    (tmp_path / "pilot" / "replies").mkdir(parents=True)
    (tmp_path / "pilot" / "manifest.jsonl").write_text("".join(json.dumps(item) + "\n" for item in items))  # analyze reads no images
    with open(tmp_path / "pilot" / "replies" / "perfect.jsonl", "w") as f:
        for item in items:
            for condition in analyze.Conditions:
                answer = "?" if condition == "no_image" else item["edited_answer"] if analyze.is_edited(condition) else item["answer"]
                f.write(json.dumps({"query_id": f"{item['id']}-{condition}", "ok": True,
                                    "text": str(answer), "stop": "done"}) + "\n")
    monkeypatch.setattr(analyze, "Data", tmp_path)
    monkeypatch.setattr("sys.argv", ["analyze.py", "pilot"])

    analyze.main()

    report = (tmp_path / "pilot" / "results.md").read_text()
    assert "corrected for the set's 42 comparisons (models x task sets x distances x measures = 1 x 2 x 7 x 3)" in report
    assert "| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 30 |" in report
    assert "| T1 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 10 | " in report


def test_structure_only_accuracy_answers_yes_exactly_for_nodes_with_two_neighbors():
    hub = {"u": "A", "answer": "yes", "edge_list": [["A", "B"], ["A", "C"]]}
    leaf_no = {"u": "A", "answer": "no", "edge_list": [["A", "B"]]}
    leaf_yes = {"u": "A", "answer": "yes", "edge_list": [["A", "B"]]}
    assert analyze.structure_only_accuracy([hub, leaf_no, leaf_yes]) == 2 / 3


def test_proximity_only_accuracy_uses_the_best_cutoff():
    def item(distance, answer):
        return {"u": "A", "v": "B", "answer": answer, "positions": {"A": [0, 0], "B": [distance, 0]}}
    # A far edge beyond a near non-edge: no cutoff gets all three, the best gets two.
    assert analyze.proximity_only_accuracy([item(1, "yes"), item(2, "no"), item(3, "yes")]) == 2 / 3


def test_counting_missing_replies_as_wrong_reports_the_decisions_that_change():
    n = 300
    complete = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n)
    complete["answers"]["no_image"] = np.zeros(n)
    gappy = table(original=[1] * n, repeat=[1] * n, reassigned=[1] * n, edited=[0] * n, truth=[1] * n, truth_edited=[0] * n,
                  d10=[Missing] * 40 + [1] * (n - 40))
    gappy["answers"]["no_image"] = np.zeros(n)
    full = {"T1": complete, "T2": complete, "T3": complete}
    assert analyze.missing_as_wrong(full, {"color tasks": analyze.analyze_tasks(full, analyze.ColorTasks, 84)}, 84) == []
    holes = {"T1": gappy, "T2": complete, "T3": complete}
    report = "\n".join(analyze.missing_as_wrong(holes, {"color tasks": analyze.analyze_tasks(holes, analyze.ColorTasks, 84)}, 84))
    assert "40 replies are missing. Decisions that change:" in report
    assert "color tasks, accuracy, recolored, d10: no change becomes drop" in report


def test_t4_rates_follow_the_shared_color_through_the_edit():
    # A model that sees an edge exactly when u and v share a color. Item 0 shares one on the original,
    # item 1 does not; the edit switches both, so every yes lands in the shared-color cell.
    items = [{"task": "T4", "u": "A", "v": "B", "groups": {"A": 0, "B": 0}},
             {"task": "T4", "u": "A", "v": "B", "groups": {"A": 0, "B": 1}}]
    t = table(original=[1, 0], repeat=[1, 0], reassigned=[1, 0], edited=[0, 1], truth=[0, 0], truth_edited=[0, 0])
    rates = analyze.shared_color_rates({"T4": t}, items)
    assert rates["tab10"] == rates["d3"] == {(False, True): 1.0, (False, False): 0.0, (True, True): None, (True, False): None}
