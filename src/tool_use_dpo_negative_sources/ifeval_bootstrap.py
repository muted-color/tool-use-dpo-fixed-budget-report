from __future__ import annotations

import argparse
import csv
import random
from collections.abc import Mapping
from pathlib import Path

from .paths import REPO_ROOT, REPRODUCED


RUNS = [
    ("r028", "step50"),
    ("r028", "final"),
    ("r029", "step50"),
    ("r029", "final"),
    ("s3d001", "step50"),
    ("s3d001", "final"),
    ("s3d002", "step50"),
    ("s3d002", "final"),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def truthy(value: str | bool | None) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes"}


def load_prompt_strict(run_id: str, checkpoint: str) -> dict[str, bool]:
    path = REPO_ROOT / "results" / "per_example" / "ifeval" / f"{run_id}_{checkpoint}.csv"
    rows = read_csv(path)
    out: dict[str, bool] = {}
    for row in rows:
        if int(row["supported_instruction_count"]) <= 0:
            continue
        out[row["prompt_id"]] = truthy(row["prompt_level_strict"])
    return out


def bootstrap_delta(
    a: Mapping[str, bool],
    b: Mapping[str, bool],
    iterations: int,
    seed: int,
) -> dict[str, object]:
    groups = sorted(set(a) & set(b))
    rng = random.Random(seed)

    def value(sample: list[str]) -> float:
        return sum((1.0 if a[key] else 0.0) - (1.0 if b[key] else 0.0) for key in sample) / len(sample)

    deltas: list[float] = []
    for _ in range(iterations):
        sample = [rng.choice(groups) for _ in groups]
        deltas.append(value(sample))
    deltas.sort()
    return {
        "metric": "ifeval_prompt_strict_accuracy",
        "point_delta": value(groups),
        "ci95_low": deltas[int(0.025 * (len(deltas) - 1))],
        "ci95_high": deltas[int(0.975 * (len(deltas) - 1))],
        "groups": len(groups),
        "iterations": iterations,
    }


def compute(iterations: int) -> list[dict[str, object]]:
    baseline = load_prompt_strict("r004", "sft_best")
    rows: list[dict[str, object]] = []
    index = 0

    for run_id, checkpoint in RUNS:
        current = load_prompt_strict(run_id, checkpoint)
        rows.append(
            {
                "comparison": "delta_vs_sft",
                "a_run": run_id,
                "b_run": "r004",
                "a_adapter": checkpoint,
                "b_adapter": "sft_best",
                **bootstrap_delta(current, baseline, iterations, seed=20260610 + index * 97),
            }
        )
        index += 1

    for run_id in ["r028", "r029", "s3d001", "s3d002"]:
        step50 = load_prompt_strict(run_id, "step50")
        final = load_prompt_strict(run_id, "final")
        rows.append(
            {
                "comparison": "step50_vs_final",
                "a_run": run_id,
                "b_run": run_id,
                "a_adapter": "step50",
                "b_adapter": "final",
                **bootstrap_delta(step50, final, iterations, seed=20260610 + index * 97),
            }
        )
        index += 1

    return rows


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-iterations", type=int, default=1000)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPRODUCED / "bootstrap" / "ifeval_prompt_strict_bootstrap_ci.csv",
    )
    args = parser.parse_args()
    rows = compute(args.bootstrap_iterations)
    write_rows(args.output, rows)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
