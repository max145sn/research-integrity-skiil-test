# Review Brief — Data and Code Check

**Paper:** Schubert et al. (2025), *Active restoration increases tree species richness and recruitment of large-seeded taxa after 16–18 years*, Ecological Applications 35(1), DOI 10.1002/eap.3053.
**Package checked:** Dryad archive 10.5061/dryad.s7h44j1gc, version dated 16 December 2025 (8 files), together with the 38-page accepted-manuscript PDF.

This brief is written for reviewers, editors and authors. It reports what was checked, what agreed, what did not, and what could not be checked. It contains no code and no verdict about the paper.

**A note on the two words used throughout.** A **concern** means a difference was actually demonstrated by re-calculating from the data. A **limitation** means a check could not be completed. A limitation is not evidence that anything is wrong.

---

## 1. Review at a glance

| Area | Assessment | What this means |
|---|---|---|
| Core census numbers | **POSITIVE** | Every headline count in the Results — 66,446 seedlings, 14,038 saplings, 3,842 trees, 1,941 surviving planted trees, 255 species, 9/9/8 plots — was re-calculated from the raw data and matched exactly. |
| Data file quality | **POSITIVE** | The census file is internally consistent. Every one of the 32 surveyed plots matches its recorded sampling area exactly. |
| Analysis code for this paper | **CONCERN** | The paper states that the code needed to reproduce its analyses is archived. The archive names that file but does not contain it. The only code file present belongs to a different paper by the same team. |
| Statistical results | **LIMITATION** | No significance test, confidence interval or ordination in the paper could be checked, because the code and model outputs are absent. |
| Checked manuscript-to-data values | **CONCERN** | Twenty reported values reproduced exactly; eleven did not. Most differences are small and do not change any conclusion. |
| One claim stated as universal | **CONCERN** | The paper says *all* large stems of the planted species in the two planted treatments were originally planted. The data contain 17 that are recorded as natural recruits. |
| Sampling-area file | **CONCERN** | The area file lists a ninth plantation plot that does not exist in the census. Whether this affected the published figures cannot be determined. |
| Figures and supplement | **LIMITATION** | The supplied PDF contains no figures and no appendix, so nothing shown in Figures 1–3 or Tables S1–S4 could be inspected. |
| Misconduct | **NEUTRAL** | This review does not assess or infer intent, and nothing here should be read that way. |

**Six things worth knowing**

- The underlying dataset is unusually clean, and the paper's descriptive backbone reproduces to the last digit.
- The single most consequential problem is a missing file, not a wrong number.
- Because that file is missing, roughly one claim in five could not be checked at all.
- Of the eleven values that did not reproduce, ten are small enough that the paper's stated conclusions still hold under the re-calculated figures.
- Two statements are wrong as written rather than merely imprecise: an identification statistic described as a percentage of individuals is actually a percentage of species, and one claim uses the word "all" where the data show exceptions.
- The archive was updated in December 2025 to serve a second manuscript; the missing file may have been present in an earlier version.

---

## 2. Issues requiring attention

