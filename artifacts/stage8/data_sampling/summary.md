# Stage8 Pool-B Robustness Summary

Status: `complete_data_sampling_source_axis_sign_stable`

## Completion

- `s8r005` noised_gold_clean_3k_pool_b: `pass`, best_step=375, best_eval_loss=0.0193102
- `s8r006` behavior_clean_3k_pool_b: `pass`, best_step=375, best_eval_loss=0.000758154

## Pool-B Gates

| run | source | selected | accept | suspect | pair overlap | content overlap | prompt overlap |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| s8r002 | noised_gold | 3000 | 0.97 | 0.01 | 0 | 0 | 401 |
| s8r003c | behavior | 3000 | 0.99 | 0.01 | 0 | 0 | 1337 |

## Best-Adapter Metrics

| pool | source | run | BFCL | When2Call acc | When2Call F1 | FunctionChat | IFEval |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| pool_a_original | noised_gold | r028 | 0.6933 | 0.5767 | 0.4795 | 0.8500 | 0.7044 |
| pool_a_original | behavior | r029 | 0.6600 | 0.6400 | 0.5278 | 0.8000 | 0.7170 |
| pool_b_replicate | noised_gold | s8r005 | 0.7033 | 0.5767 | 0.4746 | 0.8500 | 0.7107 |
| pool_b_replicate | behavior | s8r006 | 0.6633 | 0.6433 | 0.5328 | 0.8000 | 0.7107 |

## Step50 Metrics

| pool | source | run | BFCL | When2Call acc | When2Call F1 | FunctionChat | IFEval |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| pool_a_original | noised_gold | r028 | 0.7133 | 0.5667 | 0.4765 | 0.8400 | 0.7296 |
| pool_a_original | behavior | r029 | 0.6800 | 0.6333 | 0.5296 | 0.8100 | 0.7233 |
| pool_b_replicate | noised_gold | s8r005 | 0.7133 | 0.5700 | 0.4786 | 0.8400 | 0.7107 |
| pool_b_replicate | behavior | s8r006 | 0.6800 | 0.6333 | 0.5290 | 0.8100 | 0.7233 |

## Source-Axis Signs

Checked sign rows: 12
Sign failures: 0

| pool | checkpoint | BFCL delta | When2Call acc delta | When2Call F1 delta |
| --- | --- | ---: | ---: | ---: |
| pool_a_original | step50 | 0.0333 | -0.0667 | -0.0531 |
| pool_a_original | best | 0.0333 | -0.0633 | -0.0483 |
| pool_b_replicate | step50 | 0.0333 | -0.0633 | -0.0504 |
| pool_b_replicate | best | 0.0400 | -0.0667 | -0.0583 |

All pool-A original and pool-B replicate source-axis signs match the expected pattern.

## Paper Decision

Stage8 is ready to cite as scoped data-sampling robustness evidence for the two main clean conditions. It should be kept separate from Stage6 training-seed robustness and should not be described as complete source ranking or source-intrinsic superiority.
