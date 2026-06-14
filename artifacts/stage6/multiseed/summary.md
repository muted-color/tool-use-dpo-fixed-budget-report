# Stage6 Seed Stability Summary

Status: `complete_source_axis_sign_stable`

## Completion

- `s6r002` noised_gold seed2: `pass`, best_step=350, best_eval_loss=0.026467
- `s6r003` noised_gold seed3: `pass`, best_step=300, best_eval_loss=0.030456
- `s6r004` behavior seed2: `pass`, best_step=375, best_eval_loss=0.000675
- `s6r005` behavior seed3: `pass`, best_step=375, best_eval_loss=0.000744

## Best-Adapter Metrics

| run | condition | BFCL | When2Call acc | When2Call F1 | FunctionChat | IFEval |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| s6r002 | noised_gold | 0.7000 | 0.5833 | 0.4828 | 0.8500 | 0.7044 |
| s6r003 | noised_gold | 0.6933 | 0.5867 | 0.4828 | 0.8500 | 0.7107 |
| s6r004 | behavior | 0.6633 | 0.6433 | 0.5335 | 0.8100 | 0.7107 |
| s6r005 | behavior | 0.6633 | 0.6467 | 0.5333 | 0.8000 | 0.7170 |

## Stage6 Seed Means

| condition | BFCL mean | When2Call acc mean | When2Call F1 mean | BFCL range | When2Call F1 range |
| --- | ---: | ---: | ---: | ---: | ---: |
| noised_gold | 0.6967 | 0.5850 | 0.4828 | 0.0067 | 0.0000 |
| behavior | 0.6633 | 0.6450 | 0.5334 | 0.0000 | 0.0002 |

## Source-Axis Signs

Checked sign rows: 18
Sign failures: 0

| comparison | checkpoint | BFCL delta | When2Call acc delta | When2Call F1 delta |
| --- | --- | ---: | ---: | ---: |
| original | step50 | 0.0333 | -0.0667 | -0.0531 |
| original | best | 0.0333 | -0.0633 | -0.0483 |
| stage6_seed2 | step50 | 0.0400 | -0.0500 | -0.0426 |
| stage6_seed2 | best | 0.0367 | -0.0600 | -0.0508 |
| stage6_seed3 | step50 | 0.0300 | -0.0633 | -0.0489 |
| stage6_seed3 | best | 0.0300 | -0.0600 | -0.0506 |

All original, seed2, and seed3 source-axis signs match the expected pattern.
