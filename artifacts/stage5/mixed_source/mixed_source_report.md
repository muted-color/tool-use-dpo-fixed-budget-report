# s5r003 Mixed-Source Analysis Report

Status: `complete`

Generated: 2026-06-12T04:11:47+00:00

## Scope

This analysis compares `s5r002` mixed clean DPO against the Stage3d single-source runs `r028`, `r029`, `s3d001`, and `s3d002` under the same 3000-pair / 375-step budget. The mixed condition uses 1500 noised_gold clean rows plus 1500 behavior clean rows.

## Main Result

The mixed run is useful as an axis-averaging extension, but it does not support a clean Pareto-improvement claim.

- Step50 mixed BFCL core is `0.700000`, which is `-0.013333` versus `r028` step50.
- Step50 mixed When2Call macro F1 is `0.512991`, which is `-0.016645` versus `r029` step50.
- Step50 mixed IFEval prompt strict is `0.520833`, which is `-0.052083` versus `r028` step50.
- Final mixed When2Call macro F1 is `0.522456`, which is `-0.005320` versus `r029` final.
- Pareto flags over BFCL core, When2Call macro F1, and IFEval prompt strict: step50=True, final=True.

## Bootstrap Notes

Bootstrap uses grouped sampling by `prompt_id` when available, with `1000` iterations. It estimates evaluation-sample uncertainty only and does not cover training-seed variance.

- `s5r002` step50 BFCL core CI: `0.646667` to `0.756667`.
- `s5r002` final IFEval prompt strict CI: `0.420000` to `0.620000`.

## Interpretation

`s5r002` step50 improves both intended axes versus `r004`, but it trails the noised_gold specialist on BFCL core and has worse IFEval prompt strict than the best single-source step50 point. The final adapter improves behavior/FunctionChat metrics relative to step50, but the IFEval regression remains material.

Recommended decision: report as a reviewer-defense mixed-source ablation or appendix result, not as a main Pareto-frontier improvement.
