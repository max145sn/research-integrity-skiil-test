# Review Brief — Restoration Treatments and Tree Recruitment in a Costa Rican Wet Forest

**Paper:** Schubert et al. (2025), *Ecological Applications* 35(1), e3053
**Materials reviewed:** the authors' archived data package (Dryad) and the accepted-manuscript version of the paper
**Companion document:** a comprehensive technical audit accompanies this brief and contains the full evidence and coverage detail.

This brief is written for reviewers, editors, and authors. It does not require reading code. It reports what was checked, what agreed, what did not, and what could not be checked at all.

**Two terms used throughout:**

- **Independent recomputation** means the auditor recalculated a number directly from the authors' raw data using separately written software. It tests whether the data support the published number. It does not run the authors' own analysis programs.
- **Verification limitation** means a check could not be completed because something needed was not available. It is not evidence that the research is wrong.

---

## B1. Review at a glance

| Area | Assessment | What this means |
|---|---|---|
| Descriptive numbers in the paper | **POSITIVE** | 31 of 38 checkable numbers were independently recalculated from the raw data and agreed. |
| Seven numerical or wording discrepancies | **CONCERN** | Seven checked values did not agree. All are small; two are wording or scope problems rather than calculation errors. |
| Analysis code for this paper | **LIMITATION** | The program the archive's own README names for this paper is not in the archive. |
| Every statistical result in the paper | **LIMITATION** | Because that program is missing, no model, significance test, or confidence interval could be checked. |
| Running the authors' original code | **LIMITATION** | Not attempted. The relevant program is absent, and the audit machine had no R installation. |
| Underlying data quality | **POSITIVE** | No data errors were demonstrated. Two documentation problems affect reuse, not the published results. |
| Figures and supplementary material | **LIMITATION** | The supplied file is a text-only manuscript version with no figure images and no supplement. |
| Misconduct | **NEUTRAL** | This review does not assess or infer intent, and found nothing suggesting fabrication or manipulation. |

**Six key points:**

- The paper's counts and percentages hold up well against the authors' own raw data. Totals of individuals, taxa, families, species richness, plot counts, and sampled area all reproduce.
- The most consequential problem is a **missing file**, not a wrong number. The analysis program named in the archive's README is absent, and the one program that is present states in its first line that it belongs to a different paper.
- Because of that, everything statistical in the paper is unverified — not contradicted, simply unchecked.
- Of seven disagreements, the two most substantive are a wording problem (percentages described as shares "of individuals" that are in fact shares of taxa) and one word: the paper says **all** large stems of the planted species were originally planted, but the data record 17 that were not.
- The other five disagreements are percentage differences of roughly 0.4 to 6 percentage points. None changes the direction of a result or the paper's conclusions.
- **An earlier audit of this same package reported several problems that this re-check found to be incorrect.** See "A note on a prior review" at the end.

---

## B2. Issues requiring attention

Ordered by priority. "Research concern" means a demonstrated problem in the paper or data. "Audit limitation" means verification could not be completed.

