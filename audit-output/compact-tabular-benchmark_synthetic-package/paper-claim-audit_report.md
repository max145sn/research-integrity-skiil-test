# Paper Claim Audit Report — Compact Tabular Benchmark Package

**Date**: 2026-09-07
**Skill**: `paper-claim-audit` (`.github/skills/paper-claim-audit/skill.md`)
**Primary auditor**: Claude Sonnet 5
**Cross-model reviewer**: GPT-5.3-Codex, fresh zero-context task agent (no answer key provided — this was a genuine blind audit; unlike the earlier synthetic trial, this package ships no `audit_key/expected_findings.json`)
**Package audited**: `trial/compact_tabular_benchmark_package/` (`manuscript.docx`, `data/benchmark_data.csv`, `results/run_metrics.csv`, `results/aggregate_results.json`, `config/model_config.yaml`, `code/summarize_results.py`)

## Overall Verdict: ❌ FAIL

Five separate, material numeric discrepancies were found between the manuscript and the raw evidence files, independently confirmed by a second, zero-context model. The manuscript understates the dataset size arithmetic, misstates the run count and max tree depth, misreports the mean accuracy, and conflates the single best run with an "overall" aggregate result.

## Method

1. Extracted the manuscript's text from `manuscript.docx` (unzipped, parsed `word/document.xml`).
2. Independently recomputed every reproducible statistic directly from `data/benchmark_data.csv` and `results/run_metrics.csv` — deliberately **not** trusting the pre-computed `results/aggregate_results.json`, using it only as a secondary cross-check.
3. Checked `config/model_config.yaml` for internal consistency against the raw run metrics.
4. Tested every possible 6-of-7 run subset to see whether the manuscript's claimed "six-run mean of 79.6%" could be reconstructed via an undisclosed exclusion, rather than assuming it was a simple fabrication/rounding error.
5. Dispatched a **fresh, zero-context reviewer (GPT-5.3-Codex)**, given only the file paths and no other context, to redo the same recomputation from scratch. Its findings independently corroborated all discrepancies below with no additional issues raised beyond what is captured here.

## Claims Verified