| Priority | Assessment | Issue | Where to look | What the evidence shows | Why it matters | Recommended reviewer action |
|---:|---|---|---|---|---|---|
| 1 | CONCERN (audit-blocking) | **[F-01] The analysis code for this paper is not in the archive** | Open Research Statement, p. 2; archive contents | The archive's own README names a file called `FinalAnalysis_ECOLAPP...` as the code that reproduces this paper's figures and statistics. That file is absent. The one code file present states in its opening lines that it reproduces a different manuscript, on spatial patterns of recruitment, published in *Applied Vegetation Science*. | Every statistical result in the paper — the species-accumulation curves and their confidence intervals, the sampling-completeness range of 85–99 %, the ordination stress values, the PERMANOVA comparisons, and all significance letters in Figure 3 — becomes unverifiable. Six of the 43 catalogued claims are blocked by this alone. | Ask the authors to deposit the missing script, or to identify the archive version that contains it. |
| 2 | CONCERN | **[F-08] A claim stated as universal has exceptions in the data** | Results, p. 14 ("All trees (≥5 cm DBH) of these species in applied nucleation and plantation were planted…") | The census records 17 stems of the planted species at tree size in those two treatments that are marked as natural recruits, not plantings: in applied nucleation, four *Erythrina poeppigiana* (6.3–27.3 cm diameter) and seven *Inga edulis* (5.0–20.0 cm); in plantation, four *E. poeppigiana*, one *I. edulis* and one *Vochysia guatemalensis*. | The measured effect is small — 17 of 1,785 stems, about 1 % — so the underlying point that the tree layer of these species is overwhelmingly original plantings still holds. But the word "all" is not supported. | Ask on what basis these 17 stems were treated as planted, or ask for the sentence to state the exact proportion. |
| 3 | CONCERN | **[F-02] An identification statistic describes the wrong thing** | Results, p. 11 ("we identified 94.2 % of individuals to species, 4.6 % to genus, and 1.1 % to family levels") | Re-calculated as percentages of *individual stems*, the values are 99.85 %, 0.15 % and 0.00 %. Re-calculated as percentages of *distinct taxa*, they are 94.25 %, 4.60 % and 1.15 % — matching the reported numbers to the reported precision and summing to exactly the 261 taxon codes in the file. | The numbers themselves are right; the noun is wrong. As written the sentence understates how completely the census was identified. | Ask for "individuals" to be corrected to "taxa". |
| 4 | CONCERN | **[F-10] The sampling-area file lists a plantation plot that was never censused** | Supplementary data file of plot areas; Methods, p. 9 ("plantation n = 8") | The area file contains 33 plots, including one plantation plot at site BB with 243 sampling quadrats. That plot has no records anywhere in the census, and the paper itself states there were eight plantation plots. All 32 real plots match their recorded areas exactly, so this is one extra row rather than a systematic error. | Sampling area is used to convert counts into densities. If the area file were used without first restricting it to censused plots, the plantation sampling area would be 12.1 % too large and every plantation density correspondingly too low. As a worked example, later-successional tree density in plantation is 47.8 stems per hectare with the extra plot included and 53.6 without it. **Whether the published analysis was affected cannot be determined, because the code is missing.** | Ask which plot set produced the sampling-area values used in the models. |
| 5 | CONCERN | **[F-03] Species-richness totals are each one species higher than re-calculated** | Results, p. 11–12 (natural regeneration 156, applied nucleation 185, plantation 196, reference forest 205) | Re-calculating with the taxon-exclusion rule documented in the archive gives 155, 184, 195 and 204 — exactly one lower in all four treatments. Without any exclusions the totals are 156, 187, 197 and 206. No single rule tested reproduces all four reported values. | The ranking natural regeneration < applied nucleation < plantation < reference forest is identical under every rule tested, so the paper's comparative statements are unaffected. | Ask which exclusion rule generated the published totals. |
| 6 | CONCERN | **[F-04] The proportion of reference-forest species found in restored plots** | Results, p. 12 ("All but 10.5 %"); Discussion, p. 21 ("~90 %") | Twenty-seven of the 204 reference-forest taxa occur in no restoration plot, which is 13.24 % absent and 86.8 % colonised, not 10.5 % and 89.5 %. The difference amounts to about six species. | The looser Discussion phrasing of "~90 %" remains approximately supported. The precise Results figure does not reproduce. | Ask how the reference-forest species set was defined for this calculation. |
| 7 | CONCERN | **[F-05, F-06] The paper gives two different species counts for the same group** | Methods, p. 9 ("early-successional taxa (37 spp.)") vs Figure 1 caption ("early- (n = 38 spp.) … late-successional species (n = 163 spp.)") | The Methods and the figure caption disagree with each other. Re-calculation gives 38 early-successional and 162 late-successional taxa. | The early-successional discrepancy is internal to the paper and needs no data to see. For the late-successional count, the effect on Figure 1 could not be assessed because the figure was not available — impact not yet determined. | Ask which counts are correct and ensure the Methods and caption agree. |
| 8 | CONCERN | **[F-15] Three related percentages cannot all be reproduced by one rule** | Results, p. 13 (early-successional species as 54.0 %, 43.3 % and 18.6 % of saplings in the three treatments) | Seven different ways of defining the denominator were tested. The natural-regeneration and applied-nucleation values reproduce exactly under one rule (53.95 % and 43.30 %); the plantation value of 18.6 % only reproduces under a different rule, which then puts natural regeneration 3 percentage points off. | The largest gap between any reported value and its closest re-calculation is 0.4 percentage points, and the ordering holds under every rule, so the conclusion drawn from these numbers is unaffected. | Ask which stems were included in the denominator. |
| 9 | CONCERN | **[F-07] Percentage of mid-successional species with small seeds** | Methods, p. 10 ("most (64 %) mid-successional species having small seeds") | Re-calculation gives 69.2 % using the trait columns in the census file and 70.0 % using the 2025 taxonomic table. The companion figure in the same sentence — 71 % of late-successional species with seeds of 5 mm or more — reproduces correctly at 70.6 %. | The sentence exists to show that successional group and seed size are not independent. The re-calculated value supports that point at least as strongly. | Ask which species set produced 64 %. |
| 10 | CONCERN | **[F-09] Share of planted-species saplings that were original plantings** | Results, p. 14 ("60 % of these stems") | Re-calculation gives 65.3 % (126 of 193 stems in the two planted treatments). Three alternative denominators were tested; none gives 60 %. | Points in the same direction as the paper, slightly more strongly. No other result depends on it. | Ask which denominator was used. |
| 11 | CONCERN | **[F-11] Number of plant families** | Results, p. 11 ("65 families") | The census contains 64 distinct named families. Counting the five taxa that have no family recorded as one additional group would give 65. | Descriptive only; no analysis is organised by family. | Ask whether unassigned taxa were counted as a family. |
| 12 | CONCERN | **[F-14] Percentage of unidentified individuals excluded** | Methods, p. 10 ("A small number of individuals (0.04 %)") | The taxa excluded by the documented rule total 26 individuals, or 0.031 %. The taxa with no family assignment total 86 individuals, or 0.100 %. Neither equals 0.04 %. | Under every reading this is below one-tenth of one percent of the census, so the characterisation "a small number" holds and no analysis is materially affected. | Ask which records make up the excluded set. |
| 13 | CONCERN | **[F-13] The data file is harder to reuse than it needs to be** | Main census data file; archive README | The file uses Latin-1 text encoding, which is not stated in the README and causes a standard modern read to fail outright. The seed-size column stores the same three categories in two different formats, so a routine grouping operation silently splits them, affecting up to 1,308 records. Two further codes (`UNK`, `?`) are undocumented, and five taxa have a blank family field even though two of them are themselves family-level identifications. | No published claim is shown to be affected — this audit forced consistent handling — but an independent reuser could produce wrong category totals without noticing. | Ask for the encoding to be documented and the seed-size column harmonised. |

