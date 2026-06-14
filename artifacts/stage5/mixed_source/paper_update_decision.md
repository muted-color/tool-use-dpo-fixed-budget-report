# s5r004 Paper Update Decision

Status: `complete`

Created: 2026-06-12T13:37:12+09:00

## Decision

Use Stage5 as an appendix or reviewer-defense mixed-source ablation. Do not promote it as a main-text Pareto-improvement result.

Decision label: `appendix_reviewer_defense_ablation`

## Rationale

`s5r002` answers the reviewer-style question: a fixed-budget 1500 noised_gold clean plus 1500 behavior clean recipe does improve both intended axes versus the `r004` SFT baseline. However, the mixed recipe does not dominate the Stage3d single-source specialists.

Key `s5r003` findings:

- `s5r002` step50 BFCL core is `0.700000`, below `r028` step50 at `0.713333`.
- `s5r002` step50 When2Call macro F1 is `0.512991`, below `r029` step50 at `0.529636`.
- `s5r002` step50 IFEval prompt strict is `0.520833`, below the best single-source step50 prompt-strict value `0.583333`.
- `s5r002` final improves the behavior side relative to mixed step50, but still does not beat the behavior specialist on When2Call macro F1.
- Mixed step50 and final are non-dominated under the selected three-axis view, but non-dominated is weaker than Pareto dominance or material frontier improvement.

## Paper Treatment

Recommended placement:

- Put Stage5 in appendix or a short reviewer-defense paragraph.
- Label it explicitly as a post-Stage4 extension.
- Keep the main paper claim focused on source-native axis-specific movement and checkpoint-sensitive guardrail reporting.

Allowed wording:

> As a post-hoc reviewer-defense ablation, we also tested a fixed-budget mixed clean recipe with 1500 noised_gold and 1500 behavior negatives. The mixed recipe improved both intended axes over the SFT baseline but did not dominate the single-source specialists, and it retained material IFEval regression. We therefore treat it as an axis-averaging ablation rather than a new Pareto-frontier claim.

Disallowed wording:

- `Mixed-source DPO improves the Pareto frontier.`
- `Mixed clean DPO dominates the single-source recipes.`
- `Mixed-source is generally best.`
- `Stage5 is part of the original Stage4 evidence.`

## Required Follow-up

No further Stage5 experiments are required for this decision. If the paper is edited, update the run inventory and appendix table to reference:

- `s5r002` training/eval summary.
- `s5r003` mixed-vs-single-source analysis package.
- This `s5r004` decision.

## Final Stage5 Status

Stage5 is complete.
