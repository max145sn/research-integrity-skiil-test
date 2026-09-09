# Research Package Integrity Audit — Output A: Comprehensive Technical Audit

**Manuscript:** Schubert, L. K., et al. (2025). *Restoration treatments shape tree recruitment and functional composition in a Costa Rican tropical wet forest.* Ecological Applications 35(1), e3053. doi:10.1002/eap.3053 (supplied as accepted-manuscript postprint `qt2qt6s177.pdf`)
**Data package:** Dryad doi:10.5061/dryad.s7h44j1gc, snapshot `doi_10_5061_dryad_s7h44j1gc__v20251216.zip`
**Skill:** `research-package-integrity-audit2`, SHA-256 `d5bb4fba34ebed875c3d4a5dee2031e8e2e84a8e46c0d52c4fdabffad04d7595`
**Ledger:** `audit-output/dryad_s7h44j1gc_eap3053_audit_ledger.json`
**Companion:** `audit-output/dryad_s7h44j1gc_eap3053_review_brief.md` (Output B)

> This audit assesses evidence correspondence between a manuscript and its archived data and code. It does not detect intent, infer misconduct, or make any publication recommendation.

---

## 1. Execution-mode disclosure

This is an **independent re-execution** of the audit on the same package that was audited in an earlier session. It was carried out without reusing any numeric result from that earlier run: the archive was re-extracted, hashed afresh, and every claim was recomputed from the raw census file by newly written scripts.

The re-execution was undertaken specifically to test whether the earlier findings were reproducible. **They were not, in several material respects.** Five of the earlier run's reported discrepancies are retracted here as false positives, one recorded observation is retracted as a software artifact, and three values that the earlier run listed as *reported manuscript values* were found not to occur in the manuscript at all. Section 20 documents all eight corrections. The earlier, superseded outputs remain in the repository's git history at commit `eb2cc35`.

| Aspect | State |
|---|---|
| Manuscript text extraction | `pdfplumber`, 38 pages, 68,033 characters, high confidence for body text |
| Embedded figure images | 0 found across all 38 pages — postprint carries no rasterised figures |
| Supplement | Not supplied |
| Source code execution | `EXECUTION_BLOCKED` — the analysis script for this manuscript is not in the archive |
| R runtime | `ENVIRONMENT_CHECK_FAILED` — no R interpreter on the audit machine |
| Independent recomputation | `PARTIALLY_RECOMPUTED` — Python 3.12.10 / pandas 3.0.5 / numpy 2.5.3 / scipy 1.18.1 |
| Prior-run reuse | None. All values regenerated. |

The absence of an R runtime and the absence of the analysis script are recorded as **separate** conditions. Neither means the authors' code failed; neither was executed.

---

## 2. Executive summary

The manuscript's descriptive results **reproduce well** from the archived census data. Of 50 identified claims, 38 were checkable without the missing analysis script; **31 reproduced** and 7 did not.

The single most consequential problem is a **package gap**, not a numerical error: the README names `FinalAnalysis_ECOLAPP_Schubert.et.al.R` as the analysis code for this manuscript, but that file is not in the archive. The only R file present declares in its first line that it reproduces a *different* manuscript (an Applied Vegetation Science paper). Consequently every inferential result — rarefied and extrapolated richness with bootstrapped intervals, sampling completeness, NMDS, PERMANOVA, and all generalised linear mixed models behind Figure 3 — is unverifiable from what was supplied (F-01, MAJOR).

The seven numerical or scope discrepancies are all small in magnitude. Two are the most substantive:

- **F-02** — the taxonomic-resolution sentence reports percentages "of individuals". Those percentages match **taxon** counts exactly (genus = 12/261 = 4.60%), not individual counts (0.21%). The numbers are right; the noun is wrong.
- **F-05** — the manuscript states that *all* trees ≥5 cm DBH of the planted species in the two planted treatments were originally planted. The data record 17 recruit-origin stems meeting that description, spanning 5.0–27.3 cm DBH. The universal quantifier is contradicted, though the affected fraction is 0.95%.

The remaining five (F-03, F-04, F-06, F-07, F-08) are percentage differences of 0.4 to 6.3 percentage points that do not alter direction, ordering, or any stated qualitative conclusion.

Two archive-hygiene issues affect reuse rather than the published results: a `PlotQuadrantes.csv` row for a plot (`BBPL`) that has no census records and would inflate plantation sampled area by 12.1% if naively joined (F-09), and undocumented file encoding plus undocumented missing-value codes (F-10). Notably, testing showed F-09 **did not** propagate into the published result — see §9.

No evidence of data fabrication, falsification, or manipulation was found, and this audit does not assess intent.

---

## 3. Preflight and scope

| Item | State |
|---|---|
| Supplied by user | `doi_10_5061_dryad_s7h44j1gc__v20251216.zip`, `qt2qt6s177.pdf` |
| Files extracted | 8 from archive + 1 PDF = 9 |
| Readable | 9 of 9 |
| Unsupported formats | None |
| Internet access needed | No — audit performed entirely on supplied artifacts |
| User scope | "Run this complete skill on this data" — full audit, no exclusions specified |
| Preflight state | **PARTIAL** — package readable, but the analysis code named by the README is absent and no supplement was supplied |

Study type: a single observational field study — a replicated restoration experiment with four treatments (natural regeneration, applied nucleation, plantation, reference forest) censused across 32 plots.

---

## 4. File inventory and missing-artifact register

### 4.1 Supplied files (all classified; 0 unclassified)

