# Stage6 Report: Multi-Seed Robustness

Date: 2026-06-13

Runs: `s6r001`-`s6r007`

Status: `complete_source_axis_sign_stable`

Canonical artifacts:

- Stage6 design: `experiments/exp_11_stage6_multiseed_robustness/stage6_design.md`
- Stage6 notes: `experiments/exp_11_stage6_multiseed_robustness/notes.md`
- Wave 1 decision: `experiments/exp_11_stage6_multiseed_robustness/artifacts/analysis/s6r006_wave1_probe_decision/`
- Final seed-stability summary: `experiments/exp_11_stage6_multiseed_robustness/artifacts/analysis/s6r007_seed_stability_summary/`
- Final summary report: `experiments/exp_11_stage6_multiseed_robustness/artifacts/analysis/s6r007_seed_stability_summary/summary.md`

## One-Line Result

Stage6 adds two additional DPO training seeds for each main clean condition and finds that the source-axis direction is stable: clean noised_gold remains stronger on BFCL, while clean behavior remains stronger on When2Call. This supports a conference-extension seed-stability table, while keeping bootstrap uncertainty separate from training-seed variation.

## Question

Stage6 asks:

```text
Are the Stage3d source-axis patterns for clean noised_gold and clean behavior consistent across additional DPO training seeds?
```

Final answer:

```text
Yes for the scoped sign-stability claim. Across original, seed2, and seed3 comparisons, BFCL favors noised_gold and When2Call favors behavior with 0 sign failures.
```

## Run Summary

| Run | Role | Status | Key result |
|---|---|---|---|
| `s6r001` | Stage opening/design | `complete` | Stage6 staged-probe plan opened |
| `s6r002` | noised_gold clean seed2 | `pass` | 375 train steps, step50 and best eval complete |
| `s6r004` | behavior clean seed2 | `pass` | 375 train steps, step50 and best eval complete |
| `s6r006` | Wave1 decision | `continue_wave2` | 12 sign rows, 0 failures |
| `s6r003` | noised_gold clean seed3 | `pass` | 375 train steps, step50 and best eval complete |
| `s6r005` | behavior clean seed3 | `pass` | 375 train steps, step50 and best eval complete |
| `s6r007` | final seed-stability summary | `complete_source_axis_sign_stable` | 18 sign rows, 0 failures |

## Training Setup

All Stage6 DPO runs keep the Stage3d recipe fixed and vary only the DPO training seed.

| Field | Value |
|---|---:|
| model | `Qwen/Qwen3-8B` |
| SFT reference | `r004/full_sft_best_adapter` |
| pair budget | 3000 |
| DPO beta | 0.1 |
| learning rate | 5e-6 |
| micro batch | 4 |
| gradient accumulation | 2 |
| effective batch | 8 |
| optimizer steps | 375 |
| required eval points | `checkpoint_step_0050`, `dpo_best_adapter` |

The fixed pair pools are `r026/pairs_noised_gold_clean_3k.jsonl` for noised_gold and `r027b/pairs_behavior_clean_3k.jsonl` for behavior.

## Best-Adapter Results

| Run | Condition | BFCL | When2Call acc | When2Call F1 | FunctionChat | IFEval |
|---|---|---:|---:|---:|---:|---:|
| `s6r002` | noised_gold seed2 | 0.7000 | 0.5833 | 0.4828 | 0.8500 | 0.7044 |
| `s6r003` | noised_gold seed3 | 0.6933 | 0.5867 | 0.4828 | 0.8500 | 0.7107 |
| `s6r004` | behavior seed2 | 0.6633 | 0.6433 | 0.5335 | 0.8100 | 0.7107 |
| `s6r005` | behavior seed3 | 0.6633 | 0.6467 | 0.5333 | 0.8000 | 0.7170 |

Stage6 seed means:

| Condition | BFCL mean | When2Call acc mean | When2Call F1 mean | BFCL range | When2Call F1 range |
|---|---:|---:|---:|---:|---:|
| noised_gold | 0.6967 | 0.5850 | 0.4828 | 0.0067 | 0.0000 |
| behavior | 0.6633 | 0.6450 | 0.5334 | 0.0000 | 0.0002 |

Interpretation: the observed seed-to-seed range is small for the main sign-stability metrics in this scoped two-additional-seed check.

## Source-Axis Sign Stability

The sign check uses `noised_gold - behavior`.

Expected signs:

| Metric | Expected sign | Interpretation |
|---|---:|---|
| BFCL core accuracy | positive | noised_gold should be higher |
| When2Call behavior accuracy | negative | behavior should be higher |
| When2Call macro F1 | negative | behavior should be higher |

Observed deltas:

| Comparison | Checkpoint | BFCL delta | When2Call acc delta | When2Call F1 delta |
|---|---|---:|---:|---:|
| original | step50 | +0.0333 | -0.0667 | -0.0531 |
| original | best | +0.0333 | -0.0633 | -0.0483 |
| Stage6 seed2 | step50 | +0.0400 | -0.0500 | -0.0426 |
| Stage6 seed2 | best | +0.0367 | -0.0600 | -0.0508 |
| Stage6 seed3 | step50 | +0.0300 | -0.0633 | -0.0489 |
| Stage6 seed3 | best | +0.0300 | -0.0600 | -0.0506 |

Summary:

```text
checked sign rows: 18
missing inputs: 0
sign failures: 0
```

## Paper Decision

Stage6 is ready to include as a short conference-extension robustness table. It should be described narrowly:

- The source-axis direction is stable across three total seeds per main clean condition.
- The result supports the Stage3d interpretation that noised_gold and behavior clean DPO move different axes.
- Seed summaries should be reported separately from grouped bootstrap intervals.

Do not claim:

- data-sampling robustness, because pair pools were fixed;
- mixed-source robustness, because Stage5 is a separate appendix/reviewer-defense ablation;
- intrinsic source superiority, because noised_gold and behavior still differ in dataset family and task axis;
- a merged bootstrap-plus-seed uncertainty interval without a hierarchical method.

## Practical Takeaway

Stage6 closes the main training-seed robustness question for the two clean Stage3d conditions. The strongest defensible claim is sign stability, not universal source superiority: clean noised_gold consistently favors BFCL, and clean behavior consistently favors When2Call under the fixed Stage3d DPO recipe.
