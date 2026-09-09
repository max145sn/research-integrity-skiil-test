#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import pandas as pd
try:
    import chardet
except Exception:
    chardet=None

PLACEHOLDERS={'nd','n/a','na','unknown','unk','?','dummy','test','blank','none'}

def inspect_csv(p):
    raw=p.read_bytes()[:200000]
    enc=(chardet.detect(raw).get('encoding') if chardet else None) or 'utf-8'
    try: df=pd.read_csv(p,encoding=enc,low_memory=False)
    except Exception: df=pd.read_csv(p,encoding='latin-1',low_memory=False); enc='latin-1'
    cols=[]
    for c in df.columns:
        s=df[c]
        vals=set(str(x).strip().lower() for x in s.dropna().unique()[:10000])
        placeholders=sorted(vals & PLACEHOLDERS)
        zero_count=None
        if pd.api.types.is_numeric_dtype(s): zero_count=int((s==0).sum())
        cols.append({'name':str(c),'dtype':str(s.dtype),'missing':int(s.isna().sum()),'unique':int(s.nunique(dropna=True)),'placeholder_values':placeholders,'zero_values':zero_count})
    candidate_weights=[str(c) for c in df.columns if any(k in str(c).lower() for k in ['count','number','n_ind','no.','weight','frequency','freq']) and pd.api.types.is_numeric_dtype(df[c])]
    return {'encoding':enc,'rows':len(df),'columns':len(df.columns),'duplicate_rows':int(df.duplicated().sum()),'candidate_weight_columns':candidate_weights,'column_profiles':cols}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('package'); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.package); out={}
    for p in root.rglob('*'):
        if p.suffix.lower() in {'.csv','.tsv'}:
            try: out[str(p.relative_to(root))]=inspect_csv(p)
            except Exception as e: out[str(p.relative_to(root))]={'error':str(e)}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'tables':len(out),'output':a.output}))
if __name__=='__main__': main()
