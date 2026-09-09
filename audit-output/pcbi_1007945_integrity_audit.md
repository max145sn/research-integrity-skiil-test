# Research Package Integrity Audit

**Skill applied:** `research-package-integrity-audit2` (`.github/skills/research-package-integrity-audit2/skill.md`)
**Package audited:** Ayala MJC, Villela DAM (2020). "Early transmission of sensitive strain slows down
emergence of drug resistance in Plasmodium vivax." *PLOS Computational Biology* 16(6):e1007945.
https://doi.org/10.1371/journal.pcbi.1007945

## Execution-mode disclosure

This audit was performed as a single-session, sequential inspection by one model instance, not by
independently instrumented, contract-validated deterministic scripts as the skill's "Implementation
Guidance" describes for a mature deployment. R was not available in the execution environment
(`Rscript`/`R` not found), so **no code execution occurred**; all checks below are `DIRECTLY_INSPECTED`
or `CROSS_DOCUMENT_MATCH` unless explicitly marked otherwise. No values in this report should be read as
"reproduced" in the skill's technical sense.

---

## Part 0: Preflight and Scope Declaration

**Supplied files:**

| File | Role | Readable |
|---|---|---|
| `file.pdf` (main manuscript, 2.29 MB) | Manuscript | Yes (text extracted) |
| `pcbi.1007945.s001.Rmd` (32.2 KB, 780 lines) | Supplementary code (S1 File per manuscript) | Yes |

**Not supplied but referenced by the manuscript:**
- **S2 File** ("Document... generated from code in S1... to reproduce simulation and figures", PDF) — not supplied. This is the authors' own rendered output of the S1 Rmd; without it, independent code execution is the only way to check S1's output, and execution is blocked (see below).
- Code/data for the Latin Hypercube Sampling (LHS) sensitivity analysis described in the Results ("we performed a sensitivity analysis... using LHS... implemented in R using deSolve, lhs, and sensitivity packages") underlying **Fig 5** — not present anywhere in the supplied S1 Rmd.

**Execution environment:** No R/Rscript installed in this session. `deSolve`, `latex2exp`, `lhs`, `sensitivity` package availability could not be checked. **Execution status: BLOCKED for the entire package.**

**Preflight status: PARTIAL.** Only 2 of the package's referenced artifacts were supplied (manuscript + one supplementary code file), and the runtime needed to execute that code is unavailable.

---

## Part 1: File Inventory and Study/Figure Map

This is a single-study, deterministic-simulation paper (two compartmental ODE models; no empirical
raw data, no human/animal subjects data, no machine-learning components). Phase 4 (data provenance),
Phase 5's ML module, and most of Phase 7's statistical-recomputation catalogue are **NOT_APPLICABLE** —
there is no dataset to check for duplication, missingness, or leakage. The applicable checks are the
**simulation/computational-model module** (Phase 5) and **figure/parameter correspondence** (Phase 8).

The manuscript reports 5 figures. Mapping each to the supplied S1 Rmd by caption/section-header match:

| Figure | Manuscript caption (short) | S1 Rmd section | Mapping status |
|---|---|---|---|
| Fig 1 | *P. falciparum* model diagram | none (static illustration) | `NOT_APPLICABLE` (not code-generated) |
| Fig 2 | *P. vivax* model diagram | none (static illustration) | `NOT_APPLICABLE` (not code-generated) |
| Fig 3 | Drug coverage vs. R0, sensitive/resistant | `## Fig 3. Drug coverage varying the basic reproduction numbers` (R0 function + 8-panel plot, lines 1–197) | `CONFIRMED` (caption text is reproduced verbatim as the chunk header) |
| Fig 4 | Simulation of 4 treatment regimens (CQ, CQ+PQ, ACT, ACT+PQ), both species | `##Fig 4. Simulation of treatment regimens` (`falciP`/`vivax` ODE functions + `regimen_fal`/regimen-vivax simulation, lines 198–780) | `CONFIRMED` |
| Fig 5 | Parameter sensitivity (LHS) on resistance-emergence time | **absent from S1** | `BLOCKED_MISSING_CODE` — no code or LHS output data supplied for this figure |

---

## Part 2: Parameter Ledger — Code vs. Manuscript Table 1/Table 2

The R0 function in the S1 Rmd takes a 19-element parameter vector, explicitly indexed in a code
comment (`# (1) Nm, (2) Nh, (3) a, (4) b, (5) mm, (6) alpha, (7) cs, (8) ca, (9) sigma, (10) psi,
(11) mvl, (12) phit, (13) phiu, (14) varphi, (15) epsilon, (16) nu, (17) n, (18) gamma, (19) r`).
Two fixed vectors are defined for Fig 3/Fig 4: `parf` (*P. falciparum*) and `parv` (*P. vivax*).
Each element was cross-checked, where the manuscript's Table 1 or Table 2 gives a specific reported
value (`DIRECTLY_INSPECTED` + `CROSS_DOCUMENT_MATCH`; "range" entries in Table 1 are not point values
and cannot mismatch a specific code constant, so they are marked `NOT_APPLICABLE`):