| File | Bytes | Classification | Role |
|---|---:|---|---|
| `ECOLAPPS_final_Schubert.et.al.2024.csv` | 6,929,743 | `RAW_OBSERVED` (with derived trait columns) | Primary census: 67,046 rows × 18 columns |
| `IslasMaster_abbreviated2025.csv` | 21,504 | `CLEANED` | Species trait master (seed size, successional guild) |
| `PlotQuadrantes.csv` | 606 | `RAW_OBSERVED` | Per-plot quadrat counts (sampling area) |
| `FinalAnalysis_AVS_Schubert.et.al.R` | 55,606 | Code — **for a different manuscript** | Declares AVS paper in line 1 |
| `README.md` | 6,318 | Documentation | Names the absent ECOLAPP script at L67 |
| `Cartesian_coordinates_*.csv` (spatial files) | — | `RAW_OBSERVED` | Plot/quadrat geometry |
| `qt2qt6s177.pdf` | — | Manuscript postprint | 38 pages, 0 embedded images |

Full byte counts and SHA-256 digests for every artifact are recorded in the ledger under `inventory`.

### 4.2 Missing-artifact register

Manuscript- or README-referenced (denominator = 2):

| ID | Artifact | Source | Status |
|---|---|---|---|
| M-01 | `FinalAnalysis_ECOLAPP_Schubert.et.al.R` | README.md L67 | **ABSENT** |
| M-02 | Supplementary Figures S1–S4, Tables S1–S4 | Manuscript cross-references | NOT_SUPPLIED |

Inferred-required (denominator = 3):

| ID | Artifact | Basis | Status |
|---|---|---|---|
| M-03 | Per-species, per-plot initial planting records | Required to verify survival percentages | ABSENT |
| M-04 | Session/environment record (R and package versions) | Reproducibility requirement | ABSENT |
| M-05 | Derived analysis objects (iNEXT, NMDS, fitted models) | Required to check reported model output | ABSENT |

**Completeness scope statement:** completeness is asserted only against these two denominators. It is not a claim about the Dryad record as published, which may contain material not present in the supplied snapshot.

**Package completeness: `PARTIALLY_COMPLETE`.**

---

## 5. Study and evidence map

Single study; four treatments; 32 censused plots (NR 9, AN 9, PL 8, RF 6).

| Edge | Mapping status | Basis |
|---|---|---|
| Manuscript → `ECOLAPPS_final_...csv` | **CONFIRMED** | All descriptive totals (individuals, OTUs, families, richness, plot counts) recompute exactly |
| Manuscript → `PlotQuadrantes.csv` | **CONFIRMED** | All 32 census plots match their quadrat counts exactly |
| Manuscript → `IslasMaster_abbreviated2025.csv` | **PROBABLE** | The reported 71% seed-size figure reproduces at 71.1% from this file |
| Manuscript → `FinalAnalysis_ECOLAPP...R` | **UNRESOLVED** | Named in README; absent from archive |
| Manuscript → `FinalAnalysis_AVS...R` | **CONFIRMED as NOT the code for this paper** | Script header identifies a different manuscript |

**Intended code mapping, actual output provenance, numerical correspondence, and published-artifact correspondence are reported separately.** For this package, actual output provenance is `UNRESOLVED` for every inferential result because no analysis script for this manuscript exists in the archive. Numerical correspondence for descriptive claims is `RECOMPUTED` from the raw data — which verifies the data support the numbers, not that the authors' pipeline produced them.

---

## 6. Complete claim ledger

**Claim ledger status: COMPLETE** for all independently verifiable propositions locatable in the supplied postprint text. 50 claims carry stable IDs, including those that end BLOCKED, NOT_CHECKED, or NOT_APPLICABLE.

### 6.1 Reproduced claims (31 — C-01…C-31)

| ID | Location | Claim | Reported | Recomputed |
|---|---|---|---|---|
| C-01 | p.13 L247 | Seedling recruits | 66,446 | 66,446 |
| C-02 | p.13 L247 | Sapling recruits | 14,038 | 14,038 |
| C-03 | p.13 L247 | Tree recruits | 3,842 | 3,842 |
| C-04 | p.13 L248 | Planted-tree survivors | 1,941 | 1,941 |
| C-05 | Abstract L34 | Total individuals | >80,000 | 84,326 recruits; 86,267 incl. planted |
| C-06 | p.13 L247–248 | Operational taxonomic units | 255 | 255 after documented 6-taxon exclusion |
| C-07 | p.13 L248 | Families | 65 | 64 named + 1 unassigned |
| C-08 | p.13 L251 | Richness, natural regeneration | 156 | 155 retained + 1 grouped unit |
| C-09 | p.13 L252 | Richness, applied nucleation | 185 | 184 + 1 |
| C-10 | p.13 L252 | Richness, plantation | 196 | 195 + 1 |
| C-11 | p.13 L252–253 | Richness, reference forest | 205 | 204 + 1 |
| C-12–C-15 | Abstract L35–36 | Plot counts NR/AN/PL/RF | 9 / 9 / 8 / 6 | 9 / 9 / 8 / 6 |
| C-16 | p.12 L229 | Minimum sampled area | 1.01 ha | 1.0116 ha (reference forest) |
| C-17 | p.14 L298 | Planted-taxa seedlings, AN | 13.0% | 12.95% |
| C-18 | p.14 L298 | Planted-taxa seedlings, PL | 4.7% | 4.67% |
| C-19 | p.15 L300 | Planted-species saplings, all | 1.8% | 1.82% |
| C-20 | p.14 L281 | Early-successional saplings, NR | 54.0% | 53.95% |
| C-21 | p.14 L281 | Early-successional saplings, AN | 43.3% | 43.30% |
| C-22 | p.15 L311–312 | Later-successional tree density vs reference | 8% | 8.0% (BBPL excluded) |
| C-23 | p.13 L291–293 | Share in a few early-successional taxa | >75% | 79.1% |
| C-24 | p.13 L269–270 | Mid-successional species reaching tree class | ~50% | 50.0% (26/52) |
| C-25 | p.24 L469 | Reference species observed in restoration | ~90% | 89.0% |
| C-26 | p.13 L254 | Reference tree species absent | 10.5% | 10.34%–10.96% |
| C-27 | `PlotQuadrantes.csv` | Per-plot quadrat counts | 33 rows | All 32 census plots exact |
| C-28 | Fig.1 caption L874 | Mid-successional species | n = 52 | 52 |
| C-29 | Fig.1 caption L874 | Early-successional species | n = 38 | 38 |
| C-30 | Fig.1 caption L874 | Late-successional species | n = 163 | 162 + 1 grouped unit |
| C-31 | p.11 L215–216 | Late species with seeds ≥5 mm | 71% | 71.1% |