---

## 3. What checked out well

These checks were completed and passed. Each one is specific; none of them validates the paper as a whole.

| Assessment | Check completed | Result | Scope limitation |
|---|---|---|---|
| POSITIVE | The three headline recruit counts | Seedlings, saplings and trees re-calculated from the raw census as 66,446 / 14,038 / 3,842 — identical to the reported values. | Confirms the counts, not the analyses built on them. |
| POSITIVE | Surviving planted trees | 1,941 — identical to the reported value. | — |
| POSITIVE | Abstract total | The abstract's "more than 80,000" corresponds to 84,326 recruits. | — |
| POSITIVE | Species total | 255 taxonomic units, reproduced exactly once the six poorly-resolved taxa documented in the archive are removed from the 261 codes present. | The exclusion rule was inferred from the other paper's code, so this mapping is probable rather than confirmed. |
| POSITIVE | Experimental replication | Nine natural-regeneration, nine applied-nucleation and eight plantation plots, plus six reference forests — exactly as stated. | — |
| POSITIVE | Minimum sampling area | The reference-forest area used as the common basis for richness comparison re-calculates to 1.0116 hectares, matching the stated 1.01 ha. | — |
| POSITIVE | Plot-by-plot sampling areas | All 32 censused plots match their recorded quadrat counts exactly, including the irregular reference-forest layout (196 quadrats at five sites, 147 at one). | Does not cover the extra plot discussed as F-10. |
| POSITIVE | Seedlings of planted species | Applied nucleation 12.96 % and plantation 4.67 %, against reported 13.0 % and 4.7 %. | — |
| POSITIVE | Saplings of planted species | 1.82 % of all saplings, against a reported 1.8 %. | — |
| POSITIVE | Dominance of early-successional trees | The named early-successional taxa account for 79.1 % of naturally recruited trees in restored plots, supporting the stated "more than 75 %". | — |
| POSITIVE | Later-successional trees relative to reference forest | Re-calculated as 7.7 % of reference-forest density, supporting the stated "small fraction (8 %)". | Uses the area file as supplied; see F-10. |
| POSITIVE | Seed size of late-successional species | 70.6 % have seeds of 5 mm or more, against a reported 71 %. | The companion mid-successional figure did not reproduce (F-07). |
| POSITIVE | Data-file internal consistency | The 1,941 planted-stem records correctly carry no grid position, reflecting the separate survey protocol the README describes; the 789 empty-quadrat placeholder rows correctly contribute zero individuals; size-class labels agree with the stated diameter thresholds; the extrapolated-size flag appears only on planted stems, exactly as disclosed. | — |