| # | Assessment | Type | Issue | Where to look | What the evidence shows | Why it matters | Recommended reviewer action |
|---:|---|---|---|---|---|---|---|
| 1 | LIMITATION | Audit limitation | **[F-01] The analysis program for this paper is not in the archive** | Archive README, line 67 | The README names a file called `FinalAnalysis_ECOLAPP_Schubert.et.al.R` as the analysis code. That file is not present. The only analysis program in the archive declares on its first line that it reproduces a different manuscript. | No statistical result in the paper can be independently checked: not the rarefied species-richness estimates or their confidence intervals, not the sampling-completeness figures, not the ordination or composition tests, and none of the models behind Figure 3. | Request the missing analysis program before assessing the statistical results. |
| 2 | CONCERN | Research concern | **[F-02] Percentages described as shares of individuals are actually shares of taxa** | Page 13, identification-resolution sentence | The paper reports that 94.2% of individuals were identified to species, 4.6% to genus and 1.1% to family. Those percentages match **taxon** counts exactly — the genus figure is 12 of 261, or 4.60%. Calculated across individuals, the genus share is 0.21%. | The numbers themselves are correct; the word "individuals" is wrong. Read literally, the sentence misdescribes identification quality by a factor of about twenty. No analysis depends on it. | Ask for the wording to be corrected to "taxa". |
| 3 | CONCERN | Research concern | **[F-05] The word "all" is contradicted by 17 records** | Page 15, statement about trees of at least 5 cm diameter | The paper states that **all** trees of at least 5 cm diameter belonging to the planted species in the applied-nucleation and plantation treatments were planted during the original restoration. The dataset records 17 such stems marked as natural recruits — 11 in applied nucleation and 6 in plantation, across three species, ranging from 5.0 to 27.3 cm in diameter. | The affected share is small, 17 of 1,781 stems, or 0.95%, and the quantitative pattern is unaffected. But the universal claim as written is not supported by the authors' own data. | Ask for the statement to be qualified, for example to "nearly all". |
| 4 | CONCERN, impact not yet determined | Research concern | **[F-03] Late-successional species reaching tree size: 15% reported, about 21% recalculated** | Page 13, size-class sentence | The same sentence reports that about 50% of mid-successional species reached the tree size class. That figure reproduces **exactly**, at 50.0% (26 of 52), which confirms the calculation was interpreted correctly. The companion late-successional figure recalculates to 21.3%, not 15%. | The exact match on the neighbouring figure makes a misinterpretation by the auditor unlikely. The effect of the difference on any conclusion was not tested, so no impact is claimed. | Ask how the 15% figure was derived. |
| 5 | CONCERN | Research concern | **[F-07] Mid-successional small-seeded species: 64% reported, 69.2% recalculated** | Page 11, seed-size sentence | Both trait sources supplied in the archive give 36 of 52 species, or 69.2%. The companion figure in the same sentence — 71% of late-successional species with seeds of at least 5 mm — reproduces at 71.1%. | A difference of 5.2 percentage points, equal to three species. Because the neighbouring figure reproduces, this is unlikely to be a mismatch between trait tables and more likely an error in this specific value. The stated conclusion, that most mid-successional species are small-seeded, holds either way. | Ask for the 64% value to be rechecked. |
| 6 | CONCERN | Research concern | **[F-04] Share of planted-species saplings that were originally planted: 60% reported, 65.3% recalculated** | Page 15 | Counting all planted-species saplings in the two planted treatments gives 126 of 193, or 65.3%. | A difference of 5.3 percentage points. The statement that a majority were originally planted holds under both figures. | Ask which set of records formed the denominator. |
| 7 | CONCERN | Research concern | **[F-06] Early-successional share of plantation saplings: 18.6% reported, 18.19% recalculated** | Page 14 | The two companion figures in the same sentence, 54.0% and 43.3%, reproduce exactly under one counting rule, and that rule gives 18.19% for plantation. No single counting rule reproduces all three published figures in the sentence. | At most 0.41 percentage points. Treatment ordering and the qualitative contrast are unaffected. | Ask which records were counted for the plantation figure. |
| 8 | CONCERN | Research concern | **[F-08] Unidentified individuals excluded: 0.04% reported, 0.030% or 0.100% recalculated** | Page 11 | Two plausible definitions of "not identified" give 26 individuals (0.030%) or 86 individuals (0.100%). The reported figure corresponds to roughly 34 individuals, which no tested definition produces. | Negligible under every definition tested, and not material to any analysis. | Ask which records were treated as unidentified. |
| 9 | CONCERN | Research concern (data archive) | **[F-09] The plot-area file lists a plot that has no survey records** | `PlotQuadrantes.csv`, the row labelled BBPL | The area file lists 33 plots, but one of them has no records in the census file, and the paper reports eight plantation plots. Anyone joining the two files without noticing would overstate plantation area by 12.1%. | **This did not affect the published results.** The paper's reported tree-density comparison reproduces at exactly 8.0% only when this plot is excluded — positive evidence that the published analysis used the correct eight plots. The problem is a hazard for future reusers of the archive. | Ask for the row to be removed or clearly flagged. |
| 10 | CONCERN | Research concern (data archive) | **[F-10] File encoding and two missing-value codes are undocumented** | The main census file and the README | The census file uses an older text encoding that the README does not mention; a standard modern read of the file fails partway through. The seed-size column contains two codes that are never defined. Five taxa have a blank family field. | Affects reuse rather than the published results. No reported value depends on these. | Ask for the encoding and the codes to be documented in the README. |
| 11 | LIMITATION | Audit limitation | **[F-11] The supplied paper version has no figures and no supplement** | The supplied PDF | The file is a 38-page accepted-manuscript version containing no figure images on any page, and no supplementary material was supplied. | All figure-level and supplement-level checks were impossible. This concerns the materials supplied for review, not the published article. | Obtain the typeset article and its supplement. |

