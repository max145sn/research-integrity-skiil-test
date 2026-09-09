# Research Package Integrity Audit — Output A: Comprehensive Technical Audit

**Manuscript:** Schubert, S. C., R. A. Zahawi, F. Oviedo-Brenes, J. A. Rosales, K. D. Holl. *Active restoration increases tree species richness and recruitment of large-seeded taxa after 16–18 years.* Ecological Applications 35(1), 2025. DOI 10.1002/eap.3053. (Supplied as eScholarship postprint `qt2qt6s177.pdf`, 38 pages.)

**Data/code package:** Dryad `doi_10_5061_dryad_s7h44j1gc__v20251216.zip` (version dated 16 Dec 2025), DOI 10.5061/dryad.s7h44j1gc.

**Audit skill:** `research-package-integrity-audit2`

---

## 1. Execution-mode disclosure

This audit was performed in a single agent session on a Windows host. Manuscript text was extracted programmatically from the supplied PDF (`pdfplumber`, 38 pages, 68,034 characters, extraction confidence HIGH for body text). Data checks were performed by **independent recomputation in Python 3.12 / pandas**, not by executing the authors' R code.

- **R runtime:** not installed on the audit host → `ENVIRONMENT_CHECK_FAILED` for R.
- **Authors' analysis code for this manuscript:** not present in the package (see F-01) → `EXECUTION_BLOCKED`.
- Consequently **no result in this audit is a reproduction of the authors' pipeline.** All numerical agreements reported below are *independent recomputations from the supplied raw census data*, which is a weaker form of correspondence than re-running the original code.
- This audit assesses evidence correspondence only. It does not detect intent, infer misconduct, or make a publication decision.

## 2. Executive summary

The supplied census dataset is of high quality and reproduces the manuscript's **core descriptive results exactly** — the three recruit totals (66,446 / 14,038 / 3,842), the 1,941 surviving planted stems, the 255-OTU richness figure, the plot replication (9/9/8 + 6), and the 1.01 ha minimum sampling area all recompute to the reported values to the last digit. Twenty claims were independently recomputed and matched.

Against that, one structural problem dominates the audit: **the R script required to reproduce this manuscript is not in the package.** The README names `FinalAnalysis_ECOLAPP_Schubert.et.al.R`, and the manuscript's Open Research Statement asserts that "Data and R code needed to reproduce analyses are archived on Dryad platform DOI: 10.5061/dryad.s7h44j1gc." The only R file supplied is `FinalAnalysis_AVS_Schubert.et.al.R`, whose header states it reproduces a **different** manuscript (Applied Vegetation Science). Every inferential result in the paper — the iNEXT rarefaction curves and 85–99 % completeness statement, the NMDS/PERMANOVA composition analysis, and all glmmTMB/emmeans significance letters in Figure 3 — is therefore unverifiable from this package.

Eleven reported quantities did not reproduce. Most are small and do not disturb any qualitative conclusion, but two are substantive as stated: the identification-quality sentence ("94.2 % of individuals to species") is demonstrably a **taxon** proportion, not an individual proportion (the individual-level values are 99.85 % / 0.15 % / 0.00 %); and the universal claim that **all** trees ≥5 cm DBH of planted species in applied nucleation and plantation were originally planted is contradicted by 17 recruit-origin stems in the data. A further data-file inconsistency (`PlotQuadrantes.csv` lists a ninth plantation plot, `BBPL`, absent from the census) would inflate plantation sampling area by 12.1 % if joined naively; whether the published analysis was affected cannot be determined without the missing code.

## 3. Preflight and scope

| Item | State |
|---|---|
| Supplied artifacts | 1 manuscript PDF, 1 Dryad ZIP (8 files) |
| Files readable | 8/8 |
| Encoding note | Main CSV is Latin-1, not UTF-8 (byte 0xA0 at position 137401); UTF-8 read fails |
| Python 3.12 + pandas/numpy/scipy | available |
| pdfplumber | installed during audit |
| R / Rscript | **absent** → `ENVIRONMENT_CHECK_FAILED` |
| Internet needed | no (all checks local); cited prior publications not retrieved |
| User scope | audit the manuscript against the supplied data, results, configuration and code |
| Exclusions | no source files in the host repository were modified |
| **Preflight status** | **PARTIAL** |

## 4. File inventory and missing-artifact register

### 4.1 Supplied files (denominator = 9 artifacts: 8 package files + 1 manuscript)

| # | File | Bytes | Classification | Used for |
|---:|---|---:|---|---|
| 1 | `qt2qt6s177.pdf` | 1,056,094 | Manuscript (postprint, text only) | Claim extraction |
| 2 | `README.md` | 13,592 | Package documentation | Inventory, variable definitions |
| 3 | `ECOLAPPS_final_Schubert.et.al.2024.csv` | 10,138,063 | `RAW_OBSERVED` + `DERIVED` (Class column; extrapolated planted sizes) | Primary recomputation source |
| 4 | `PlotQuadrantes.csv` | 348 | `MODEL_INPUT` (sampling-area offsets) | Area/density recomputation |
| 5 | `IslasMaster_abbreviated2025.csv` | 18,497 | `CLEANED` taxonomic attribute table (2025 revision) | Sensitivity check on trait claims |
| 6 | `FinalAnalysis_AVS_Schubert.et.al.R` | 511,092 | Analysis code for a **different** manuscript | Inference of exclusion rules only |
| 7 | `Cartesian.Standard.Meters.csv` | 5,691 | `MODEL_INPUT` (spatial coordinates) | `NOT_APPLICABLE` to this manuscript |
| 8 | `Cartesian.Long.Meters.csv` | 4,079 | `MODEL_INPUT` | `NOT_APPLICABLE` |
| 9 | `Cartesian.Reference.Meters.csv` | 5,509 | `MODEL_INPUT` | `NOT_APPLICABLE` |

No file was left unclassified.

### 4.2 Missing-artifact register

| ID | Artifact | Source of expectation | Status |
|---|---|---|---|
| M-01 | `FinalAnalysis_ECOLAPP_Schubert.et.al.R` | Named verbatim in README §"Files and variables"; required by manuscript Open Research Statement (p. 2, lines 21–22) | **ABSENT** |
| M-02 | Figures 1, 2, 3 (graphics) | Manuscript figure captions, p. 37 | Absent — supplied PDF contains **0 embedded images** |
| M-03 | Appendix S1: Tables S1–S4, Figures S1–S4 | Cited 14× in manuscript body | Not supplied |
| M-04 | Per-species, per-plot initial planting counts | Required to verify survival percentages (p. 9, lines 176–179) | Not supplied (referred to Holl et al. 2011) |
| M-05 | Session/environment record (R 4.3.3, package versions, seeds) | Manuscript p. 10 line 223 states R 4.3.3 | Not supplied |

