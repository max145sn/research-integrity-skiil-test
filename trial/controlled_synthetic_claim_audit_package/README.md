# Controlled Synthetic Claim-Audit Package

This package is intentionally synthetic and contains six planted manuscript flaws. It is designed to test claim-auditing software. Do not cite it as scientific evidence.

## Contents
- manuscript.docx: correlated manuscript containing planted flaws
- data/study_data.csv and .xlsx: 520 synthetic observations
- results/run_results.csv: six run-level result rows
- results/test_predictions.csv: test predictions for all runs
- results/summary_statistics.json: machine-readable ground truth summary
- config/experiment_config.yaml: actual configuration
- code/analysis.py: lightweight audit script
- audit_key/expected_findings.json: answer key

## Run
python code/analysis.py

## License
CC0 1.0. All data are synthetic and non-personal.