---

## B3. What checked out well

These checks were **completed** and passed. They do not establish that the whole paper is correct.

| Assessment | Check completed | Result | Scope limitation |
|---|---|---|---|
| POSITIVE | Total individuals censused, by size class | All three totals reproduce exactly: 66,446 seedlings, 14,038 saplings, 3,842 trees, plus 1,941 surviving planted trees. | Confirms counting only; says nothing about how those counts were analysed. |
| POSITIVE | The abstract's "more than 80,000 individuals" | Reproduces at 84,326 naturally recruited individuals. | — |
| POSITIVE | Number of taxa and families | 255 taxa reproduces exactly once the archive's own documented exclusion of six poorly resolved taxa is applied. 65 families is 64 named families plus one unassigned group. | Depends on the exclusion rule recovered from the archive's code. |
| POSITIVE | Species richness in all four treatments | All four published values (156, 185, 196, 205) are consistent with the paper's documented practice of grouping inconsistently identified taxa into a single unit. | Consistency with a documented rule, not an exact raw-count match. |
| POSITIVE | Number of plots per treatment, and sampled area | 9, 9, 8 and 6 plots all confirmed, and the minimum sampled area of 1.01 hectares reproduces. | — |
| POSITIVE | Every plot's survey-unit count | All 32 surveyed plots match the archive's area file exactly. | The 33rd row in that file is the subject of item 9 above. |
| POSITIVE | Ten reported percentages about planted species, successional groups, and seed size | Reproduce within their stated precision, including 13.0% and 4.7% for planted-taxa seedlings, 1.8% for saplings, 54.0% and 43.3% for early-successional saplings, the "more than 75%" dominance figure at 79.1%, and 71% for large-seeded late-successional species at 71.1%. | Descriptive percentages only. |
| POSITIVE | The comparison of later-successional tree density against reference forest | The reported 8% reproduces at exactly 8.0%. | — |
| POSITIVE | The two claims about reference-forest species coverage | "About 90% of reference forest species" reproduces at 89.0%, and the companion figure of 10.5% absent reproduces in the range 10.34% to 10.96%. | — |
| POSITIVE | Figure 1 caption sample sizes | 52 mid-successional and 38 early-successional species reproduce exactly; 163 late-successional is consistent with the same grouping rule as species richness. | Caption text only; the figure itself was not available. |
| POSITIVE | Data-quality screening | No duplicate records, no impossible measurement values, consistent plot-to-treatment assignment, and consistent handling of empty survey units. | Screening, not exhaustive validation. |
| POSITIVE | Agreement between the two trait sources in the archive | Identical results on every trait calculation tested. | Shows internal consistency, not external correctness. |

---

## B4. What could not be verified

None of the items below is evidence that the research is wrong.

