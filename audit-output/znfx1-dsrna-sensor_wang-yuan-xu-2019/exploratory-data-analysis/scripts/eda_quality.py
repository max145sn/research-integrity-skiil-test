import sys, json, collections
import openpyxl
from decimal import Decimal
from pathlib import Path
sd=Path(sys.argv[1]); out={}
for f in sorted(sd.glob("*.xlsx")):
    ws=openpyxl.load_workbook(f,data_only=True).active
    dp=collections.Counter(); zeros=[]; vals={}; rows=collections.Counter()
    for row in ws.iter_rows():
        rowvals=[]
        for c in row:
            v=c.value
            if isinstance(v,(int,float)) and not isinstance(v,bool):
                s=repr(float(v)); d=len(s.split(".")[1].rstrip("0")) if "." in s else 0
                dp[d]+=1
                if v==0: zeros.append(c.coordinate)
                vals.setdefault(round(float(v),9),[]).append(c.coordinate)
                rowvals.append(round(float(v),6))
        if len(rowvals)>=3: rows[tuple(rowvals)]+=1
    dupvals={k:v for k,v in vals.items() if len(v)>1 and k not in (0.0,1.0)}
    out[f.name]={
      "decimal_places_histogram": dict(sorted(dp.items())),
      "high_precision_cells(>=6dp)": sum(n for d,n in dp.items() if d>=6),
      "low_precision_cells(<=2dp)": sum(n for d,n in dp.items() if d<=2),
      "zero_cells": zeros,
      "duplicate_value_groups(excl 0/1)": len(dupvals),
      "example_duplicates": {str(k):v for k,v in list(dupvals.items())[:6]},
      "duplicate_numeric_rows": {str(k):n for k,n in rows.items() if n>1},
    }
json.dump(out,open(sys.argv[2],"w",encoding="utf-8"),indent=1,default=str)
for k,v in out.items():
    print("==",k)
    print("   dp hist:",v["decimal_places_histogram"])
    print("   >=6dp:",v["high_precision_cells(>=6dp)"]," <=2dp:",v["low_precision_cells(<=2dp)"])
    print("   zeros:",v["zero_cells"])
    print("   dup value groups:",v["duplicate_value_groups(excl 0/1)"],"| dup numeric rows:",len(v["duplicate_numeric_rows"]))
    if v["example_duplicates"]: print("   examples:",v["example_duplicates"])