### 6.2 Non-reproducing claims (7 — C-32…C-38)

Each is developed in §12 as findings F-02 through F-08.

| ID | Location | Reported | Recomputed | Finding |
|---|---|---|---|---|
| C-32 | p.13 L249–250 | 94.2% / 4.6% / 1.1% "of individuals" | Exact as **taxon** shares; 98.9% / 0.21% / 0.92% as individuals | F-02 |
| C-33 | p.13 L269–270 | 15% late species in tree class | 21.3% (21.0% retained) | F-03 |
| C-34 | p.15 L300–301 | 60% originally planted | 65.3% (126/193) | F-04 |
| C-35 | p.15 L301–303 | "All" trees ≥5 cm DBH were planted | 17 recruit-origin stems, 5.0–27.3 cm | F-05 |
| C-36 | p.14 L282 | 18.6% early saplings, plantation | 18.19% / 18.52% | F-06 |
| C-37 | p.11 L214–215 | 64% mid species small-seeded | 69.2% (36/52), both trait sources | F-07 |
| C-38 | p.11 L219 | 0.04% unidentified | 0.030% (26) or 0.100% (86) | F-08 |

### 6.3 Blocked (9 — C-39…C-47)

| ID | Claim | Reason |
|---|---|---|
| C-39 | iNEXT rarefied/extrapolated richness at 1.01 ha, bootstrapped 95% CI | Analysis script absent (F-01) |
| C-40 | Sampling completeness 85–99% | Analysis script absent |
| C-41 | NMDS ordination and stress values | Analysis script absent |
| C-42 | PERMANOVA pairwise composition tests | Script and supplement absent |
| C-43 | glmmTMB abundance models; emmeans groupings (Fig. 3) | Analysis script absent |
| C-44 | Significantly elevated seedling/sapling establishment | Inferential model not reproducible |
| C-45 | Plantation large-seeded densities similar to reference | Inferential model not reproducible |
| C-46 | Per-plot planting counts (313 PL, 86 AN) | Initial planting records absent |
| C-47 | All supplementary figures and tables | No supplement supplied; text-only postprint |

### 6.4 Not checked (2)

- **C-48** — Cartesian coordinate files. Inspection was feasible; no verified claim depends on them, so they were not evaluated. This is `NOT_CHECKED`, not `BLOCKED`.
- **C-49** — A prior audit recorded a Methods statement of "37 early-successional species" conflicting with the Figure 1 caption's 38. That string could not be located in this extraction. The conflict is **neither confirmed nor refuted** and is not asserted as a finding (see X-08).

### 6.5 Not applicable (1)

- **C-50** — Execution of `FinalAnalysis_AVS_Schubert.et.al.R`. The script reproduces a different manuscript; executing it would not test this paper's claims.

---

## 7. Data-provenance checks

| Check | Result |
|---|---|
| Row semantics | **Rows are not individuals.** `No..indiv.` is a count column; all abundance work sums it. Treating rows as individuals inflates counts substantially. |
| Empty-quadrat placeholders | 789 rows carry `Especie == "ND"` and sum to 0 individuals. Excluded from abundance; **retained** when counting surveyed quadrats. |
| Quadrat identity | Unique quadrat = the **(`Parcela`, `Quadrante`) pair**. Only 4 distinct `Quadrante` values exist per plot; keying on `Quadrante` alone produces spurious mismatches. |
| Planted stems | All 1,941 `Origin == "Planted"` rows have blank `Parcela`/`Quadrante` (separate protocol) — correctly excluded from quadrat-based density. |
| Documented exclusion | Six poor-resolution taxa (`BORAGINACEAE, HIRAEA, RUBIACEAE, INGA, GUAREA, LAURACEAE`) recovered from the AVS script L49–55; 261 codes → 255 OTUs, matching C-06. |
| Genus-level coding | Genus IDs are coded via epithet tokens `{sp, sp., sp1, sp. A, spp.}`, **not** null values. |
| Sampled area formula | `N.Quad × 9 m² / 10000` ha. Reproduces the reported 1.01 ha minimum. |
| Duplicate/ID integrity | No duplicate record identifiers detected. |
| Range checks | DBH and height values within plausible bounds; no impossible negatives. |
| Encoding | **Latin-1, undocumented** — a standard UTF-8 read fails at byte 137401 (F-10). |
| Missing-value coding | `seed_size` contains undocumented `UNK` (16 records) and `?` (1 record); 5 taxa have blank `Family` (86 individuals) (F-10). |

**Empirical data integrity: `NO_DEMONSTRATED_ISSUES`.** The defects recorded under F-10 are documentation and encoding hygiene problems, not data errors, and none propagates to a reported value.

### 7.1 A software artifact, not a data defect

An earlier audit reported that `seed_size` was stored in mixed string and float formats, placing 1,308 records at risk of silent category splitting. **This is retracted (X-01).** Reading the file with the standard-library CSV reader shows only the tokens `1`, `2`, `3`, `NA`, `UNK`, `?`. The decimal-formatted tokens `1.0/2.0/3.0` appear *only* under `pandas.read_csv(low_memory=True)` — the default — which infers types per chunk and splits categories across chunk boundaries. With `low_memory=False` the values are clean. The observation described a property of the reader, not of the file.

---

## 8. Code, configuration, and domain checks