| Assessment | Item | Why it could not be verified | Effect on the review | What would resolve it |
|---|---|---|---|---|
| LIMITATION | Rarefied and extrapolated species-richness estimates and their confidence intervals | The analysis program for this paper is not in the archive. | A central result of the paper is unverified. | Supply the analysis program. |
| LIMITATION | Sampling-completeness estimates of 85–99% | Same. | Unverified. | Supply the analysis program. |
| LIMITATION | The ordination analysis and its reported stress values | Same. | Unverified. | Supply the analysis program. |
| LIMITATION | The statistical tests comparing community composition between treatments | The analysis program and the supplement are both absent. | Unverified. | Supply both. |
| LIMITATION | The abundance models and significance groupings behind Figure 3 | The analysis program is absent. | The paper's principal statistical figure is unverified. | Supply the analysis program. |
| LIMITATION | The abstract's claims of significantly elevated seedling and sapling establishment, and of plantation large-seeded densities resembling reference forest | These rest on models that could not be run. | Two headline conclusions are unverified. | Supply the analysis program. |
| LIMITATION | Survival percentages of originally planted trees | Records of what was planted, by species and plot, are not in the archive. | Survival rates cannot be recalculated. | Supply the planting records. |
| LIMITATION | All supplementary figures and tables | No supplement was supplied. | Unverified. | Supply the supplement. |
| LIMITATION | Running the authors' own code in its native environment | The relevant program is absent, and the audit machine had no R installation. These are two separate reasons; neither indicates the code fails. | The review rests on independent recalculation rather than on rerunning the authors' analysis. | Supply the program and run it in a suitable environment. |
| NOT ASSESSED | The spatial coordinate files in the archive | Inspecting them was possible, but no checked claim depends on them, so this was not completed. | No conclusion can be drawn from this review about those files. | A short follow-up inspection. |
| NOT ASSESSED | A previously reported conflict between the Methods and the Figure 1 caption over the number of early-successional species | The relevant sentence could not be located in the text extracted from the supplied manuscript version. | The conflict is neither confirmed nor refuted here, and is not counted as a finding. | Check the typeset article. |
| NOT ASSESSED | Study design, statistical appropriateness, and ecological interpretation | Outside the scope of this review, which examines whether reported numbers correspond to the archived evidence. | No judgement is offered on the quality of the science. | A subject-matter peer review. |

---

## B5. Paper navigation guide

| Paper location | What to check | Related item |
|---|---|---|
| Page 11, seed-size sentence | Whether 64% of mid-successional species are small-seeded; the neighbouring 71% figure is confirmed | F-07 |
| Page 11, exclusion sentence | Which records were counted as unidentified | F-08 |
| Page 13, identification-resolution sentence | Whether the percentages describe individuals or taxa | F-02 |
| Page 13, size-class sentence | How the 15% late-successional figure was derived; the neighbouring 50% is confirmed exactly | F-03 |
| Page 13–14, totals and richness | High-value positive verification — all totals and richness values reproduce | C-01 to C-11 |
| Page 14, sapling composition sentence | Which records were counted for the plantation figure | F-06 |
| Page 15, planted-species paragraph | The 60% denominator, and the word "all" in the following sentence | F-04, F-05 |
| Page 15, density comparison | High-value positive verification — the 8% figure reproduces exactly | F-09 |
| Figure 3 and its statistical results | Locate the missing analysis program before assessing | F-01 |
| Archive README, line 67 | Confirm which analysis program belongs to this paper | F-01 |

---

## B6. Author questions

All questions are neutral and none speculates about intent.

