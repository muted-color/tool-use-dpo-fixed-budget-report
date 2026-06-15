# Direct-Answer Coverage Audit

This note documents the Stage7 direct-answer coverage audit used by the paper.
Stage7 is an evaluation-coverage diagnostic only. It does not add a new DPO run
and it does not make the When2Call result a balanced four-label estimate.

## Public When2Call Coverage

The released audit checks the exposed public `nvidia/When2Call` configurations
used in this project.

| Config | Split | Rows | Direct-answer gold status | Observed labeled gold values |
|---|---|---:|---|---|
| `test` | `llm_judge` | 300 | 0 labeled rows | 100 `tool_call`, 100 `request_for_info`, 100 `cannot_answer` |
| `test` | `mcq` | 3652 | 0 labeled rows | 1295 `tool_call`, 1062 `request_for_info`, 1295 `cannot_answer` |
| `train_sft` | `train` | 15000 | unlabeled | public `correct_answer` is `None` |
| `train_pref` | `train` | 9000 | unlabeled | public `correct_answer` is `None` |

The paper's frozen When2Call evaluation slice therefore covers represented
tool-call, follow-up-question, and unable-to-answer gold labels. The public
training configurations audited here do not expose `correct_answer` labels, so
they are not evidence of labeled direct-answer coverage. Direct-answer is
included by the frozen evaluator as a zero-support class because the model can
still predict that label, but the metric should not be interpreted as a balanced
four-class estimate.

## Auxiliary Existing-Artifact Diagnostics

The repository also releases existing-artifact diagnostics over direct-answer
or direct-answer-like rows:

- SFT-dev direct-answer rows: `n=93`
- BFCL relevance direct-answer-like rows: `n=60`
- Combined auxiliary diagnostic rows: `n=153`

These diagnostics are useful for checking whether direct-answer-like behavior is
obviously broken, but they are not a matched When2Call direct-answer slice and
are not part of the main Pareto claim.

## Released Files

- `artifacts/stage7/direct_answer/when2call_direct_answer_audit.json`
- `artifacts/stage7/direct_answer/when2call_direct_answer_audit.csv`
- `artifacts/stage7/direct_answer/existing_direct_answer_summary.json`
- `artifacts/stage7/direct_answer/existing_direct_answer_summary.csv`
- `artifacts/stage7/direct_answer/existing_direct_answer_delta_vs_r004.csv`

## Claim Boundary

Supported wording:

> The exposed labeled public When2Call splits audited here contain no
> direct-answer gold rows, while the audited training configs do not expose
> `correct_answer` labels. Direct-answer behavior therefore remains an auxiliary
> diagnostic rather than a matched When2Call behavior slice.

Unsupported wording:

- Direct-answer behavior is solved.
- The reported When2Call metric should be read as full four-label behavior coverage.
- Stage7 adds a new DPO result or changes the main Pareto frontier.
