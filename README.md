# Tool-Use DPO Negative Sources

Reproducibility materials for the technical report:

**Reporting Tool-Use DPO Under Fixed Budgets: Recipe--Checkpoint Profiles and
Guardrail Trade-offs**

```text
Base model family: Qwen3
Shared SFT reference: r004
Main DPO/control runs: r028, r029, s3d001, s3d002
Post-hoc support runs: s5r002, s6r002-s6r005, s8r005-s8r006
Primary metrics: BFCL core, When2Call behavior accuracy, When2Call macro F1, IFEval prompt-strict
Main claim: fixed-budget source-native recipe comparison, not source-intrinsic causal ranking
```

The goal here is narrow: make the report's tables, confidence intervals,
overlap checks, and Pareto figures easy to verify from released artifacts.

This is not an end-to-end training release. Full DPO retraining and raw
benchmark reconstruction require upstream dataset access, restricted raw
artifacts, and substantial GPU resources, so they are outside the default public
scope.

## What You Can Check

| Check | Status | Command or file |
|---|---:|---|
| Artifact manifest integrity | Pass | `python scripts/verify_artifacts.py` |
| Contamination/overlap release checks | Pass | `python scripts/verify_overlap.py` |
| Table reproduction | Supported | `python scripts/reproduce_tables.py` |
| Figure reproduction | Supported | `python scripts/reproduce_figures.py` |
| Grouped bootstrap recomputation | Supported | `python scripts/compute_grouped_bootstrap.py --bootstrap-iterations 1000` |
| IFEval bootstrap recomputation | Supported | `python scripts/compute_ifeval_bootstrap.py --bootstrap-iterations 1000` |
| Raw/private data exclusion policy | Documented | `docs/redistribution_policy.md` |

## Contents

- Aggregate CSV/JSON results used in the report tables.
- Sanitized per-example evaluation rows: prompt IDs and hashes, metric flags,
  generated-output hashes, and token counts.
- Pairwise and grouped bootstrap summaries.
- Pareto point tables, figure inputs, and regenerated SVG figures.
- Post-Stage4 mixed-source appendix ablation summaries.
- Stage6 multi-seed source-axis sign-stability summaries.
- Stage7 direct-answer coverage audit and auxiliary direct-answer diagnostics.
- Stage8 independent pair-pool data-sampling robustness summaries.
- Hash-only contamination and train-pool overlap reports.
- Run inventory, benchmark versions, DPO/evaluation config notes, and recovered
  evaluator/parser details.
- Data access, license, redistribution, reference, and claim-scope notes.
- Small scripts for checking the artifacts and regenerating tables/figures.

## Data Boundary

Raw benchmark data, benchmark prompt text, full processed DPO pairs, raw
generated benchmark outputs, private audit materials, credentials, and
model/adapter weights are not redistributed here. See
`docs/redistribution_policy.md` and `docs/data_availability_statement.md`.

## Quick Start

```bash
python -m pip install -e '.[dev]'
python scripts/verify_artifacts.py
python scripts/verify_overlap.py
python scripts/compute_grouped_bootstrap.py --bootstrap-iterations 1000
python scripts/compute_ifeval_bootstrap.py --bootstrap-iterations 1000
python scripts/reproduce_tables.py
python scripts/reproduce_figures.py
pytest
```

These commands reproduce the released tables, bootstrap summaries, and figure
inputs from the files in this repository.

## Repository Layout

```text
artifacts/   Public aggregate artifacts used by the report
configs/     Run inventory, benchmark notes, and artifact manifest
results/     Sanitized per-example and aggregate evaluation outputs
docs/        Reproduction, data access, and claim-scope documentation
scripts/     Reproduction and verification commands
src/         Python package used by the scripts
tests/       Lightweight smoke tests
```

## Main Commands

```bash
python scripts/verify_artifacts.py
```

Checks the artifact manifest and rejects raw/private files that should not be in
the public release.

```bash
python scripts/verify_overlap.py
```

Checks the released Stage1/Stage2 contamination reports and Stage3d train-pool
overlap summaries. If the private pair artifacts are available locally, they can
be recomputed with:

```bash
python scripts/verify_overlap.py --workspace-root .. --write-artifacts
```

```bash
python scripts/compute_grouped_bootstrap.py --bootstrap-iterations 1000
```

Recomputes grouped bootstrap CIs from sanitized per-example primary evaluation
outputs. The bootstrap unit is `prompt_id`; intervals are percentile CIs.

```bash
python scripts/compute_ifeval_bootstrap.py --bootstrap-iterations 1000
```

Recomputes IFEval prompt-strict CIs from sanitized per-example IFEval outputs.
The denominator excludes zero-supported prompts, matching the paper metric.

```bash
python scripts/reproduce_tables.py
```

Rebuilds compact derived tables from the included aggregate artifacts.

```bash
python scripts/reproduce_figures.py
```

Regenerates the public Pareto SVG from `artifacts/stage4/pareto/pareto_points.csv`.

## Evaluation Outputs

`results/per_example/` contains sanitized per-example evaluation outputs. The
files keep prompt IDs/hashes, metric components, parse/schema flags, behavior
labels, token counts, and generated-output hashes. They do not include prompt
text, tool schemas, generated text, or benchmark raw data.

`results/aggregate/` contains absolute and delta metrics used to trace the
reported point estimates.

`artifacts/stage7/direct_answer/` contains the public When2Call direct-answer
coverage audit and auxiliary existing-artifact direct-answer diagnostics. These
files document that the exposed public When2Call labeled splits used here have
0 direct-answer gold rows; they do not replace a matched When2Call
direct-answer slice.

`artifacts/stage8/data_sampling/` contains sanitized fixed summaries for the
independent pool-B replicate. It documents that noised_gold and behavior pool-B
gates passed, DPO/eval completed for `s8r005/s8r006`, and pool-A plus pool-B
source-axis signs matched the expected direction in 12/12 point-estimate sign
checks. It is scoped data-sampling robustness for the two main clean
conditions, not broad distribution robustness or source-intrinsic ranking.

## Citation

Use `CITATION.cff` for citation metadata. Dataset and benchmark attribution
notes are in `docs/data_license_table.md` and `docs/data_and_model_access.md`.

## Notes

- Bootstrap intervals use `prompt_id` as the grouped resampling unit with 1000
  iterations.
- Stage3d comparisons are fixed-budget, source-native recipe comparisons. They
  should not be read as source-intrinsic causal rankings.
- `configs/artifact_manifest.json` records file sizes and SHA-256 hashes for the
  released files.
- `artifacts/stage5/mixed_source/` contains sanitized summary artifacts for the
  post-Stage4 mixed-source appendix ablation; it is reviewer-defense evidence,
  not part of the main Stage4 claim.
- `artifacts/stage6/multiseed/` contains sanitized summary artifacts for the
  post-Stage5 training-seed robustness check. It supports source-axis sign
  stability across fixed pair pools, not data-sampling robustness.
- `artifacts/stage7/direct_answer/` contains the direct-answer coverage audit.
  Stage7 is a scope/coverage diagnostic, not a new DPO training result.
- `artifacts/stage8/data_sampling/` contains sanitized summary artifacts for
  one independent pair-pool data-sampling robustness replicate. It is scoped to
  clean noised_gold and clean behavior.
- The pre-release checklist is summarized in `docs/release_readiness.md`.

## Data Availability Statement

Some raw benchmark and training examples cannot be redistributed because of
license and benchmark-integrity constraints. This repository provides the
metadata, sanitized outputs, aggregate metrics, bootstrap artifacts, and figure
scripts needed to verify the reported results.