| # | Location | Question for the authors | Why this question is needed |
|---:|---|---|---|
| 1 | Archive README, line 67 | Could you supply the analysis program named there for this paper? It is not present in the archive. | Without it, no statistical result in the paper can be checked. |
| 2 | Page 13, identification-resolution sentence | Should "of individuals" read "of taxa"? | The reported percentages match taxon counts exactly, not individual counts. |
| 3 | Page 15, trees of at least 5 cm diameter | Should the word "all" be qualified? | The data record 17 stems of the planted species at that size that are marked as natural recruits. |
| 4 | Page 13, size-class sentence | How was the 15% figure for late-successional species derived? | The same calculation reproduces the companion 50% figure exactly but gives about 21% here. |
| 5 | Page 11, seed-size sentence | Could the 64% figure be rechecked? | Both trait sources in the archive give 69.2%, while the companion 71% figure reproduces. |
| 6 | Page 15, planted-species saplings | Which records formed the denominator for the 60% figure? | Counting all planted-species saplings in the two planted treatments gives 65.3%. |
| 7 | Page 14, sapling composition | Which counting rule produced the 18.6% plantation figure? | No single rule reproduces all three percentages in that sentence. |
| 8 | Page 11, exclusion sentence | Which records were counted as not identified? | Plausible definitions give 0.030% or 0.100%, not 0.04%. |
| 9 | The plot-area file | Should the row for the plot with no survey records be removed or flagged? | Reusers joining the files could overstate plantation area by 12.1%. |
| 10 | Archive README | Could the file encoding and the two undefined seed-size codes be documented? | A standard read of the census file currently fails partway through. |
| 11 | Methods | Does the Methods text state a count of early-successional species, and if so what is it? | A previously reported conflict with the Figure 1 caption could not be located in the supplied version. |

---

## B7. Bottom line

**What is good:** the paper's descriptive results stand up. Thirty-one published values — total counts, taxa, families, species richness, plot numbers, sampled area, and ten percentages — were independently recalculated from the authors' raw data and agreed. No data errors were demonstrated.

**What needs attention:** one file named by the archive's own README is missing. Seven checked values disagree; the two clearest are percentages described as shares of individuals when they are shares of taxa, and a statement that *all* large stems of the planted species were planted, contradicted by 17 records.

**What remains unknown:** every statistical result, because the analysis program is absent, along with all figures and supplementary material.

**What this does not mean:** this review does not assess intent and infers no misconduct. Unchecked claims have been neither validated nor invalidated.

---

## B8. Scope note

> This brief lists demonstrated issues, completed positive checks, and central verification limitations. A concern indicates an evidence-backed discrepancy, while a limitation indicates that verification could not be completed. Neither label implies misconduct. Absence from this brief does not mean every other claim was independently reproduced. See the comprehensive technical audit for the full evidence, coverage, and limitations.

---

## A note on a prior review

This package was reviewed once before, and that earlier review is superseded by this one. This re-check was performed from scratch, without reusing any earlier number, and it found that several of the earlier conclusions were wrong.

| Earlier statement | Now |
|---|---|
| Species richness values do not reproduce | **Withdrawn.** They are consistent with the paper's own documented practice of grouping inconsistently identified taxa. |
| The family count does not reproduce | **Withdrawn.** 64 named families plus one unassigned group equals the published 65. |
| The claim about reference-forest species absent from restoration does not reproduce | **Withdrawn.** The earlier check used the wrong set of species; using the set the paper specifies, the published figure is reproduced. |
| The Figure 1 late-successional sample size does not reproduce | **Withdrawn.** It follows the same grouping rule as species richness. |
| The census file has a data-formatting defect affecting 1,308 records | **Withdrawn.** The apparent defect was produced by the spreadsheet-reading software used, not by the file. |
| Three values were listed as published figures that matched the data | **Corrected.** Those three numbers do not appear anywhere in the paper; they were the earlier review's own calculated results, recorded in the wrong column. The paper's actual claims at those points are confirmed. |

The net effect is that the paper's descriptive numbers reproduce **better** than the earlier review reported. The genuine issues are the missing analysis program and the seven small discrepancies listed above.

This correction is included deliberately. It shows that audits of this kind can themselves be wrong, and that an apparent mismatch must be tested against alternative denominators, populations, and documented exclusion rules before it is reported as a discrepancy.
