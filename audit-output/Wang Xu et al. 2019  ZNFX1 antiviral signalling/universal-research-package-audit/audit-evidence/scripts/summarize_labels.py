import openpyxl, sys, io
from pathlib import Path
base = Path(sys.argv[1]); out = open(sys.argv[2], "w", encoding="utf-8")
for f in sorted(base.glob("*.xlsx")):
    wb = openpyxl.load_workbook(f, data_only=True)
    for ws in wb.worksheets:
        out.write("="*70 + "\n")
        out.write(f"{f.name} :: {ws.title} :: dims={ws.dimensions}\n")
        for r in ws.iter_rows():
            txt = [(c.coordinate, str(c.value)) for c in r if isinstance(c.value, str) and c.value.strip()]
            nums = [c.coordinate for c in r if isinstance(c.value,(int,float))]
            if txt:
                rng = f" | numeric:{nums[0]}..{nums[-1]}({len(nums)})" if nums else ""
                out.write("  " + "; ".join(f"{k}={v[:70]}" for k,v in txt) + rng + "\n")
            elif nums:
                out.write(f"  [{nums[0]}..{nums[-1]}] {len(nums)} numeric\n")
out.close()