---

## 4. What could not be verified

Nothing in this table is evidence that the research is wrong.

| Assessment | Item | Why it could not be verified | Effect on the review | What would resolve it |
|---|---|---|---|---|
| LIMITATION | All statistical models behind Figure 3, including every significance letter and every "significantly greater / not significant" statement | The analysis code and model outputs for this paper are not in the archive. | No inferential claim in the paper was checked. This covers the paper's central comparative conclusions. | Deposit the analysis script and the model outputs. |
| LIMITATION | The species-accumulation curves in Figure 1 and the stated 85–99 % sampling completeness | Requires the rarefaction code and its random-seed settings, which are absent. | The richness comparisons remain unverified. | Deposit the script with seed settings. |
| LIMITATION | The ordination in Figure 2, including the stated stress values of 0.17–0.18, and the PERMANOVA comparisons | The code is absent and the rules for building the community matrices exist only in that code. | Composition results unverified. | Deposit the script. |
| LIMITATION | Survival percentages of the four planted species | The number originally planted per species per plot is not in the archive. Assuming an equal four-way split of the stated 86 stems per applied-nucleation plot produces survival above 100 % for two species, which shows the assumption is wrong rather than the reported figures. | The survival statement is unverified in either direction. | Supply the original planting counts by species and plot. |
| LIMITATION | **[F-12]** Everything shown in Figures 1–3 and in the supplementary tables and figures | The supplied file is the accepted-manuscript version; it contains no graphics on any of its 38 pages and no appendix. | Figure-level and supplement-level claims are unchecked. This is a limitation of what was supplied to this review, not a defect of the published article. | Supply the typeset article or the figure source data. |
| LIMITATION | The comparison with the team's 2017 survey ("more than twice the expected number of species") and the planting densities of 313 and 86 trees | These values come from earlier publications, not from this archive. | Outside what this package can support. | Consult the cited papers. |
| NOT ASSESSED | An independent rebuild of the community-dissimilarity ordination | Technically possible, but the rules for constructing the matrices are defined only in the missing code, so an independent version would test the auditor's assumptions rather than the authors' work. | No conclusion can be drawn from this review about the ordination. | Complete once the code is available. |
| NOT ASSESSED | An independent rarefaction and sampling-completeness calculation | Feasible with the supplied data, but not completed within this review's scope. | No conclusion either way. | Complete as a follow-up calculation. |
| NOT APPLICABLE | The three spatial coordinate files and the R script in the archive | These support the team's separate *Applied Vegetation Science* manuscript, not this paper. | — | — |

---

## 5. Paper navigation guide

