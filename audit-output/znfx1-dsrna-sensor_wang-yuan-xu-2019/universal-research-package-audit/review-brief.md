# Research Package Review Brief

**Paper:** *Mitochondria-localised ZNFX1 functions as a dsRNA sensor to initiate antiviral responses through MAVS* — Wang, Yuan, Jia, Ge, Ling, Nie, Lan, Chen & Xu, *Nature Cell Biology* 21:1346–1356 (2019)
**What was reviewed:** the manuscript text plus the seven author-deposited Source Data files
**Companion document:** `technical-audit.md` (full evidence and calculations) · `audit-ledger.json` (machine-readable record)

This brief is written for readers who want the findings without the tooling detail. Every label is explained in words, and no conclusion here is stronger than the one in the technical audit.

---

## Review at a glance

| Area | Assessment | What this means |
|---|---|---|
| Statistical method as stated | POSITIVE | Where the spreadsheets store the authors' own p-values, recalculating from the raw replicate numbers reproduces them almost exactly. The test named in the paper is the test that was used. |
| Sample sizes in the patient and mouse experiments | POSITIVE | The number of samples and animals in the spreadsheets matches what the figure legends say, for Figures 1f, 1g, 2a, 2b, 2g and 3a–3c. |
| Descriptions that disagree with the data | CONCERN | Four places where the paper's wording does not match the deposited numbers: a group size, a replicate count, a genotype label, and the data-availability statement. |
| The three headline mechanism claims | LIMITATION | Mitochondrial location, RNA binding and the MAVS interaction rest on Figures 4–6, which were supplied only as blot images with no numbers. They could not be checked numerically. |
| Two Figure 7 panels | LIMITATION | Only part of each panel's data was deposited, so the printed p-values cannot be traced to the numbers provided. |
| Blot images | NOT ASSESSED | Image-integrity analysis was outside this audit's scope and no validated tool for it was available. |
| Seven other claims | NOT ASSESSED | Data were deposited but this audit did not recalculate them. They are neither confirmed nor questioned. |
| Audit output quality | POSITIVE | The automated validator passed this audit's own ledger with zero errors and zero warnings. |

---

## Issues requiring attention

| Priority | Assessment | Issue | Where to look | What the evidence shows | Why it matters | Reviewer action |
|---:|---|---|---|---|---|---|
| 1 | CONCERN | Survival experiment group size | Fig. 3f; legend at manuscript line 1083; data in `Source Data Fig 3.xlsx` cells B32:C41 | The legend says 10 mice per group. The deposited series never rises above 5 in either group. Three other readings were tested (percent survival, pooled cohorts, number-at-risk); none produces 10. | Group size affects how much confidence a survival difference carries. | Ask for the per-animal survival table and confirm the group size used for the test. |
| 1 | CONCERN | Genotype label disagreement | Fig. 7c; legend at manuscript line 2537; data labels in `Source Data Fig 7.xlsx` cells B38 and B41 | The legend describes wild-type or *Mda5*−/− cells. The deposited rows are labelled *Rig-i*−/− and *Mda5*−/−. There is no wild-type row. | This panel supports the claim that ZNFX1 works without RIG-I, so which genotype was used matters to the interpretation. | Ask which genotypes were used, and correct either the legend or the data labels. |
| 2 | CONCERN | Replicate count disagreement | Fig. 2h; legend at manuscript line 910; data in `Source Data Fig 2.xlsx` rows 57–60 | The legend states three independent experiments. The influenza/HSV-1 half of the panel deposits four replicate rows for every group. The VSV/EMCV half correctly has three. | The stated number of repeats should match the data used. | Ask the authors to confirm the number of repeats for each part of the panel. |
| 2 | CONCERN | Data-availability statement is broader than the package | Manuscript line 3011 | The statement promises source data for Figures 1–7 and Supplementary Figures 1–6. The package supplied here has numbers for Figures 1, 2, 3 and 7 only, plus blot images for 4–6, and nothing for the supplementary figures. | Readers relying on the statement may expect files that were not in this package. | Confirm whether the additional files exist and can be added. |
| 3 | UNRESOLVED | One replicate far below its siblings | `Source Data Fig 7.xlsx` cell G40 | The value is 4,176.86, about ten and a half times below its two sibling replicates (45,514.85 and 42,552.97) in the same group. | A ten-fold gap is the signature of a misplaced decimal point, but it can also be a real outlier. The package contains nothing that distinguishes the two. | Ask the authors to check this cell against the original instrument output. |
| 3 | NEUTRAL | Control arms fixed at exactly 1 | `Source Data Fig 2.xlsx` and `Fig 7.xlsx` control columns | Control groups are deposited as the constant 1 in every replicate, with no spread at all. | This is ordinary fold-change normalisation, not an error. It is worth knowing when reading these panels, because the variability in such a comparison comes entirely from the treated group. | No action; context for interpretation. |

