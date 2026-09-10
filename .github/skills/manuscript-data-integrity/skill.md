---
name: manuscript-data-integrity-check
description: Run statistical data integrity checks on a submitted manuscript (PDF) and its raw data files (CSV/spreadsheet), to screen for fabrication, manipulation, or reporting errors before or during editorial/peer review. Use this skill whenever the user uploads a manuscript plus raw data and asks for a data integrity check, statistical audit, fabrication screening, GRIM/GRIMMER test, statcheck-style consistency check, or asks whether the numbers in a paper "add up" or "look right." Also trigger on requests like "screen this submission," "check this data," "audit these results," or "does this look fabricated," even if the user doesn't name a specific test. This skill should always be used over ad hoc manual checking when both a manuscript and raw data are available.
---

# Manuscript Data Integrity Check

Runs a structured battery of statistical integrity checks against a manuscript PDF and its underlying raw data (CSV/XLSX), and produces a flagged screening report for a human editor or reviewer to act on.

**This is a screening tool, not a verdict.** It surfaces mathematical inconsistencies and implausibilities. It never concludes fraud, error, or misconduct. Every flagged item goes to a human for judgment.

## Workflow

1. **Extract manuscript content.** Read the PDF (use the pdf-reading skill's approach if bundled/available: text extraction first, then targeted page rasterization for any tables that don't extract cleanly as text). Pull out:
   - Every reported sample size (N) — overall, per group, per analysis
   - Every reported mean, SD, and test statistic (t, F, chi-square, r) with its df and p-value
   - The stated study design and discipline (clinical trial, psychology/behavioral, genomics, preclinical/bench, imaging, survey) — this determines which discipline-specific checks apply (see `references/discipline_checks.md`)

2. **Load raw data files.** Read each CSV/XLSX into a dataframe. Note column names, row counts, and how they map to the manuscript's reported N's.

3. **Run the five universal checks** (always, regardless of discipline):
   - **Sample size / df consistency** — cross-check every N and df mentioned in text, tables, and figures against each other and against the raw data row counts. Do this by direct comparison; no script needed, just careful reading.
   - **GRIM / GRIMMER** — run `scripts/grim_check.py` on every reported mean (and SD, for GRIMMER) that comes from integer or fixed-scale data (Likert items, counts, discrete scores) paired with its N.
   - **Statistic/p-value recomputation** — run `scripts/statcheck.py` on every reported (test type, statistic, df, p-value) tuple to check the p-value is mathematically consistent with the statistic, and flag cases where the significance conclusion (p<.05) would flip.
   - **Internal consistency** — manually cross-read: does the abstract match the results text, do table percentages sum correctly, do figure values match table values. No script; this is close reading.
   - **Terminal digit analysis** — run `scripts/digit_analysis.py` on any table with 20+ reported numeric values to test whether the last-digit distribution is suspiciously non-uniform.
   - **Duplication scan** — run `scripts/duplicate_scan.py` on each raw data file to catch exact duplicate rows, duplicate ID fields, and suspiciously high pairwise row correlations (near-duplicate fabrication).

4. **Run discipline-specific checks.** Open `references/discipline_checks.md` and apply the section matching the manuscript's design (clinical, psych/behavioral, genomics, preclinical/bench, imaging, survey). Most of these are manual cross-checks against the raw data using the reasoning described there, not scripts — call them out explicitly in the report as "manual check" vs. "automated check."

5. **Compile the report.** For every check, state: what was tested, the result, and a flag level:
   - 🔴 **Flag** — mathematically inconsistent or implausible, needs editorial follow-up before proceeding
   - 🟡 **Note** — inconsistent but plausibly explained by rounding/reporting convention, worth a clarifying question to authors
   - 🟢 **Clear** — passed
   Group by check, not by table, so the reviewer can scan flags fast. Never state or imply fabrication, intent, or misconduct — describe only what was tested and what the numbers show.

6. **Note what wasn't checked.** Explicitly list anything out of scope for this pass — image/blot forensics (needs dedicated tools like ImageTwin or Forensically, not scriptable here), plagiarism, and anything requiring domain expertise beyond arithmetic (e.g., whether a clinical endpoint choice was appropriate).

## Notes on scope

- Image duplication/manipulation forensics (western blots, microscopy, gels) is **not** covered by this skill — it requires dedicated pixel-forensics software. Flag in the report that this pass is needed separately.
- This skill checks whether the numbers are internally possible and consistent, not whether the underlying science or methodology is sound. Say so if asked to comment beyond that scope.
- If a script errors on malformed input (unparseable numbers, missing columns), report the parsing problem to the user rather than silently skipping the check.
