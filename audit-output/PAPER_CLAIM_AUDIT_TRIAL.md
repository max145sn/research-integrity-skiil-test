# Paper Claim Audit Report — Trial Fixture

**Date**: 2026-09-07  
**Skill**: `paper-claim-audit` (replayed manually from `.github/skills/paper-claim-audit/skill.md`)  
**Primary auditor**: GPT-5.4-mini  
**Cross-model reviewer**: GPT-5.3-Codex, zero-context task agent  
**Fixture**: `trial/controlled_synthetic_claim_audit_package/` (extracted under `audit-output/trial_fixture/`)

## Overall Verdict: **FAIL**

The synthetic manuscript intentionally contains six planted reporting flaws. Against the evidence files in the trial package, I found the expected sample-size, run-count, configuration, and scope problems. The mean accuracy is correctly rounded, and the best-run accuracy is numerically correct, but one sentence frames that best run as the method’s headline accuracy, which is a cherry-pick.

## Evidence checked

- `audit-output/trial_fixture/manuscript.docx`
- `audit-output/trial_fixture/data/study_data.csv`
- `audit-output/trial_fixture/results/run_results.csv`
- `audit-output/trial_fixture/results/summary_statistics.json`
- `audit-output/trial_fixture/config/experiment_config.yaml`
- `audit-output/trial_fixture/code/analysis.py`

## Claims verified

| # | Claim | Paper text / value | Evidence | Status |
|---|---|---|---|---|
| 1 | Final sample size | “The final sample contained **524 observations**” | `study_data.csv` has **520** rows | **FAIL** |
| 2 | Mean accuracy | “Mean accuracy was **82.4%**” | Mean of six accuracies = **82.352941...%** | **PASS** |
| 3 | Best accuracy | “The best-performing run reached **84.7%** accuracy” | Max accuracy = **84.705882...%** at `run_id=4` | **PASS** |
| 4 | Best-accuracy framing | “Method accuracy was **84.7%** on the held-out test set” | 84.7% is only the best run; overall mean is 82.35% | **WARN** |
| 5 | Run count | “Across **five independent runs**” / “Number of runs **5**” | `run_results.csv` has **6** runs; config says `runs: 6` | **FAIL** |
| 6 | Max tree depth | “maximum tree depth of **5**” | Config and all runs use **3** | **FAIL** |
| 7 | Learning rate | “learning rate of **0.08**” | Config and runs use **0.08** | **PASS** |
| 8 | Scope claim | “generalizes across **all tabular classification domains**” | Evidence is one synthetic dataset and one split | **UNSUPPORTED** |

## Issues found

### [FAIL] Sample size overstated
- **Location**: Abstract; Methods 2.1; Table 1
- **Paper says**: final sample contained **524** observations
- **Evidence shows**: `data/study_data.csv` contains **520** rows
- **Fix**: Replace 524 with 520, or explain the discrepancy if a subset was excluded before analysis.

### [FAIL] Run count understated
- **Location**: Abstract; Methods 2.3; Table 1
- **Paper says**: **five independent runs**
- **Evidence shows**: `results/run_results.csv` contains **six** run rows, and `config/experiment_config.yaml` says `runs: 6`
- **Fix**: Update the manuscript to six runs.

### [FAIL] Maximum depth misreported
- **Location**: Methods 2.2
- **Paper says**: maximum tree depth of **5**
- **Evidence shows**: config and all run results use **max_depth = 3**
- **Fix**: Replace 5 with 3.

### [WARN] Cherry-pick framing in headline result
- **Location**: Abstract; Results 3; Table 1
- **Paper says**: “Method accuracy was **84.7%**”
- **Evidence shows**: 84.7% is the **best run only**; the six-run mean is **82.35%**
- **Fix**: Qualify the sentence as “best-run accuracy” or report the mean headline instead.

### [UNSUPPORTED] Scope overclaim
- **Location**: Abstract; Discussion 4
- **Paper says**: the method “generalizes across **all tabular classification domains**”
- **Evidence shows**: one synthetic dataset, one train/test split, six seeded runs
- **Fix**: Narrow the claim to this benchmark task only.

## Notes on the synthetic package

- The package is explicitly labeled synthetic and contains an answer key in `audit_key/expected_findings.json`.
- I did **not** use that answer key as primary evidence; it only served as a sanity check after independent recomputation.
- `code/analysis.py` is consistent with the raw results and confirms the six-run summary from the CSV files.