| Check | Result |
|---|---|
| Entry point for this manuscript | **Absent** (F-01) |
| Entry point present | `FinalAnalysis_AVS_Schubert.et.al.R` — header declares the Applied Vegetation Science manuscript |
| Reusable content in the present script | The six-taxon exclusion rule (L49–55) was recovered and independently validated against C-06 |
| Seeds / RNG state | Not inspectable — the relevant script is absent |
| Hardcoded outputs | None detected in the supplied script |
| Stale or overwritten outputs | Not assessable — no derived objects archived |
| Configuration files | None present |

Machine-learning and simulation checks are **NOT_APPLICABLE**: this is an observational field study with no model-input configuration, no train/test splits, and no simulation parameters.

**Configuration and model-input integrity: `NOT_APPLICABLE`.**

---

## 9. Source-execution report

**Source execution: `EXECUTION_BLOCKED`.**

Two independent conditions, deliberately reported separately:

1. The analysis script for this manuscript is **not present** in the archive (F-01). No amount of environment provisioning resolves this.
2. The audit machine has **no R runtime** — `ENVIRONMENT_CHECK_FAILED`.

Neither condition constitutes evidence that the authors' code fails, errors, or produces wrong output. No execution was attempted, and no claim in this audit rests on execution.

---

## 10. Independent-recomputation report

**Independent recomputation: `PARTIALLY_RECOMPUTED`.**

38 of 50 claims were checkable without the missing script. All were recomputed in Python from the raw census, area, and trait files by scripts written for this audit. Tolerances were set from each claim's reported precision (a value given as "13.0%" is matched to one decimal place; a value given as "~50%" is matched at the stated approximation).

**Result: 31 MATCH, 7 MISMATCH.**

### 10.1 Reconciliation work that resolved apparent mismatches (Phase 9)

Before raising any mismatch, alternative denominators, exclusion rules, populations, and roundings were tested. Five apparent discrepancies were resolved to **matches**:

**The +1 grouping rule (C-08…C-11, C-30, C-07).** Reported richness equals retained richness **plus exactly one** in all four treatments (155→156, 184→185, 195→196, 204→205), and the Figure 1 late-successional count follows the same pattern (162→163). Families are 64 named **plus one** unassigned group = 65.

This rule *discriminates* rather than merely fits: applied nucleation contains three of the six excluded taxa yet still gains only +1, which rules out per-taxon reinstatement — the only mechanism that would explain a +1 in every treatment is a single pooled "grouped unidentified" unit. The manuscript documents exactly this at p.11 L217–218 (grouping of inconsistently identified taxa for diversity analyses). All six values are therefore **consistent with the documented method**, not discrepancies.

**The tree-species denominator (C-26, C-25).** The "10.5%" claim concerns reference-forest **tree species**. Computed across all size classes it gives 13.24%; restricted as the manuscript states, it gives 10.34%–10.96%, bracketing the reported value. The companion claim of "~90% of reference forest species" independently reproduces at 89.0%.

**The BBPL plot set (C-22).** The 8% later-successional density ratio reproduces at **exactly 8.0%** when BBPL is excluded, and at 7.7% when included. This is positive evidence that the published analysis used the correct 8-plot set, and it converts F-09 from an undetermined-impact concern into a demonstrated **archive reuse hazard with no effect on the published result**.

### 10.2 Discriminating evidence supporting the seven raised mismatches

Each raised mismatch survived the same reconciliation testing:

- **F-02** — the reported percentages match taxon counts to three significant figures (4.6% = 12/261 = 4.60%), which is far too exact to be coincidence, while the individual-level value differs by a factor of ~22.
- **F-03** — the *companion* figure in the same sentence (mid-successional, ~50%) reproduces at exactly 50.0% under the same rule, validating the interpretation and isolating the late-successional value.
- **F-06** — the two companion figures in the same sentence (53.95%, 43.30%) reproduce exactly under the all-records rule, which yields 18.19% for plantation. No single rule reproduces all three stated values.
- **F-07** — the companion figure in the same sentence (71% late, ≥5 mm seeds) reproduces at 71.1%, arguing against systematic trait-table drift and pointing to an error in the 64% value specifically. Both supplied trait sources give 69.2% identically.
- **F-08** — four candidate definitions of "not identified" were tested; all fall outside 0.04%.

**Computational reproducibility: `BLOCKED`** — recomputation from raw data verifies that the data support the numbers; it does not reproduce the authors' pipeline, which requires the absent script.

---

## 11. Figure, table, and source-data correspondence

The supplied PDF is a text-only postprint with **zero embedded images** across all 38 pages, and no supplement was supplied.

| Artifact | Status | Note |
|---|---|---|
| Figure 1 caption values (n = 52, 38, 163) | `FIGURE_PUBLISHED_VALUES_COMPARED` | Caption text extracted and recomputed; 52 and 38 exact, 163 via the +1 grouping rule |
| Figure 1 plotted values | `FIGURE_CHECK_BLOCKED` | No image; no plotting code |
| Figure 2 | `FIGURE_CHECK_BLOCKED` | No image; no plotting code |
| Figure 3 (model estimates, emmeans groupings) | `FIGURE_CHECK_BLOCKED` | No image; the generating script is absent (F-01) |
| Figures S1–S4, Tables S1–S4 | `FIGURE_CHECK_BLOCKED` | Supplement not supplied |
| Figure regeneration | `FIGURE_EXECUTION_NOT_ATTEMPTED` | No plotting code available |

`FIGURE_NUMERICALLY_MATCHED` is **not** used anywhere in this audit, because no published or supplied figure values beyond caption text were available for comparison. `PUBLISHED_FIGURE_PROVENANCE_VERIFIED` is not used for any figure.

---

## 12. Detailed findings

Every finding records: category, locations, claim IDs, evidence, reported vs observed values, reconciliation attempted, impact, severity basis, certainty, misconduct inference, reviewer action, and author question. **Misconduct inference is `NONE` for all eleven findings.**