| Paper location | What to check | Related item |
|---|---|---|
| Open Research Statement, p. 2 | Confirm that the code said to be archived is actually retrievable | F-01 |
| Methods, p. 9, line 206 | Early-successional species count (37) against the Figure 1 caption (38) | F-05 |
| Methods, p. 10, lines 214–215 | The 64 % small-seeded mid-successional figure | F-07 |
| Methods, p. 10, lines 219–220 | The 0.04 % of excluded unidentified individuals | F-14 |
| Results, p. 11, line 248 | The count of 65 families | F-11 |
| Results, p. 11, lines 249–250 | "94.2 % of individuals" — should read taxa | F-02 |
| Results, p. 11–12, lines 251–253 | The four richness totals | F-03 |
| Results, p. 12, lines 254–255 | The 10.5 % of reference-forest species | F-04 |
| Results, p. 13, lines 281–282 | The three early-successional sapling percentages | F-15 |
| Results, p. 14, lines 300–303 | The 60 % figure and the word "all" | F-09, F-08 |
| Figure 1 caption | Species counts per successional group | F-05, F-06 |
| Figure 3 and Figure S2 | Which plot set supplied the sampling areas behind these densities | F-10 |
| Results, p. 11, line 247 and p. 3, line 34 | High-value positive check: all headline counts verified exactly | — |

---

## 6. Author questions

| # | Location | Question for the authors | Why this question is needed |
|---:|---|---|---|
| 1 | Archive / Open Research Statement | Could the analysis script for this manuscript be deposited, or the archive version containing it identified? | The README names it, but the supplied version does not contain it. |
| 2 | Results, p. 11 | Should "94.2 % of individuals" read "94.2 % of taxa"? | The figures match taxon counts exactly and differ substantially from the individual-level values. |
| 3 | Results, p. 11–12 | Which taxon-exclusion rule produced richness totals of 156, 185, 196 and 205? | Re-calculation gives 155/184/195/204 with the documented rule and 156/187/197/206 without it. |
| 4 | Results, p. 12 | How was the reference-forest species set defined for the 10.5 % figure? | Re-calculation gives 13.24 %. |
| 5 | Methods p. 9 and Figure 1 caption | Are the early- and late-successional species counts 37 or 38, and 162 or 163? | The two locations disagree, and re-calculation gives 38 and 162. |
| 6 | Methods, p. 10 | Which species set gives 64 % of mid-successional species with small seeds? | Re-calculation gives 69–70 % under both available trait versions. |
| 7 | Results, p. 14 | On what basis were the 17 tree-sized stems of planted species recorded as natural recruits treated as plantings, and which denominator gives 60 %? | The data contain those stems, and the proportion re-calculates to 65.3 %. |
| 8 | Sampling-area file | Which plot set produced the sampling areas used in the density models — the 33 rows in the file or the 32 censused plots? | The extra plantation plot would inflate that treatment's area by 12.1 %. |
| 9 | Results, p. 11 | Does "65 families" include taxa with no family assignment? | The data contain 64 named families. |
| 10 | Data archive | Could the text encoding be documented and the seed-size column stored in a single consistent format? | A standard read of the file currently fails, and category totals can silently split. |
| 11 | Methods, p. 10 | Which records constitute the 0.04 % of excluded unidentified individuals? | Candidate definitions give 0.031 % or 0.100 %. |
| 12 | Results, p. 13 | Which single denominator produces 54.0 %, 43.3 % and 18.6 % together? | None of seven tested definitions reproduces all three. |

---

## 7. Bottom line

**What is good.** The census dataset is clean and well documented, and the paper's descriptive backbone reproduces exactly: all three recruit totals, the surviving planted trees, the species total, the plot replication, the per-plot sampling areas and the 1.01-hectare comparison basis were all independently re-calculated and matched.

**What needs attention.** The analysis code named in the archive is not in it, and the only script present belongs to a different paper. Eleven reported values did not reproduce; two are wrong as written — an identification statistic labelled as a percentage of individuals is a percentage of species, and one claim says "all" where 17 stems say otherwise. A sampling-area file lists a plantation plot that was never censused.

**What remains unknown.** Every statistical result — the richness curves, the ordination, the significance tests behind Figure 3 — is unverified, as is planted-tree survival and everything in the figures and supplement.

**What this does not mean.** No misconduct is assessed, suggested or implied. Claims that could not be checked have been neither validated nor invalidated.

---

## 8. Scope note

> This brief lists demonstrated issues, completed positive checks, and central verification limitations. A concern indicates an evidence-backed discrepancy, while a limitation indicates that verification could not be completed. Neither label implies misconduct. Absence from this brief does not mean every other claim was independently reproduced. See the comprehensive technical audit for the full evidence, coverage, and limitations.

*Companion document: `dryad_s7h44j1gc_eap3053_integrity_audit.md`.*