| # | Param | `parf` (falciparum) | Table 1/2 value (falciparum) | Match | `parv` (vivax) | Table 1/2 value (vivax) | Match |
|---|---|---|---|---|---|---|---|
| 1 | Nm | 2435 | 2435 | ✅ | 2435 | 2435 | ✅ |
| 2 | Nh | **624** | **625** (`m = Nm/Nh (dimensionless) = 2435/625`) | ❌ **C-01** | **624** | **625** | ❌ **C-01** |
| 3 | a | 0.21 | 0.21 | ✅ | 0.21 | 0.21 | ✅ |
| 4 | b | 0.5 | 0.5 | ✅ | 0.5 | 0.5 | ✅ |
| 5 | μm | 0.033 | 0.033 | ✅ | 0.033 | 0.033 | ✅ |
| 6 | α (cost) | 0.28 | range 0–0.6 | N/A (range) | 0.28 | range 0–0.6 | N/A (range) |
| 7 | cs | 0.4 | 0.4 | ✅ | 0.4 | 0.4 | ✅ |
| 8 | ca | 0.12 | 0.12 | ✅ | 0.12 | 0.12 | ✅ |
| 9 | σ | 0.9 (σf) | 0.9 | ✅ | 0.33 (σv) | 0.33 | ✅ |
| 10 | ψ | 0 | N/A for falciparum (no hypnozoites) | N/A | 1/60 | 1/60 | ✅ |
| 11 | μvl | 1 | N/A for falciparum | N/A | 1/425 | 1/425 | ✅ |
| 12 | φt | 0 | N/A for falciparum | N/A | **0.29** | **0.21** | ❌ **C-02** |
| 13 | φu | 0 | N/A for falciparum | N/A | 0.9 | range 0.4–0.9 | ✅ (in range) |
| 14 | φ (varphi) | 0.5 | 0–1 (varied param) | ✅ (baseline) | 0.5 | 0–1 | ✅ (baseline) |
| 15 | ε | 11 | 11 days (CQ, falciparum, Table 2) | ✅ | 2.1 | 2.1 days (CQ, vivax, Table 2) | ✅ |
| 16 | ν | 1/10¹² | 10⁻¹² (CQ, Table 2) | ✅ | 1/10¹² | 10⁻¹² | ✅ |
| 17 | n | 1 | 1 | ✅ | 1 | 1 | ✅ |
| 18 | γ | 1/2 (γf) | 1/2 | ✅ | 1/9 (γv) | 1/9 | ✅ |
| 19 | r | 1/287 (rf) | 1/287 | ✅ | 1/60 (rv) | 1/60 | ✅ |

**16 of 19 elements match the reported Table 1/2 values exactly** for each species vector (or are
within a stated range); **2 distinct values are inconsistent** with the manuscript's own tables
(`C-01`, `C-02`).

---

## Part 3: Detailed Findings

### Finding F-01 — `Nh` in code (624) does not match Table 1's reported value (625)

- **Category:** `CODE_DATA_MISMATCH` / `REPORTING_INCONSISTENCY`
- **Location:** manuscript Table 1, row "m — Mosquitoes per human, N_m/N_h = 2435/625"; S1 Rmd, `parf<-c(2435,624,...)` and `parv<-c(2435,624,...)`.
- **Evidence status:** `DIRECTLY_INSPECTED`, `CROSS_DOCUMENT_MATCH`
- **Certainty:** `DEMONSTRATED` (both values are unambiguous, plain numeric literals; "625" does not appear anywhere else in the manuscript as an alternative population figure, and "624" never appears in the manuscript at all)
- **Innocent explanations tested:**
  - *Rounding* — not applicable; both are exact integers, off by 1.
  - *Internal self-consistency with initial conditions* — **plausible partial explanation**: in the Fig 4 simulation code, initial conditions are `Sh=623, Is=1` (falciparum) and the analogous vivax split, which sum to `Nh=624`. The R0 fixed-parameter vectors (`parf`, `parv`) reuse this same `624` for consistency with the ODE initial state used later in the same script, rather than the `625` ratio quoted in Table 1. This does not eliminate the discrepancy — the R0 curves in Fig 3 are computed from `Nh=624`, not the `625` the paper reports as the model's human-population parameter — but it indicates the mismatch likely originates from reusing an initial-condition-derived constant rather than a transcription slip.