### F-01 — Analysis script named by the README is absent

- **Category:** `FILE_OR_PACKAGE_GAP` · **Severity:** MAJOR · **Certainty:** HIGH · **Assessment:** LIMITATION
- **Claims:** C-39 … C-45
- **Location:** `README.md` L67; package root
- **Evidence:** The README names `FinalAnalysis_ECOLAPP_Schubert.et.al.R` as the analysis code for this manuscript (L112 names the AVS script separately). The ECOLAPP file is not in the archive. The only R file present declares in line 1 that it reproduces the Applied Vegetation Science manuscript.
- **Reconciliation attempted:** The full archive was searched for any other executable analysis file; none exists. The AVS script was inspected to determine whether it also covers this manuscript; its header and analysis structure indicate it does not.
- **Impact:** Blocks independent verification of *every* inferential result: rarefied and extrapolated richness with bootstrapped confidence intervals, sampling completeness, NMDS, PERMANOVA, and all model-based comparisons underlying Figure 3.
- **Severity basis (tested):** claim coverage — 7 of 50 ledger claims, comprising **all** inferential claims, cannot be evaluated.
- **Reviewer action:** Request the ECOLAPP analysis script.
- **Author question:** Could you supply `FinalAnalysis_ECOLAPP_Schubert.et.al.R`, which the README lists but which is not present in the archive?

### F-02 — Taxonomic-resolution percentages describe taxa, not individuals

- **Category:** `REPORTING_INCONSISTENCY` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Claim:** C-32 · **Location:** p.13 L249–250
- **Evidence:** The sentence states that of the naturally recruited taxa, 94.2% **of individuals** were identified to species, 4.6% to genus, 1.1% to family. The genus figure matches taxon counts *exactly*: 12 of 261 = 4.60%. At individual level the genus share is 0.21% and the species share 98.9%.
- **Reconciliation attempted:** Individual-level shares computed on recruit-only, all-record, and retained-set denominators; none approaches the reported values. Taxon-level computation matches on the first try.
- **Impact:** Descriptive only. The percentages are correct as taxon proportions; the word "individuals" is the error. No downstream analysis depends on this sentence.
- **Severity basis (tested):** exact taxon-level match found; individual-level value differs by a factor of ~22; no analytic result depends on it.
- **Author question:** Should "of individuals" read "of taxa"? The reported percentages match taxon counts rather than individual counts.

### F-03 — Late-successional species in the tree size class

- **Category:** `NUMERICAL_MISMATCH` · **Severity:** **UNDETERMINED** · **Certainty:** MEDIUM · **Assessment:** CONCERN
- **Claim:** C-33 · **Location:** p.13 L269–270
- **Evidence:** Reported: ~50% of mid-successional and 15% of late-successional species were recorded in the tree size class in any restoration treatment. Mid recomputes to **exactly 50.0%** (26/52). Late recomputes to **21.3%** (35/164), or 21.0% on the retained set.
- **Reconciliation attempted:** Per-treatment, pooled, retained-set and full-set denominators tested; all give 21.0%–21.3%.
- **Impact:** **Not evaluated.** The exact match on the companion figure indicates the interpretation is correct, but the effect of the late-successional difference on any conclusion was not tested.
- **Severity basis:** `UNDETERMINED` — *the discrepancy is demonstrated, but its effect was not evaluated.*
- **Author question:** How was the 15% figure derived? The same calculation reproduces the companion 50% figure exactly but yields about 21% here.

### F-04 — Proportion of planted-species saplings that were originally planted

- **Category:** `NUMERICAL_MISMATCH` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Claim:** C-34 · **Location:** p.15 L300–301
- **Evidence:** Reported 60%; recomputed **65.3%** (126 of 193).
- **Reconciliation attempted:** Recruit-only and all-record denominators tested; per-treatment splits tested. None yields 60%.
- **Impact:** 5.3 percentage points. The direction and the qualitative statement that a majority were originally planted are unaffected.
- **Severity basis (tested):** recomputed on the full sapling set; the majority claim holds under both values.
- **Author question:** Which denominator produced 60%? Counting all planted-species saplings in applied nucleation and plantation gives 65.3%.

### F-05 — The universal claim that all large planted-species stems were planted

- **Category:** `UNSUPPORTED_SCOPE_CLAIM` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Claim:** C-35 · **Location:** p.15 L301–303
- **Evidence:** The manuscript states that **all** trees ≥5 cm DBH of these species in applied nucleation and plantation were planted as part of the initial restoration. The dataset records **17 such stems coded as recruits**: 11 in applied nucleation (4 *Erythrina poeppigiana*, 7 *Inga edulis*) and 6 in plantation (4 *E. poeppigiana*, 1 *I. edulis*, 1 *Vochysia guatemalensis*), spanning **5.0 to 27.3 cm DBH**.
- **Reconciliation attempted:** Checked whether these are data-entry artifacts (they span a wide size range across three species and two treatments, so are unlikely to be); checked whether a different DBH threshold removes them (it does not — the largest is 27.3 cm).
- **Impact:** 17 of 1,781 such stems = **0.95%**. The quantitative pattern is unaffected; only the universal quantifier is contradicted.
- **Severity basis (tested):** affected stems counted against the full set (17/1,781 = 0.95%).
- **Author question:** The data record 17 recruit-origin stems of the planted species at ≥5 cm DBH in these treatments. Should the statement be qualified?

### F-06 — Early-successional share of plantation saplings

