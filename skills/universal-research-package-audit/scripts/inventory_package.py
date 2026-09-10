#!/usr/bin/env python3
import argparse, hashlib, json, mimetypes
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20), b''): h.update(chunk)
    return h.hexdigest()

def classify(p):
    ext=p.suffix.lower()
    if ext in {'.pdf','.docx','.tex','.md','.txt'}: return 'NARRATIVE_OR_DOCUMENTATION'
    if ext in {'.csv','.tsv','.xls','.xlsx','.sav','.dta'}: return 'STRUCTURED_DATA'
    if ext in {'.r','.rmd','.py','.ipynb','.jl','.m','.sas','.do'}: return 'ANALYTICAL_CODE'
    if ext in {'.yaml','.yml','.json','.toml','.ini','.cfg'}: return 'CONFIGURATION_OR_STRUCTURED_RECORD'
    if ext in {'.png','.jpg','.jpeg','.tif','.tiff','.svg'}: return 'IMAGE_OR_FIGURE'
    if ext in {'.wav','.mp3','.mp4','.mov'}: return 'MEDIA_EVIDENCE'
    return 'UNKNOWN'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('package'); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.package)
    records=[]
    for i,p in enumerate(sorted(x for x in root.rglob('*') if x.is_file()),1):
        try: digest=sha256(p); readable=True; error=None
        except Exception as e: digest=None; readable=False; error=str(e)
        records.append({'file_id':f'FILE-{i:04d}','path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':digest,'mime':mimetypes.guess_type(str(p))[0],'classification':classify(p),'readable':readable,'error':error})
    out={'package_root':str(root),'files':records,'file_count':len(records),'unclassified_count':sum(r['classification']=='UNKNOWN' for r in records)}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'files':len(records),'unclassified':out['unclassified_count'],'output':a.output}))
if __name__=='__main__': main()