- **Impact:** Affects the R0 formula's `Nm/Nh` ratio (`m`) used to generate all 8 panels of Fig 3, and the `m <- Nm/Nh` term inside both ODE functions used for Fig 4. The effect size is small (624 vs. 625 is a 0.16% relative difference in `m`) and very unlikely to be visually or qualitatively detectable in the published figures, but the code's constant does not equal the value stated in the paper's own parameter table.
- **Misconduct inference:** NONE.
- **Author question:** "Table 1 reports N_h = 625, but both `parf` and `parv` in the supplied S1 Rmd use `Nh = 624` (matching the sum of the Fig 4 initial conditions `Sh=623 + Is=1`). Could you confirm which value (624 or 625) was actually used to generate the published Fig 3, and clarify whether Table 1 or the code should be corrected?"

### Finding F-02 — `φt` (post-treatment latent probability) in the *P. vivax* code (0.29) does not match Table 1's reported value (0.21)

- **Category:** `CODE_DATA_MISMATCH` / `REPORTING_INCONSISTENCY`
- **Location:** manuscript Table 1, row "ϕt — Probability of post-treatment human of remaining with latent parasites = 0.21 [58]"; S1 Rmd, `parv<-c(...,0.29,...)` (12th element).
- **Evidence status:** `DIRECTLY_INSPECTED`, `CROSS_DOCUMENT_MATCH`
- **Certainty:** `DEMONSTRATED` — "0.29" does not appear anywhere in the extracted manuscript text (verified by full-text search), and "0.21" is the only φt value ever stated.
- **Innocent explanations tested:**
  - *Rounding* — no; not a rounding of 0.21 or any other reported figure.
  - *Different regimen/table row* — Table 2 (treatment-regimen-specific parameters) does not list φt at all; φt is only given once, in Table 1, as a single point value (not a range like φu). No alternative reported value of 0.29 exists elsewhere in the paper to reconcile against.
  - *OCR/extraction artifact* — the manuscript PDF was extracted to text and the digit sequence for φt was unambiguous ("0.21 [58]"); could not be independently confirmed against the original PDF glyphs beyond the extraction pass performed here, so a residual, low-probability OCR-adjacent error on the manuscript side cannot be fully excluded, but no textual evidence supports it.
- **Impact:** φt is a fixed baseline parameter feeding every *P. vivax* R0 panel in Fig 3 (1b–4b) and the vivax branch of the R0 formula. Because R0 was not independently recomputed here (no R runtime), the quantitative effect on the published curve shapes is `NOT_CHECKED`; only the parameter-value mismatch itself is `DEMONSTRATED`.
- **Misconduct inference:** NONE.
- **Author question:** "Table 1 gives ϕt = 0.21, but the `parv` vector in S1 Rmd (element 12) uses ϕt = 0.29. Which value was used to generate the published *P. vivax* R0 curves (Fig 3, panels 1b–4b), and should Table 1 or the code be corrected?"

---

## Part 4: Checked but Not Raised

- **α (resistance cost) = 0.28** in both `parf`/`parv`: Table 1 only states a range (0–0.6); 0.28 is a valid baseline choice within range and is exactly what the Fig 1a/1b loop varies from 0.1–0.6, so this is consistent with the described methodology. Not raised.
- **φu = 0.9** in both vectors: Table 1 gives a range (0.4–0.9); 0.9 is the upper bound of that range and plausible as a chosen baseline. Not raised.
- **ε (epsilon) and ν values** (11/2.1 days; 10⁻¹²): match Table 2's CQ-regimen row exactly for both species. Not raised.
- **γ, r, ψ, μvl, cs, ca, a, b, Nm, n**: all match Table 1/2 exactly for both species. Not raised.
- **ψ, μvl, φt, φu = 0** in the falciparum vector (`parf`): the *P. falciparum* model has no latent/hypnozoite compartment per the manuscript's own model description (Fig 1 caption), so zeroing these vivax-only parameters for falciparum is expected model structure, not a data-integrity issue. Not raised.

---

## Part 5: Coverage Report

```text
Files supplied: 2 (manuscript, S1 Rmd)
Files referenced but missing: 2 (S2 File document, LHS sensitivity-analysis code/data for Fig 5)

Figures identified: 5
  Mapped (code present, caption-matched): 2 (Fig 3, Fig 4)
  Not applicable (static diagrams): 2 (Fig 1, Fig 2)
  Blocked - missing code: 1 (Fig 5)
Figures regenerated: 0 (execution blocked — no R runtime available)
Figures numerically checked only: 0
Figures parameter-cross-checked via direct inspection: 2 (Fig 3, Fig 4, via the parameter ledger above)

Parameter values checked against manuscript tables: 19 x 2 vectors = 38 cells
  Confirmed match: 32
  Not applicable (range values): 4
  Not applicable (species-inapplicable, zeroed): 4 (overlaps with N/A count above; falciparum-only cells)
  Demonstrated mismatch: 2 (F-01, F-02)

Executions attempted: 0 (BLOCKED — R/Rscript not available in this environment)
Independent recomputations: 0 (BLOCKED, same reason)
```

