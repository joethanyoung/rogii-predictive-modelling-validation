"""Compare simulated held-out model losses with paired group resampling."""

from math import sqrt
from random import Random
from statistics import quantiles
from typing import NamedTuple


class GroupLoss(NamedTuple):
    rows: int
    baseline_sse: float
    candidate_sse: float


def pooled_rmse(groups):
    """Calculate both RMSEs across all rows represented by the groups."""
    rows = sum(group.rows for group in groups)
    baseline = sqrt(sum(group.baseline_sse for group in groups) / rows)
    candidate = sqrt(sum(group.candidate_sse for group in groups) / rows)
    return baseline, candidate


def paired_interval(groups):
    """Return the middle 90% of resampled candidate-minus-baseline RMSEs."""
    rng = Random(2026)
    differences = []
    for _ in range(5_000):
        sample = rng.choices(groups, k=len(groups))
        baseline, candidate = pooled_rmse(sample)
        differences.append(candidate - baseline)

    twentieths = quantiles(differences, n=20, method="inclusive")
    return twentieths[0], twentieths[-1]


def main():
    assert pooled_rmse((GroupLoss(1, 4, 9), GroupLoss(3, 32, 7))) == (3.0, 2.0)

    groups = (
        GroupLoss(80, 1400, 1080),
        GroupLoss(100, 2150, 1800),
        GroupLoss(85, 1900, 1600),
        GroupLoss(120, 2700, 2160),
        GroupLoss(95, 2200, 1700),
        GroupLoss(70, 1300, 1000),
        GroupLoss(105, 2350, 1900),
        GroupLoss(90, 1800, 1500),
        GroupLoss(125, 6500, 7870),
        GroupLoss(140, 8500, 9830),
    )
    baseline, candidate = pooled_rmse(groups)
    lower, upper = paired_interval(groups)
    squared_errors = sorted((group.baseline_sse for group in groups), reverse=True)
    top_two_share = sum(squared_errors[:2]) / sum(squared_errors)

    print(f"Synthetic held-out groups: {len(groups)}")
    print(f"Baseline pooled RMSE: {baseline:.3f}")
    print(f"Candidate pooled RMSE: {candidate:.3f}")
    print(f"Candidate minus baseline: {candidate - baseline:+.3f}")
    print(f"Paired group-bootstrap interval (90%): [{lower:+.3f}, {upper:+.3f}]")
    print(f"Top two groups' share of baseline squared error: {top_two_share:.1%}")


if __name__ == "__main__":
    main()
