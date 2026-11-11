# Results: main

1200 drawings. Differences are in percentage points (pp). Each has a 95% interval and one corrected for the set's 84 comparisons (models x task sets x distances x measures = 2 x 2 x 7 x 3): percentile intervals of 100,000 resamples of the drawings. Decisions use the corrected interval; the margin for answer change is 5 pp.

## Claude Opus 5.5

Output tokens per reply, reasoning included: mean 70, median 58.

Answers changed on the repeat: 0.1% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 300 | 50.0% | 300 of 300 |
| T2 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 300 | 20.0% | 300 of 300 |
| T3 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 300 | 57.7% | 300 of 300 |
| T4 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 300 | 89.3% | 300 of 300 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [-0.3, 0.3] | [-0.6, 0.6] | supported | 900 |
| 20 | -0.1 | [-0.3, 0.0] | [-0.7, 0.0] | supported | 900 |
| 14 | -0.1 | [-0.3, 0.0] | [-0.7, 0.0] | supported | 900 |
| 10 | -0.1 | [-0.3, 0.0] | [-0.7, 0.0] | supported | 900 |
| 7 | 0.3 | [-0.1, 0.9] | [-0.4, 1.3] | supported | 900 |
| 5 | 5.7 | [4.2, 7.2] | [3.1, 8.6] | inconclusive | 900 |
| 3 | 41.3 | [38.3, 44.3] | [36.1, 46.6] | rejected | 900 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | -0.1 | [-0.3, 0.0] | [-0.7, 0.0] | no change | 900 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 7 | -0.4 | [-0.9, -0.1] | [-1.3, 0.0] | no change | 900 |
| 5 | -5.8 | [-7.3, -4.3] | [-8.7, -3.3] | drop | 900 |
| 3 | -41.4 | [-44.4, -38.4] | [-46.7, -36.2] | drop | 900 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 20 | -0.1 | [-0.3, 0.0] | [-0.7, 0.0] | no change | 900 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 900 |
| 7 | -1.0 | [-1.7, -0.4] | [-2.3, -0.1] | drop | 900 |
| 5 | -6.7 | [-8.3, -5.1] | [-9.8, -4.1] | drop | 900 |
| 3 | -38.7 | [-41.7, -35.8] | [-43.8, -33.4] | drop | 900 |

