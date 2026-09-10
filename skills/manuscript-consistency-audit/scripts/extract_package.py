#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pymupdf4llm", "openpyxl"]
# ///
"""Extract a manuscript package into readable text + a source-data inventory.

Run with uv so dependencies resolve without touching any project venv:

    uv run extract_package.py <input_dir> <work_dir>

Converts every PDF in input_dir to markdown (line-numbered prose survives the
conversion, which is what lets you cite "main text line 337" back to the author)
and inventories every sheet of every spreadsheet so you know what source data
exists before you start opening sheets.

Prints a manifest to stdout. Nothing is written outside work_dir.
"""

import sys
import pathlib


def convert_pdfs(in_dir: pathlib.Path, out_dir: pathlib.Path) -> list:
    import pymupdf4llm

    manifest = []
    for pdf in sorted(in_dir.glob("*.pdf")):
        stem = pdf.stem
        # File names from submission systems are opaque (650557_2_art_file_...).
        # Keep the full stem so the mapping back to the original is unambiguous.
        dest = out_dir / f"{stem}.md"
        try:
            md = pymupdf4llm.to_markdown(str(pdf), show_progress=False)
        except Exception as exc:  # noqa: BLE001 - report and continue
            manifest.append((pdf.name, "FAILED", str(exc)))
            continue
        dest.write_text(md, encoding="utf-8")
        manifest.append((pdf.name, dest.name, f"{len(md):,} chars"))
    return manifest


def inventory_workbooks(in_dir: pathlib.Path) -> list:
    import openpyxl

    inv = []
    patterns = ("*.xlsx", "*.xlsm")
    for xl in sorted(p for pat in patterns for p in in_dir.glob(pat)):
        try:
            wb = openpyxl.load_workbook(xl, read_only=True)
        except Exception as exc:  # noqa: BLE001
            inv.append((xl.name, ["<could not open: %s>" % exc]))
            continue
        inv.append((xl.name, list(wb.sheetnames)))
        wb.close()
    return inv


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2

    in_dir = pathlib.Path(sys.argv[1]).expanduser().resolve()
    out_dir = pathlib.Path(sys.argv[2]).expanduser().resolve()
    if not in_dir.is_dir():
        print(f"error: {in_dir} is not a directory", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"# Manuscript package: {in_dir}\n")

    docs = convert_pdfs(in_dir, out_dir)
    print("## Converted documents\n")
    if not docs:
        print("(no PDFs found)\n")
    for src, dest, note in docs:
        print(f"- {src}  ->  {dest}  ({note})")
    print()

    books = inventory_workbooks(in_dir)
    print("## Source data workbooks\n")
    if not books:
        print("(no spreadsheets found)\n")
    for name, sheets in books:
        print(f"- {name}: {len(sheets)} sheets")
        for s in sheets:
            print(f"    {s!r}")
    print()

    other = [
        p.name
        for p in sorted(in_dir.iterdir())
        if p.is_file()
        and p.suffix.lower() not in {".pdf", ".xlsx", ".xlsm"}
        and not p.name.startswith(".")
    ]
    if other:
        print("## Other files (not auto-converted)\n")
        for name in other:
            print(f"- {name}")
        print()

    print(f"Text written to: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