**One thing deliberately not listed as a problem.** Recalculating the only Figure 7g comparison that was deposited gives results far from the two printed p-values. That looks like a serious mismatch, and it is *not* reported as one. The deposited block contains only two of the four groups the panel displays, and the missing groups are the ones the printed p-values most likely compare. On this evidence the printed values can be neither confirmed nor contradicted. It is recorded as something that could not be verified, not as an error.

---

## What checked out well

| Assessment | Check completed | Result | Scope limitation |
|---|---|---|---|
| POSITIVE | Recalculated the Figure 2h VSV comparison from the raw replicates | Matched the authors' stored p-value to fifteen decimal places (0.004186885624489591 vs 0.004186885624489595) | Applies to this one cell only |
| POSITIVE | Recalculated the Figure 2h EMCV comparison | Matched the stored p-value to the same precision | Applies to this one cell only |
| POSITIVE | Tested whether a different common test could explain the stored values | The alternative (Welch) test gives 0.0237 and 0.0110 and does **not** match, confirming the paper's stated test is the one used | Covers the two cells above |
| POSITIVE | Counted patient and macaque samples against the legend | 9 controls, 14 HIV-infected, 18 SIV samples — all exactly as stated | Counts only; the values themselves were not re-derived |
| POSITIVE | Counted animals per group in the mouse experiments | Figures 3a and 3b have 4 per group, Figure 3c has 8 and 4 per group, all as stated | Counts only |
| POSITIVE | Checked every deposited file opens and is intact | All 8 files readable, all fingerprinted | Structural check only |
| POSITIVE | Screened every deposited replicate group for internal outliers | Only the one cell noted above stood out | Numeric screen only |

---

## What could not be verified

| Assessment | Item | Why verification was incomplete | Effect on review | What would resolve it |
|---|---|---|---|---|
| LIMITATION | Mitochondrial location, RNA binding, and the MAVS interaction (Figures 4, 5, 6) | Supplied as uncropped blot images only, with no numbers behind them | These are the paper's three headline mechanism claims, and none could be checked numerically | Quantification tables for those panels |
| LIMITATION | Figure 7g printed p-values | Only 2 of the 4 displayed groups were deposited | The printed values can be neither confirmed nor questioned | The ZNFX1 and ZNFX1+VSV replicate values, plus confirmation of which pair each p-value compares |
| LIMITATION | Figure 7e quantification | Only the empty-vector arms were deposited | The comparison cannot be reproduced | The ZNFX1, RIG-I and MDA5 arms |
| LIMITATION | Figure 3f survival statistic | Timepoint units and per-animal records were not deposited | The effect of the group-size discrepancy on the result could not be tested | The per-animal survival table |
| LIMITATION | Extended Data and Supplementary figures | Not present in the package | Those panels were outside what could be reviewed | The corresponding source data |
| LIMITATION | Any analysis code | None was supplied | Nothing could be re-run; recalculation was done independently instead | Not expected for a package of this type — noted so the absence is not misread |
| NOT ASSESSED | Blot image integrity | Outside this audit's scope; no validated tool available | Image-level questions are simply unexamined | A specialist image-integrity review |
| NOT ASSESSED | Seven further claims with deposited data | This audit did not recalculate them | They are unexamined, not cleared | A follow-up recalculation pass |

