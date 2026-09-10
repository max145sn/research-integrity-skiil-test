# Research Package Integrity Review — Accessible Brief (Output B)

**Paper reviewed:** "Chromosomal translocation-derived aberrant Rab22a
drives metastasis of osteosarcoma" (Liao et al., *Nature Cell Biology*,
2020)

This brief summarizes a review of how well this paper's reported results
can be checked against the underlying data and code. It is written for
researchers, reviewers, editors, and authors, without requiring you to read
any code. See the companion technical audit
(`research-package-integrity-audit2_integrity-audit.md`) for full evidence
and reasoning.

## B1. Review at a glance

| Area | Assessment | What this means |
|---|---|---|
| Package completeness | LIMITATION | Only the manuscript text was available to review. No analysis code, no configuration files, and no result data files exist locally — the underlying sequencing data is stored in an external public archive (SRA accession SRP181860) that was not retrieved for this review. |
| Checked manuscript-internal consistency | POSITIVE | Every number that could be cross-checked against itself elsewhere in the paper (cohort totals, a percentage calculation, a unit conversion, a peptide-length calculation) reconciled exactly. |
| Manuscript wording consistency | CONCERN | One drug-dosing description uses two different, non-interchangeable units in two different places in the paper. |
| Replicate-count consistency | CONCERN | One figure has an unexplained difference in the number of repeated experiments between closely related panels. |
| Scope of the paper's central claim | CONCERN | The paper's title and abstract state a general causal claim that is broader than the specific patient numbers given in its own Results section. |
| Independent recalculation of raw results | LIMITATION | No raw measurement data was available, so statistical results (p-values, survival curves) could not be independently recalculated. |
| Misconduct inference | NEUTRAL | This review does not assess or infer intent, and does not conclude that any finding reflects wrongdoing. |

**Six key facts:**
- Only the manuscript itself was reviewable; no code or raw data package was supplied.
- All internally-checkable arithmetic in the paper (percentages, subgroup totals, unit conversions) was correct.
- Drug-dosing units are inconsistent between two mentions of the same treatment (milligrams per kilogram vs. milligrams per milliliter).
- One figure has an unexplained difference in replicate count between similar panels.
- The paper's headline causal claim is broader than the specific evidence (a rare gene fusion found in 2 of 37, i.e. 5.4%, of a screened patient subgroup) described in its own Results.
- No statistical result or figure could be independently recalculated because the raw measurements are not available in this review.

## B2. Issues requiring attention

| Priority | Assessment | Issue | Where to look | What the evidence shows | Why it matters | Recommended reviewer action |
|---:|---|---|---|---|---|---|
| 1 | CONCERN | [F-01] Two different units used for the same drug dose | Methods (drug administration) and Extended Data Figure 10 legend | The Methods section states the iRGD peptide was given at "1 or 10 milligrams per kilogram" of body weight. The Extended Data Figure 10 legend instead describes the same treatment arms as "1 and 10 milligrams per milliliter," a concentration, not a dose. | These are not the same kind of quantity, so a reader cannot tell from the paper alone what was actually administered. Impact on the reported result was not determined — resolving it needs the original dosing records. | Ask the authors to confirm the correct unit and make the two passages consistent. |
| 2 | CONCERN | [F-02] Unexplained difference in replicate count within one figure | Extended Data Figure 10 legend, panels c–f versus panel g | Panels c through f report 3 independent repeats of a migration/invasion experiment; panel g, testing a closely related outcome in the same figure, reports 4. | A different number of repeats for one panel is not necessarily wrong, but the paper does not explain why it differs, so a reader cannot judge whether the extra repeat changes confidence in that one result relative to its neighbors. | Ask the authors why panel g used a different number of repeats. |
| 3 | CONCERN | [F-03] The paper's title claim is broader than the patient evidence described in its own Results | Title/Abstract vs. the clinical-cohort paragraph in Results | The title states this gene fusion "drives metastasis of osteosarcoma" in general terms. The Results section states the fusion was found in only 2 of 37 (5.4%) screened metastatic patients, and most of the direct evidence from real (not laboratory-engineered) patient tissue comes from a single patient's cell lines. | A general disease-wide claim, if taken at face value, could overstate how common or generalizable this specific mechanism is in osteosarcoma patients as a whole. | Ask whether the title/abstract should specify the rare-fusion, single-institution-cohort scope. |
| 4 | CONCERN | [F-04] "Multiple cancer types" claim is broader than the cited case count | Results, cross-cancer generalization sentence | The paper states this type of fusion "occur[s] and drive[s] metastasis in multiple cancer types," citing only 2 clinical cases and 2 cell lines to support that statement. | A "multiple cancer types" claim implies broader evidence than 2 cases provide. | Ask the authors to specify exactly which cancer types and how many cases/cell lines support this statement. |

All four items above are demonstrated from the manuscript's own text; none
required raw data that was unavailable. Impact on the paper's overall
conclusions was not evaluated for any of them — evaluating impact was not
possible without the underlying raw data.

## B3. What checked out well

