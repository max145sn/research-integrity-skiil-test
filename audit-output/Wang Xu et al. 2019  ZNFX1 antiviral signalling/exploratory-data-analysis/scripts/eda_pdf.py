import sys, json, hashlib, re, collections
import pdfplumber, pypdf

p = sys.argv[1]
out = {}
h = hashlib.sha256(open(p,"rb").read()).hexdigest()
out["sha256"] = h

r = pypdf.PdfReader(p)
md = r.metadata or {}
out["metadata"] = {k: str(v) for k,v in md.items()}
out["pdf_version"] = getattr(r, "pdf_header", None)
out["encrypted"] = r.is_encrypted
out["n_pages"] = len(r.pages)
try:
    out["outline_entries"] = len(r.outline)
except Exception as e:
    out["outline_entries"] = f"error: {e}"
try:
    out["has_xmp"] = r.xmp_metadata is not None
except Exception:
    out["has_xmp"] = None

pages=[]; fonts=collections.Counter(); imgs=0; img_detail=[]
total_chars=0; total_words=0
with pdfplumber.open(p) as pdf:
    for i, pg in enumerate(pdf.pages, 1):
        t = pg.extract_text() or ""
        w = pg.extract_words()
        ims = pg.images
        imgs += len(ims)
        for im in ims:
            img_detail.append({"page": i, "w": round(im.get("srcsize",(0,0))[0] or 0,1),
                               "h": round(im.get("srcsize",(0,0))[1] or 0,1),
                               "colorspace": str(im.get("colorspace"))[:40]})
        for ch in pg.chars:
            fonts[ch.get("fontname","?")] += 1
        total_chars += len(t); total_words += len(w)
        pages.append({"page": i, "chars": len(t), "words": len(w), "images": len(ims),
                      "tables": len(pg.find_tables()),
                      "width": round(pg.width,1), "height": round(pg.height,1),
                      "rotation": pg.rotation})
out["pages"] = pages
out["total_chars"] = total_chars
out["total_words"] = total_words
out["total_images"] = imgs
out["image_detail"] = img_detail
out["fonts"] = fonts.most_common()
out["page_sizes"] = sorted({(pp["width"],pp["height"]) for pp in pages})
json.dump(out, open(sys.argv[2],"w",encoding="utf-8"), indent=1, default=str)
print(json.dumps({k:v for k,v in out.items() if k not in ("pages","image_detail","fonts","metadata")}, indent=1)[:1500])
print("FONTS:", fonts.most_common(12))
print("META:", out["metadata"])
