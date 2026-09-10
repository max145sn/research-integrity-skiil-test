"""
Recomputes p-values from reported test statistics and flags mismatches
against the reported p-value, including cases where the significance
conclusion (p < .05) would flip. Covers t, F, and chi-square tests, and
Pearson r (converted to t internally).

Requires scipy.

Usage:
    python statcheck.py --test t --stat 2.31 --df1 48 --p 0.03
    python statcheck.py --test f --stat 4.12 --df1 2 --df2 45 --p 0.05
    python statcheck.py --test chi2 --stat 6.8 --df1 2 --p 0.09
    python statcheck.py --test r --stat 0.32 --df1 38 --p 0.04   # df1 = n-2
    python statcheck.py --csv reported_tests.csv
"""

import argparse
import csv
import sys

from scipy import stats


def recompute_p(test_type, stat, df1, df2=None, tail="two"):
    stat = abs(float(stat))
    df1 = float(df1)

    if test_type == "t":
        p = 2 * (1 - stats.t.cdf(stat, df1)) if tail == "two" else (1 - stats.t.cdf(stat, df1))
    elif test_type == "f":
        if df2 is None:
            raise ValueError("F test requires df2")
        p = 1 - stats.f.cdf(stat, df1, float(df2))
    elif test_type == "chi2":
        p = 1 - stats.chi2.cdf(stat, df1)
    elif test_type == "r":
        # convert correlation r (stat) with df1 = n-2 to a t statistic
        n_minus_2 = df1
        t_val = stat * ((n_minus_2) ** 0.5) / ((1 - stat ** 2) ** 0.5)
        p = 2 * (1 - stats.t.cdf(abs(t_val), n_minus_2))
    else:
        raise ValueError(f"Unsupported test type: {test_type}")

    return p


def check(test_type, stat, df1, df2, reported_p, tolerance=0.01):
    computed_p = recompute_p(test_type, stat, df1, df2)
    diff = abs(computed_p - float(reported_p))
    mismatch = diff > tolerance
    flip = (computed_p < 0.05) != (float(reported_p) < 0.05)

    print(f"Test: {test_type}, stat={stat}, df1={df1}, df2={df2}")
    print(f"  Reported p = {reported_p}")
    print(f"  Recomputed p = {computed_p:.4f}")
    if flip:
        print("  FLAG: significance conclusion (p<.05) would FLIP -- high priority review")
    elif mismatch:
        print("  FLAG: p-value mismatch beyond rounding tolerance")
    else:
        print("  PASS: consistent with reported p-value")
    return {"mismatch": mismatch, "flip": flip, "computed_p": computed_p}


def run_batch(csv_path):
    flags = []
    total = 0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            result = check(
                row["test"],
                row["stat"],
                row["df1"],
                row.get("df2") or None,
                row["p"],
            )
            if result["mismatch"] or result["flip"]:
                flags.append({**row, **result})
            print()

    print(f"Checked {total} reported test statistics. {len(flags)} flagged.")
    return flags


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recompute p-values from test statistics")
    parser.add_argument("--test", choices=["t", "f", "chi2", "r"])
    parser.add_argument("--stat", type=str)
    parser.add_argument("--df1", type=str)
    parser.add_argument("--df2", type=str, default=None)
    parser.add_argument("--p", type=str)
    parser.add_argument("--csv", type=str, help="batch mode: CSV with test,stat,df1,df2,p columns")
    args = parser.parse_args()

    if args.csv:
        run_batch(args.csv)
    elif args.test and args.stat and args.df1 and args.p:
        check(args.test, args.stat, args.df1, args.df2, args.p)
    else:
        print("Provide --test/--stat/--df1/--p (and --df2 for F tests) or --csv for batch mode.")
        sys.exit(1)