- **Category:** `NUMERICAL_MISMATCH` · **Severity:** MINOR · **Certainty:** MEDIUM · **Assessment:** CONCERN
- **Claim:** C-36 · **Location:** p.14 L282
- **Evidence:** Reported 18.6%; recomputed **18.19%** (all records) or **18.52%** (recruits only). The two companion figures in the same sentence reproduce exactly under the all-records rule (NR 53.95%, AN 43.30%), which yields 18.19% for plantation.
- **Reconciliation attempted:** Four inclusion rules tested. **No single rule reproduces all three values in the sentence.**
- **Impact:** At most 0.41 percentage points. Treatment ordering and the qualitative contrast are unaffected.
- **Severity basis (tested):** four denominator rules; maximum deviation 0.41 pp; ordering preserved in every variant.
- **Author question:** No single inclusion rule reproduces all three sapling percentages in this sentence. Which rule was used for the plantation value?

### F-07 — Mid-successional small-seeded species percentage

- **Category:** `NUMERICAL_MISMATCH` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Claim:** C-37 · **Location:** p.11 L214–215
- **Evidence:** Reported 64% of mid-successional species have small seeds (<5 mm); recomputed **69.2%** (36 of 52) — identically from the census trait fields and from the 2025 trait master. The companion figure in the same sentence (71% of late-successional species with seeds ≥5 mm) reproduces at 71.1%.
- **Reconciliation attempted:** Both trait sources cross-checked; seed-size threshold direction verified; `UNK`/`?` records tested as included and excluded.
- **Impact:** 5.2 percentage points = 3 species of 52. The stated qualitative conclusion (most mid-successional species have small seeds) holds under both values.
- **Severity basis (tested):** both trait sources agree at 69.2%; the companion figure reproduces, which argues against systematic trait-table drift.
- **Author question:** Both trait sources give 69.2% (36/52) rather than 64%, while the companion 71% figure reproduces exactly. Could the 64% value be rechecked?

### F-08 — Unidentified-individual exclusion percentage

- **Category:** `NUMERICAL_MISMATCH` · **Severity:** MINOR · **Certainty:** MEDIUM · **Assessment:** CONCERN
- **Claim:** C-38 · **Location:** p.11 L219
- **Evidence:** Reported 0.04% of individuals not identified and excluded. Candidate definitions give **0.030%** (26 individuals in the six poor-resolution taxa) and **0.100%** (86 individuals with blank `Family`). 0.04% corresponds to ~34 individuals; no tested definition yields that.
- **Reconciliation attempted:** Four candidate definitions of "not identified" tested against recruit and all-record denominators.
- **Impact:** Not material to any analysis. The excluded fraction is negligible under every definition tested.
- **Severity basis (tested):** four definitions; all fall outside the reported value; absolute quantity negligible in every case.
- **Author question:** Which records were counted as "not identified"? Candidate definitions give 0.030% or 0.100% rather than 0.04%.

### F-09 — Plot listed in the area file with no census records

- **Category:** `DATA_STRUCTURE_ERROR` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Claims:** C-14, C-27 · **Location:** `PlotQuadrantes.csv`, the `BBPL` row
- **Evidence:** The area file lists 33 plots including `BBPL` (243 quadrats), but BBPL has **no records** in the census file, and the manuscript reports 8 plantation plots. A naive join would inflate plantation sampled area from 1.8108 to 2.0295 ha (**+12.1%**).
- **Reconciliation attempted:** The downstream effect was directly tested against a published value.
- **Impact:** **Tested and found not to have propagated.** The reported later-successional tree density ratio of 8% reproduces at exactly 8.0% only when BBPL is *excluded* (7.7% if included). This is positive evidence that the published analysis used the correct 8-plot set.
- **Severity basis (tested):** the discrepancy is a **reuse hazard in the archive**, not an error in the published result.
- **Author question:** `PlotQuadrantes.csv` contains a `BBPL` row with no corresponding census records. Should it be removed or flagged so reusers do not join it into area calculations?

### F-10 — Undocumented encoding and missing-value codes

- **Category:** `REPRODUCIBILITY_LIMITATION` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** CONCERN
- **Location:** `ECOLAPPS_final_Schubert.et.al.2024.csv`
- **Evidence:** The file is Latin-1 encoded, which the README does not state; a standard UTF-8 read fails at byte 137401. `seed_size` contains two undocumented codes: `UNK` (16 records) and `?` (1 record). Five taxa have a blank `Family` field, covering 86 individuals.
- **Impact:** Affects reuse rather than the reported results. No published value depends on these defects.
- **Severity basis (tested):** each defect reproduced directly; none propagates to a reported value.
- **Author question:** Could the README state the file encoding and define the `UNK` and `?` codes in `seed_size`?

### F-11 — Supplied manuscript is a text-only postprint without figures or supplement

- **Category:** `REPRODUCIBILITY_LIMITATION` · **Severity:** MINOR · **Certainty:** HIGH · **Assessment:** LIMITATION
- **Claim:** C-47 · **Location:** `qt2qt6s177.pdf`
- **Evidence:** 38-page accepted-manuscript postprint with **no embedded images on any page** and no supplementary material.
- **Impact:** All figure-level and supplement-level claims are unverifiable from what was supplied. This is a limitation of the **review materials**, not a defect of the published article.
- **Severity basis (tested):** image extraction returned zero images across all 38 pages.
- **Author question:** Not applicable — this concerns the materials supplied to the audit.

---

## 13. Checked but not raised

The following were examined and produced **no finding**. Recording them prevents the absence of a finding being mistaken for absence of a check.

| Check | Outcome |
|---|---|
| Duplicate record identifiers in the census | None detected |
| Impossible or negative DBH / height values | None detected |
| Plot–treatment assignment consistency across files | Consistent |
| Per-plot quadrat counts, all 32 census plots | Exact match to `PlotQuadrantes.csv` |
| Sampled-area formula (`N.Quad × 9 m² / 10000`) | Reproduces the reported 1.01 ha minimum |
| Empty-quadrat (`ND`) placeholder handling | Internally consistent; sums to 0 individuals |
| Planted-stem protocol separation | All 1,941 planted rows consistently lack quadrat keys |
| Six-taxon exclusion rule | Applied consistently; 261 → 255 OTUs as reported |
| Trait-source agreement (census fields vs 2025 master) | Identical results on every trait computation tested |
| `seed_size` value domain (raw token inspection) | Clean — see §7.1; the earlier "mixed dtypes" report is retracted |
| Species-code ↔ family cross-consistency | Consistent apart from the 5 blank-family taxa in F-10 |