**Completeness denominator statement.** Manuscript-referenced required artifacts = 5 (M-01…M-05). Supplied = 0 of 5. Data artifacts required for the descriptive claims = 2 (census CSV, area CSV); supplied = 2 of 2.

**Package completeness: `INCOMPLETE`.**

## 5. Study and evidence map

Single observational study; one census (June–July 2022) of a randomized restoration experiment established 2004–2006.

| Node | Value | Evidence |
|---|---|---|
| Study | 16–18-yr census, 10 sites, S Costa Rica | `DIRECTLY_INSPECTED` (manuscript + README agree) |
| Design | 3 treatments (NR / AN / PL) + reference forest (RF) | `DIRECTLY_INSPECTED` |
| Units | 3×3 m quadrats nested in 6×6 m `Parcela` | `RECOMPUTED` |
| Dataset | `ECOLAPPS_final_...2024.csv`, 67,046 rows | `RECOMPUTED` |
| Area offsets | `PlotQuadrantes.csv`, 33 rows | `RECOMPUTED` |
| Analysis code | **unmapped** — no code node exists for this manuscript | `BLOCKED` |
| Result objects | none supplied (no `.RData`, no model output, no figure source data) | `BLOCKED` |
| Figures 1–3 | captions only | `FIGURE_CHECK_BLOCKED` |

**Mapping statuses.** Manuscript → dataset: `CONFIRMED` (README explicitly links the CSV to Schubert et al. 2024; all descriptive totals recompute exactly). Manuscript → analysis code: `UNRESOLVED` (the required file is absent; the supplied R file self-identifies as a different manuscript). Figures → code: `UNRESOLVED`. Published-figure provenance: **not verified and not verifiable from this package.**

The supplied AVS script was used only to *infer* one documented data-cleaning rule (exclusion of six poor-resolution taxa). Because that script belongs to a different manuscript, this inference is `PROBABLE`, not `CONFIRMED`.

## 6. Claim ledger

**Claim ledger status: COMPLETE for numerically verifiable claims in the main text; `BLOCKED` for supplementary-material claims (Appendix S1 not supplied).**
**Reporting correspondence: `PARTIALLY_VERIFIED`.**

| ID | Location | Reported proposition | Expected support | Mapping | Evidence | Outcome |
|---|---|---|---|---|---|---|
| C-01 | p.11 l.247 | 66,446 seedling recruits | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (66,446) |
| C-02 | p.11 l.247 | 14,038 sapling recruits | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (14,038) |
| C-03 | p.11 l.247 | 3,842 tree recruits | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (3,842) |
| C-04 | p.11 l.248 | 1,941 surviving planted trees | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (1,941) |
| C-05 | p.3 l.34 | ">80,000 seedlings, saplings and trees" | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (84,326) |
| C-06 | p.11 l.247 | 255 operational taxonomic units | census CSV | PROBABLE | RECOMPUTED | **MATCH** (261 codes − 6 poor-resolution taxa = 255) |
| C-07 | p.3 l.34–35; p.9 l.164 | 26 restoration plots: NR 9, AN 9, PL 8 | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (9/9/8) |
| C-08 | p.3 l.35 | six reference forests | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (6) |
| C-09 | p.10 l.229 | 1.01 ha = minimum area sampled across the four treatments | `PlotQuadrantes.csv` | CONFIRMED | RECOMPUTED | **MATCH** (RF = 1.0116 ha) |
| C-10 | p.13 l.298 | planted-taxa seedlings 13.0 % in AN | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (12.96 %) |
| C-11 | p.13 l.298 | planted-taxa seedlings 4.7 % in PL | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (4.67 %) |
| C-12 | p.14 l.300 | planted-taxa saplings = 1.8 % of all saplings | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (1.82 %) |
| C-13 | p.13 l.281 | early-successional = 54.0 % of NR saplings | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (53.95 %) |
| C-14 | p.13 l.281 | early-successional = 43.3 % of AN saplings | census CSV | PROBABLE | RECOMPUTED | **MATCH** (43.30–43.31 %) |
| C-15 | p.13 l.282 | early-successional = 18.6 % of PL saplings | census CSV | UNRESOLVED | RECOMPUTED | **MISMATCH** → F-15 (18.19–18.59 % across 7 rules) |
| C-16 | p.14 l.312 | later-successional tree density in restoration = 8 % of RF | census + area CSV | CONFIRMED | RECOMPUTED | **MATCH** (7.7 %) |
| C-17 | p.13 l.293 | listed early-successional taxa > 75 % of recruited trees in restored plots | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (79.1 %) |
| C-18 | p.10 l.215 | 71 % of late-successional species have seeds ≥5 mm | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (70.6 %; 70.9 % on 2025 traits) |
| C-19 | Fig. 1 caption | mid-successional n = 52 spp | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (52) |
| C-20 | Fig. 1 caption | early-successional n = 38 spp | census CSV | CONFIRMED | RECOMPUTED | **MATCH** (38) |
| C-21 | p.9–10 l.192–197 | plot quadrat counts (256 / 252 / 196 / 147 …) | census vs area CSV | CONFIRMED | RECOMPUTED | **MATCH** (all 32 census plots agree exactly) |
| C-22 | p.11 l.249–250 | "we identified 94.2 % of **individuals** to species, 4.6 % to genus, 1.1 % to family" | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-02 |
| C-23 | p.11–12 l.251–253 | observed richness NR 156, AN 185, PL 196, RF 205 | census CSV | PROBABLE | RECOMPUTED | **MISMATCH** → F-03 (155/184/195/204) |
| C-24 | p.12 l.254–255 | "All but 10.5 % of tree species recorded in reference forest" colonized ≥1 restoration plot | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-04 (13.24 %) |
| C-25 | p.9 l.206 | early-successional taxa (37 spp.) | census CSV + Fig. 1 caption | CONFIRMED | RECOMPUTED | **MISMATCH** → F-05 (38) |
| C-26 | Fig. 1 caption | late-successional n = 163 spp | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-06 (162) |
| C-27 | p.10 l.214–215 | "most (64 %) mid-successional species having small seeds" | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-07 (69.2 %) |
| C-28 | p.14 l.302–303 | "**All** trees (≥5 cm DBH) of these species in AN and PL were planted" | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-08 (17 recruit-origin stems) |
| C-29 | p.14 l.300–301 | 60 % of planted-taxa saplings in the two planted treatments were originally planted | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-09 (65.3 %) |
| C-30 | p.11 l.248 | 65 families | census CSV | CONFIRMED | RECOMPUTED | **MISMATCH** → F-11 (64) |
| C-31 | p.10 l.219–220 | 0.04 % of individuals not identified and excluded | census CSV | UNRESOLVED | RECOMPUTED | **MISMATCH** → F-14 (0.031 % or 0.100 %) |
| C-32 | p.10 l.226–227 | sampling completeness 85–99 % across classes/groups | iNEXT run | UNRESOLVED | BLOCKED | code + result objects absent |
| C-33 | p.10 l.228–229; Fig. 1 | bootstrapped 95 % CIs for accumulated richness at 1.01 ha | iNEXT run | UNRESOLVED | BLOCKED | code + figures absent |
| C-34 | Fig. 2 caption | NMDS stress = 0.17–0.18 for all three size classes | vegan run | UNRESOLVED | BLOCKED | code absent |
| C-35 | p.12 l.277; Table S4 | PERMANOVA pairwise treatment differences (Bonferroni) | Table S4 | UNRESOLVED | BLOCKED | supplement absent |
| C-36 | Fig. 3; p.14–15 | glmmTMB/emmeans significance letters and all "significant / not significant" statements | model objects | UNRESOLVED | BLOCKED | code + figures absent |
| C-37 | p.9 l.176–179 | survival: *E. poeppigiana* 34.5 ± 28.5 %, *I. edulis* 22.9 ± 18.5 %, *V. guatemalensis* 82.8 ± 18.4 %, *T. amazonia* 82.1 ± 17.8 % | initial planting counts | UNRESOLVED | BLOCKED | denominators absent (see §10, B-05) |
| C-38 | p.15 l.334–335 | NR had "more than twice the expected number of species" vs Holl et al. 2017 | external publication | UNRESOLVED | BLOCKED | prior-publication values not in package |
| C-39 | p.9 l.168–169 | 313 trees planted in PL, 86 in AN | Holl et al. 2011 | UNRESOLVED | BLOCKED | external |
| C-40 | Figs S1–S4, Tables S1–S3 | all supplementary-derived claims | Appendix S1 | UNRESOLVED | BLOCKED | supplement absent |
| C-41 | p.10–11 l.230–235 | Chao-dissimilarity community matrices / NMDS ordination | independent reimplementation | UNRESOLVED | NOT_CHECKED | feasible in Python but matrix-construction rules are defined only in the absent code |
| C-42 | p.10 l.224–229 | independent rarefaction / coverage estimation | independent reimplementation | UNRESOLVED | NOT_CHECKED | feasible; outside completed scope |
| C-43 | — | spatial (Cartesian) analyses | `Cartesian.*.csv` | NOT_APPLICABLE | NOT_APPLICABLE | these files support the Applied Vegetation Science manuscript |

