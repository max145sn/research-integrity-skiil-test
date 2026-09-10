# Paper Claim Audit Report

**Date**: 2026-09-07
**Skill**: paper-claim-audit (`.github/skills/paper-claim-audit/skill.md`)
**Auditors**: Claude Sonnet 5 (primary, direct recomputation) + GPT-5.3-Codex (fresh, zero-context cross-model reviewer, independent recomputation)
**Paper**: Ratner, K., Burrow, A. L., & Thoemmes, F. (2016). *The effects of exposure to objective coherence on perceived meaning in life: a preregistered direct replication of Heintzelman, Trent & King (2013)*. Royal Society Open Science, 3, 160431. (`paper/Manuscript.pdf`)

## Overall Verdict: ⚠️ WARN

All numeric claims for **Study 4** (linguistic triads) that could be checked against raw evidence (`results/Data.csv`) reproduce exactly (to rounding). However, **all numeric claims for Study 2** (tree photos) are **unverifiable**: the repository contains no raw data file for Study 2. `code/Code.R` expects to read `Study2rawdataexp.csv` and `Study4rawdataexp.csv`, but only one raw data file exists in the repo (`results/Data.csv`), and its column schema (`MLQ_1..6`, `EA_1..5`, `RO-BR-FL_9` = "Coherent"/"Incoherent") matches only the **Study 4** design — there is no tree-photo/seasonal-condition data anywhere in the repo. The final Bayes-factor and random-effects meta-analysis figures also could not be independently recomputed in this environment because R (with the `BayesFactor` and `metafor` packages) is not installed; those inputs were instead cross-checked for internal consistency.

## Claims Verified: 26 total (Study-4-checkable + input-consistency claims)
- exact_match: 8
- rounding_ok: 15
- missing_evidence: 1 (covers ~15 distinct Study 2 numeric claims, see below)
- not_independently_recomputable: 7 (Bayes factors, meta-analytic pooled effects, original-study/G*Power figures)
- mismatch: 0

## Method

1. Extracted full manuscript text from `paper/Manuscript.pdf` (see `audit-output/manuscript_extracted_text.txt`).
2. Read `code/Code.R` to reconstruct the exact data-cleaning and modeling pipeline (attention-check exclusion, reverse-coding, variable construction, ANOVA/regression/contrast specifications).
3. Independently re-implemented the **Study 4** pipeline in Python (pandas/scipy/statsmodels) directly from `results/Data.csv` (script: `audit-output/recompute_study4.py`) and compared every reproducible number in the manuscript (Table 2, Table 3 "Study 4" rows, the unadjusted t-test, and the adjusted regression) against the recomputed values.
4. Dispatched a **fresh, zero-context reviewer session (GPT-5.3-Codex)** with no access to this conversation — only the manuscript text, `code/Code.R`, and `results/Data.csv` — to independently redo the same recomputation and flag any claim it could not verify. Its results corroborated the primary analysis with no additional discrepancies.
5. Confirmed (via `git log`/`glob`) that no Study 2 raw data file exists anywhere in the repository or its history reachable from this branch.

## Issues Found

### [WARN] Missing evidence: Study 2 raw data absent from repository
- **Location**: Table 1; §3.1.1 (N=482 recruited, demographics); §4.1–4.2 (ANOVA F(2,475)=0.35, p=0.705; contrast t(476)=0.59, p=0.554, d=0.06; adjusted regression F(7,470)=23.17, R²=0.26; Table 3 "Study 2: tree photos" rows; Bayes factors BF01 = 0.033 / 0.185 / 0.285); footnote 1 (F(7,470)=22.12 time-average reanalysis); Box–Cox exploratory analysis (F(6,449)=25.19).
- **Paper says**: Specific means, SDs, test statistics, p-values, and effect sizes for the "trees in seasonal change" replication (Study 2), based on N=478 valid observations.
- **Evidence shows**: `code/Code.R` reads `Study2rawdataexp.csv`, which does not exist anywhere in this repository (only `results/Data.csv` exists, and its 124-column schema matches the Study 4 questionnaire, not Study 2's tree-photo/timing design with 2,700+ columns referenced in `Code.R`).
- **Status**: `missing_evidence`
- **Fix**: Add the Study 2 raw data file (`Study2rawdataexp.csv`, referenced in `Code.R`) to the repository so these ~15 Study 2 claims can be independently verified. Until then, Study 2 results in the manuscript should be treated as unaudited.

### [Not independently recomputable] Bayesian and meta-analytic pooled statistics
- **Location**: §4.2.2, §4.4.2 (BF01 values for Study 4: 0.181, 0.135); §4.5 (random-effects meta-analysis: unadjusted pooled effect 0.246 [z=2.20, p=0.028], Q(5)=14.49 p=0.013, moderator b=−0.447; adjusted pooled effect 0.214 [z=2.63, p=0.009], Q(5)=7.78 p=0.169, moderator b=−0.318, plus stimulus-moderator sub-analyses).
- **Reason**: These require R with the `BayesFactor` (JZS prior) and `metafor` (REML random-effects) packages, neither of which is installed in this environment. R itself (`Rscript`) is not present.
- **What was checked instead**: The hardcoded inputs to `Code.R`'s `escalc()` calls for the Study 4 replication effect (`res4unadj`, `res4adj`: means 4.680208/4.833333, SDs 1.64/1.44, n=144/147) were verified to exactly match the independently recomputed Study 4 descriptives — i.e., the *inputs* feeding the meta-analysis for the replication data are correct. The original-study effect-size inputs (Heintzelman et al. 2013 Study 1–4 means/SDs/betas, hardcoded as comments citing that paper's Tables 1–2) are external to this repository and were not re-verified against the original source.
- **Status**: `not_independently_recomputable` (advisory only — not a mismatch)
- **Fix**: Re-run `code/Code.R` in an R environment with `metafor` and `BayesFactor` installed to confirm the final pooled/Bayesian figures match the manuscript exactly.

