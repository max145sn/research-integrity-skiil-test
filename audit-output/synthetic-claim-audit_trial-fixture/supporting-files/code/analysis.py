#!/usr/bin/env python3
"""Audit the supplied synthetic results. No model training is required."""
import csv, json
from statistics import mean
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with open(ROOT/'data'/'study_data.csv', newline='') as f:
    data=list(csv.DictReader(f))
with open(ROOT/'results'/'run_results.csv', newline='') as f:
    runs=list(csv.DictReader(f))
acc=[float(r['accuracy']) for r in runs]
out={
 'sample_n':len(data),
 'run_count':len(runs),
 'mean_accuracy':mean(acc),
 'best_accuracy':max(acc),
 'best_run_id':int(max(runs,key=lambda r:float(r['accuracy']))['run_id']),
 'max_depth_values':sorted({int(r['max_depth']) for r in runs})
}
print(json.dumps(out,indent=2))
