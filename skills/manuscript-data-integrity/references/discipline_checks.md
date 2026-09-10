# Discipline-specific data integrity checks

Apply the section matching the manuscript's design, in addition to the five universal checks in SKILL.md. Most of these are manual cross-checks between the manuscript text and the raw data — call them out as "manual check" in the report rather than implying a script ran.

## Clinical / biomedical trials

- **CONSORT flow consistency.** Trace the same participant count through every stage: enrolled → randomized → allocated per arm → completed → analyzed. The flow diagram, the methods text, and the results table must all agree. Any unexplained drop between stages is a flag.
- **Baseline comparability.** Compare baseline characteristics between arms using standardized mean differences from the raw data, not just the reported p-values (a "non-significant" baseline difference can still be a large, meaningful imbalance if the sample is small). Flag large SMDs (commonly >0.1–0.2) that the authors don't address.
- **Outcome switching.** If a trial registration or protocol is available, compare the pre-specified primary/secondary outcomes to what's actually reported as primary in the manuscript. A switched primary outcome, especially one that happens to be significant when the original wasn't, is a flag.
- **Survival analysis consistency.** Check that reported hazard ratios, confidence intervals, and event/censoring counts are consistent with the raw time-to-event data and with the shape of any reported Kaplan-Meier curve description.

## Psychology / behavioral / social science

- **Statcheck sweep.** Run `scripts/statcheck.py` across every t-test, F-test, and chi-square in the manuscript, not just a sample. This is the single highest-yield automated check for this discipline.
- **GRIM/GRIMMER on all Likert/count means.** Any mean derived from integer response scales should pass `scripts/grim_check.py`.
- **SPRITE-style plausibility.** For any reported mean + SD, manually check whether a distribution of integers within the scale's bounds (e.g., 1–7) can actually produce that mean and SD at that N. If the SD is implausibly low or high given the scale range, flag it. (Full SPRITE simulation is out of scope for this skill; flag for follow-up with dedicated SPRITE tooling if the check looks borderline.)
- **p-value clustering near .05.** Note (without treating as fabrication) if the manuscript has an unusual number of p-values just below .05 (e.g., .041–.049) relative to how many tests were run — worth a comment to the editor about possible p-hacking, distinct from fabrication.

## Genomics / omics

- **Batch effect check.** If raw expression/sequencing data is available, check whether samples cluster by a technical variable (processing date, batch, site) rather than the biological variable of interest. Unexplained batch clustering undermines the reported comparison.
- **Multiple testing correction verification.** If the manuscript claims FDR or Bonferroni correction, recompute the correction from the raw p-values (if available) and confirm the reported "significant" hits match.
- **Metadata-data consistency.** Cross-check sample metadata (sex, tissue type, genotype, condition) against what the raw data itself implies (e.g., sex-linked gene expression should match the stated sex).

## Preclinical / bench science

- **Image forensics — out of scope for this skill.** Note in the report that blot/image duplication and manipulation screening requires dedicated tools (e.g., ImageTwin, Forensically) and was not performed here.
- **Replicate independence.** If raw per-replicate values are available, check whether "biological replicates" are suspiciously tightly correlated (near-identical values), which can indicate the same sample measured multiple times rather than independent replicates. `scripts/duplicate_scan.py`'s correlation check can be reused here.
- **Outlier exclusion symmetry.** If the manuscript describes excluding outliers, check whether the stated exclusion rule (e.g., ">2 SD from mean") was applied evenly across all groups, or only to the group that would otherwise weaken the result.

## Imaging / neuroimaging

- **Multiple comparison correction across voxels/ROIs.** Confirm the manuscript's claimed correction method and threshold match what's actually applied, if raw statistical maps or ROI-level data are available.
- **Motion/exclusion criteria consistency.** Check that data-quality exclusion criteria (e.g., motion thresholds) were applied identically across comparison groups, not more leniently in one.

## Survey / large-N observational

- **Straightlining / careless-response detection.** In the raw response file, flag respondents who gave identical or near-identical answers across many items (a common bot or low-effort response signature). `scripts/duplicate_scan.py` can help surface these as near-duplicate rows.
- **Weighting verification.** If survey weights are used, recompute a handful of headline weighted statistics from the raw data and weights, and confirm they match the reported figures.

## When raw data isn't available for a discipline-specific check

Say so explicitly in the report rather than skipping the item silently — e.g., "Batch effect check not performed: raw expression matrix not provided, only summary statistics." This tells the editor what to request from authors if a deeper check is warranted.
