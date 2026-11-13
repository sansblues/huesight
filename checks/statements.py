"""Reproduces numbers that the thesis states in its text but that no table holds: exact binomial bounds,
the drawings behind an uncertain drop, counts of wrong answers, the decisions that would differ without
the Bonferroni correction, and how far adjacent palette colors lie apart in sRGB.

Run from the repository root: uv run checks/statements.py

Reads the main manifest and replies. Sends no queries and writes no files.
"""

import json
import sys
from pathlib import Path

import numpy as np

Root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Root / "study"))
import analyze
import generate

Tests = analyze.comparisons(models=2, task_sets=2)


def main():
    folder = Root / "data/main"
    items = [json.loads(line) for line in (folder / "manifest.jsonl").read_text().splitlines()]
    print(f"corrected level: {analyze.Level / Tests:.4f} two-sided, {analyze.Level / Tests / 2:.5f} per side")
    for changed in (0, 1):
        print(f"exact upper bound for {changed} of 900 drawings: {100 * binomial_upper(changed, 900, analyze.Level / Tests / 2):.2f}%")
    for model in ("claude", "qwen"):
        tables = analyze.answer_tables(items, analyze.first_replies(folder / "replies" / f"{model}.jsonl"))
        results = analyze.analyze_tasks(tables, analyze.ColorTasks, Tests)
        print(analyze.ModelNames[model])
        wide = [c for r in analyze.Recolorings[:4] for c in (r, analyze.edited_twin(r))]  # 52 down to 10 units
        print("  not correct from 52 to 10 units:", wrong(tables, wide), "of", answered(tables, wide), "images of the color tasks")
        at_ten = ("d10", "d10-edited")
        print("  not correct at 10 units:", wrong(tables, at_ten), "of", answered(tables, at_ten))
        for name in ("accuracy, edited, d7", "accuracy, recolored, d14", "accuracy, edited, d14"):
            values = np.concatenate([analyze.differences(tables[task])[name] for task in analyze.ColorTasks])
            print(f"  {name}: {int((values < 0).sum())} drawings worse, {int((values > 0).sum())} better, "
                  f"decision {results[name]['decision']}")
        near = [results[f"answer change, {r}"] for r in analyze.Recolorings if 0.02 < results[f"answer change, {r}"]["estimate"] < 0.08]
        print("  corrected intervals of answer changes near the margin:",
              [f"{100 * e['estimate']:.1f} [{100 * e['corrected'][0]:.1f}, {100 * e['corrected'][1]:.1f}]" for e in near])
        for task_set, tasks in analyze.TaskSets.items():
            entries = results if tasks == analyze.ColorTasks else analyze.analyze_tasks(tables, tasks, Tests)
            print(f"  {task_set}, decided differently by the uncorrected 95% interval:",
                  [f"{name}: {e['decision']} becomes {analyze.decision(name, *e['interval'])}" for name, e in entries.items()
                   if analyze.decision(name, *e["interval"]) != e["decision"]])
    steps = [int(np.abs(rgb(palette[k]) - rgb(palette[1])).max()) for (_, d), palette in generate.LadderPalettes.items() if d == 10
             for k in (0, 2)]
    print("adjacent colors at 10 units differ by", min(steps), "to", max(steps), "of 255 levels in the channel that differs most")
    for distance in generate.Distances:
        largest = {hue: max(int(np.abs(rgb(palette[k]) - rgb(palette[1])).max()) for k in (0, 2))
                   for (hue, d), palette in generate.LadderPalettes.items() if d == distance}
        print(f"  at {distance} units, the largest difference per base hue:", dict(sorted(largest.items())),
              "smallest at", min(largest, key=largest.get))


def binomial_upper(changed, n, level):
    """The exact (Clopper-Pearson) upper bound: the largest rate at which `changed` or fewer of n is still
    as likely as `level`."""
    low, high = 0.0, 1.0
    for _ in range(100):
        rate = (low + high) / 2
        tail = sum(comb(n, k) * rate**k * (1 - rate) ** (n - k) for k in range(changed + 1))
        low, high = (rate, high) if tail > level else (low, rate)
    return high


def comb(n, k):
    return float(np.prod([(n - i) / (i + 1) for i in range(k)]))


def wrong(tables, conditions):
    return sum(int((analyze.accuracy_values(tables[task], c) == 0).sum()) for task in analyze.ColorTasks for c in conditions)


def answered(tables, conditions):
    return sum(int((~np.isnan(analyze.accuracy_values(tables[task], c))).sum()) for task in analyze.ColorTasks for c in conditions)


def rgb(color):
    return np.array([int(color[i:i + 2], 16) for i in (1, 3, 5)])


if __name__ == "__main__":
    main()