---

## 14. Reconciled coverage

```text
Claim denominator:        50
Recomputed match:         31
Recomputed mismatch:       7
Blocked:                   9
Not checked:               2
Not applicable:            1
Total classified:         50
Reconciliation:         PASS

Distinct findings:        11
Affected claim cells:     23
```

Categories are mutually exclusive and sum to the denominator. **Affected claim cells (23) and distinct findings (11) use separate denominators** and must not be conflated: F-01 alone accounts for 7 affected cells.

Severity distribution: MAJOR 1, MINOR 9, UNDETERMINED 1, CRITICAL 0.

Restricted to the 38 checkable claims, the descriptive-reporting match rate is **31/38 = 81.6%**; all 7 non-matching claims are descriptive percentages or a quantifier, none of which alters a stated conclusion's direction.

---

## 15. Separate status architecture

| Dimension | Status |
|---|---|
| Package completeness | `PARTIALLY_COMPLETE` |
| Source execution | `EXECUTION_BLOCKED` |
| Independent recomputation | `PARTIALLY_RECOMPUTED` |
| Computational reproducibility | `BLOCKED` |
| Reporting correspondence | `PARTIALLY_VERIFIED` |
| Empirical data integrity | `NO_DEMONSTRATED_ISSUES` |
| Configuration and model-input integrity | `NOT_APPLICABLE` |

**Verdict scope (Gate 8).** `MATCHES`, `MINOR_DISCREPANCIES`, and `MATERIAL_DISCREPANCIES` are **not** used. Coverage excludes every model-based result, so it is not broad enough to characterise reporting correspondence for the manuscript as a whole. The verdict is `PARTIALLY_VERIFIED`, and the checked subset is: *all descriptive and derived numerical claims recoverable from the supplied census, area, and trait files; no inferential result.*

Methodological quality is reported separately and was **not assessed**: this audit evaluates evidence correspondence, not study design, statistical appropriateness, or ecological interpretation.

---

## 16. Author queries

| # | Location | Question | Why needed |
|---:|---|---|---|
| 1 | `README.md` L67 | Could you supply `FinalAnalysis_ECOLAPP_Schubert.et.al.R`? | Named in the README but absent; blocks all inferential verification (F-01) |
| 2 | p.13 L249–250 | Should "of individuals" read "of taxa"? | The percentages match taxon counts exactly, not individual counts (F-02) |
| 3 | p.13 L269–270 | How was the 15% late-successional figure derived? | The same method reproduces the companion 50% exactly but gives ~21% here (F-03) |
| 4 | p.15 L300–301 | Which denominator produced 60%? | All planted-species saplings in AN + PL gives 65.3% (F-04) |
| 5 | p.15 L301–303 | Should "all" be qualified? | 17 recruit-origin stems ≥5 cm DBH exist in these treatments (F-05) |
| 6 | p.14 L282 | Which inclusion rule produced 18.6%? | No single rule reproduces all three values in the sentence (F-06) |
| 7 | p.11 L214–215 | Could the 64% mid-successional figure be rechecked? | Both trait sources give 69.2% while the companion 71% reproduces (F-07) |
| 8 | p.11 L219 | Which records were counted as "not identified"? | Candidates give 0.030% or 0.100%, not 0.04% (F-08) |
| 9 | `PlotQuadrantes.csv` | Should the `BBPL` row be removed or flagged? | It has no census records and would inflate area by 12.1% on a naive join (F-09) |
| 10 | `README.md` | Could the encoding and the `UNK`/`?` codes be documented? | The file is Latin-1 and the codes are undefined (F-10) |
| 11 | Methods | Does the Methods text state a count of early-successional species, and if so what is it? | A previously reported conflict with the Figure 1 caption could not be located (C-49) |

All questions are neutral and none speculates about intent.

---

## 17. Blocked and not-checked register

| ID | Item | State | Cause | What would resolve it |
|---|---|---|---|---|
| C-39 | iNEXT rarefied/extrapolated richness + bootstrapped CI | BLOCKED | Analysis script absent | Supply the ECOLAPP script |
| C-40 | Sampling completeness 85–99% | BLOCKED | Analysis script absent | Supply the ECOLAPP script |
| C-41 | NMDS ordination and stress | BLOCKED | Analysis script absent | Supply the ECOLAPP script |
| C-42 | PERMANOVA pairwise tests | BLOCKED | Script + supplement absent | Supply both |
| C-43 | glmmTMB models, emmeans groupings (Fig. 3) | BLOCKED | Analysis script absent | Supply the ECOLAPP script |
| C-44 | Elevated seedling/sapling establishment | BLOCKED | Model not reproducible | Supply the ECOLAPP script |
| C-45 | Plantation large-seeded densities vs reference | BLOCKED | Model not reproducible | Supply the ECOLAPP script |
| C-46 | Per-plot planting counts (313 / 86) | BLOCKED | Initial planting records absent | Supply planting records |
| C-47 | Supplementary figures and tables | BLOCKED | Supplement not supplied | Supply the supplement |
| C-48 | Cartesian coordinate files | NOT_CHECKED | Feasible, but no verified claim depends on them | Complete a follow-up inspection |
| C-49 | Methods count of early-successional species | NOT_CHECKED | String not locatable in this extraction | Check the typeset article |
| C-50 | Execution of the AVS script | NOT_APPLICABLE | It reproduces a different manuscript | — |