---

## Paper navigation guide

| Paper location | What to check | Related item |
|---|---|---|
| Title and Abstract | The mechanism claims they assert rest on Figures 4–6, the part of the package with no numeric data | L-001 |
| Figure 2h legend (line 910) | Stated repeat count against the deposited rows | F-001 |
| Figure 3f legend (line 1083) | Stated group size against the deposited series | F-002 |
| Figure 7c legend (line 2537) | Stated genotypes against the deposited row labels | F-003 |
| Figure 7g panel (lines 2463–2464) | Which groups each printed p-value compares | L-002 |
| Data availability (line 3011) | Scope of the promise against what is actually present | F-005 |
| Methods, Statistics (lines 2853–2854) | The stated test — this one checked out | F-006 |

---

## Questions for the authors

| # | Location | Question | Why this is needed |
|---:|---|---|---|
| 1 | Fig. 3f | Could you supply the per-animal survival table and confirm the number of mice per group? | The legend states 10 per group; the deposited data describe at most 5. |
| 2 | Fig. 7c | Which host genotypes were used in this panel? | The legend says wild-type or *Mda5*−/−; the data are labelled *Rig-i*−/− and *Mda5*−/−. |
| 3 | Fig. 2h | How many independent experiments underlie each sub-panel? | The influenza/HSV-1 block deposits four replicate rows against a stated three. |
| 4 | Fig. 7g | Which two groups does each printed p-value compare, and could you supply the ZNFX1 arms? | Only two of the four displayed groups were deposited. |
| 5 | Fig. 7d/7e | Could you supply the ZNFX1, RIG-I and MDA5 arms of the FACS quantification? | Only the empty-vector arms were deposited. |
| 6 | `Source Data Fig 7.xlsx`, cell G40 | Could you confirm this value against the original qPCR output? | It sits about ten-fold below its two sibling replicates. |
| 7 | Figs. 4–6 | Do quantification tables exist for these panels? | Only blot images were supplied, so the mechanism claims could not be checked numerically. |
| 8 | Data availability | Do source data exist for the Extended Data and Supplementary figures? | The statement indicates they do; they were not in this package. |

---

## Bottom line

- **What is good:** The statistical method the paper names is demonstrably the method used — recalculating from the raw replicates reproduces the authors' own stored p-values to fifteen decimal places, and a plausible alternative test does not. Sample and animal counts match the legends everywhere they could be checked. All deposited files were intact and readable.

- **What needs attention:** Four places where the paper's description does not match its own deposited data — the Figure 3f group size (10 stated, at most 5 deposited), the Figure 7c genotype labels, the Figure 2h replicate count, and the scope of the data-availability statement. One spreadsheet cell sits about ten-fold below its siblings and should be confirmed against the original record.

- **What remains unknown:** Whether any of those four discrepancies changes a published result. The audit could not test that, and deliberately did not guess. The paper's three headline mechanism claims — mitochondrial location, RNA binding, MAVS interaction — could not be checked numerically at all, because no numbers were supplied for Figures 4–6. Two Figure 7 panels deposited only part of their data. Seven further claims were left unexamined.

- **What this does not mean:** None of this indicates fabrication, falsification or any other misconduct, and none of it is a publication decision — this audit makes no recommendation about acceptance, rejection or retraction, and takes no position on whether readers should rely on the paper. A discrepancy between a legend and a spreadsheet is a correspondence problem; it is not evidence that the underlying experiment is wrong. Missing files limit what could be verified and say nothing about whether the results are correct. Equally, the checks that passed cover only what they cover.

> This brief lists demonstrated issues, completed positive checks, and central verification limitations. A concern is an evidence-backed discrepancy, while a limitation means verification could not be completed. Neither implies misconduct. Absence from this brief does not mean every other claim was reproduced.

**Output validation:** PASS (0 errors, 0 warnings) — this certifies the structure and arithmetic of the audit's own records, not the research package.