---

## Part 6: Verdict Architecture

- **Package completeness:** `PARTIALLY_COMPLETE` — main manuscript and the primary supplementary code file (S1) are present; the S2 rendered-output document and the Fig 5 sensitivity-analysis code/data are not.
- **Computational reproducibility:** `BLOCKED` — no R runtime was available in this environment; the supplied Rmd was never executed, so no figure was `EXECUTED`, `RECOMPUTED`, or `REPRODUCED_WITH_ENVIRONMENTAL_ADAPTATION`. This is a limitation of the audit environment, not a demonstrated property of the code itself.
- **Reporting correspondence:** `MINOR_DISCREPANCIES` — 2 of 19 cross-checkable fixed-parameter values in the supplied code do not match the manuscript's own Table 1 (F-01, F-02); all other checkable values match.
- **Data-integrity evidence:** `NOT_ASSESSED` — this is a deterministic simulation study with no empirical dataset in the supplied package; Phase 4's data-integrity checks do not apply.

---

## Part 7: Ready-to-Send Author Queries

1. Table 1 reports N_h = 625, but both `parf` and `parv` parameter vectors in the supplied S1 Rmd use N_h = 624 (which matches the sum of the Fig 4 initial conditions, Sh=623 + Is=1). Could you confirm which value was used to generate the published Fig 3 R0 curves, and reconcile the table and code?
2. Table 1 reports ϕt = 0.21, but the `parv` vector (12th element) in S1 Rmd uses ϕt = 0.29 for all *P. vivax* R0 panels (Fig 3, 1b–4b). Which value reflects what was actually used to generate the published figure?
3. The manuscript references an "S2 File" (a rendered document produced from the S1 code) and a Latin Hypercube Sampling sensitivity analysis underlying Fig 5, using additional R packages (`lhs`, `sensitivity`) not invoked anywhere in the supplied S1 Rmd. Could the code/data used to generate Fig 5 be supplied, to allow that figure to be checked?

---

## Part 8: Machine-Readable Ledger

```yaml
package: pcbi.1007945
files:
  - path: file.pdf
    role: manuscript
    readable: true
  - path: pcbi.1007945.s001.Rmd
    role: code
    manuscript_ref: "S1 File"
    readable: true
  - path: "S2 File (rendered document)"
    role: documentation
    status: MISSING_FILE
  - path: "Fig 5 sensitivity-analysis code/data (LHS)"
    role: code
    status: MISSING_FILE

figure_map:
  - figure: Fig1
    mapping_status: NOT_APPLICABLE
  - figure: Fig2
    mapping_status: NOT_APPLICABLE
  - figure: Fig3
    code_section: "R0 chunk, lines 1-197"
    mapping_status: CONFIRMED
  - figure: Fig4
    code_section: "simulation chunk, lines 198-780"
    mapping_status: CONFIRMED
  - figure: Fig5
    mapping_status: BLOCKED_MISSING_CODE

findings:
  - finding_id: F-01
    category: CODE_DATA_MISMATCH
    location: "Table 1 (Nh=625) vs parf/parv[2] (Nh=624)"
    severity: MINOR
    certainty: DEMONSTRATED
    evidence_status: [DIRECTLY_INSPECTED, CROSS_DOCUMENT_MATCH]
    reported: 625
    in_code: 624
    innocent_explanations_tested: [rounding, initial_condition_consistency]
    misconduct_inference: NONE
  - finding_id: F-02
    category: CODE_DATA_MISMATCH
    location: "Table 1 (phit=0.21) vs parv[12] (phit=0.29)"
    severity: MINOR
    certainty: DEMONSTRATED
    evidence_status: [DIRECTLY_INSPECTED, CROSS_DOCUMENT_MATCH]
    reported: 0.21
    in_code: 0.29
    innocent_explanations_tested: [rounding, alternate_table_row, ocr_artifact]
    misconduct_inference: NONE

blocked_checks:
  - reason: "No R/Rscript runtime available"
    affected_phases: [Phase6_execution, Phase7_recomputation, Phase8_figure_regeneration]
  - reason: "Fig 5 sensitivity-analysis code/data not supplied"
    affected_phases: [Phase2_study_map, Phase8_figure_correspondence]

verdict:
  package_completeness: PARTIALLY_COMPLETE
  computational_reproducibility: BLOCKED
  reporting_correspondence: MINOR_DISCREPANCIES
  data_integrity_evidence: NOT_ASSESSED
```