`BLOCKED` and `NOT_CHECKED` are distinct: blocked work was impossible with the supplied evidence; not-checked work was feasible but not completed.

---

## 18. Limitations

1. **No inferential result was verified.** Nine claims are blocked, and every model-based conclusion in the manuscript falls into that set. This audit says nothing about whether those results are correct.
2. **Recomputation is not reproduction.** Reproducing a value from raw data shows the data support the number. It does not show that the authors' pipeline produced it, and it cannot detect an error that happens to be reproduced by an independently chosen but identically wrong method.
3. **Text extraction is imperfect.** Claim locations cite line numbers in an extracted text file. One previously reported conflict (C-49) could not be located, which may reflect extraction rather than absence.
4. **Postprint only.** No figures and no supplement were available (F-11), so all figure-level correspondence is unverified.
5. **No interpretation of derived-column provenance.** The census file's trait columns are derived; the code that derived them is not archived, so agreement between the census fields and the trait master demonstrates internal consistency, not external correctness.
6. **Methodological quality not assessed.** Design, statistical appropriateness, and ecological interpretation are outside this skill's scope.
7. **Single-analyst, single-session execution.** No independent second analyst reviewed the recomputation scripts. The corrections in §20 illustrate concretely that this class of audit is itself error-prone.

---

## 19. Output-validation result

Programmatic and manual checks run before delivery:

| Check | Result |
|---|---|
| Both human-readable outputs exist | PASS |
| Both generated from the same validated ledger | PASS |
| Finding IDs identical across Output A, Output B, and ledger | PASS (F-01 … F-11) |
| Claim IDs referenced consistently | PASS (C-01 … C-50) |
| Coverage arithmetic reconciles (31+7+9+2+1 = 50) | PASS |
| Output B never strengthens Output A | PASS |
| Every Output B item carries an assessment label and reason | PASS |
| No code fences, YAML, JSON, hashes, or commits in Output B | PASS |
| Ledger kept separate from Output B | PASS |
| Every severity has a tested impact basis or is UNDETERMINED | PASS (F-03 is UNDETERMINED with stated reason) |
| No publication verdict language | PASS |
| No misconduct inference | PASS (`NONE` on all 11 findings) |
| Every supplied file inventoried; 0 unclassified | PASS (9 of 9) |
| Completeness denominators documented | PASS (2 referenced, 3 inferred) |
| Source execution separated from independent recomputation | PASS |
| Figure-code mapping separated from published-figure provenance | PASS |
| Affected cells and distinct findings use separate denominators | PASS (23 vs 11) |

**Output validation: PASS**

---

## 20. Corrections to the prior audit run

The earlier audit of this same package (preserved at commit `eb2cc35`) contained errors that this independent re-execution identified. They are listed here in full because those outputs are already committed to the repository.

| ID | Prior statement | Status | Basis for the correction |
|---|---|---|---|
| **X-01** | `seed_size` is stored in mixed string and float formats, putting 1,308 records at risk of silent category splitting | **RETRACTED** | Raw token inspection with the standard-library CSV reader shows only `1, 2, 3, NA, UNK, ?`. The decimal tokens appear only under pandas' default chunked type inference — an artifact of the reader, not a property of the file. |
| **X-02** | Richness values 156/185/196/205 do not reproduce (recomputed 155/184/195/204) | **RETRACTED** | Reported = retained + 1 in all four treatments. The rule discriminates: applied nucleation contains 3 excluded taxa yet still gains only +1, ruling out per-taxon reinstatement. The manuscript documents grouping of inconsistently identified taxa at p.11 L217–218. |
| **X-03** | 65 families reported but only 64 present | **RETRACTED** | 64 named + 1 unassigned = 65, under the same documented grouping rule. |
| **X-04** | The "all but 10.5%" claim does not reproduce (recomputed 13.24%) | **RETRACTED** | The prior figure used all size classes; the manuscript says **tree species**. The correct denominator gives 10.34%–10.96%, bracketing 10.5%. The companion "~90%" claim also reproduces, at 89.0%. |
| **X-05** | Figure 1 caption value of 163 late-successional species does not reproduce (recomputed 162) | **RETRACTED** | 162 + 1 grouped unit = 163 — the same rule that reconciles richness. |
| **X-06** | The values 7.7%, 79.1% and 70.6% were recorded as *reported manuscript values* that matched exactly | **CORRECTED** | **None of these strings occurs in the manuscript.** They were the prior run's own recomputed values entered into the reported-value column. The actual claims are 8%, ">75%", and 71%, which recompute to 8.0%, 79.1% and 71.1% and are confirmed (C-22, C-23, C-31). |
| **X-07** | BBPL inflates plantation area; impact UNDETERMINED | **RESOLVED** | The 8% density claim reproduces at exactly 8.0% only with BBPL excluded, demonstrating the published analysis used the correct 8-plot set. The archive defect is retained as F-09, a reuse hazard. |
| **X-08** | The Methods state 37 early-successional species, conflicting with the Figure 1 caption's 38 | **UNCONFIRMED** | The string could not be located in this extraction. Recorded as C-49 `NOT_CHECKED` rather than asserted as a finding. |

**Net effect.** The manuscript's descriptive numbers reproduce substantially **better** than the prior audit reported. Five reported discrepancies were false positives arising from the wrong denominator or an unrecognised documented grouping rule; one reported data defect was a software artifact; and three "matches" were bookkeeping errors in which the audit's own outputs were recorded as the paper's claims.

The methodological lesson is that Phase 9 reconciliation must be exhausted — testing alternative denominators, populations, and documented exclusion rules — before any mismatch is raised, and that every "reported value" must be verified as a literal string present in the manuscript.

---

*End of Output A. See `dryad_s7h44j1gc_eap3053_review_brief.md` for the accessible issue-focused brief and `dryad_s7h44j1gc_eap3053_audit_ledger.json` for the machine-readable ledger.*
