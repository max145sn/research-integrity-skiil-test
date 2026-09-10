#!/usr/bin/env python3
import csv, json
from pathlib import Path
from statistics import mean, stdev
ROOT=Path(__file__).resolve().parents[1]
with open(ROOT/'data'/'benchmark_data.csv',newline='') as f: data=list(csv.DictReader(f))
with open(ROOT/'results'/'run_metrics.csv',newline='') as f: runs=list(csv.DictReader(f))
acc=[float(x['accuracy']) for x in runs]
print(json.dumps({
  "dataset_rows":len(data),
  "run_count":len(runs),
  "mean_accuracy":mean(acc),
  "accuracy_sd":stdev(acc),
  "best_accuracy":max(acc),
  "depths":sorted({int(x['max_depth']) for x in runs})
},indent=2))