## 7. Data-provenance checks

| Check | Result | Evidence |
|---|---|---|
| Row/record semantics | 67,046 rows; `No..indiv.` is a count, not 1 row = 1 stem. Individual totals must be summed, not counted. | `RECOMPUTED` |
| Placeholder rows | 789 rows coded `Especie = "ND"` (empty quadrats), all with `No..indiv.` summing to 0 → correctly excluded from totals | `RECOMPUTED` |
| Origin coding | `Recruit` 84,326 individuals; `Planted` 1,941 individuals; total 86,267 | `RECOMPUTED` |
| Class coding vs DBH rule | `seedling` / `sapling` / `tree` consistent with the stated <1 / 1–<5 / ≥5 cm DBH rule | `DIRECTLY_INSPECTED` |
| Grid completeness | All 1,941 `Planted` rows have blank `Parcela`/`Quadrante` — consistent with the README's statement that planted-stem survival used a separate protocol. Once these are excluded, **all 32 census plots' distinct quadrat counts equal `PlotQuadrantes.N.Quad` exactly** (32/32, difference 0). | `RECOMPUTED` |
| Plot inventory cross-file | `PlotQuadrantes.csv` contains **33** plots; census contains **32**. `BBPL` (243 quadrats) is in the area file only. | `RECOMPUTED` → F-10 |
| Extrapolated values | 509 rows flagged `Measured = Extrapolated`, all `Origin = Planted`, consistent with README disclosure | `DIRECTLY_INSPECTED` |
| Missing-value coding | 5 taxa carry blank `Family`/`Genus`/`Specific.Epithet` (`BORAGINACEAE`, `HIRAEA`, `ING_SP1`, `LAU_SP2`, `RUBIACEAE`), 86 individuals | `RECOMPUTED` → F-13 |
| Type consistency | `seed_size` mixes string `"1"/"2"/"3"` with float-formatted `1.0/2.0/3.0`, plus `"UNK"` (16 ind.) and `"?"` (1 ind.) | `RECOMPUTED` → F-13 |
| Encoding | file is Latin-1; not declared in README | `DIRECTLY_INSPECTED` → F-13 |
| Duplicate/ID integrity | not applicable — no individual-level IDs in the redacted file | `NOT_APPLICABLE` |
| Attribute-table drift | `IslasMaster_abbreviated2025.csv` (256 taxa) is a **later** revision: 4 codes it contains are absent from the census and 11 census codes are absent from it (nomenclature updates, e.g. `OCO_CER`→`OCO_LEP`). Trait claims were therefore tested against both versions. | `RECOMPUTED` |

**Empirical data integrity: `NO_DEMONSTRATED_ISSUES`** for the census records themselves.
**Configuration and model-input integrity: `DEMONSTRATED_ISSUES`** (F-10, area-offset file).

## 8. Code, configuration, and domain checks

| Check | Result |
|---|---|
| Entry point for this manuscript | **none exists in the package** (F-01) |
| Supplied R file identity | `FinalAnalysis_AVS_Schubert.et.al.R`, 12,434 lines; header lines 1–5 read "CODE TO REPRODUCE ANALYSIS OF APPLIED VEGETATION SCIENCE MANUSCRIPT … Restoration method influences spatial patterns of tree seedling and sapling recruitment…" |
| Hardcoded paths | the supplied script sets the working directory to a personal absolute path on the first author's machine (`C:/Users/scsch/OneDrive/Desktop/...`), which would fail on any other system |
| Input files consumed by supplied script | `ECOLAPPS_final_Schubert.et.al.2024.csv`, `IslasMaster_abbreviated2025.csv` |
| Documented cleaning rule recovered | the script drops six poor-resolution taxa (`BORAGINACEAE`, `HIRAEA`, `RUBIACEAE`, `INGA`, `GUAREA`, `LAURACEAE`); applying this rule reproduces the manuscript's 255-OTU figure exactly |
| Seeds / RNG state | not set in the supplied script for the bootstrap or NMDS steps; not documented anywhere for this manuscript |
| Package versions | not recorded; manuscript states R 4.3.3 only |
| Stale/overwritten outputs | `NOT_CHECKED` — no result objects are supplied |
| Leakage / split / tuning checks | `NOT_APPLICABLE` (no machine-learning component) |
| Simulation checks | `NOT_APPLICABLE` (no simulation component) |

