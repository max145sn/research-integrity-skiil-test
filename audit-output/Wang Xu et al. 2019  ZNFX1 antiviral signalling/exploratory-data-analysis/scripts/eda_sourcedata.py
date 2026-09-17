import sys, json, hashlib, statistics, collections
import openpyxl, pdfplumber
from pathlib import Path
sd = Path(sys.argv[1]); res = {}
for f in sorted(sd.iterdir()):
    d = {"bytes": f.stat().st_size,
         "sha256": hashlib.sha256(f.read_bytes()).hexdigest()[:16]}
    if f.suffix.lower() == ".xlsx":
        wb = openpyxl.load_workbook(f, data_only=True)
        d["format"] = "Office Open XML workbook (.xlsx)"
        d["sheets"] = wb.sheetnames
        sh = []
        for ws in wb.worksheets:
            num, txt, blank, neg, zero = [], 0, 0, 0, 0
            vals = []
            for row in ws.iter_rows():
                for c in row:
                    v = c.value
                    if v is None: blank += 1
                    elif isinstance(v, bool): txt += 1
                    elif isinstance(v, (int, float)):
                        num.append(v); vals.append(v)
                        if v < 0: neg += 1
                        if v == 0: zero += 1
                    else: txt += 1
            cells = ws.max_row * ws.max_column
            ent = {"sheet": ws.title, "dims": ws.dimensions, "rows": ws.max_row, "cols": ws.max_column,
                   "total_cells": cells, "numeric": len(num), "text": txt, "empty": blank,
                   "pct_empty": round(100*blank/cells, 1) if cells else 0,
                   "negatives": neg, "zeros": zero,
                   "formulas_preserved": False}
            if num:
                ent.update({"min": min(num), "max": max(num),
                            "median": statistics.median(num),
                            "mean": round(statistics.mean(num), 4),
                            "dynamic_range_orders": round(__import__("math").log10(max(num)/min(x for x in num if x > 0)), 1) if any(x > 0 for x in num) else None})
                ct = collections.Counter(num)
                ent["most_common_value"] = list(ct.most_common(1)[0])
                ent["exact_ones"] = ct.get(1, 0)
            sh.append(ent)
        d["sheet_profiles"] = sh
    elif f.suffix.lower() == ".pdf":
        d["format"] = "PDF (raster scan container)"
        with pdfplumber.open(f) as pdf:
            d["pages"] = len(pdf.pages)
            ti, tc = 0, 0
            pg = []
            for i, p in enumerate(pdf.pages, 1):
                t = p.extract_text() or ""
                ti += len(p.images); tc += len(t)
                pg.append({"page": i, "images": len(p.images), "text_chars": len(t),
                           "w": round(p.width, 1), "h": round(p.height, 1)})
            d["total_embedded_images"] = ti
            d["total_text_chars"] = tc
            d["chars_per_page"] = round(tc / len(pdf.pages), 1)
            d["page_detail"] = pg
    res[f.name] = d
json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), indent=1, default=str)
for k, v in res.items():
    print("==", k, "|", v["format"], "|", v["bytes"], "B")
    for s in v.get("sheet_profiles", []):
        print("   ", s["sheet"], s["dims"], "cells", s["total_cells"], "num", s["numeric"], "txt", s["text"],
              "empty%", s["pct_empty"], "min", s.get("min"), "max", s.get("max"), "exact_1s", s.get("exact_ones"),
              "neg", s["negatives"], "zeros", s["zeros"])
    if "pages" in v:
        print("    pages", v["pages"], "images", v["total_embedded_images"], "text_chars", v["total_text_chars"], "chars/pg", v["chars_per_page"])
