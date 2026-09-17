# ZNFX1 mitochondrial dsRNA sensor (Wang, Yuan, Jia, Ge, Ling, Nie, Lan, Chen & Xu, Nature Cell Biology 21:1346-1356, 2019; DOI 10.1038/s41556-019-0416-0): Review Brief

## Review at a glance

| Area | Assessment | What this means |
|---|---|---|
| Audit output | PASS | The ledger validator returned PASS. |

## Issues requiring attention

| Priority | Assessment | Issue | Why it matters | Reviewer action |
|---:|---|---|---|---|
| 1 | CONCERN | [F-002] Figure 3f survival legend states n = 10 mice per group; deposited series describe at most 5 per group | Verification: MAJOR; result correctness: NOT_DETERMINED. | Ask the authors for the per-animal survival table (one row per mouse, with time of death or censoring) and confirm the group size used for the Gehan-Breslow-Wilcoxon test. |
| 1 | CONCERN | [F-003] Figure 7c legend names wild-type cells; the deposited block is labelled Rig-i-/- and Mda5-/- | Verification: MAJOR; result correctness: NOT_DETERMINED. | Ask the authors which genotypes were used in Figure 7c and to correct either the legend or the deposited row labels. |
| 2 | CONCERN | [F-001] Figure 2h H1N1/HSV-1 block deposits four replicate rows while the legend states n = 3 | Verification: MINOR; result correctness: NOT_DETERMINED. | Ask the authors to confirm the number of independent experiments for each Figure 2h sub-panel and to align the legend with the deposited rows. |
| 2 | CONCERN | [F-005] Data-availability statement promises broader source data than the supplied package contains | Verification: MAJOR; result correctness: NOT_DETERMINED. | Confirm whether numeric source data for Figures 4-6, the Extended Data figures and Supplementary Figs 1-6 exist and can be added to the package. |
| 3 | UNRESOLVED | [F-004] One Figure 7c replicate is about ten-fold below its two sibling replicates | Verification: MINOR; result correctness: NOT_DETERMINED. | Ask the authors to confirm the value in this cell against the original qPCR output. |
| 3 | NEUTRAL | [F-008] Control arms are deposited as the exact constant 1 with zero variance | Verification: MINOR; result correctness: NOT_DETERMINED. | Note when reading the panels: where a t-test compares a treated arm against a fold-change reference fixed at 1.0, the spread comes entirely from the treated arm. |
| 4 | POSITIVE | [F-006] Figure 2h VSV and EMCV p-values reproduce exactly from the deposited replicates using the stated test | Verification: NONE; result correctness: NONE_DEMONSTRATED. | No action required; this check supports correspondence for these two cells only. |
| 4 | POSITIVE | [F-007] Clinical-sample and mouse group sizes match the legend-stated n where they are deposited | Verification: NONE; result correctness: NONE_DEMONSTRATED. | No action required. |

## What could not be verified

| Assessment | Item | Meaning |
|---|---|---|
| LIMITATION | [L-001] No numeric source data for Figures 4, 5 and 6 | This limits verification and does not by itself show the research result is wrong. |
| LIMITATION | [L-002] Figure 7g deposits two of the four displayed groups, so its printed P values cannot be attributed | This limits verification and does not by itself show the research result is wrong. |
| LIMITATION | [L-003] Figure 7e deposits only the empty-vector arms | This limits verification and does not by itself show the research result is wrong. |
| LIMITATION | [L-004] No analysis code, scripts or workflow supplied | This limits verification and does not by itself show the research result is wrong. |
| LIMITATION | [L-005] Extended Data and Supplementary figure source data absent from the package | This limits verification and does not by itself show the research result is wrong. |
| LIMITATION | [L-006] Figure 3f timepoint units and per-animal records are not deposited | This limits verification and does not by itself show the research result is wrong. |
| NOT_ASSESSED | [B-001] Image forensics on the uncropped blot scans was not performed | This limits verification and does not by itself show the research result is wrong. |
| NOT_ASSESSED | [B-002] Seven deposited claims were not independently recomputed | This limits verification and does not by itself show the research result is wrong. |
| NOT_ASSESSED | [B-003] Panel-to-P-value mapping relies on the manuscript text layer and is positional for some panels | This limits verification and does not by itself show the research result is wrong. |

## Bottom line

- **What is good:** See completed positive checks in the technical audit.
- **What needs attention:** See the concern rows above.
- **What remains unknown:** See the verification and audit limitations.
- **What this does not mean:** The audit does not infer misconduct or make a publication decision.

**Output validation:** PASS