### Control (T4)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 5 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 3 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 5 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 3 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 5 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 3 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [-1.0, 1.0] | 300 |
| 20 | -0.3 | [-1.0, 0.0] | 300 |
| 14 | -0.3 | [-1.0, 0.0] | 300 |
| 10 | -0.3 | [-1.0, 0.0] | 300 |
| 7 | -0.3 | [-1.0, 0.0] | 300 |
| 5 | 3.0 | [1.0, 5.3] | 300 |
| 3 | 26.0 | [21.0, 31.0] | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | -0.3 | [-1.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.0 | [0.0, 0.0] | 300 |
| 5 | -3.3 | [-5.3, -1.3] | 300 |
| 3 | -26.3 | [-31.3, -21.3] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | -0.7 | [-1.7, 0.0] | 300 |
| 5 | -4.7 | [-7.3, -2.3] | 300 |
| 3 | -23.0 | [-28.0, -18.3] | 300 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 1.0 | [0.0, 2.3] | 300 |
| 5 | 10.0 | [6.7, 13.7] | 300 |
| 3 | 68.3 | [63.0, 73.7] | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | -1.0 | [-2.3, 0.0] | 300 |
| 5 | -10.0 | [-13.7, -6.7] | 300 |
| 3 | -68.3 | [-73.7, -63.0] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | -2.0 | [-3.7, -0.7] | 300 |
| 5 | -10.3 | [-14.0, -7.0] | 300 |
| 3 | -64.7 | [-70.0, -59.3] | 300 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.3 | [0.0, 1.0] | 300 |
| 5 | 4.0 | [2.0, 6.3] | 300 |
| 3 | 29.7 | [24.7, 35.0] | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | -0.3 | [-1.0, 0.0] | 300 |
| 5 | -4.0 | [-6.3, -2.0] | 300 |
| 3 | -29.7 | [-35.0, -24.7] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | -0.3 | [-1.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | -0.3 | [-1.0, 0.0] | 300 |
| 5 | -5.0 | [-7.7, -2.7] | 300 |
| 3 | -28.3 | [-33.3, -23.3] | 300 |

### T4 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.0 | [0.0, 0.0] | 300 |
| 5 | 0.0 | [0.0, 0.0] | 300 |
| 3 | 0.0 | [0.0, 0.0] | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.0 | [0.0, 0.0] | 300 |
| 5 | 0.0 | [0.0, 0.0] | 300 |
| 3 | 0.0 | [0.0, 0.0] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.0 | [0.0, 0.0] | 300 |
| 5 | 0.0 | [0.0, 0.0] | 300 |
| 3 | 0.0 | [0.0, 0.0] | 300 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | supported | supported | supported | supported | rejected | rejected |
| color tasks | 5 pp | supported | supported | supported | supported | supported | inconclusive | rejected |
| color tasks | 10 pp | supported | supported | supported | supported | supported | supported | rejected |
| control | 2.5 pp | supported | supported | supported | supported | supported | supported | supported |
| control | 5 pp | supported | supported | supported | supported | supported | supported | supported |
| control | 10 pp | supported | supported | supported | supported | supported | supported | supported |

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 0 | - |
| T2 | 0 | - |
| T3 | 0 | - |
| T4 | 0 | - |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 2 | 0 | 0 |
| without image | 1200 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 100.0% | 0.0% | 99.7% | 0.0% |
| d14 | 100.0% | 0.0% | 100.0% | 0.0% |
| d10 | 100.0% | 0.0% | 100.0% | 0.0% |
| d7 | 99.3% | 0.0% | 100.0% | 0.7% |
| d5 | 96.3% | 4.3% | 99.3% | 8.0% |
| d3 | 88.3% | 37.7% | 95.3% | 53.3% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 0 | 1 | 0 |
| d14 | 0 | 0 | 0 |
| d10 | 0 | 0 | 0 |
| d7 | 9 | 4 | 0 |
| d5 | 86 | 25 | 1 |
| d3 | 642 | 79 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 | T4 |
| --- | --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| repeat | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 99.7% (1 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d7 | 100.0% (0 inv, 0 miss) | 99.0% (0 inv, 0 miss) | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d7-edited | 99.3% (0 inv, 0 miss) | 98.0% (0 inv, 0 miss) | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d5 | 96.7% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) | 96.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d5-edited | 95.3% (0 inv, 0 miss) | 89.7% (0 inv, 0 miss) | 95.0% (1 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d3 | 73.7% (0 inv, 0 miss) | 31.7% (0 inv, 0 miss) | 70.3% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d3-edited | 77.0% (0 inv, 0 miss) | 35.3% (0 inv, 0 miss) | 71.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| no_image | 0.0% (300 inv, 0 miss) | 0.0% (300 inv, 0 miss) | 0.0% (300 inv, 0 miss) | 0.0% (300 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 100.0% | 100.0% | 100.0% | 98.0% | 82.0% | 47.0% |
| 115 | 100.0% | 100.0% | 100.0% | 100.0% | 99.3% | 78.0% |
| 175 | 100.0% | 100.0% | 100.0% | 100.0% | 98.7% | 68.3% |
| 235 | 100.0% | 100.0% | 100.0% | 98.0% | 88.7% | 45.3% |
| 295 | 99.7% | 100.0% | 100.0% | 100.0% | 98.7% | 60.3% |
| 355 | 100.0% | 100.0% | 100.0% | 99.7% | 95.3% | 60.7% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 100.0% | 100.0% | 100.0% | 97.4% | 82.8% | 18.8% | 96 |
| outer | 100.0% | 100.0% | 100.0% | 99.0% | 93.1% | 40.4% | 204 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 73 to 223 px | 100.0% | 100.0% | 100.0% | 100.0% | 96.0% | 68.0% | 100 |
| 229 to 376 px | 100.0% | 100.0% | 100.0% | 100.0% | 95.0% | 57.0% | 100 |
| 377 to 694 px | 100.0% | 100.0% | 100.0% | 100.0% | 96.0% | 62.0% | 100 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 92.5% | 300 |
| 11 | 92.3% | 300 |
| 12 | 91.6% | 300 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 93.0% | 450 |
| dense | 91.3% | 450 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 92.8% | 463 |
| 1-2 | 91.8% | 344 |
| 3-5 | 90.2% | 84 |
| 6+ | 91.7% | 9 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 91.5% | 123 |
| 2 | 91.7% | 249 |
| 3 | 93.1% | 240 |
| 4 | 92.1% | 180 |
| 5 | 92.1% | 108 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 3 to 49 | 99.1% | 2689 |
| 50 to 76 | 97.6% | 2623 |
| 77 to 121 | 94.5% | 2779 |
| 122 to 755 | 77.6% | 2709 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

### T4 yes answers by edge and shared color (exploratory)

| Palette | No edge, shared color | No edge, other colors | Edge, shared color | Edge, other colors |
| --- | --- | --- | --- | --- |
| tab10 | 0.0% | 0.0% | 100.0% | 100.0% |
| d20 | 0.0% | 0.0% | 100.0% | 100.0% |
| d14 | 0.0% | 0.0% | 100.0% | 100.0% |
| d10 | 0.0% | 0.0% | 100.0% | 100.0% |
| d7 | 0.0% | 0.0% | 100.0% | 100.0% |
| d5 | 0.0% | 0.0% | 100.0% | 100.0% |
| d3 | 0.0% | 0.0% | 100.0% | 100.0% |

Cells: share of valid answers that are yes. tab10 pools the original, reassigned and edited drawings.

## Qwen3.8-27B

Output tokens per reply, reasoning included: mean 330, median 290.

Answers changed on the repeat: 0.6% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 55.7% | 44.3 [38.7, 50.0], n = 300 | 50.0% | 0 of 300 |
| T2 | 99.0% | 22.2% | 76.7 [71.8, 81.4], n = 296 | 20.0% | 15 of 297 |
| T3 | 98.7% | 49.5% | 49.2 [43.4, 54.9], n = 297 | 57.7% | 0 of 299 |
| T4 | 99.7% | 49.7% | 50.0 [44.3, 55.7], n = 300 | 89.3% | 1 of 300 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.1 | [-0.2, 0.6] | [-0.6, 0.9] | supported | 890 |
| 20 | 0.7 | [0.1, 1.3] | [-0.2, 1.9] | supported | 893 |
| 14 | 3.4 | [2.2, 4.6] | [1.4, 5.6] | inconclusive | 892 |
| 10 | 17.8 | [15.4, 20.4] | [13.5, 22.2] | rejected | 891 |
| 7 | 36.7 | [33.7, 39.7] | [31.6, 42.0] | rejected | 891 |
| 5 | 47.8 | [44.7, 50.8] | [42.5, 53.1] | rejected | 894 |
| 3 | 60.2 | [57.3, 63.2] | [55.0, 65.4] | rejected | 893 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.4 | [-0.1, 1.1] | [-0.6, 1.7] | no change | 893 |
| 20 | 0.1 | [-0.7, 0.9] | [-1.3, 1.6] | no change | 896 |
| 14 | -2.6 | [-3.9, -1.2] | [-5.0, -0.3] | drop | 895 |
| 10 | -17.2 | [-19.8, -14.7] | [-21.7, -12.8] | drop | 894 |
| 7 | -36.2 | [-39.2, -33.3] | [-41.5, -31.0] | drop | 894 |
| 5 | -47.6 | [-50.7, -44.6] | [-52.9, -42.3] | drop | 897 |
| 3 | -59.8 | [-62.8, -56.9] | [-65.0, -54.6] | drop | 896 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [-0.7, 0.7] | [-1.2, 1.2] | no change | 895 |
| 20 | -0.1 | [-1.0, 0.8] | [-1.6, 1.3] | no change | 895 |
| 14 | -3.4 | [-4.7, -2.0] | [-5.9, -1.1] | drop | 895 |
| 10 | -18.1 | [-20.7, -15.5] | [-22.7, -13.8] | drop | 896 |
| 7 | -37.6 | [-40.6, -34.5] | [-42.8, -32.4] | drop | 892 |
| 5 | -47.4 | [-50.5, -44.3] | [-52.6, -42.0] | drop | 890 |
| 3 | -60.9 | [-63.8, -58.0] | [-66.1, -55.9] | drop | 896 |

### Control (T4)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [0.0, 1.0] | [0.0, 2.0] | supported | 300 |
| 20 | -0.3 | [-1.0, 0.0] | [-2.0, 0.0] | supported | 300 |
| 14 | -0.3 | [-1.0, 0.0] | [-2.0, 0.0] | supported | 300 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |
| 7 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | supported | 300 |
| 5 | 0.7 | [0.0, 1.7] | [0.0, 2.7] | supported | 300 |
| 3 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [-1.0, 1.0] | [-1.7, 1.7] | no change | 300 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 300 |
| 10 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |
| 7 | 0.0 | [-1.0, 1.0] | [-1.7, 2.0] | no change | 300 |
| 5 | -0.3 | [-1.7, 0.7] | [-2.7, 1.7] | no change | 300 |
| 3 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | n |
| --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |
| 20 | -0.3 | [-1.0, 0.0] | [-2.0, 0.0] | no change | 300 |
| 14 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |
| 10 | 0.0 | [-1.0, 1.0] | [-2.0, 1.7] | no change | 300 |
| 7 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |
| 5 | 0.3 | [0.0, 1.0] | [0.0, 2.0] | no change | 300 |
| 3 | -0.7 | [-1.7, 0.0] | [-2.7, 0.0] | no change | 300 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 298 |
| 20 | 0.3 | [0.0, 1.0] | 298 |
| 14 | 1.0 | [0.0, 2.3] | 298 |
| 10 | 10.4 | [7.0, 14.0] | 298 |
| 7 | 20.2 | [15.7, 24.8] | 297 |
| 5 | 30.5 | [25.3, 35.8] | 298 |
| 3 | 45.6 | [40.1, 51.3] | 298 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 300 |
| 20 | -0.3 | [-1.0, 0.0] | 300 |
| 14 | -1.0 | [-2.3, 0.0] | 300 |
| 10 | -10.3 | [-14.0, -7.0] | 300 |
| 7 | -20.1 | [-24.7, -15.7] | 299 |
| 5 | -30.3 | [-35.7, -25.3] | 300 |
| 3 | -45.3 | [-51.0, -39.7] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 298 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | -1.7 | [-3.3, -0.3] | 299 |
| 10 | -13.7 | [-17.7, -10.0] | 300 |
| 7 | -25.1 | [-30.1, -20.3] | 299 |
| 5 | -33.3 | [-38.8, -28.1] | 297 |
| 3 | -48.0 | [-53.7, -42.3] | 300 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | -0.3 | [-1.0, 0.0] | 296 |
| 20 | -0.3 | [-1.0, 0.0] | 298 |
| 14 | 3.4 | [1.3, 5.7] | 297 |
| 10 | 25.3 | [20.5, 30.4] | 296 |
| 7 | 60.9 | [55.3, 66.6] | 297 |
| 5 | 75.8 | [70.9, 80.6] | 298 |
| 3 | 89.9 | [86.2, 93.3] | 298 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 1.0 | [0.0, 2.3] | 297 |
| 20 | 1.0 | [0.0, 2.3] | 299 |
| 14 | -2.7 | [-5.3, -0.3] | 298 |
| 10 | -25.3 | [-30.3, -20.3] | 297 |
| 7 | -60.7 | [-66.3, -55.0] | 298 |
| 5 | -75.9 | [-80.7, -71.0] | 299 |
| 3 | -90.0 | [-93.3, -86.3] | 299 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [0.0, 1.0] | 299 |
| 20 | 0.3 | [-1.0, 1.7] | 298 |
| 14 | -3.7 | [-6.4, -1.0] | 298 |
| 10 | -23.1 | [-28.0, -18.3] | 299 |
| 7 | -58.8 | [-64.4, -53.2] | 296 |
| 5 | -72.7 | [-77.8, -67.6] | 297 |
| 3 | -91.3 | [-94.3, -88.0] | 298 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.7 | [0.0, 1.7] | 296 |
| 20 | 2.0 | [0.7, 3.7] | 297 |
| 14 | 5.7 | [3.3, 8.4] | 297 |
| 10 | 17.8 | [13.6, 22.3] | 297 |
| 7 | 29.0 | [23.8, 34.2] | 297 |
| 5 | 36.9 | [31.4, 42.5] | 298 |
| 3 | 45.1 | [39.5, 50.8] | 297 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [-1.0, 2.0] | 296 |
| 20 | -0.3 | [-2.4, 1.7] | 297 |
| 14 | -4.0 | [-7.0, -1.3] | 297 |
| 10 | -16.2 | [-20.8, -11.7] | 297 |
| 7 | -27.9 | [-33.3, -22.6] | 297 |
| 5 | -36.6 | [-42.3, -31.0] | 298 |
| 3 | -44.1 | [-50.0, -38.3] | 297 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | -0.3 | [-2.3, 1.7] | 298 |
| 20 | -0.7 | [-2.7, 1.4] | 297 |
| 14 | -4.7 | [-7.4, -2.0] | 298 |
| 10 | -17.5 | [-22.1, -13.1] | 297 |
| 7 | -29.0 | [-34.2, -23.8] | 297 |
| 5 | -36.1 | [-41.7, -30.6] | 296 |
| 3 | -43.6 | [-49.3, -37.8] | 298 |

### T4 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [0.0, 1.0] | 300 |
| 20 | -0.3 | [-1.0, 0.0] | 300 |
| 14 | -0.3 | [-1.0, 0.0] | 300 |
| 10 | 0.0 | [0.0, 0.0] | 300 |
| 7 | 0.3 | [0.0, 1.0] | 300 |
| 5 | 0.7 | [0.0, 1.7] | 300 |
| 3 | 0.0 | [0.0, 0.0] | 300 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [-1.0, 1.0] | 300 |
| 20 | 0.0 | [0.0, 0.0] | 300 |
| 14 | 0.0 | [0.0, 0.0] | 300 |
| 10 | 0.3 | [0.0, 1.0] | 300 |
| 7 | 0.0 | [-1.0, 1.0] | 300 |
| 5 | -0.3 | [-1.7, 0.7] | 300 |
| 3 | 0.3 | [0.0, 1.0] | 300 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.3 | [0.0, 1.0] | 300 |
| 20 | -0.3 | [-1.0, 0.0] | 300 |
| 14 | 0.3 | [0.0, 1.0] | 300 |
| 10 | 0.0 | [-1.0, 1.0] | 300 |
| 7 | 0.3 | [0.0, 1.0] | 300 |
| 5 | 0.3 | [0.0, 1.0] | 300 |
| 3 | -0.7 | [-1.7, 0.0] | 300 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | supported | inconclusive | rejected | rejected | rejected | rejected |
| color tasks | 5 pp | supported | supported | inconclusive | rejected | rejected | rejected | rejected |
| color tasks | 10 pp | supported | supported | supported | rejected | rejected | rejected | rejected |
| control | 2.5 pp | supported | supported | supported | supported | supported | inconclusive | supported |
| control | 5 pp | supported | supported | supported | supported | supported | supported | supported |
| control | 10 pp | supported | supported | supported | supported | supported | supported | supported |

### Missing replies counted as wrong and as changed answers (sensitivity)

44 replies are missing. Decisions that change:

- color tasks, accuracy, recolored, d14: drop becomes no change (-2.4 [-5.0, 0.0])

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 300 | 25.7% |
| T2 | 282 | 2.8 |
| T3 | 299 | 6.7% |
| T4 | 299 | 7.7% |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 1 | 0 | 0 |
| without image | 16 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 99.7% | 0.0% | 99.0% | 2.7% |
| d14 | 99.0% | 1.7% | 98.3% | 9.7% |
| d10 | 97.7% | 21.7% | 96.3% | 32.8% |
| d7 | 91.3% | 36.3% | 96.0% | 55.7% |
| d5 | 87.2% | 50.8% | 94.0% | 68.9% |
| d3 | 93.0% | 86.3% | 97.3% | 87.3% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 8 | 6 | 0 |
| d14 | 53 | 14 | 0 |
| d10 | 299 | 32 | 0 |
| d7 | 610 | 65 | 0 |
| d5 | 774 | 90 | 1 |
| d3 | 1022 | 76 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 | T4 |
| --- | --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 99.0% (0 inv, 1 miss) | 98.7% (0 inv, 2 miss) | 99.7% (0 inv, 0 miss) |
| repeat | 100.0% (0 inv, 2 miss) | 99.7% (0 inv, 1 miss) | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 2 miss) | 99.0% (0 inv, 2 miss) | 99.7% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 2 miss) | 99.3% (0 inv, 0 miss) | 98.3% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 99.7% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 98.3% (0 inv, 1 miss) | 99.7% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 99.3% (0 inv, 1 miss) | 98.0% (0 inv, 1 miss) | 99.3% (0 inv, 0 miss) |
| d14 | 99.0% (0 inv, 0 miss) | 96.3% (0 inv, 1 miss) | 94.6% (0 inv, 1 miss) | 99.7% (0 inv, 0 miss) |
| d14-edited | 98.3% (0 inv, 1 miss) | 95.3% (0 inv, 1 miss) | 94.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10 | 89.7% (0 inv, 0 miss) | 73.8% (0 inv, 2 miss) | 82.6% (0 inv, 1 miss) | 100.0% (0 inv, 0 miss) |
| d10-edited | 86.3% (0 inv, 0 miss) | 76.0% (0 inv, 0 miss) | 80.9% (0 inv, 1 miss) | 99.7% (0 inv, 0 miss) |
| d7 | 79.9% (0 inv, 1 miss) | 38.1% (0 inv, 1 miss) | 70.9% (0 inv, 1 miss) | 99.7% (0 inv, 0 miss) |
| d7-edited | 74.9% (0 inv, 1 miss) | 40.4% (0 inv, 3 miss) | 69.6% (0 inv, 1 miss) | 100.0% (0 inv, 0 miss) |
| d5 | 69.7% (0 inv, 0 miss) | 23.0% (0 inv, 0 miss) | 62.3% (1 inv, 0 miss) | 99.3% (0 inv, 0 miss) |
| d5-edited | 66.7% (0 inv, 3 miss) | 26.5% (0 inv, 2 miss) | 62.4% (0 inv, 2 miss) | 100.0% (0 inv, 0 miss) |
| d3 | 54.7% (0 inv, 0 miss) | 9.0% (0 inv, 0 miss) | 54.8% (0 inv, 1 miss) | 100.0% (0 inv, 0 miss) |
| d3-edited | 52.0% (0 inv, 0 miss) | 8.0% (0 inv, 1 miss) | 55.0% (0 inv, 0 miss) | 99.0% (0 inv, 0 miss) |
| no_image | 55.7% (0 inv, 0 miss) | 22.2% (15 inv, 3 miss) | 49.5% (0 inv, 1 miss) | 49.7% (1 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 99.7% | 99.3% | 88.0% | 62.0% | 54.2% | 39.8% |
| 115 | 99.3% | 98.7% | 94.6% | 76.5% | 60.1% | 48.0% |
| 175 | 98.3% | 90.9% | 70.7% | 58.0% | 48.8% | 36.7% |
| 235 | 99.3% | 91.3% | 68.3% | 52.0% | 46.3% | 34.8% |
| 295 | 99.0% | 99.3% | 88.0% | 63.9% | 51.5% | 38.7% |
| 355 | 99.7% | 98.0% | 79.9% | 61.5% | 49.7% | 35.7% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 99.5% | 95.3% | 59.7% | 22.5% | 12.0% | 3.7% | 96 |
| outer | 99.8% | 96.1% | 82.1% | 47.2% | 30.7% | 10.8% | 204 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 73 to 223 px | 100.0% | 99.0% | 74.0% | 60.0% | 40.0% | 9.0% | 100 |
| 229 to 376 px | 100.0% | 99.0% | 84.0% | 68.0% | 51.0% | 17.0% | 100 |
| 377 to 694 px | 100.0% | 97.0% | 77.0% | 63.0% | 56.6% | 15.0% | 100 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 72.1% | 300 |
| 11 | 72.2% | 300 |
| 12 | 70.7% | 300 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 71.6% | 450 |
| dense | 71.7% | 450 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 71.4% | 463 |
| 1-2 | 72.1% | 344 |
| 3-5 | 72.0% | 84 |
| 6+ | 65.7% | 9 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 68.2% | 123 |
| 2 | 70.1% | 249 |
| 3 | 72.6% | 240 |
| 4 | 73.6% | 180 |
| 5 | 74.0% | 108 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 53 to 218 | 79.6% | 2685 |
| 219 to 326 | 79.1% | 2697 |
| 327 to 455 | 71.1% | 2686 |
| 456 to 4644 | 57.0% | 2704 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

### T4 yes answers by edge and shared color (exploratory)

| Palette | No edge, shared color | No edge, other colors | Edge, shared color | Edge, other colors |
| --- | --- | --- | --- | --- |
| tab10 | 0.0% | 0.4% | 100.0% | 99.6% |
| d20 | 0.7% | 0.7% | 99.3% | 100.0% |
| d14 | 0.0% | 0.7% | 100.0% | 100.0% |
| d10 | 0.0% | 0.0% | 99.3% | 100.0% |
| d7 | 0.0% | 0.0% | 99.3% | 100.0% |
| d5 | 0.0% | 0.7% | 99.3% | 100.0% |
| d3 | 1.3% | 0.0% | 99.3% | 100.0% |

Cells: share of valid answers that are yes. tab10 pools the original, reassigned and edited drawings.

