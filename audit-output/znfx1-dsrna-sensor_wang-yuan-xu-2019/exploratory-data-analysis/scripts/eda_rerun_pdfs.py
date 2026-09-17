import os, glob, json
import pymupdf

# Source-data directory. Override with EDA_DATA_DIR; defaults to the copies
# archived in this repository under ../../supporting-files/source-data.
D = os.environ.get("EDA_DATA_DIR") or os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "..", "..", "supporting-files", "source-data"))
out = []
for f in sorted(glob.glob(os.path.join(D, "*.pdf"))):
    doc = pymupdf.open(f)
    out.append("=" * 80)
    out.append(f"FILE: {os.path.basename(f)}  size={os.path.getsize(f)} bytes  pages={doc.page_count}")
    out.append(f"metadata: {json.dumps(doc.metadata, default=str)}")
    for pno in range(doc.page_count):
        p = doc[pno]
        r = p.rect
        imgs = p.get_images(full=True)
        txt = p.get_text().strip()
        txt_short = " / ".join([t.strip() for t in txt.splitlines() if t.strip()][:40])
        out.append(f"-- page {pno+1}: {r.width:.0f}x{r.height:.0f}pt  images={len(imgs)}  textchars={len(txt)}")
        for im in imgs:
            xref, smask, w, h, bpc, cs, alt, name, filt = im[:9]
            out.append(f"     img xref={xref} {w}x{h} bpc={bpc} cs={cs} filter={filt} smask={smask}")
        if txt_short:
            out.append(f"     text: {txt_short[:1500]}")
    doc.close()
print("\n".join(out))
