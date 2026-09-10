"""
GRIM and GRIMMER tests.

GRIM: checks whether a reported mean is mathematically achievable given the
sample size N and the number of decimal places reported. For data made of
whole numbers (Likert items, counts, discrete scores), the mean must equal
some integer sum divided by N -- most decimal values are impossible for a
given N.

GRIMMER: extends this to the reported standard deviation, checking whether
the implied sum of squares is consistent with integer-valued raw data.

Usage:
    python grim_check.py --mean 3.67 --n 20
    python grim_check.py --mean 3.67 --sd 1.14 --n 20   # runs GRIM + GRIMMER
    python grim_check.py --csv reported_stats.csv        # batch mode

CSV batch mode expects columns: label, mean, n, sd (sd optional), decimals (optional)
"""

import argparse
import csv
import sys


def decimals_in(value_str):
    value_str = value_str.strip()
    if "." in value_str:
        return len(value_str.split(".")[1])
    return 0


def grim_test(mean_str, n):
    """Returns (consistent: bool, nearest_achievable_mean: float, detail: str)."""
    decimals = decimals_in(mean_str)
    mean = float(mean_str)
    n = int(n)

    total = mean * n
    nearest_int_sum = round(total)
    reconstructed_mean = round(nearest_int_sum / n, decimals)

    tolerance = 0.5 * (10 ** (-decimals))
    consistent = abs(reconstructed_mean - mean) < tolerance + 1e-9

    detail = (
        f"reported mean {mean} at {decimals} decimal(s), N={n} -> "
        f"nearest achievable mean is {reconstructed_mean} "
        f"(from integer sum {nearest_int_sum})"
    )
    return consistent, reconstructed_mean, detail


def grimmer_test(mean_str, sd_str, n):
    """
    Simplified GRIMMER check: verifies the implied sum of squares of the raw
    (assumed integer) data is close to an integer, which it must be if the
    data really are whole numbers. This is a heuristic screen, not a full
    GRIMMER implementation -- flag failures for manual follow-up rather than
    treating them as definitive.
    """
    decimals = decimals_in(mean_str)
    mean = float(mean_str)
    sd = float(sd_str)
    n = int(n)

    total = mean * n
    nearest_int_sum = round(total)

    # sum of squares implied by variance formula: SD^2 * (n-1) = sum((x-mean)^2)
    # sum(x^2) = SD^2*(n-1) + (sum_x)^2 / n
    sum_sq = sd ** 2 * (n - 1) + (nearest_int_sum ** 2) / n
    nearest_int_sum_sq = round(sum_sq)
    consistent = abs(sum_sq - nearest_int_sum_sq) < 0.02

    detail = (
        f"reported SD {sd} implies sum-of-squares {sum_sq:.4f} "
        f"(should be ~integer if data are whole numbers)"
    )
    return consistent, detail


def run_single(mean, n, sd=None):
    ok, recon, detail = grim_test(mean, n)
    print(f"[GRIM] {'PASS' if ok else 'FAIL - flag for review'}")
    print(f"       {detail}")

    if sd is not None:
        ok2, detail2 = grimmer_test(mean, sd, n)
        print(f"[GRIMMER] {'PASS' if ok2 else 'FAIL - flag for review'}")
        print(f"          {detail2}")


def run_batch(csv_path):
    results = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            label = row.get("label", "")
            mean = row["mean"]
            n = row["n"]
            sd = row.get("sd") or None

            ok, recon, detail = grim_test(mean, n)
            row_result = {
                "label": label,
                "grim_pass": ok,
                "grim_detail": detail,
            }
            if sd:
                ok2, detail2 = grimmer_test(mean, sd, n)
                row_result["grimmer_pass"] = ok2
                row_result["grimmer_detail"] = detail2
            results.append(row_result)

    flags = [r for r in results if not r["grim_pass"] or not r.get("grimmer_pass", True)]

    print(f"Checked {len(results)} reported values.")
    print(f"{len(flags)} flagged for review:\n")
    for r in flags:
        print(f"- {r['label']}: {r['grim_detail']}")
        if "grimmer_detail" in r:
            print(f"  {r['grimmer_detail']}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GRIM/GRIMMER consistency check")
    parser.add_argument("--mean", type=str)
    parser.add_argument("--sd", type=str)
    parser.add_argument("--n", type=str)
    parser.add_argument("--csv", type=str, help="batch mode: CSV with label,mean,n,sd columns")
    args = parser.parse_args()

    if args.csv:
        run_batch(args.csv)
    elif args.mean and args.n:
        run_single(args.mean, args.n, args.sd)
    else:
        print("Provide either --mean/--n (and optional --sd) or --csv for batch mode.")
        sys.exit(1)
