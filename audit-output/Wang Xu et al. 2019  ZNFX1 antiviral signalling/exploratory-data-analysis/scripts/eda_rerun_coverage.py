import os, re, glob, json
import openpyxl
import pymupdf

# Source-data directory. Override with EDA_DATA_DIR; defaults to the copies
# archived in this repository under ../../supporting-files/source-data.
D = os.environ.get("EDA_DATA_DIR") or os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "..", "..", "supporting-files", "source-data"))
PANEL = re.compile(r"^\s*Fig(?:ure)?\.?\s*([1-7])\s*([a-z])\s*$", re.I)

cov = {}
prov = {}

for f in sorted(glob.glob(os.path.join(D, "*.xlsx"))):
    base = os.path.basename(f)
    wb = openpyxl.load_workbook(f, data_only=True)
    prov[base] = dict(creator=wb.properties.creator,
                      created=str(wb.properties.created),
                      lastModifiedBy=wb.properties.lastModifiedBy,
                      modified=str(wb.properties.modified))
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    marks = []
    for i, r in enumerate(rows):
        for c in r:
            if isinstance(c, str):
                m = PANEL.match(c)
                if m:
                    marks.append((i, f"{m.group(1)}{m.group(2).lower()}"))
    marks.append((len(rows), None))
    for j in range(len(marks) - 1):
        start, key = marks[j]
        end = marks[j + 1][0]
        nums = [v for r in rows[start:end] for v in r
                if isinstance(v, (int, float)) and not isinstance(v, bool)]
        cov.setdefault(key, {"file": base, "rows": 0, "numeric": 0})
        cov[key]["rows"] += end - start
        cov[key]["numeric"] += len(nums)

pdf_panels = {}
for f in sorted(glob.glob(os.path.join(D, "*.pdf"))):
    base = os.path.basename(f)
    doc = pymupdf.open(f)
    prov[base] = dict(creator=doc.metadata.get("creator"),
                      created=doc.metadata.get("creationDate"),
                      lastModifiedBy="", modified=doc.metadata.get("modDate"))
    txt = doc[0].get_text()
    found = sorted({f"{m.group(1)}{m.group(2).lower()}"
                    for m in re.finditer(r"Fig(?:ure)?\.?\s*([1-7])\s*([a-z])\b", txt, re.I)})
    pdf_panels[base] = dict(panels=found, n_images=len(doc[0].get_images(full=True)))
    doc.close()

print("## Provenance")
for k, v in prov.items():
    print(f"  {k}: creator={v['creator']!r} created={v['created']} modBy={v['lastModifiedBy']!r} modified={v['modified']}")

print("\n## Numeric panel coverage (XLSX)")
for k in sorted(cov, key=lambda s: (s is None, s)):
    if k is None:
        continue
    v = cov[k]
    print(f"  Fig {k}: file={v['file']} rows={v['rows']} numeric_cells={v['numeric']}")

print("\n## Image panel coverage (PDF)")
for k, v in pdf_panels.items():
    print(f"  {k}: images={v['n_images']} panels={v['panels']}")

numeric_panels = sorted(k for k in cov if k)
image_panels = sorted({p for v in pdf_panels.values() for p in v["panels"]})
print(f"\nnumeric panels ({len(numeric_panels)}): {numeric_panels}")
print(f"image panels   ({len(image_panels)}): {image_panels}")
print(f"overlap: {sorted(set(numeric_panels) & set(image_panels))}")
