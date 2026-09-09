# Experiment Audit Report — "error file" Package (`tabular_model_research_package.zip`)

**Date**: 2026-09-07
**Auditor**: External reviewer backend, fresh zero-context cross-model reviewer
(`gpt-5.3-codex`, high reasoning effort, sandboxed, no prior conversation
context), substituting for `mcp__codex__codex` per the `experiment-audit`
skill's reviewer-independence requirement (that MCP tool is unavailable in
this environment).
**Project**: `documents/error file/tabular_model_research_package.zip`
(extracted read-only to `audit-output/error_file_extracted/` for inspection —
the original zip and `documents/` tree were not modified)

## Overall Verdict: FAIL

## Integrity Status: fail

**Important cross-check**: this package's `data/benchmark_data.csv`,
`results/run_metrics.csv`, `results/aggregate_results.json`,
`config/model_config.yaml`, `code/summarize_results.py`, and `manuscript.docx`
are **byte-identical** (confirmed via `git diff --no-index` and file-hash
comparison) to the previously-audited `trial/compact_tabular_benchmark_package/`
(see `audit-output/PAPER_CLAIM_AUDIT_COMPACT_BENCHMARK.md`). This package adds
three extra files not present in that trial package: `LICENSE.txt`, `README.md`,
`data/benchmark_data.xlsx` (a formatted workbook independently verified to be
cell-for-cell consistent with the CSV), and `results/predictions.csv`
(record-level predictions, not present in the earlier package). None of these
additions change the underlying findings — they are the same planted
discrepancies, now with per-record prediction data available to independently
verify accuracy from first principles.

## Checks

### A. Ground Truth Provenance: PASS
- **Evidence**: `data/benchmark_data.csv:1` (`outcome` column), `results/predictions.csv:1` (`actual`, `predicted` columns), cross-referenced record IDs (e.g. `data/benchmark_data.csv` rows 322/323/331/481 vs `results/predictions.csv` rows 2/3/11/162/1121), `code/summarize_results.py:6-15`.
- **Details**: The reviewer performed a full join across all 1,120 prediction rows against the raw dataset's `outcome` column and found **zero mismatches** — `actual` in `predictions.csv` is genuinely sourced from the dataset, not derived from `predicted`. Per-run accuracy in `run_metrics.csv` exactly matches an independent recomputation of `predicted == actual` counts. No fabricated or circular ground truth.

### B. Score Normalization: PASS
- **Evidence**: `results/run_metrics.csv` rows 2-8 (per-run `correct` / `test_n` columns), `code/summarize_results.py:8-15`.
- **Details**: Accuracy uses a fixed, independent denominator (`test_n = 160`, the actual held-out test set size) — e.g. run 1: 126/160 = 0.7875; run 4: 131/160 = 0.81875. Raw counts are reported alongside the percentage. No self-referential normalization against the model's own output statistics. No score is suspiciously close to 100% (best observed: 81.875%).

### C. Result File Existence & Claim Verification: FAIL
- **Evidence**: manuscript text (extracted from `manuscript.docx`) vs. `data/benchmark_data.csv` (480 data rows + header), `results/run_metrics.csv` (7 runs), `config/model_config.yaml` (`max_depth: 4`, `learning_rate: 0.06`), `results/aggregate_results.json`.
- **Details** — all values independently recomputed from raw files, not taken from `aggregate_results.json` or trusted from the manuscript:
  - Manuscript claims **486 records** → actual **480** rows. **Mismatch.**
  - Manuscript claims **six independent runs** → actual **7** runs in `run_metrics.csv`. **Mismatch.**
  - Manuscript claims mean accuracy **79.6%** → recomputed mean across all 7 runs is **80.0%** exactly. No 6-of-7 run subset reproduces 79.6% either (closest subset, excluding the best run, gives 79.6875% ≈ 79.7%, still not an exact match). **Mismatch, unreproducible via any disclosed or plausible undisclosed exclusion.**
  - Manuscript claims **maximum tree depth of 6** → actual/config value is **4** (consistent across `model_config.yaml` and every row of `run_metrics.csv`). **Mismatch.**
  - Manuscript's peak/"overall" accuracy figure of **81.9%** is consistent with the true best single run (0.81875, run 4) — but presenting the single best run's number as an "overall model accuracy" conflates best-case with aggregate performance (cherry-picking framing, addressed further under Scope).
  - `learning_rate = 0.06` **matches** across manuscript, config, and data — correctly reported.
  - No experiment tracker file exists in this package (not applicable, by package design — not itself a flag).

