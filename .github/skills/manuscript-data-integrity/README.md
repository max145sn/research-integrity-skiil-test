# Manuscript Data Integrity Check — Documentation

A Claude Skill that screens a submitted manuscript (PDF) and its raw data (CSV/XLSX) for statistical fabrication, manipulation, or reporting errors, and produces a flagged report for an editor or reviewer to act on.

This document explains what the skill does, how to use it, what each script checks, and where its limits are. `SKILL.md` inside the package is Claude's own instructions, this file is for the human running it.

## What it does

Give it a manuscript plus its underlying data, and it runs a fixed battery of checks:

- Five universal checks, on every manuscript regardless of field
- Discipline-specific checks, matched to the study design (clinical, psych/behavioral, genomics, preclinical, imaging, survey)
- A compiled report with each item marked 🔴 Flag, 🟡 Note, or 🟢 Clear

It never concludes fraud or misconduct. It surfaces numbers that don't add up and leaves the judgment call to a human.

## Installation

1. Download `manuscript-data-integrity.skill`.
2. In Claude, use the "Save skill" option on the file card, or upload it through Settings → Skills.
3. It activates automatically in a conversation where you upload a manuscript and raw data and ask for a data integrity check, fabrication screen, or similar. You don't need to invoke it by name.

## How to use it

Upload the manuscript PDF and the raw data file(s), then ask something like:

- "Run a data integrity check on this submission."
- "Does this manuscript's data look consistent with the raw files?"
- "Screen this for fabrication before it goes to review."

Claude will read the manuscript, extract reported statistics, load the raw data, run the checks below, and return the flagged report inline. It does not need you to name individual tests, though you can ask it to run just one (e.g., "just run GRIM on Table 2").

## The five universal checks

| Check | What it catches | How |
|---|---|---|
| Sample size / df consistency | Mismatched N's between text, tables, and raw data | Manual cross-read, no script |
| GRIM / GRIMMER | Means/SDs that are mathematically impossible for the stated N | `scripts/grim_check.py` |
| Statistic/p-value recomputation | p-values inconsistent with the reported test statistic, including flipped significance | `scripts/statcheck.py` |
| Internal consistency | Abstract vs. results mismatches, tables that don't sum correctly | Manual cross-read, no script |
| Terminal digit analysis | Unnatural clustering of last digits across a table of values | `scripts/digit_analysis.py` |
| Duplication scan | Exact duplicate rows, duplicate IDs, near-identical "independent" replicates | `scripts/duplicate_scan.py` |

## Discipline-specific checks

Defined in `references/discipline_checks.md`, applied based on the manuscript's stated design:

- **Clinical/biomedical**: CONSORT flow consistency, baseline comparability (standardized mean differences), outcome switching against the trial registration, survival analysis consistency
- **Psychology/behavioral**: full statcheck sweep, GRIM/GRIMMER on all scale means, SPRITE-style plausibility, p-value clustering near .05
- **Genomics/omics**: batch effect detection, multiple testing correction verification, metadata-data consistency
- **Preclinical/bench**: replicate independence, outlier exclusion symmetry (image forensics flagged as out of scope)
- **Imaging/neuroimaging**: multiple comparison correction verification, motion/exclusion criteria consistency across groups
- **Survey/observational**: straightlining detection, survey weighting verification

Most of these are manual cross-checks Claude performs by reasoning over the raw data, not scripts, they're marked as such in the report.

## Running the scripts directly

You can also run any script standalone, outside a Claude conversation, for testing or batch processing.

**GRIM/GRIMMER**
```
python scripts/grim_check.py --mean 3.67 --n 20 --sd 1.14
python scripts/grim_check.py --csv reported_stats.csv   # columns: label,mean,n,sd
```

**Statistic/p-value recomputation**
```
python scripts/statcheck.py --test t --stat 2.31 --df1 48 --p 0.03
python scripts/statcheck.py --test f --stat 4.12 --df1 2 --df2 45 --p 0.05
python scripts/statcheck.py --csv reported_tests.csv    # columns: test,stat,df1,df2,p
```
Supported test types: `t`, `f`, `chi2`, `r` (Pearson correlation, df1 = n-2).

**Terminal digit analysis**
```
python scripts/digit_analysis.py --values 3.4,5.6,7.2,1.0,...
python scripts/digit_analysis.py --csv table_values.csv --column value
```
Needs at least ~20 values to be statistically meaningful.

**Duplication scan**
```
python scripts/duplicate_scan.py --file data.csv --id-column subject_id
python scripts/duplicate_scan.py --file data.xlsx --corr-threshold 0.999
```
Near-duplicate row detection only runs when there are 4+ numeric columns, fewer than that produces meaningless correlations.

Dependencies: `scipy`, `pandas`, `openpyxl` (for `.xlsx` support).

## Reading the report

Each check gets one of three flags:

- 🔴 **Flag** — mathematically inconsistent or implausible, needs editorial follow-up before proceeding
- 🟡 **Note** — inconsistent but plausibly a rounding or reporting convention, worth a clarifying question to the authors
- 🟢 **Clear** — passed

The report also lists what wasn't checked, most importantly image/blot forensics, which needs dedicated tools this skill doesn't run.

## Limitations, read before relying on this

- **GRIMMER here is simplified**, not the full published algorithm. Treat its flags as "worth a second look," not definitive proof of inconsistency.
- **No image or figure forensics.** Duplicated or spliced blots, gels, and micrographs need dedicated pixel-forensics tools (e.g., ImageTwin, Forensically). This skill will say so rather than skip it silently.
- **PDF table extraction quality varies.** Manuscripts with numbers embedded as images of tables, rather than real text, will extract poorly. Spot-check the extracted numbers against the source PDF, especially for anything flagged.
- **Doesn't judge methodology.** It checks whether the numbers are internally possible, not whether the study design, endpoint choice, or analysis plan was sound.
- **False positives will happen**, especially with GRIM/GRIMMER on data that isn't actually integer-scaled, and with digit analysis on small tables. Every flag is a prompt to look closer, not a conclusion.

## Suggested next step

Run it against two or three manuscripts you already know well and compare the flags against your own read. That's the fastest way to calibrate thresholds (especially the correlation cutoff in the duplication scan) to your editorial context before relying on it for live submissions.
