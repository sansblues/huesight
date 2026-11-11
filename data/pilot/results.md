# Results: pilot

60 drawings. Differences are in percentage points (pp). Each has a 95% interval and one corrected for the set's 84 comparisons (models x task sets x distances x measures = 4 x 1 x 7 x 3): percentile intervals of 100,000 resamples of the drawings. Decisions use the corrected interval; the margin for answer change is 5 pp. The sign test is exact and two-sided; its corrected level is 0.0006.

## Claude Opus 5.5

Output tokens per reply, reasoning included: mean 87, median 68.

Answers changed on the repeat: 0.0% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 20 | 50.0% | 20 of 20 |
| T2 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 20 | 20.0% | 20 of 20 |
| T3 | 100.0% | 0.0% | 100.0 [100.0, 100.0], n = 20 | 55.0% | 20 of 20 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 5 | 6.7 | [1.7, 13.3] | [0.0, 20.0] | inconclusive | 0.12 | 60 |
| 3 | 41.7 | [30.0, 53.3] | [21.7, 61.7] | rejected | 6e-08 | 60 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 5 | -6.7 | [-13.3, -1.7] | [-20.0, 0.0] | no change | 0.12 | 60 |
| 3 | -41.7 | [-53.3, -30.0] | [-61.7, -21.7] | drop | 6e-08 | 60 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 7 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 5 | -6.7 | [-13.3, -1.7] | [-20.0, 0.0] | no change | 0.12 | 60 |
| 3 | -45.0 | [-56.7, -33.3] | [-65.0, -25.0] | drop | 1.5e-08 | 60 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 5.0 | [0.0, 15.0] | 20 |
| 3 | 30.0 | [10.0, 50.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -5.0 | [-15.0, 0.0] | 20 |
| 3 | -30.0 | [-50.0, -10.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -5.0 | [-15.0, 0.0] | 20 |
| 3 | -20.0 | [-40.0, -5.0] | 20 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 15.0 | [0.0, 30.0] | 20 |
| 3 | 70.0 | [50.0, 90.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -15.0 | [-30.0, 0.0] | 20 |
| 3 | -70.0 | [-90.0, -50.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -10.0 | [-25.0, 0.0] | 20 |
| 3 | -75.0 | [-90.0, -55.0] | 20 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 0.0 | [0.0, 0.0] | 20 |
| 3 | 25.0 | [10.0, 45.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 0.0 | [0.0, 0.0] | 20 |
| 3 | -25.0 | [-45.0, -10.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -5.0 | [-15.0, 0.0] | 20 |
| 3 | -40.0 | [-60.0, -20.0] | 20 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | supported | supported | supported | supported | inconclusive | rejected |
| color tasks | 5 pp | supported | supported | supported | supported | supported | inconclusive | rejected |
| color tasks | 10 pp | supported | supported | supported | supported | supported | inconclusive | rejected |

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 0 | - |
| T2 | 0 | - |
| T3 | 0 | - |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 0 | 0 | 0 |
| without image | 60 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 100.0% | 0.0% | 100.0% | 0.0% |
| d14 | 100.0% | 0.0% | 100.0% | 0.0% |
| d10 | 100.0% | 0.0% | 100.0% | 0.0% |
| d7 | 100.0% | 0.0% | 100.0% | 0.0% |
| d5 | 95.0% | 5.0% | 95.0% | 0.0% |
| d3 | 85.0% | 35.0% | 100.0% | 65.0% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 0 | 0 | 0 |
| d14 | 0 | 0 | 0 |
| d10 | 0 | 0 | 0 |
| d7 | 0 | 0 | 0 |
| d5 | 5 | 3 | 0 |
| d3 | 48 | 4 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 |
| --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| repeat | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d7 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d7-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d5 | 95.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d5-edited | 95.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d3 | 70.0% (0 inv, 0 miss) | 30.0% (0 inv, 0 miss) | 75.0% (0 inv, 0 miss) |
| d3-edited | 80.0% (0 inv, 0 miss) | 25.0% (0 inv, 0 miss) | 60.0% (0 inv, 0 miss) |
| no_image | 0.0% (20 inv, 0 miss) | 0.0% (20 inv, 0 miss) | 0.0% (20 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 100.0% | 100.0% | 100.0% | 100.0% | 77.8% | 38.9% |
| 115 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 66.7% |
| 175 | 100.0% | 100.0% | 100.0% | 100.0% | 94.4% | 61.1% |
| 235 | 100.0% | 100.0% | 100.0% | 100.0% | 91.7% | 50.0% |
| 295 | 100.0% | 100.0% | 100.0% | 100.0% | 95.8% | 62.5% |
| 355 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 61.1% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 100.0% | 100.0% | 100.0% | 100.0% | 77.8% | 11.1% | 9 |
| outer | 100.0% | 100.0% | 100.0% | 100.0% | 95.5% | 40.9% | 11 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 127 to 310 px | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 57.1% | 7 |
| 328 to 431 px | 100.0% | 100.0% | 100.0% | 100.0% | 83.3% | 83.3% | 6 |
| 462 to 677 px | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 57.1% | 7 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 92.4% | 24 |
| 11 | 92.6% | 18 |
| 12 | 89.8% | 18 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 91.1% | 30 |
| dense | 92.2% | 30 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 91.7% | 31 |
| 1-2 | 92.0% | 27 |
| 3-5 | 87.5% | 2 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 85.4% | 8 |
| 2 | 91.7% | 17 |
| 3 | 92.9% | 21 |
| 4 | 94.8% | 8 |
| 5 | 91.7% | 6 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 5 to 49 | 98.3% | 177 |
| 50 to 79 | 96.7% | 181 |
| 80 to 123 | 95.6% | 180 |
| 124 to 616 | 76.4% | 182 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

## Gemini 3.8 Flash

Output tokens per reply, reasoning included: mean 668, median 322.

Answers changed on the repeat: 0.0% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 65.0% | 35.0 [15.0, 55.0], n = 20 | 50.0% | 2 of 20 |
| T2 | 100.0% | 10.0% | 90.0 [75.0, 100.0], n = 20 | 20.0% | 0 of 20 |
| T3 | 100.0% | 50.0% | 50.0 [30.0, 70.0], n = 20 | 55.0% | 0 of 20 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 14 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | inconclusive | 1 | 60 |
| 10 | 6.7 | [1.7, 13.3] | [0.0, 20.0] | inconclusive | 0.12 | 60 |
| 7 | 30.0 | [18.3, 41.7] | [11.7, 51.7] | rejected | 7.6e-06 | 60 |
| 5 | 41.7 | [31.7, 51.7] | [23.3, 60.0] | rejected | 6e-08 | 60 |
| 3 | 66.7 | [56.7, 76.7] | [48.3, 85.0] | rejected | 1.8e-12 | 60 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 14 | -1.7 | [-5.0, 0.0] | [-10.0, 0.0] | no change | 1 | 60 |
| 10 | -6.7 | [-13.3, -1.7] | [-20.0, 0.0] | no change | 0.12 | 60 |
| 7 | -30.0 | [-41.7, -18.3] | [-51.7, -11.7] | drop | 7.6e-06 | 60 |
| 5 | -41.7 | [-51.7, -31.7] | [-60.0, -23.3] | drop | 6e-08 | 60 |
| 3 | -66.7 | [-76.7, -56.7] | [-85.0, -48.3] | drop | 1.8e-12 | 60 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 10 | -6.7 | [-13.3, -1.7] | [-20.0, 0.0] | no change | 0.12 | 60 |
| 7 | -23.3 | [-33.3, -13.3] | [-41.7, -6.7] | drop | 0.00012 | 60 |
| 5 | -41.7 | [-53.3, -30.0] | [-63.3, -21.7] | drop | 6e-08 | 60 |
| 3 | -66.7 | [-76.7, -56.7] | [-85.0, -48.3] | drop | 1.8e-12 | 60 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 15.0 | [0.0, 30.0] | 20 |
| 5 | 15.0 | [0.0, 30.0] | 20 |
| 3 | 50.0 | [30.0, 70.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | -15.0 | [-30.0, 0.0] | 20 |
| 5 | -15.0 | [-30.0, 0.0] | 20 |
| 3 | -50.0 | [-70.0, -30.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -5.0 | [-15.0, 0.0] | 20 |
| 7 | -10.0 | [-25.0, 0.0] | 20 |
| 5 | -30.0 | [-50.0, -10.0] | 20 |
| 3 | -50.0 | [-70.0, -30.0] | 20 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 5.0 | [0.0, 15.0] | 20 |
| 10 | 10.0 | [0.0, 25.0] | 20 |
| 7 | 45.0 | [25.0, 65.0] | 20 |
| 5 | 80.0 | [60.0, 95.0] | 20 |
| 3 | 100.0 | [100.0, 100.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | -5.0 | [-15.0, 0.0] | 20 |
| 10 | -10.0 | [-25.0, 0.0] | 20 |
| 7 | -45.0 | [-65.0, -25.0] | 20 |
| 5 | -80.0 | [-95.0, -60.0] | 20 |
| 3 | -100.0 | [-100.0, -100.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -10.0 | [-25.0, 0.0] | 20 |
| 7 | -45.0 | [-65.0, -25.0] | 20 |
| 5 | -60.0 | [-80.0, -40.0] | 20 |
| 3 | -100.0 | [-100.0, -100.0] | 20 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 10.0 | [0.0, 25.0] | 20 |
| 7 | 30.0 | [10.0, 50.0] | 20 |
| 5 | 30.0 | [10.0, 50.0] | 20 |
| 3 | 50.0 | [30.0, 70.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -10.0 | [-25.0, 0.0] | 20 |
| 7 | -30.0 | [-50.0, -10.0] | 20 |
| 5 | -30.0 | [-50.0, -10.0] | 20 |
| 3 | -50.0 | [-70.0, -30.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -5.0 | [-15.0, 0.0] | 20 |
| 7 | -15.0 | [-30.0, 0.0] | 20 |
| 5 | -35.0 | [-55.0, -15.0] | 20 |
| 3 | -50.0 | [-70.0, -30.0] | 20 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | supported | inconclusive | inconclusive | rejected | rejected | rejected |
| color tasks | 5 pp | supported | supported | inconclusive | inconclusive | rejected | rejected | rejected |
| color tasks | 10 pp | supported | supported | inconclusive | inconclusive | rejected | rejected | rejected |

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 18 | 22.2% |
| T2 | 20 | 3.7 |
| T3 | 20 | 50.0% |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 2 | 0 | 0 |
| without image | 2 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 100.0% | 0.0% | 100.0% | 0.0% |
| d14 | 100.0% | 0.0% | 100.0% | 0.0% |
| d10 | 100.0% | 5.0% | 100.0% | 15.0% |
| d7 | 95.0% | 20.0% | 100.0% | 45.0% |
| d5 | 90.0% | 35.0% | 90.0% | 55.0% |
| d3 | 100.0% | 100.0% | 100.0% | 100.0% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 0 | 0 | 0 |
| d14 | 1 | 0 | 0 |
| d10 | 8 | 0 | 0 |
| d7 | 29 | 3 | 0 |
| d5 | 44 | 4 | 2 |
| d3 | 80 | 0 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 |
| --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| repeat | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14 | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10 | 100.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) |
| d10-edited | 95.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d7 | 85.0% (0 inv, 0 miss) | 55.0% (0 inv, 0 miss) | 70.0% (0 inv, 0 miss) |
| d7-edited | 90.0% (0 inv, 0 miss) | 55.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) |
| d5 | 85.0% (0 inv, 0 miss) | 20.0% (2 inv, 0 miss) | 70.0% (0 inv, 0 miss) |
| d5-edited | 70.0% (0 inv, 0 miss) | 40.0% (0 inv, 0 miss) | 65.0% (0 inv, 0 miss) |
| d3 | 50.0% (0 inv, 0 miss) | 0.0% (0 inv, 0 miss) | 50.0% (0 inv, 0 miss) |
| d3-edited | 50.0% (0 inv, 0 miss) | 0.0% (0 inv, 0 miss) | 50.0% (0 inv, 0 miss) |
| no_image | 65.0% (2 inv, 0 miss) | 10.0% (0 inv, 0 miss) | 50.0% (0 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 100.0% | 100.0% | 100.0% | 66.7% | 55.6% | 33.3% |
| 115 | 100.0% | 100.0% | 100.0% | 83.3% | 66.7% | 33.3% |
| 175 | 100.0% | 100.0% | 88.9% | 55.6% | 38.9% | 33.3% |
| 235 | 100.0% | 95.8% | 75.0% | 62.5% | 62.5% | 33.3% |
| 295 | 100.0% | 100.0% | 100.0% | 79.2% | 54.2% | 33.3% |
| 355 | 100.0% | 100.0% | 100.0% | 94.4% | 72.2% | 33.3% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 100.0% | 94.4% | 88.9% | 38.9% | 11.1% | 0.0% | 9 |
| outer | 100.0% | 100.0% | 90.9% | 68.2% | 45.5% | 0.0% | 11 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 127 to 310 px | 100.0% | 100.0% | 85.7% | 85.7% | 57.1% | 0.0% | 7 |
| 328 to 431 px | 100.0% | 100.0% | 100.0% | 83.3% | 100.0% | 0.0% | 6 |
| 462 to 677 px | 100.0% | 100.0% | 100.0% | 71.4% | 42.9% | 0.0% | 7 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 76.0% | 24 |
| 11 | 78.7% | 18 |
| 12 | 74.1% | 18 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 75.6% | 30 |
| dense | 76.9% | 30 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 78.0% | 31 |
| 1-2 | 74.1% | 27 |
| 3-5 | 79.2% | 2 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 62.5% | 8 |
| 2 | 77.5% | 17 |
| 3 | 77.4% | 21 |
| 4 | 79.2% | 8 |
| 5 | 83.3% | 6 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 63 to 236 | 75.0% | 180 |
| 238 to 395 | 78.7% | 178 |
| 396 to 705 | 83.5% | 182 |
| 706 to 9519 | 67.8% | 180 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

## GPT-6.1 Sol

Output tokens per reply, reasoning included: mean 30, median 22.

Answers changed on the repeat: 1.7% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 65.0% | 35.0 [15.0, 55.0], n = 20 | 50.0% | 0 of 20 |
| T2 | 95.0% | 0.0% | 95.0 [85.0, 100.0], n = 20 | 20.0% | 20 of 20 |
| T3 | 100.0% | 55.0% | 45.0 [25.0, 65.0], n = 20 | 55.0% | 3 of 20 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 20 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | inconclusive | 1 | 60 |
| 14 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 10 | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 7 | 3.3 | [0.0, 8.3] | [0.0, 13.3] | inconclusive | 0.5 | 60 |
| 5 | 11.7 | [5.0, 20.0] | [0.0, 26.7] | inconclusive | 0.016 | 60 |
| 3 | 40.0 | [28.3, 51.7] | [20.0, 60.0] | rejected | 1.2e-07 | 60 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 20 | 0.0 | [-5.0, 5.0] | [-8.3, 8.3] | no change | 1 | 60 |
| 14 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 10 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 7 | -1.7 | [-6.7, 3.3] | [-11.7, 8.3] | no change | 1 | 60 |
| 5 | -10.0 | [-18.3, -1.7] | [-26.7, 3.3] | no change | 0.07 | 60 |
| 3 | -40.0 | [-51.7, -28.3] | [-60.0, -20.0] | drop | 1.2e-07 | 60 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 20 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 14 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | no change | 1 | 60 |
| 10 | -1.7 | [-6.7, 3.3] | [-13.3, 8.3] | no change | 1 | 60 |
| 7 | -3.3 | [-8.3, 0.0] | [-13.3, 0.0] | no change | 0.5 | 60 |
| 5 | -15.0 | [-23.3, -6.7] | [-31.7, -1.7] | drop | 0.0039 | 60 |
| 3 | -40.0 | [-53.3, -26.7] | [-61.7, -16.7] | drop | 8e-07 | 60 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 5.0 | [0.0, 15.0] | 20 |
| 3 | 30.0 | [10.0, 50.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -5.0 | [-15.0, 0.0] | 20 |
| 3 | -30.0 | [-50.0, -10.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 0.0 | [0.0, 0.0] | 20 |
| 3 | -30.0 | [-50.0, -10.0] | 20 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 5.0 | [0.0, 15.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | 15.0 | [0.0, 30.0] | 20 |
| 3 | 65.0 | [45.0, 85.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 5.0 | [0.0, 15.0] | 20 |
| 20 | 0.0 | [-15.0, 15.0] | 20 |
| 14 | 5.0 | [0.0, 15.0] | 20 |
| 10 | 5.0 | [0.0, 15.0] | 20 |
| 7 | 5.0 | [0.0, 15.0] | 20 |
| 5 | -10.0 | [-30.0, 10.0] | 20 |
| 3 | -65.0 | [-85.0, -45.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 5.0 | [0.0, 15.0] | 20 |
| 20 | 5.0 | [0.0, 15.0] | 20 |
| 14 | 5.0 | [0.0, 15.0] | 20 |
| 10 | 0.0 | [-15.0, 15.0] | 20 |
| 7 | 0.0 | [0.0, 0.0] | 20 |
| 5 | -30.0 | [-50.0, -10.0] | 20 |
| 3 | -50.0 | [-75.0, -25.0] | 20 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | 10.0 | [0.0, 25.0] | 20 |
| 5 | 15.0 | [0.0, 30.0] | 20 |
| 3 | 25.0 | [10.0, 45.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 0.0 | [0.0, 0.0] | 20 |
| 7 | -10.0 | [-25.0, 0.0] | 20 |
| 5 | -15.0 | [-30.0, 0.0] | 20 |
| 3 | -25.0 | [-45.0, -10.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -5.0 | [-15.0, 0.0] | 20 |
| 7 | -10.0 | [-25.0, 0.0] | 20 |
| 5 | -15.0 | [-30.0, 0.0] | 20 |
| 3 | -40.0 | [-60.0, -20.0] | 20 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | inconclusive | supported | supported | inconclusive | inconclusive | rejected |
| color tasks | 5 pp | supported | inconclusive | supported | supported | inconclusive | inconclusive | rejected |
| color tasks | 10 pp | supported | inconclusive | supported | supported | inconclusive | inconclusive | rejected |

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 20 | 15.0% |
| T2 | 0 | - |
| T3 | 17 | 70.6% |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 0 | 0 | 0 |
| without image | 23 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 100.0% | 0.0% | 100.0% | 0.0% |
| d14 | 100.0% | 0.0% | 100.0% | 0.0% |
| d10 | 100.0% | 0.0% | 100.0% | 5.0% |
| d7 | 100.0% | 0.0% | 100.0% | 20.0% |
| d5 | 100.0% | 5.0% | 100.0% | 30.0% |
| d3 | 100.0% | 60.0% | 100.0% | 65.0% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 1 | 0 | 0 |
| d14 | 0 | 0 | 0 |
| d10 | 2 | 0 | 0 |
| d7 | 5 | 0 | 0 |
| d5 | 13 | 4 | 0 |
| d3 | 50 | 0 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 |
| --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| repeat | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d14-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d10-edited | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d7 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) |
| d7-edited | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) |
| d5 | 95.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) |
| d5-edited | 100.0% (0 inv, 0 miss) | 65.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) |
| d3 | 70.0% (0 inv, 0 miss) | 30.0% (0 inv, 0 miss) | 75.0% (0 inv, 0 miss) |
| d3-edited | 70.0% (0 inv, 0 miss) | 45.0% (0 inv, 0 miss) | 60.0% (0 inv, 0 miss) |
| no_image | 65.0% (0 inv, 0 miss) | 0.0% (20 inv, 0 miss) | 55.0% (3 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 100.0% | 100.0% | 100.0% | 94.4% | 94.4% | 55.6% |
| 115 | 100.0% | 100.0% | 100.0% | 100.0% | 83.3% | 77.8% |
| 175 | 100.0% | 100.0% | 100.0% | 100.0% | 83.3% | 50.0% |
| 235 | 100.0% | 100.0% | 95.8% | 87.5% | 79.2% | 66.7% |
| 295 | 100.0% | 100.0% | 100.0% | 100.0% | 95.8% | 58.3% |
| 355 | 94.4% | 100.0% | 94.4% | 94.4% | 77.8% | 38.9% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 100.0% | 100.0% | 94.4% | 94.4% | 61.1% | 16.7% | 9 |
| outer | 95.5% | 100.0% | 100.0% | 100.0% | 86.4% | 54.5% | 11 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 127 to 310 px | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 42.9% | 7 |
| 328 to 431 px | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 50.0% | 6 |
| 462 to 677 px | 100.0% | 100.0% | 100.0% | 100.0% | 85.7% | 28.6% | 7 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 90.6% | 24 |
| 11 | 90.7% | 18 |
| 12 | 87.0% | 18 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 91.7% | 30 |
| dense | 87.5% | 30 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 92.5% | 31 |
| 1-2 | 85.8% | 27 |
| 3-5 | 95.8% | 2 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 84.4% | 8 |
| 2 | 88.7% | 17 |
| 3 | 90.1% | 21 |
| 4 | 92.7% | 8 |
| 5 | 93.1% | 6 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 5 to 22 | 93.6% | 359 |
| 23 to 33 | 89.5% | 171 |
| 34 to 275 | 82.1% | 190 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

## Qwen3.8-27B

Output tokens per reply, reasoning included: mean 365, median 303.

Answers changed on the repeat: 0.0% (mean over tasks).

### Baseline check

| Task | Accuracy, original | Accuracy, no image | Gain (95% interval) | Bar | Invalid without image |
| --- | --- | --- | --- | --- | --- |
| T1 | 100.0% | 60.0% | 40.0 [20.0, 60.0], n = 20 | 50.0% | 0 of 20 |
| T2 | 100.0% | 20.0% | 80.0 [60.0, 95.0], n = 20 | 20.0% | 2 of 20 |
| T3 | 100.0% | 50.0% | 50.0 [30.0, 70.0], n = 20 | 55.0% | 0 of 20 |

Invalid includes refusals: without the image, some models decline to answer, and that counts as wrong.

### Color tasks (T1, T2, T3)

| Answer change | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | supported | 1 | 60 |
| 20 | 1.7 | [0.0, 5.0] | [0.0, 10.0] | inconclusive | 1 | 60 |
| 14 | 5.0 | [0.0, 11.7] | [0.0, 16.7] | inconclusive | 0.25 | 60 |
| 10 | 20.0 | [10.0, 30.0] | [5.0, 38.3] | inconclusive | 0.00049 | 60 |
| 7 | 36.7 | [25.0, 48.3] | [16.7, 56.7] | rejected | 4.8e-07 | 60 |
| 5 | 43.3 | [31.7, 55.0] | [23.3, 61.7] | rejected | 3e-08 | 60 |
| 3 | 58.3 | [46.7, 70.0] | [38.3, 78.3] | rejected | 5.8e-11 | 60 |

| Accuracy, recolored | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | -1.7 | [-5.0, 0.0] | [-10.0, 0.0] | no change | 1 | 60 |
| 14 | -5.0 | [-11.7, 0.0] | [-16.7, 0.0] | no change | 0.25 | 60 |
| 10 | -20.0 | [-30.0, -10.0] | [-38.3, -5.0] | drop | 0.00049 | 60 |
| 7 | -36.7 | [-48.3, -25.0] | [-56.7, -16.7] | drop | 4.8e-07 | 60 |
| 5 | -43.3 | [-55.0, -31.7] | [-61.7, -23.3] | drop | 3e-08 | 60 |
| 3 | -58.3 | [-70.0, -46.7] | [-78.3, -38.3] | drop | 5.8e-11 | 60 |

| Accuracy, edited | Difference (pp) | 95% interval | Corrected interval | Decision | Sign test p | n |
| --- | --- | --- | --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | [0.0, 0.0] | no change | 1 | 60 |
| 20 | -1.7 | [-5.0, 0.0] | [-8.3, 0.0] | no change | 1 | 60 |
| 14 | -6.7 | [-13.3, -1.7] | [-20.0, 0.0] | no change | 0.12 | 60 |
| 10 | -18.3 | [-28.3, -8.3] | [-36.7, -3.3] | drop | 0.00098 | 60 |
| 7 | -28.3 | [-40.0, -16.7] | [-50.0, -10.0] | drop | 1.5e-05 | 60 |
| 5 | -60.0 | [-71.7, -48.3] | [-78.3, -40.0] | drop | 2.9e-11 | 60 |
| 3 | -61.7 | [-71.7, -51.7] | [-80.0, -43.3] | drop | 1.5e-11 | 60 |

### T1 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 5.0 | [0.0, 15.0] | 20 |
| 10 | 15.0 | [0.0, 30.0] | 20 |
| 7 | 20.0 | [5.0, 40.0] | 20 |
| 5 | 10.0 | [0.0, 25.0] | 20 |
| 3 | 45.0 | [25.0, 65.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | -5.0 | [-15.0, 0.0] | 20 |
| 10 | -15.0 | [-30.0, 0.0] | 20 |
| 7 | -20.0 | [-40.0, -5.0] | 20 |
| 5 | -10.0 | [-25.0, 0.0] | 20 |
| 3 | -45.0 | [-65.0, -25.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | -5.0 | [-15.0, 0.0] | 20 |
| 10 | -15.0 | [-30.0, 0.0] | 20 |
| 7 | -20.0 | [-40.0, -5.0] | 20 |
| 5 | -45.0 | [-65.0, -25.0] | 20 |
| 3 | -45.0 | [-65.0, -25.0] | 20 |

### T2 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | 25.0 | [5.0, 45.0] | 20 |
| 7 | 55.0 | [35.0, 75.0] | 20 |
| 5 | 65.0 | [45.0, 85.0] | 20 |
| 3 | 85.0 | [70.0, 100.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | 0.0 | [0.0, 0.0] | 20 |
| 10 | -25.0 | [-45.0, -5.0] | 20 |
| 7 | -55.0 | [-75.0, -35.0] | 20 |
| 5 | -65.0 | [-85.0, -45.0] | 20 |
| 3 | -85.0 | [-100.0, -70.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 0.0 | [0.0, 0.0] | 20 |
| 14 | -10.0 | [-25.0, 0.0] | 20 |
| 10 | -25.0 | [-45.0, -10.0] | 20 |
| 7 | -40.0 | [-60.0, -20.0] | 20 |
| 5 | -90.0 | [-100.0, -75.0] | 20 |
| 3 | -95.0 | [-100.0, -85.0] | 20 |

### T3 alone (descriptive)

| Answer change | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | 5.0 | [0.0, 15.0] | 20 |
| 14 | 10.0 | [0.0, 25.0] | 20 |
| 10 | 20.0 | [5.0, 40.0] | 20 |
| 7 | 35.0 | [15.0, 55.0] | 20 |
| 5 | 55.0 | [35.0, 75.0] | 20 |
| 3 | 45.0 | [25.0, 65.0] | 20 |

| Accuracy, recolored | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | -5.0 | [-15.0, 0.0] | 20 |
| 14 | -10.0 | [-25.0, 0.0] | 20 |
| 10 | -20.0 | [-40.0, -5.0] | 20 |
| 7 | -35.0 | [-55.0, -15.0] | 20 |
| 5 | -55.0 | [-75.0, -35.0] | 20 |
| 3 | -45.0 | [-65.0, -25.0] | 20 |

| Accuracy, edited | Difference (pp) | 95% interval | n |
| --- | --- | --- | --- |
| 52 (reassigned) | 0.0 | [0.0, 0.0] | 20 |
| 20 | -5.0 | [-15.0, 0.0] | 20 |
| 14 | -5.0 | [-15.0, 0.0] | 20 |
| 10 | -15.0 | [-30.0, 0.0] | 20 |
| 7 | -25.0 | [-45.0, -10.0] | 20 |
| 5 | -45.0 | [-65.0, -25.0] | 20 |
| 3 | -45.0 | [-65.0, -25.0] | 20 |

### H1 under other margins (descriptive)

| Task set | Margin | 52 (reassigned) | 20 | 14 | 10 | 7 | 5 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color tasks | 2.5 pp | supported | inconclusive | inconclusive | rejected | rejected | rejected | rejected |
| color tasks | 5 pp | supported | inconclusive | inconclusive | inconclusive | rejected | rejected | rejected |
| color tasks | 10 pp | supported | inconclusive | inconclusive | inconclusive | rejected | rejected | rejected |

### Answers without the image (descriptive)

| Task | Valid replies | Yes, or mean count |
| --- | --- | --- |
| T1 | 20 | 20.0% |
| T2 | 18 | 2.9 |
| T3 | 20 | 10.0% |

### Invalid replies by kind (descriptive)

| Drawing | No answer line | Truncated | Blocked |
| --- | --- | --- | --- |
| with image | 0 | 0 | 0 |
| without image | 2 | 0 | 0 |

### Yes answers by correct answer on the controlled palettes (descriptive)

| Recoloring | T1, answer yes | T1, answer no | T3, answer yes | T3, answer no |
| --- | --- | --- | --- | --- |
| d20 | 100.0% | 0.0% | 95.0% | 5.0% |
| d14 | 100.0% | 10.0% | 100.0% | 15.0% |
| d10 | 85.0% | 15.0% | 100.0% | 35.0% |
| d7 | 100.0% | 40.0% | 95.0% | 55.0% |
| d5 | 85.0% | 40.0% | 85.0% | 85.0% |
| d3 | 95.0% | 85.0% | 100.0% | 90.0% |

Cells: share of valid answers that are yes.

### Error directions on the controlled palettes (exploratory)

| Recoloring | False yes or overcount | False no or undercount | Invalid |
| --- | --- | --- | --- |
| d20 | 1 | 1 | 0 |
| d14 | 7 | 0 | 0 |
| d10 | 19 | 4 | 0 |
| d7 | 35 | 4 | 0 |
| d5 | 50 | 12 | 0 |
| d3 | 70 | 2 | 0 |

### Accuracy per condition and task

| Condition | T1 | T2 | T3 |
| --- | --- | --- | --- |
| original | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| repeat | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| reassigned | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) |
| d20 | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d20-edited | 100.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d14 | 95.0% (0 inv, 0 miss) | 100.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) |
| d14-edited | 95.0% (0 inv, 0 miss) | 90.0% (0 inv, 0 miss) | 95.0% (0 inv, 0 miss) |
| d10 | 85.0% (0 inv, 0 miss) | 75.0% (0 inv, 0 miss) | 80.0% (0 inv, 0 miss) |
| d10-edited | 85.0% (0 inv, 0 miss) | 75.0% (0 inv, 0 miss) | 85.0% (0 inv, 0 miss) |
| d7 | 80.0% (0 inv, 0 miss) | 45.0% (0 inv, 0 miss) | 65.0% (0 inv, 0 miss) |
| d7-edited | 80.0% (0 inv, 0 miss) | 60.0% (0 inv, 0 miss) | 75.0% (0 inv, 0 miss) |
| d5 | 90.0% (0 inv, 0 miss) | 35.0% (0 inv, 0 miss) | 45.0% (0 inv, 0 miss) |
| d5-edited | 55.0% (0 inv, 0 miss) | 10.0% (0 inv, 0 miss) | 55.0% (0 inv, 0 miss) |
| d3 | 55.0% (0 inv, 0 miss) | 15.0% (0 inv, 0 miss) | 55.0% (0 inv, 0 miss) |
| d3-edited | 55.0% (0 inv, 0 miss) | 5.0% (0 inv, 0 miss) | 55.0% (0 inv, 0 miss) |
| no_image | 60.0% (0 inv, 0 miss) | 20.0% (2 inv, 0 miss) | 50.0% (0 inv, 0 miss) |

Cells: accuracy, then invalid and missing replies.

### Accuracy by base hue (exploratory)

| Base hue | d20 | d14 | d10 | d7 | d5 | d3 |
| --- | --- | --- | --- | --- | --- | --- |
| 55 | 94.4% | 100.0% | 83.3% | 61.1% | 55.6% | 38.9% |
| 115 | 100.0% | 100.0% | 94.4% | 94.4% | 61.1% | 44.4% |
| 175 | 94.4% | 88.9% | 72.2% | 55.6% | 33.3% | 33.3% |
| 235 | 100.0% | 83.3% | 66.7% | 62.5% | 41.7% | 33.3% |
| 295 | 100.0% | 95.8% | 83.3% | 62.5% | 50.0% | 45.8% |
| 355 | 100.0% | 100.0% | 88.9% | 72.2% | 50.0% | 44.4% |

### T2 accuracy by the position of u's color in the controlled palette (exploratory)

| u's color | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| middle | 100.0% | 94.4% | 61.1% | 44.4% | 16.7% | 0.0% | 9 |
| outer | 100.0% | 95.5% | 86.4% | 59.1% | 27.3% | 18.2% | 11 |

Each cell pools the recolored and the edited drawing.

### T1 accuracy by the spatial separation of u and v in the drawing (exploratory)

Drawings where u and v have adjacent, different colors of a controlled palette.

| Distance between u and v | d20 | d14 | d10 | d7 | d5 | d3 | Items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 127 to 310 px | 100.0% | 100.0% | 85.7% | 57.1% | 71.4% | 14.3% | 7 |
| 328 to 431 px | 100.0% | 66.7% | 83.3% | 33.3% | 66.7% | 16.7% | 6 |
| 462 to 677 px | 100.0% | 100.0% | 85.7% | 85.7% | 42.9% | 14.3% | 7 |

### Accuracy on the controlled palettes by properties of the drawing (exploratory)

| nodes | Accuracy | Items |
| --- | --- | --- |
| 10 | 71.5% | 24 |
| 11 | 72.2% | 18 |
| 12 | 70.8% | 18 |

| edge band | Accuracy | Items |
| --- | --- | --- |
| sparse | 69.7% | 30 |
| dense | 73.3% | 30 |

| crossings | Accuracy | Items |
| --- | --- | --- |
| 0 | 72.6% | 31 |
| 1-2 | 70.4% | 27 |
| 3-5 | 70.8% | 2 |

| edited node degree | Accuracy | Items |
| --- | --- | --- |
| 1 | 59.4% | 8 |
| 2 | 75.0% | 17 |
| 3 | 71.0% | 21 |
| 4 | 76.0% | 8 |
| 5 | 73.6% | 6 |

### Accuracy on the controlled palettes by output tokens (exploratory)

| Output tokens | Accuracy | Replies |
| --- | --- | --- |
| 55 to 217 | 77.8% | 176 |
| 218 to 324 | 77.2% | 184 |
| 325 to 463 | 69.4% | 180 |
| 466 to 3350 | 61.7% | 180 |

Rows are quartiles of this model's replies on the controlled palettes; tied token counts share a row.

## Parser against hand coding

172 of 172 distinct replies hand coded, 0 not yet; 0 disagree with the parser; 0 queries have no reply. The parser check passes.