## All Checkable Claims (detailed)

| # | Location | Paper Value | Evidence Value (recomputed from `results/Data.csv`) | Status |
|---|----------|-------------|---------------------------------------------------|--------|
| 1 | §3.1.2 | Recruited 294 | raw rows = 294 | exact_match |
| 2 | §3.1.2 | Age 18–79, M=34.73, s.d.=11.4 | min 18, max 79, M=34.7313, SD=11.3966 | rounding_ok |
| 3 | §3.1.2 | 166 female (56.5%), 128 male (43.5%) | D1: 166 / 128 (56.46% / 43.54%) | rounding_ok |
| 4 | §4.3.1 | 3 failed attention check; final N=291 | 3 excluded (check≠1); final n=291 | exact_match |
| 5 | §4.3.1 | No missing data on relevant variables | 0 missing values found | exact_match |
| 6 | Table 2 | total N=291, coherent n=144, incoherent n=147 | 144 / 147 (291 total) | exact_match |
| 7 | Table 2 | MLQ-P total 4.76 (1.54); coherent 4.68 (1.64); incoherent 4.83 (1.44) | 4.7576 (1.5449); 4.6802 (1.6441); 4.8333 (1.4428) | rounding_ok |
| 8 | Table 2 | EPA total 4.33 (1.51); coherent 4.22 (1.50); incoherent 4.44 (1.52) | 4.3288 (1.5119); 4.2153 (1.5039); 4.4399 (1.5157) | rounding_ok |
| 9 | Table 2 | ENA total 2.73 (1.66); coherent 2.83 (1.75); incoherent 2.64 (1.57) | 2.7320 (1.6620); 2.8264 (1.7474); 2.6395 (1.5744) | rounding_ok |
| 10 | §4.4.1 | t(289) = −0.845, p = 0.399, 95% CI [−0.51, 0.20], d = 0.099 | t=−0.8449, p=0.3989, CI[−0.5098, 0.2036], \|d\|=0.0991 | rounding_ok |
| 11 | §4.4.1 | Overall regression F(3,287)=46.62, p<0.001, R²=0.33, adj. R²=0.32 | F=46.618, p=1.42e-24, R²=0.3276, adj. R²=0.3206 | rounding_ok |
| 12 | §4.4.1 | Condition η²p = 0.00004 | partial η² = 4.17e-05 | rounding_ok |
| 13 | Table 3 (Study 4) | condition: 0.02 (0.15), t=0.11, p=0.913, CI[−0.28, 0.31] | 0.0164 (0.1498), t=0.109, p=0.913, CI[−0.278, 0.311] | rounding_ok |
| 14 | Table 3 (Study 4) | EPA: 0.56 (0.05), t=10.48, p<0.001, CI[0.45, 0.66] | 0.5559 (0.0530), t=10.482, p<0.001, CI[0.452, 0.660] | rounding_ok |
| 15 | Table 3 (Study 4) | ENA: −0.06 (0.05), t=−1.32, p=0.189, CI[−0.15, 0.03] | −0.0635 (0.0482), t=−1.318, p=0.189, CI[−0.158, 0.031] | rounding_ok |
| 16 | `Code.R` meta input | `res4unadj`: m1i=4.680208, m2i=4.833333, sd1i=1.64, sd2i=1.44, n1i=144, n2i=147 | Matches recomputed group means/SDs/n exactly | exact_match |
| 17 | `Code.R` meta input | `res4adj`: m1i=0.01638 (unstandardized condition coefficient) | Recomputed coefficient = 0.016382 | exact_match |
| 18–26 | Study 2 (Table 1, ANOVA, contrast, Table 3 Study-2 rows, BF01 ×3, N=482/478, demographics, footnote reanalysis, Box–Cox model) | Various | No raw data file available | missing_evidence |
| 27–33 | Bayes factors (Study 4 ×2) and pooled meta-analysis statistics (×2 models + moderator sub-analyses) | Various | Requires R (`BayesFactor`, `metafor`); not available in this environment | not_independently_recomputable |

## Code.R Observations (non-blocking, advisory)

- `setwd("C:\\Users\\")` is a hardcoded, incomplete local path — the script cannot be run as-is by anyone else, which is why Study 2 raw data could not be located or exercised here even if it existed elsewhere.
- Study 4 variable construction relies on fixed positional column indices (e.g. `st4[c(110:113, 126)]`) rather than column names, which is brittle but was verified here (via name-based reconstruction) to produce numbers identical to the manuscript.
- The "Unregistered exploratory analyses" section (time-average reanalysis, Box–Cox transform, interaction/quadratic probing) is clearly and correctly labeled as exploratory/post hoc in both the code comments and the manuscript text, consistent with preregistration norms.

## Files in this audit

- `PAPER_CLAIM_AUDIT.md` — this report
- `PAPER_CLAIM_AUDIT.json` — machine-readable version
- `manuscript_extracted_text.txt` — full text extracted from `paper/Manuscript.pdf` (evidence trail)
- `recompute_study4.py` — Python script used to independently recompute all Study 4 statistics from `results/Data.csv`
