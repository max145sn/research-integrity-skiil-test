"""
Terminal digit analysis: tests whether the last digit of a set of reported
numeric values is uniformly distributed (0-9), as genuine measured data
tends to be. Fabricated or lightly manipulated values often show unnatural
clustering (e.g., excess of 0s and 5s).

Uses a chi-square goodness-of-fit test against a uniform distribution.
Needs at least ~20 values to be meaningful; more is better.

Usage:
    python digit_analysis.py --values 3.4,5.6,7.2,1.0,9.5,...
    python digit_analysis.py --csv table_values.csv --column value
"""

import argparse
import csv
import sys
from collections import Counter

from scipy import stats


def last_digit(value_str):
    value_str = value_str.strip()
    digits_only = value_str.replace(".", "").replace("-", "")
    if not digits_only:
        return None
    return int(digits_only[-1])


def analyze(values):
    digits = [last_digit(v) for v in values if last_digit(v) is not None]
    n = len(digits)
    if n < 20:
        print(f"Warning: only {n} values provided. Terminal digit analysis is "
              f"unreliable below ~20 values; treat results as indicative only.")

    counts = Counter(digits)
    observed = [counts.get(d, 0) for d in range(10)]
    expected = [n / 10] * 10

    chi2, p = stats.chisquare(observed, expected)

    print(f"N values analyzed: {n}")
    print("Digit distribution (0-9):")
    for d in range(10):
        print(f"  {d}: {observed[d]} ({100*observed[d]/n:.1f}%)")
    print(f"\nChi-square = {chi2:.2f}, p = {p:.4f}")

    if p < 0.05:
        print("FLAG: digit distribution deviates significantly from uniform. "
              "Worth a closer look at how these values were measured/reported.")
    else:
        print("PASS: digit distribution consistent with uniform/random.")

    return {"n": n, "chi2": chi2, "p": p, "flag": p < 0.05}


def run_from_csv(csv_path, column):
    values = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            v = row.get(column)
            if v not in (None, ""):
                values.append(v)
    return analyze(values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Terminal digit distribution test")
    parser.add_argument("--values", type=str, help="comma-separated list of numeric values")
    parser.add_argument("--csv", type=str)
    parser.add_argument("--column", type=str, help="column name to analyze (with --csv)")
    args = parser.parse_args()

    if args.csv and args.column:
        run_from_csv(args.csv, args.column)
    elif args.values:
        analyze(args.values.split(","))
    else:
        print("Provide --values as a comma-separated list, or --csv with --column.")
        sys.exit(1)