## 9. Source-execution report

**Source execution: `EXECUTION_BLOCKED`.**

Two independent blockers: (a) the manuscript's analysis script is absent from the package; (b) no R runtime is installed on the audit host. Blocker (a) is decisive — installing R would not resolve it. No execution was attempted, and **no statement in this audit should be read as a failed reproduction attempt.**

## 10. Independent-recomputation report

**Independent recomputation: `PARTIALLY_RECOMPUTED`.**

All recomputations were written from the manuscript's own textual definitions and the README variable dictionary, in Python, without reference to the authors' code. Tolerances were set from the reported precision of each value (e.g. a value reported as `18.6 %` was accepted if the recomputed value lay within ±0.1 pp; `8 %` within ±0.5 pp).

### 10.1 Census totals (exact)

| Class | Recruit | Planted |
|---|---:|---:|
| seedling | **66,446** | 51 |
| sapling | **14,038** | 126 |
| tree | **3,842** | 1,764 |
| **total** | **84,326** | **1,941** |

Reported: 66,446 / 14,038 / 3,842 recruits and 1,941 planted survivors. **Exact agreement on all four values.**

### 10.2 Richness and taxonomy

- 261 distinct `Especie` codes in the census; removing the six poor-resolution taxa gives **255** — the reported OTU count, exactly.
- Distinct named families = **64** (reported 65) → F-11.
- Taxon-level identification: 246 species-level, 12 genus-level, 3 family-level out of 261 → **94.25 % / 4.60 % / 1.15 %**, matching the reported 94.2 % / 4.6 % / 1.1 % to the reported precision. The corresponding **individual-level** proportions are **99.85 % / 0.15 % / 0.00 %** → F-02.
- Observed richness by treatment (255-taxon set): NR **155**, AN **184**, PL **195**, RF **204**; reported 156 / 185 / 196 / 205 → F-03. Using the unfiltered 261-code set gives 156 / 187 / 197 / 206. No single exclusion rule tested reproduces all four reported values.
- Species per successional group (255-taxon set): Early **38**, Mid **52**, Late **162**, unassigned 3 (`CITRUS`, `ING_SP1`, `LAU_SP2`). Figure 1 caption reports 38 / 52 / 163; Methods text reports 37 early → F-05, F-06.

### 10.3 Trait claims

| Reported | Recomputed (2024 columns) | Recomputed (2025 master) | Outcome |
|---|---|---|---|
| 64 % of mid-successional species have small (<5 mm) seeds | 36/52 = **69.2 %** | 35/50 = **70.0 %** | MISMATCH (F-07) |
| 71 % of late-successional species have seeds ≥5 mm | 113/160 = **70.6 %** | 112/158 = **70.9 %** | MATCH |

### 10.4 Composition and abundance

| Reported | Recomputed | Outcome |
|---|---|---|
| early-successional share of saplings: NR 54.0 % | 53.95 % | MATCH |
| … AN 43.3 % | 43.30 % (all saplings) / 43.74 % (recruit-origin only) | MATCH under one rule |
| … PL 18.6 % | 18.19 % / 18.52 % / 18.59 % depending on rule | MISMATCH (F-15) |
| planted-taxa seedlings AN 13.0 %, PL 4.7 % | **12.96 %**, **4.67 %** | MATCH |
| planted-taxa saplings = 1.8 % of all saplings | **1.82 %** | MATCH |
| 60 % of planted-taxa saplings in AN+PL were originally planted | 126/193 = **65.3 %** | MISMATCH (F-09) |
| listed early-successional taxa > 75 % of recruited trees in restored plots | **79.1 %** (2,142/2,707) | MATCH |
| all planted-taxa trees in AN and PL were originally planted | 17 recruit-origin stems (AN 11, PL 6; DBH 5.0–27.3 cm) | MISMATCH (F-08) |
| ~90 % / "all but 10.5 %" of RF species colonized ≥1 restoration plot | **86.76 %** (27 of 204 absent = 13.24 %) | MISMATCH (F-04) |

### 10.5 Densities and sampling area

Sampled area = `N.Quad × 9 m²`. Treatment areas: NR 1.7640 ha, AN 1.9431 ha, PL 2.0295 ha, RF 1.0116 ha. The RF value confirms the manuscript's "**1.01 ha, which was the minimum area sampled for all four treatments**" exactly.

Later-successional (mid + late) recruits in the tree size class:

| Treatment | stems | ha | stems/ha |
|---|---:|---:|---:|
| NR | 111 | 1.7640 | 62.9 |
| AN | 252 | 1.9431 | 129.7 |
| PL | 97 | 2.0295 | 47.8 |
| **restoration pooled** | 460 | 5.7366 | **80.2** |
| RF | 1,052 | 1.0116 | **1,039.9** |

Ratio = **7.7 %**, matching the reported "small fraction (8 %)".

Note that the PL area above uses the area file as supplied, i.e. including the phantom `BBPL` plot; excluding it gives 1.8108 ha and 53.6 stems/ha (see F-10).

## 11. Figure, table, and source-data correspondence

| Artifact | Status | Basis |
|---|---|---|
| Figure 1 (species-accumulation curves) | `FIGURE_CHECK_BLOCKED` | no graphic in supplied PDF; no code; no result object. Only the caption's species counts were checkable (C-19, C-20, C-26). |
| Figure 2 (NMDS) | `FIGURE_CHECK_BLOCKED` | as above; stress values unverifiable |
| Figure 3 (mean stem densities) | `FIGURE_CHECK_BLOCKED` | as above; underlying raw densities were independently recomputed (§10.5) but **published figure values were not compared** |
| Tables S1–S4 | `FIGURE_CHECK_BLOCKED` | Appendix S1 not supplied |
| Figures S1–S4 | `FIGURE_CHECK_BLOCKED` | Appendix S1 not supplied |

`FIGURE_CODE_SECTION_MAPPED` was **not** achieved for any figure, because no code file for this manuscript exists. `PUBLISHED_FIGURE_PROVENANCE_VERIFIED` is not claimed anywhere in this audit.

## 12. Detailed findings