### D. Dead Code Detection: PASS
- **Evidence**: `code/summarize_results.py` (16 lines total).
- **Details**: Every statistic the script computes (`dataset_rows`, `run_count`, `mean_accuracy`, `accuracy_sd`, `best_accuracy`, `depths`) is emitted in the final JSON output. No unused functions or abandoned code paths.

### E. Scope Assessment: WARN
- **Evidence**: `data/benchmark_data.csv` (1 dataset, fixed 320/160 train/test split), `results/run_metrics.csv` (7 seeds/runs, same 160-record test set reused each run), manuscript language ("dependable performance across small structured-data applications", "supports use ... across ... applications").
- **Details**: The actual tested scope is a single simulated dataset with one fixed train/test partition, evaluated across 7 random seeds — not multiple datasets, domains, or partitions. The manuscript's generalization language ("across ... applications") exceeds this single-dataset, single-partition scope.

### F. Evaluation Type: simulation_only
- **Evidence**: `README.md` ("The benchmark records are simulated and non-personal"), `data/benchmark_data.csv:1`, `results/predictions.csv:1`.
- **Details**: Ground truth is genuinely dataset-provided (not model-derived), but the underlying dataset itself is explicitly simulated, not real-world/human data. This is disclosed in the README but should be classified as `simulation_only` rather than `real_gt` when assessing how much the results generalize to real-world tabular data — worth noting given the manuscript's generalization claims (see Scope, above).

## Action Items
- Correct the manuscript's stated dataset size (486 → 480 records) and run count (six → seven runs).
- Correct or investigate the mean accuracy discrepancy (stated 79.6% vs recomputed 80.0%) — no disclosed or plausible run-subset exclusion explains this value; if an exclusion was applied, it must be disclosed and re-verified, otherwise the number should be corrected.
- Correct the stated maximum tree depth (6 → 4), consistent with both the config file and every run's metadata.
- Clarify the "overall model accuracy was 81.9%" statement — this is the single best run's accuracy, not an aggregate/mean figure; re-label it as "best observed run" or replace with the true mean (80.0%) to avoid a cherry-picking impression.
- Qualify or remove generalization language ("across small structured-data applications") given the single-dataset, single-partition test scope, and explicitly disclose that the dataset is simulated (not real-world data) when discussing generalizability.

## Claim Impact
- Dataset size (486 records): **unsupported** — actual is 480.
- Run count (six independent runs): **unsupported** — actual is 7.
- Mean accuracy (79.6%): **unsupported** — actual is 80.0%, not reproducible via any run subset.
- Max tree depth (6): **unsupported** — actual/config is 4.
- Learning rate (0.06): **supported** — matches exactly.
- Peak/"overall" accuracy (81.9%): **needs qualifier** — numerically consistent with the single best run, but mislabeled as an overall/aggregate figure.
- Generalization across "small structured-data applications": **unsupported** — only one dataset/partition tested.

## Reviewer Backend Note

As with the prior audits in this repository, `mcp__codex__codex` and
`mcp__manual_review__review` (the skill's specified reviewer backends) are
unavailable in this environment. The executor (Claude, this session) collected
file paths only and dispatched a separate, stateless `task`-tool agent
(`agent_type: general-purpose`, `model: gpt-5.3-codex`, high reasoning effort,
a single self-contained prompt with no reference to this conversation or to
prior audits of the near-identical `compact_tabular_benchmark_package`) to
perform the actual A-F integrity judgment, preserving the skill's reviewer-
independence requirement.