| Assessment | Check completed | Result | Scope limitation |
|---|---|---|---|
| POSITIVE | Percentage calculation for the headline prevalence figure (2 of 37 patients) | Recalculated independently as 5.4054%, matching the paper's stated "5.4%." | Only checks the calculation itself, not whether the underlying count of 2 or 37 is accurate. |
| POSITIVE | Patient cohort subgroup totals (37 metastatic + 60 non-metastatic patients; 2 fusion-positive + 35 fusion-negative within the metastatic group) | Both subgroup totals add up exactly to the stated overall totals (97 and 37). | Only checks internal arithmetic consistency, not whether the original patient counts are correct. |
| POSITIVE | Tumor-volume unit conversion (1,500 cubic millimeters stated as equal to 1.5 cubic centimeters) | The conversion is mathematically correct and is used consistently everywhere it appears in the paper. | Confirms internal consistency only. |
| POSITIVE | Peptide-length calculation (a stated amino-acid range matches a stated "15-amino-acid" peptide length) | The math is exactly correct. | Confirms internal consistency only. |
| POSITIVE | Sequencing-depth figures and pipeline settings restated in different parts of the paper | Every restatement matched exactly, with no contradictions found. | Confirms the paper is internally consistent about these numbers; does not confirm the pipeline was actually run this way. |

## B4. What could not be verified

| Assessment | Item | Why it could not be verified | Effect on the review | What would resolve it |
|---|---|---|---|---|
| LIMITATION | Any figure or table's underlying data | No "Source Data" files (which this journal normally makes available alongside the paper) were retrieved for this review. | No figure or table value in this paper could be independently checked against its underlying measurements. | Retrieve the journal's Source Data files for this paper and re-run this review against them. |
| LIMITATION | Statistical test results (p-values, survival-time comparisons) | These require the raw measurements behind each test, which were not supplied. | The correctness of individual statistical calculations remains unverified by this review. | Supply the raw measurement data underlying each reported statistic. |
| LIMITATION | The RNA-sequencing/genome-sequencing analysis that identified the gene fusion | The underlying sequencing data is stored in a public archive (accession SRP181860) that was not downloaded for this review. | The core molecular-discovery claim (that this fusion exists and was correctly identified) could not itself be independently re-verified. | Download and independently re-analyze the deposited sequencing data. |
| NOT ASSESSED | Whether the paper corrected for testing many statistical comparisons across its many figures | This was technically feasible to at least partially discuss from the text, and was already covered by a previous, separate review in this same folder (`experiment-audit_report.md`); it was not re-assessed as a new item here to avoid duplicating that existing finding. | No additional conclusion is added here beyond what the prior review already states. | See `experiment-audit_report.md` in this same folder for this specific point. |

None of the rows above should be read as evidence that the paper's results
are incorrect — they indicate only that this review could not check them
with the material available.

## B5. Paper navigation guide

| Paper location | What to check | Related item |
|---|---|---|
| Title and Abstract | Compare the general causal claim against the specific patient numbers given later in the paper | F-03 |
| Results, clinical-cohort paragraph | Confirm the 2-of-37 (5.4%) fusion-positive figure and how it relates to the paper's general claims | F-03 |
| Results, cross-cancer generalization sentence | Check how many cases/cell lines actually support the "multiple cancer types" statement | F-04 |
| Methods, drug administration section | Compare the stated iRGD peptide dose/unit against the Extended Data Figure 10 legend | F-01 |
| Extended Data Figure 10 legend | Compare the number of repeated experiments across panels c–f versus panel g | F-02 |

## B6. Author questions

| # | Location | Question for the authors | Why this question is needed |
|---:|---|---|---|
| 1 | Methods; Extended Data Figure 10 legend | Which unit is correct for the iRGD peptide treatment doses — milligrams per kilogram of body weight, or milligrams per milliliter of solution — and are the two mentions describing the same treatment arms? | The paper currently states two different, non-interchangeable units for what appears to be the same treatment. |
| 2 | Extended Data Figure 10 legend | Why does panel g use 4 independent repeats while panels c–f use 3, in the same figure testing related outcomes? | The paper does not explain this difference. |
| 3 | Title/Abstract | Would the authors consider specifying that the reported mechanism is based on a fusion found in 2 of 37 (5.4%) screened patients at a single institution? | The current general wording is broader than the specific evidence given in the Results section. |
| 4 | Results, cross-cancer generalization sentence | Which specific cancer types, and how many cases or cell lines, support the statement that this fusion occurs and drives metastasis "in multiple cancer types"? | Only 2 cases and 2 cell lines are cited for what reads as a broader claim. |

## B7. Bottom line

**What is good:** every number in the paper that could be checked against
another restatement of itself elsewhere in the same text — patient cohort
totals, a percentage calculation, a unit conversion, and a peptide-length
calculation — was internally consistent and mathematically correct.

**What needs attention:** a unit inconsistency in one drug-dosing
description, an unexplained replicate-count difference within one figure,
and two places where the paper's general causal wording reads as broader
than the specific patient/case numbers given in its own Results section.

**What remains unknown:** whether any individual figure, table, or
statistical result matches its underlying raw data, because no code, raw
data, or journal Source Data file was available for this review — only the
manuscript text itself was reviewed.

**What this does not mean:** this review does not conclude that the paper
is wrong, does not infer any intent to mislead, and does not validate or
invalidate any claim that could not be checked. Absence of a listed concern
elsewhere in the paper does not mean that material was independently
verified.

## B8. Scope note

> This brief lists demonstrated issues, completed positive checks, and
> central verification limitations. A concern indicates an evidence-backed
> discrepancy, while a limitation indicates that verification could not be
> completed. Neither label implies misconduct. Absence from this brief does
> not mean every other claim was independently reproduced. See the
> comprehensive technical audit for the full evidence, coverage, and
> limitations.