---
### F-01 — Analysis code for this manuscript is not in the package
- **Category:** `FILE_OR_PACKAGE_GAP`
- **Locations:** README §"Files and variables" (names `FinalAnalysis_ECOLAPP_Schubert.et.al.R`); manuscript p. 2 lines 21–22 (Open Research Statement); package root
- **Claims affected:** C-32 … C-36, C-40 (6 blocked claims), plus all figure provenance
- **Evidence:** `DIRECTLY_INSPECTED`. Package contains exactly one `.R` file, `FinalAnalysis_AVS_Schubert.et.al.R`; its lines 1–5 identify it as the code for the Applied Vegetation Science manuscript "Restoration method influences spatial patterns of tree seedling and sapling recruitment in the second decade of tropical forest recovery". The README's December 2025 update note confirms the package was extended for that second paper.
- **Reported vs observed:** Open Research Statement asserts "Data and R code needed to reproduce analyses are archived"; observed = data archived, code for this manuscript not archived in v20251216.
- **Reconciliation attempted:** searched all 8 files for an ECOLAPP entry point; checked whether the AVS script reproduces the manuscript's inferential outputs — it does not (different response variables, different spatial models).
- **Impact (tested):** blocks verification of 100 % of the manuscript's inferential results — the iNEXT completeness and rarefaction (C-32, C-33), the NMDS stress and PERMANOVA (C-34, C-35), and every significance statement in Figure 3 (C-36). 6 of 43 ledger claims move to `BLOCKED` solely because of this finding.
- **Severity:** **MAJOR** (evidence-backed: the affected claims include all hypothesis tests supporting the paper's central conclusions)
- **Certainty:** HIGH. **Misconduct inference: NONE** — an earlier Dryad version may have contained the file, and versioning/replacement is a routine archiving outcome.
- **Reviewer action:** request the ECOLAPP analysis script (or the specific Dryad version that contains it).
- **Author question:** AQ-1

---
### F-02 — Identification percentages are taxon proportions, not individual proportions
- **Category:** `REPORTING_INCONSISTENCY`
- **Location:** p. 11, lines 249–250
- **Claim:** C-22
- **Evidence:** `RECOMPUTED`
- **Reported:** "we identified 94.2 % of individuals to species, 4.6 % to genus, and 1.1 % to family levels."
- **Observed:** as proportions of **individuals** — 99.85 % species, 0.15 % genus, 0.00 % family, 0.10 % unassigned. As proportions of the **261 OTU codes** — 246/261 = 94.25 %, 12/261 = 4.60 %, 3/261 = 1.15 %.
- **Tolerance:** ±0.1 pp (one unit of reported precision). Individual-level deviation = 5.65 pp; taxon-level deviation ≤ 0.05 pp.
- **Reconciliation attempted:** tested individual-level and taxon-level denominators, with and without the six excluded taxa, and with/without `Origin = Planted`. Only the taxon-level, 261-code denominator reproduces all three values simultaneously (and they sum to exactly 261 taxa).
- **Impact (tested):** wording only; no downstream analysis uses this quantity. The error **understates** the identification quality of the dataset.
- **Severity:** **MINOR**
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Reviewer action:** ask for the word "individuals" to be corrected to "taxa"/"OTUs".
- **Author question:** AQ-2

---
### F-03 — Observed species richness is one species higher than recomputed in every treatment
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** p. 11–12, lines 251–253
- **Claim:** C-23
- **Evidence:** `RECOMPUTED`
- **Reported:** NR 156, AN 185, PL 196, RF 205. **Observed:** 155, 184, 195, 204 (255-taxon set) or 156, 187, 197, 206 (all 261 codes).
- **Reconciliation attempted:** four exclusion rules tested. The uniform +1 offset is consistent with the reported values counting all excluded/unresolved taxa as a single additional OTU per treatment, but this cannot be confirmed without the missing code. Per-treatment presence of the six excluded taxa is uneven (NR 1, AN 3, PL 2, RF 2), so no simple subset rule reproduces all four values.
- **Impact (tested):** the rank order NR < AN < PL < RF is preserved under every rule tested, so every comparative statement built on these numbers ("richness increased across the planting gradient", "reference forest highest") remains supported.
- **Severity:** **MINOR** (impact tested: no qualitative conclusion changes)
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-3

---
### F-04 — Proportion of reference-forest species absent from restoration plots
- **Category:** `NUMERICAL_MISMATCH`
- **Locations:** p. 12, lines 254–255; p. 21, line 469 ("~90 % of reference forest species")
- **Claim:** C-24
- **Evidence:** `RECOMPUTED`
- **Reported:** "All but 10.5 %" (i.e. 89.5 % colonized). **Observed:** 27 of 204 reference-forest OTUs occur in no restoration plot = **13.24 %** absent, 86.76 % colonized.
- **Reconciliation attempted:** tested the full 261-code set (13.59 %), the 255-taxon set (13.24 %), recruits-only (13.24 %), and a tree-size-class-only reading of "tree species" (58.62 %, clearly not the intended sense).
- **Impact (tested):** the looser Discussion statement "~90 %" remains approximately supported (86.8 %); the precise Results figure of 10.5 % is 2.7 pp from the recomputed value, i.e. 6 species.
- **Severity:** **MINOR**
- **Certainty:** MEDIUM (species-set definition is not fully specified in the text). **Misconduct inference: NONE.**
- **Author question:** AQ-4

---
### F-05 — Internal inconsistency in the early-successional species count (37 vs 38)
- **Category:** `REPORTING_INCONSISTENCY`
- **Locations:** p. 9 line 206 ("early-successional taxa (37 spp.)") vs Figure 1 caption p. 37 ("early- (n = 38 spp.)")
- **Claim:** C-25
- **Evidence:** `CROSS_DOCUMENT_MATCH` + `RECOMPUTED`
- **Observed:** 38 early-successional OTUs in the 255-taxon set (36 if the two early-successional planted species, *E. poeppigiana* and *I. edulis*, are excluded).
- **Impact (tested):** descriptive only; the manuscript performs no calculation on this count. Note that neither 37 nor 38 is reachable by a single consistent rule if planted taxa are excluded, which is what the Methods sentence implies.
- **Severity:** **MINOR**
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-5

---
### F-06 — Late-successional species count in Figure 1 caption
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** Figure 1 caption, p. 37
- **Claim:** C-26
- **Reported:** n = 163. **Observed:** 162. **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** with/without planted taxa, with/without the six excluded taxa, and using the 2025 attribute table (158). None yields 163.
- **Impact (tested):** the caption count is a label; Figure 1's curves could not be inspected, so the effect on the plotted result is **not determined**.
- **Severity:** **UNDETERMINED** — the discrepancy is demonstrated, but its effect on the figure was not evaluated because the figure is absent.
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-5

---
### F-07 — Percentage of mid-successional species with small seeds
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** p. 10, lines 214–215
- **Claim:** C-27
- **Reported:** 64 %. **Observed:** 36/52 = **69.2 %** (2024 attribute columns); 35/50 = **70.0 %** (2025 master table). **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** both attribute versions; with and without planted taxa; with and without the six excluded taxa. The companion statistic in the same sentence (71 % of late-successional species with seeds ≥5 mm) **does** reproduce (70.6 %), which argues against a systematic trait-coding difference.
- **Impact (tested):** the sentence's purpose is to establish that successional group and seed size are non-independent. The recomputed value (69.2 %) supports that point at least as strongly as the reported one, so no conclusion changes.
- **Severity:** **MINOR**
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-6

---
### F-08 — Universal claim about planted-species trees is contradicted by the data
- **Category:** `UNSUPPORTED_SCOPE_CLAIM`
- **Location:** p. 14, lines 302–303
- **Claim:** C-28
- **Reported:** "All trees (≥5 cm DBH) of these species in applied nucleation and plantation were planted as part of the initial restoration (Fig 3C)."
- **Observed:** the census contains **17 stems** of planted taxa in the tree size class in those two treatments carrying `Origin = Recruit`: applied nucleation — *E. poeppigiana* 4 (DBH 6.3–27.3 cm) and *I. edulis* 7 (5.0–20.0 cm); plantation — *E. poeppigiana* 4 (5.0–9.5 cm), *I. edulis* 1 (5.8 cm), *V. guatemalensis* 1 (6.5 cm). **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** checked whether these stems are `Measured = Extrapolated` (they are not; all are empirical), and whether excluding the six poor-resolution taxa removes them (it does not).
- **Impact (tested):** 17 of 1,785 planted-taxa tree stems in AN + PL = **0.95 %**. The qualitative point (the tree layer of planted species is overwhelmingly original plantings) survives; the universal quantifier "All" does not.
- **Severity:** **MINOR** (impact tested: <1 % of stems; conclusion direction unchanged)
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Reviewer action:** ask for "All" to be replaced with the exact proportion, or for the basis on which these 17 stems were reclassified.
- **Author question:** AQ-7

---
### F-09 — Share of planted-taxa saplings that were originally planted
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** p. 14, lines 300–301
- **Claim:** C-29
- **Reported:** 60 %. **Observed:** 126 of 193 = **65.3 %** in AN + PL. **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** all-treatment denominator (126/258 = 48.8 %); AN alone (48/105 = 45.7 %); PL alone (78/88 = 88.6 %). None equals 60 %.
- **Impact (tested):** supports the same qualitative statement (a majority of these saplings were original plantings) more strongly, not less. No downstream analysis depends on it.
- **Severity:** **MINOR**
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-7

---
### F-10 — Area file contains a plantation plot that has no census records
- **Category:** `CONFIGURATION_MISMATCH`
- **Locations:** `PlotQuadrantes.csv` row `BBPL`; README §PlotQuadrantes ("all 33 of the sample plots"); manuscript p. 9 line 165 ("plantation n = 8")
- **Claims affected:** C-16 and, potentially, every density result in Figure 3 and Figure S2
- **Evidence:** `RECOMPUTED`
- **Observed:** `PlotQuadrantes.csv` lists 33 plots (NR 9, AN 9, PL 9, RF 6). The census contains 32 (NR 9, AN 9, PL 8, RF 6). `BBPL`, with 243 quadrats, appears only in the area file. The manuscript states plantation n = 8, so the census is the authoritative count.
- **Reconciliation attempted:** confirmed `BBPL` has zero rows in the census under any spelling of the key; confirmed all 32 shared plots agree exactly on quadrat counts, so this is an extra record rather than a systematic mis-keying.
- **Impact (tested, conditional):** if the area file is joined on treatment without first restricting to censused plots, plantation sampling area is 2.0295 ha instead of 1.8108 ha — an inflation of **12.1 %** — which deflates every plantation density by the same factor. Worked example: later-successional tree density in plantation is 47.8 stems/ha with the extra plot and 53.6 stems/ha without it. **Whether the published analysis made this join naively cannot be determined, because the manuscript's code is absent.** The pooled restoration-to-reference ratio (C-16) is affected by <0.5 pp either way and still rounds to 8 %.
- **Severity:** **UNDETERMINED** — the file-level inconsistency is demonstrated and its potential magnitude is quantified, but its actual effect on the published figures was not evaluated.
- **Certainty:** HIGH for the inconsistency; NOT DETERMINED for the effect. **Misconduct inference: NONE.**
- **Reviewer action:** ask which plot set generated the area offsets used in the models.
- **Author question:** AQ-8

---
### F-11 — Family count
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** p. 11, line 248
- **Claim:** C-30
- **Reported:** 65 families. **Observed:** **64** distinct named families in the census (identical for the 261-code and 255-taxon sets; the 2025 master table also lists 64). **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** counting the five taxa with a blank `Family` field as one additional group yields 65, which would reconcile the reported value.
- **Impact (tested):** descriptive only; no analysis is stratified by family.
- **Severity:** **MINOR**
- **Certainty:** MEDIUM. **Misconduct inference: NONE.**
- **Author question:** AQ-9

---
### F-12 — Supplementary material and figures were not supplied
- **Category:** `REPRODUCIBILITY_LIMITATION`
- **Locations:** manuscript references to Tables S1–S4 and Figures S1–S4 (14 in-text citations); Figure captions p. 37
- **Claims affected:** C-33, C-35, C-40
- **Evidence:** `DIRECTLY_INSPECTED` — the supplied PDF is the accepted-manuscript postprint; programmatic inspection found **0 embedded images across all 38 pages**, and no appendix.
- **Impact (tested):** all statistical comparison tables (S3, S4) and all figure-derived claims are unverifiable. This is a **limitation of this audit's inputs**, not a defect of the published article, which carries its figures in the journal version.
- **Severity:** `NOT_APPLICABLE` (audit-scope limitation, not a research finding)
- **Misconduct inference: NONE.**

---
### F-13 — Data-file coding and documentation defects
- **Category:** `DATA_STRUCTURE_ERROR`
- **Location:** `ECOLAPPS_final_Schubert.et.al.2024.csv`
- **Evidence:** `RECOMPUTED` / `DIRECTLY_INSPECTED`
- **Observed:** (a) the file is Latin-1 encoded but the README does not say so, and a standard UTF-8 read fails at byte 137,401; (b) `seed_size` mixes quoted strings (`"1"`, 35,193 rows) with float-formatted values (`1.0`, 550 rows) for the same category, so a naive `groupby` splits categories; (c) `seed_size` contains 16 individuals coded `UNK` and 1 coded `?`, neither documented in the README; (d) five OTUs (`BORAGINACEAE`, `HIRAEA`, `ING_SP1`, `LAU_SP2`, `RUBIACEAE`, 86 individuals) have blank `Family` even though `BORAGINACEAE` and `RUBIACEAE` are themselves family-level identifications present elsewhere in the `Family` column.
- **Reconciliation attempted:** confirmed these are file properties, not import artefacts.
- **Impact (tested):** a reuser who reads the file with default settings either errors out or silently mis-aggregates seed-size categories, splitting up to 1,308 individuals into duplicate groups. No manuscript claim is shown to be affected — all audit recomputations forced a consistent string dtype.
- **Severity:** **MINOR**
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-10

---
### F-14 — Percentage of unidentified individuals excluded
- **Category:** `NUMERICAL_MISMATCH`
- **Location:** p. 10, lines 219–220
- **Claim:** C-31
- **Reported:** 0.04 %. **Observed:** the six poor-resolution taxa excluded by the documented rule total 26 individuals = **0.031 %** of 86,267 (0.031 % of recruits); the taxa lacking any family assignment total 86 individuals = **0.100 %**. **Evidence:** `RECOMPUTED`.
- **Reconciliation attempted:** four candidate exclusion sets and two denominators; none yields 0.04 %.
- **Impact (tested):** at most 86 of 84,326 individuals — below 0.1 % under every candidate definition, so no analysis is materially affected. The manuscript's characterisation ("a small number") holds under all readings.
- **Severity:** **MINOR**
- **Certainty:** MEDIUM (the exclusion set is not fully specified in the text). **Misconduct inference: NONE.**
- **Author question:** AQ-11

---
### F-15 — The three early-successional sapling percentages are not jointly reproducible
- **Category:** `MAPPING_AMBIGUITY`
- **Location:** p. 13, lines 281–282
- **Claim:** C-15 (and the denominator basis of C-13, C-14)
- **Reported:** NR 54.0 %, AN 43.3 %, PL 18.6 %.
- **Observed across seven denominator rules:**

| Rule | NR | AN | PL |
|---|---:|---:|---:|
| all saplings, 255-taxon set | 53.95 | 43.31 | 18.19 |
| all saplings, all 261 codes | 53.95 | **43.30** | 18.19 |
| recruit-origin only | 53.95 | 43.74 | 18.52 |
| excluding the four planted taxa | 52.87 | 43.44 | 18.43 |
| denominator restricted to known successional stage | 57.00 | 43.83 | **18.59** |

- **Evidence:** `RECOMPUTED`
- **Reconciliation attempted:** seven rules (five shown). NR reproduces under six of seven; AN reproduces exactly under the all-saplings rules; PL reproduces only under the known-successional-stage rule, which then breaks NR by 3.0 pp. **No single rule reproduces all three.**
- **Impact (tested):** the maximum deviation of any reported value from its closest recomputation is 0.4 pp, and the ordering NR > AN ≫ PL holds under every rule. The manuscript's conclusion — that compositional differences among restoration treatments in the sapling layer are partly driven by early-successional relative abundance — is unaffected.
- **Severity:** **MINOR** (impact tested)
- **Certainty:** HIGH. **Misconduct inference: NONE.**
- **Author question:** AQ-12

---

## 13. Checked but not raised

The following were examined and produced no finding:

- Class assignment (`seedling`/`sapling`/`tree`) against the stated DBH thresholds — consistent throughout.
- The 789 `ND` placeholder rows — correctly carry zero individuals and do not contaminate any total.
- `Measured = Extrapolated` flag — restricted entirely to planted stems (509 rows), exactly as the README discloses; no recruit record is extrapolated.
- Quadrat counts per plot — all 32 censused plots match `PlotQuadrantes.csv` exactly once the 1,941 off-grid planted-stem records are excluded. The apparent +1 offset in AN and PL plots is fully explained by those records and is **not** a defect.
- Planted species codes — exactly the four species named in the manuscript (`ERY_POE`, `ING_EDU`, `TER_AMA`, `VOC_GUA`).
- Treatment codes and site codes — 10 sites, 4 treatment levels, no stray categories.
- Abstract-to-Results consistency for the census totals and plot replication — consistent.
- Reference-forest quadrat design (four 21×21 m plots at five sites, three at one) — `PlotQuadrantes.csv` gives 196 quadrats at five RF plots and 147 at `RSRF`, matching the Methods exactly.

## 14. Reconciled coverage

```text
Claim ledger (denominator = independently identifiable claims): 43
  Recomputed and matched:                20
  Recomputed and mismatched:             11
  Blocked (evidence absent):              9
  Not checked (feasible, not completed):  2
  Not applicable:                         1
  Total classified:                      43
  Reconciliation: PASS

Distinct findings:                       15
  Findings tied to a claim mismatch:     11
  Findings not tied to a claim:           4   (F-01, F-10, F-12, F-13)

Severity distribution:
  MAJOR:          1   (F-01)
  MINOR:         10   (F-02, F-03, F-04, F-05, F-07, F-08, F-09, F-11, F-13, F-15)
  UNDETERMINED:   2   (F-06, F-10)
  Not a research finding: 2  (F-12 audit-scope limitation; F-14 counted MINOR below)
  — recount: MAJOR 1 + MINOR 11 (incl. F-14) + UNDETERMINED 2 + scope-limitation 1 = 15
  Reconciliation: PASS

File inventory: 9 supplied / 9 classified / 0 unclassified. PASS
Missing required artifacts: 5 identified, 0 supplied.
Census plots: 32 in data / 33 in area file / 32 stated by manuscript.
```

## 15. Separate status architecture

| Dimension | Status |
|---|---|
| Package completeness | `INCOMPLETE` |
| Source execution | `EXECUTION_BLOCKED` (code absent; R runtime also absent) |
| Independent recomputation | `PARTIALLY_RECOMPUTED` (20 of 31 checkable claims matched, 11 mismatched) |
| Computational reproducibility | `BLOCKED` |
| Reporting correspondence | `PARTIALLY_VERIFIED` |
| Empirical data integrity | `NO_DEMONSTRATED_ISSUES` |
| Configuration and model-input integrity | `DEMONSTRATED_ISSUES` (F-10) |
| Methodological quality | `NOT_ASSESSED` — outside this skill's scope |
| Integrity evidence (misconduct) | `NOT_APPLICABLE` — not assessed, not inferred |

## 16. Author queries

| # | Location | Question | Why needed |
|---:|---|---|---|
| AQ-1 | Package root / Open Research Statement | Could `FinalAnalysis_ECOLAPP_Schubert.et.al.R` be deposited, or the Dryad version that contains it be identified? | The README names it but v20251216 does not contain it; without it no inferential result can be verified. |
| AQ-2 | p. 11 ll. 249–250 | Should "94.2 % of individuals" read "94.2 % of taxa"? | The three percentages match OTU counts (246/12/3 of 261) exactly; the individual-level values are 99.85/0.15/0.00. |
| AQ-3 | p. 11–12 ll. 251–253 | Which taxon-exclusion rule produced richness of 156/185/196/205? | Recomputation gives 155/184/195/204 with the documented rule and 156/187/197/206 without it. |
| AQ-4 | p. 12 ll. 254–255 | How was the reference-forest species set defined for the 10.5 % figure? | Recomputation gives 13.24 % (27 of 204 OTUs). |
| AQ-5 | p. 9 l. 206 vs Fig. 1 caption | Is the early-successional count 37 or 38, and is the late-successional count 162 or 163? | The Methods and the figure caption disagree; recomputation gives 38 and 162. |
| AQ-6 | p. 10 ll. 214–215 | What denominator gives 64 % of mid-successional species with small seeds? | Recomputation gives 69.2 % (2024 traits) and 70.0 % (2025 traits). |
| AQ-7 | p. 14 ll. 300–303 | On what basis were the 17 `Origin = Recruit` tree-sized stems of planted species in AN and PL treated as planted, and what denominator gives 60 %? | The data contain those 17 stems, and the sapling proportion recomputes to 65.3 %. |
| AQ-8 | `PlotQuadrantes.csv` | Which plot set generated the sampling-area offsets — the 33 rows in the file or the 32 censused plots? | `BBPL` has no census records; including it inflates plantation area by 12.1 %. |
| AQ-9 | p. 11 l. 248 | Does "65 families" include the group of taxa with no family assignment? | The data contain 64 named families. |
| AQ-10 | Data file | Could the README record the Latin-1 encoding and harmonise `seed_size` coding (mixed string/float, plus `UNK` and `?`)? | Default reads fail or silently split categories. |
| AQ-11 | p. 10 ll. 219–220 | Which records make up the 0.04 % of unidentified, excluded individuals? | Candidate sets give 0.031 % (26 individuals) or 0.100 % (86 individuals). |
| AQ-12 | p. 13 ll. 281–282 | What single denominator produces 54.0 / 43.3 / 18.6 % simultaneously? | No rule among seven tested reproduces all three. |

## 17. Blocked and not-checked register

| ID | Item | Status | Reason | Resolution |
|---|---|---|---|---|
| B-01 | Execution of the manuscript's analysis pipeline | `EXECUTION_BLOCKED` | code absent (F-01); R runtime also absent | supply the ECOLAPP script |
| B-02 | iNEXT completeness 85–99 % (C-32) and Fig. 1 rarefaction/CIs (C-33) | `BLOCKED` | code and result objects absent | supply script + seeds |
| B-03 | NMDS stress 0.17–0.18 (C-34) | `BLOCKED` | code absent; matrix construction rules unspecified | supply script |
| B-04 | PERMANOVA pairwise results, Table S4 (C-35) | `BLOCKED` | supplement not supplied | supply Appendix S1 |
| B-05 | Planted-species survival percentages (C-37) | `BLOCKED` | per-species, per-plot initial planting counts are not in the package. Assuming an equal 4-way split of the stated 86 stems per AN plot yields >100 % survival for *T. amazonia* (105 %) and *V. guatemalensis* (107 %), which demonstrates the equal-split assumption is invalid rather than that the reported survival is wrong. | supply initial planting counts |
| B-06 | Figure 3 significance letters and all significance statements (C-36) | `BLOCKED` | model objects, code and figures absent | supply script + model outputs |
| B-07 | Figures 1–3 published values | `FIGURE_CHECK_BLOCKED` | supplied PDF contains no graphics | supply the typeset article or figure source data |
| B-08 | Comparison with Holl et al. 2017 (C-38) and planting densities from Holl et al. 2011 (C-39) | `BLOCKED` | values live in external prior publications | out of package scope |
| N-01 | Independent Chao-dissimilarity / NMDS reimplementation (C-41) | `NOT_CHECKED` | technically feasible in Python; the abundance-matrix construction rules exist only in the missing code, so an independent implementation would test my assumptions rather than the authors' | complete as follow-up once code is available |
| N-02 | Independent rarefaction / coverage estimation (C-42) | `NOT_CHECKED` | feasible; outside completed audit scope | complete as follow-up |
| NA-01 | `Cartesian.*.csv` spatial analyses (C-43) | `NOT_APPLICABLE` | these files and the supplied R script belong to the Applied Vegetation Science manuscript | — |

## 18. Limitations

1. **No source execution occurred.** Every "match" below the level of a raw count is an independent recomputation from the census file using definitions read out of the manuscript. Where the manuscript's definitions are ambiguous (F-03, F-04, F-15), a mismatch may reflect my reading rather than an error by the authors.
2. **The supplied manuscript is a text-only postprint.** No figure, table, or appendix content was available; 9 of 43 claims are blocked partly for this reason.
3. **The package is a later Dryad version** (16 Dec 2025) extended for a second manuscript. Earlier versions may have contained the ECOLAPP script. This audit characterises v20251216 only.
4. **Statistical inference was not audited at all.** No model specification, seed, or output for this manuscript was available, so nothing in this report speaks to whether the reported significance results are correct.
5. **Trait attributions** were tested against both the embedded 2024 columns and the 2025 master table; the manuscript's own version is not separately archived.
6. **No misconduct assessment was performed or is implied.** Every finding is a correspondence observation.

## 19. Output-validation result

| Check | Result |
|---|---|
| Every supplied file inventoried | PASS (9/9) |
| Completeness denominators documented | PASS (§4.2) |
| Every identifiable claim has a stable ID | PASS (C-01…C-43, including blocked/not-checked) |
| Mappings evidence-backed | PASS |
| Source execution vs independent recomputation kept separate | PASS (§9 vs §10) |
| Figure-code mapping separate from published-figure provenance | PASS (§11; no provenance claimed) |
| Every severity has a tested impact basis or is UNDETERMINED | PASS |
| Coverage counts reconcile | PASS (§14, 43 = 20+11+9+2+1) |
| Affected cells vs distinct findings use separate denominators | PASS (43 claims vs 15 findings) |
| Methodological notes kept separate | PASS (`NOT_ASSESSED`) |
| No misconduct inference or publication verdict | PASS |
| Output A / Output B / ledger built from the same records | PASS |

**Output validation: PASS**

---
*Companion documents: `dryad_s7h44j1gc_eap3053_review_brief.md` (Output B), `dryad_s7h44j1gc_eap3053_audit_ledger.json` (machine-readable ledger).*