| # | Location | Paper Value | Evidence Value | Status |
|---|----------|-------------|-----------------|--------|
| 1 | Abstract; §2.1; Table 1 | "analytical dataset contained **486 records**" / "final dataset comprised **486 records**" | `benchmark_data.csv` has **480** rows | **mismatch** |
| 2 | §2.1; Table 1 | Training partition **320** | `split == 'train'` count = **320** | exact_match |
| 3 | §2.1 (implied) | "retained the remaining records for testing" → implies 486 − 320 = **166** test records | `split == 'test'` count = **160**; every run's `test_n` = 160 | **internal_inconsistency** |
| 4 | §2.1 | "three predictors and a binary outcome" | Columns `signal_a, signal_b, category_c` (3 predictors); `outcome` ∈ {0,1} | exact_match |
| 5 | §2.1 | "All records were complete and therefore included in analysis" | 0 missing values in any column | exact_match |
| 6 | §2.2 | "maximum tree depth of **6**" | `run_metrics.csv` distinct `max_depth` = {4}; `model_config.yaml` `max_depth: 4` | **mismatch** |
| 7 | §2.2 | "learning rate of **0.06**" | All runs and config use **0.06** | exact_match |
| 8 | Abstract; §2.3; Table 1 | "**six** independent runs" / "Run count **6**" | `run_metrics.csv` contains **7** runs (run_id 1–7); config `runs: 7` | **mismatch** |
| 9 | Abstract; §3; Table 1 | "Mean accuracy across runs was **79.6%**" | Mean of all 7 run accuracies = **80.0%** exactly | **mismatch** |
| 10 | (subset check for #9) | — | Tested all seven possible 6-of-7 subsets; closest is excluding run 4 (the best run), giving 79.6875% (rounds to 79.7%, not 79.6%) — no subset reproduces 79.6% | **mismatch** (not explained by undisclosed exclusion either) |
| 11 | Abstract; §3; Table 1 | "Peak accuracy reached **81.9%**" | Max single-run accuracy = 81.875% (run 4) | rounding_ok |
| 12 | §3 | "**Overall model accuracy was 81.9%** on the held-out test set" | 81.9% is the *best run only*; the actual overall/mean accuracy is 80.0% | **cherry_pick** |
| 13 | §4 Discussion; Abstract | "dependable performance across **small structured-data applications**" / "supports use of the selected configuration across small structured-data applications" | Evidence is a single simulated dataset with one fixed train/test partition and 7 seeds — no other datasets or applications tested | **unsupported_scope** |
| 14 | (consistency check) | — | `model_config.yaml` (training_rows=320, test_rows=160, runs=7, max_depth=4, learning_rate=0.06) is fully consistent with the raw run/data files | exact_match (config vs. raw data agree; the **manuscript** is what diverges from both) |

## Issues Found

### [FAIL] Dataset size overstated, and internally inconsistent with its own training/test split
- **Location**: Abstract; §2.1 Data; Table 1
- **Paper says**: "final dataset comprised 486 records," with 320 assigned to training and "the remaining records" (implying 166) reserved for testing.
- **Evidence shows**: `benchmark_data.csv` has 480 rows total (320 train + 160 test, matching `config/model_config.yaml` exactly).
- **Status**: `mismatch` (number inflation) + `internal_inconsistency` (the paper's own stated total and training count imply a test count that matches neither the actual data nor the paper's own Table 1, which never states the test count explicitly).
- **Fix**: Correct 486 → 480 throughout (abstract, §2.1, Table 1).

### [FAIL] Run count understated
- **Location**: Abstract; §2.3 Evaluation; Table 1
- **Paper says**: "six independent runs" / "Run count 6."
- **Evidence shows**: `results/run_metrics.csv` contains 7 run rows (run_id 1–7); `config/model_config.yaml` states `runs: 7`.
- **Fix**: Correct 6 → 7 throughout.

### [FAIL] Maximum tree depth misreported
- **Location**: §2.2 Model and configuration
- **Paper says**: "maximum tree depth of 6."
- **Evidence shows**: `config/model_config.yaml` and every row of `run_metrics.csv` use `max_depth = 4`.
- **Fix**: Correct 6 → 4.

### [FAIL] Mean accuracy does not match any accounting of the raw runs
- **Location**: Abstract; §3 Results; Table 1
- **Paper says**: "Mean accuracy across runs was 79.6%" (attributed to "six runs").
- **Evidence shows**: The mean of all 7 actual runs is exactly 80.0%. Exhaustively testing every possible 6-of-7 run subset (in case one run was silently excluded) produces means ranging 79.69%–80.21%, none of which equal 79.6%. The closest subset (excluding the best run, #4) yields 79.6875%, which itself rounds to 79.7%, not 79.6%.
- **Fix**: Report the true 7-run mean (80.0%), or if an exclusion was intended, disclose which run was dropped and why — the currently reported figure is unsupported either way.

### [WARN] Cherry-picked best run reported as "overall" accuracy
- **Location**: §3 Results
- **Paper says**: "Overall model accuracy was 81.9% on the held-out test set" — stated immediately after (and seemingly in contrast to/supplementing) the mean-accuracy sentence.
- **Evidence shows**: 81.9% (81.875%) is the single best run's accuracy (run 4), not an aggregate/overall figure. The true overall mean is 80.0%.
- **Fix**: Relabel this figure explicitly as "best-run" or "peak" accuracy (as Table 1 correctly does — "Peak accuracy" — creating an inconsistency between the body text's "Overall model accuracy" phrasing and Table 1's own "Peak accuracy" label for the identical number).

### [WARN] Unsupported scope/generalization claim
- **Location**: Abstract; §4 Discussion
- **Paper says**: performance is "dependable ... across small structured-data applications" and the configuration is supported "across small structured-data applications."
- **Evidence shows**: Only one simulated benchmark dataset with one fixed train/test partition (7 random seeds of the same split) was evaluated — no other datasets, domains, or partitions were tested.
- **Fix**: Narrow the claim to this specific benchmark/dataset; broader applicability across "small structured-data applications" in general is not supported by a single-dataset, single-partition study.

## Files in this audit
- `PAPER_CLAIM_AUDIT_COMPACT_BENCHMARK.md` — this report
- `PAPER_CLAIM_AUDIT_COMPACT_BENCHMARK.json` — machine-readable version
- `trial_fixture2_manuscript_text.txt` — full text extracted from `trial/compact_tabular_benchmark_package/manuscript.docx`
