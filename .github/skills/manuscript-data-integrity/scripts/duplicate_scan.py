"""
Scans a raw data file (CSV/XLSX) for signs of duplication:
  - exact duplicate rows
  - duplicate values in an ID-like column (e.g. participant/sample ID)
  - near-duplicate rows among numeric columns (pairwise correlation above
    a high threshold), which can indicate copy-pasted or lightly altered
    "independent" replicates

Requires pandas.

Usage:
    python duplicate_scan.py --file data.csv
    python duplicate_scan.py --file data.xlsx --id-column subject_id --corr-threshold 0.999
"""

import argparse
import sys

import pandas as pd


def load(path):
    if path.lower().endswith(".csv"):
        return pd.read_csv(path)
    return pd.read_excel(path)


def scan(path, id_column=None, corr_threshold=0.999):
    df = load(path)
    n_rows = len(df)
    report = {}

    # 1. Exact duplicate rows
    exact_dupes = df[df.duplicated(keep=False)]
    report["exact_duplicate_rows"] = len(exact_dupes)
    print(f"Rows: {n_rows}")
    print(f"Exact duplicate rows: {len(exact_dupes)}")
    if len(exact_dupes) > 0:
        print("FLAG: exact duplicate rows found -- indices:", list(exact_dupes.index))

    # 2. Duplicate IDs
    if id_column and id_column in df.columns:
        dupe_ids = df[df[id_column].duplicated(keep=False)]
        report["duplicate_ids"] = len(dupe_ids)
        print(f"\nDuplicate values in '{id_column}': {len(dupe_ids)}")
        if len(dupe_ids) > 0:
            print("FLAG: duplicate ID values found -- indices:", list(dupe_ids.index))
    elif id_column:
        print(f"\nWarning: column '{id_column}' not found in file.")

    # 3. Near-duplicate rows via pairwise correlation on numeric columns
    numeric_df = df.select_dtypes(include="number")
    near_dupes = []
    # Row-wise correlation needs several numeric columns per row to be
    # meaningful; with only 2 columns, any two rows correlate at +-1 trivially.
    if numeric_df.shape[1] >= 4 and numeric_df.shape[0] >= 2:
        corr_matrix = numeric_df.T.corr()
        n = corr_matrix.shape[0]
        for i in range(n):
            for j in range(i + 1, n):
                val = corr_matrix.iloc[i, j]
                if pd.notna(val) and val >= corr_threshold:
                    near_dupes.append((i, j, round(float(val), 5)))

    report["near_duplicate_row_pairs"] = len(near_dupes)
    print(f"\nNear-duplicate row pairs (correlation >= {corr_threshold}): {len(near_dupes)}")
    if near_dupes:
        print("FLAG: suspiciously similar rows found -- review these as possible "
              "copy-pasted or lightly altered 'independent' replicates:")
        for i, j, corr in near_dupes[:20]:
            print(f"  rows {i} & {j}: correlation {corr}")
        if len(near_dupes) > 20:
            print(f"  ...and {len(near_dupes) - 20} more pairs")
    elif numeric_df.shape[1] < 4:
        print(f"\nNear-duplicate row check skipped: needs at least 4 numeric "
              f"columns per row to be meaningful (found {numeric_df.shape[1]}).")

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan raw data for duplication")
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--id-column", type=str, default=None)
    parser.add_argument("--corr-threshold", type=float, default=0.999)
    args = parser.parse_args()

    scan(args.file, args.id_column, args.corr_threshold)
