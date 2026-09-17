# Experiment Audit Report

**Date**: 2026-09-16
**Auditor**: External cross-model reviewer, high reasoning (read-only)
**Reviewer-Model**: `gpt-5.4` (self-declared; cross-family relative to the executor)
**Executor-Model**: `claude-opus-5` (path collection + report transcription only — did **not** participate in the integrity judgement)
**Skill**: `experiment-audit` (`.claude/commands/experiment-audit.md`)
**Project / subject**: Wang, Yuan, Xu et al. 2019, *Nature Cell Biology* `s41556-019-0416-0` — "ZNFX1 is a novel mitochondrial dsRNA sensor..." + author-deposited Source Data Fig. 1–7

---

## Overall Verdict: FAIL

## Integrity Status: fail

> This verdict reflects **material source-data incompleteness and panel/metadata inconsistencies**. It is **not** an allegation of misconduct. Many deposited values do reproduce the reported statistics exactly.

---

## Reviewer Backend Note (deviation from skill default, recorded for the record)

The skill's default `REVIEWER_BACKEND = codex` (`mcp__codex__codex`) and its `manual` alternative
(`mcp__manual_review__review`) are **both unavailable as MCP tools in this session**. To install the
default backend:

```
claude mcp add codex -- npx -y @openai/codex-mcp
```

Rather than emit `REVIEW_UNAVAILABLE`, the audit was routed to an **independent cross-family
reviewer agent** run read-only, receiving the skill's **verbatim** A–F audit prompt plus an explicit
wet-lab domain translation. This preserves the skill's core principle — *the executor collects file
paths, the reviewer reads the artifacts and judges* — but it is **not** the canonical MCP backend.
The reviewer self-declared as `gpt-5.4` rather than the requested `gpt-5.6-sol`; the identity is
cross-family relative to the Claude executor, so the cross-model requirement holds, but the exact
model routing was not under executor control. Treat the verdict as valid-but-non-canonical.

---

## Domain Mapping (ML checklist → wet-lab molecular biology)

| Check | Wet-lab meaning applied |
|---|---|
| A. Ground truth provenance | Provenance of qPCR housekeeping references, blot loading controls, mock/untreated, IgG, siRNA and empty-vector controls |
| B. Score normalization | Fold-change/control normalization, relative densitometry, controls fixed at exactly 1 |
| C. Result file existence | Correspondence between manuscript panels, deposited sheets/images, sample sizes, means, SDs and *P* values |
| D. Dead code | Unreported/orphan conditions and assays; absence of analysis code prevents true dead-code analysis |
| E. Scope | Biological/technical replication, cell lines, animals, viruses vs. generalization language |
| F. Evaluation type | Independent physical assay = `real_gt`; internally normalized relative assay = `self_supervised_proxy`; visual scoring = `human_eval` |

---

## Source-Data Inventory

### XLSX workbooks

Each workbook contains exactly one visible, non-hidden sheet; no hidden rows/columns.

| File / sheet | Dimensions | Contents and panel mapping |
|---|---:|---|
| `Source Data Fig 1.xlsx:Sheet1` | A1:K81; 400 numeric cells | Fig. 1b time-course qPCR; 1e tissue expression/infection; 1f HIV datasets; 1g SIV datasets; 1h IFN time courses; 1j ruxolitinib; 1k *Ifnar1* knockout; 1l promoter reporters |
| `Source Data Fig 2.xlsx:Sheet1` | A1:M72; 353 numeric cells | Fig. 2a FACS; 2b plaque titres; 2d knockout FACS; 2e rescue; 2g IFN-β ELISA; 2h viral qPCR; 2i/j IFN-β ELISA |
| `Source Data Fig 3.xlsx:Sheet1` | A1:T41; 180 numeric cells | Fig. 3a viral RNA; 3b *Ifnb1*; 3c serum IFNs; 3f survival-count sequence |
| `Source Data Fig 7.xlsx:Sheet1` | A1:K105; 424 numeric cells | Fig. 7a/b qPCR; 7c viral loads; **partial** 7e; 7f heatmap values; **partial** 7g; 7h qPCR; 7i/j FACS |

### Blot PDFs

- `Source Data Fig 4.pdf` — 1 page, 17 embedded images; extractable labels for Fig. 4b,c,f,g,h
- `Source Data Fig 5.pdf` — 1 page, 16 embedded images; extractable labels for Fig. 5b,g,h,i,j,k,l
- `Source Data Fig 6.pdf` — 1 page, 36 embedded images; extractable labels for Fig. 6a,c,d,e,f,g,i,j,k

Not image-only, but their text layers carry **panel/protein/molecular-weight labels, not numerical
measurements**. Pixel-level blot duplication, splicing, contrast and lane forensics are **out of
scope** here and require a separate image-forensics pass.

---

## Checks

### A. Ground Truth Provenance: WARN

**Evidence**
- qPCR normalized to β-actin within each sample, `2^-ΔΔCt` — `manuscript_extracted.txt:2738-2745`
- Luciferase: Firefly ÷ Renilla — `manuscript_extracted.txt:2759-2760`
- Fig. 1 uses untreated/time-zero, muscle, healthy-control and empty-vector references — `Source Data Fig 1.xlsx:Sheet1:B3:K6,B9:K12,B27:K45,C59:H66,C69:K81`
- Fig. 5 includes IgG and input controls — `manuscript_extracted.txt:921-953,1750-1769`
- Blots identify GAPDH, β-actin, Lamin B1 or COX IV controls — Source Data Fig 4/6 PDFs, page 1

**Details** — Controls are conventional and generally independently motivated; **no comparator was
shown to be circularly derived from a scored experimental output**. Plaque titres and ELISAs are the
closest to independent physical standards. However, raw Ct values, standard curves, FACS event
files/gates, ELISA absorbances and blot quantification are all absent, so reference stability and
control quality cannot be independently checked.

### B. Score Normalization: WARN

**Evidence** — Numerous deposited reference groups are exactly `1.000` for every replicate:

| Panel | Cells |
|---|---|
| Fig. 1b time zero | `Source Data Fig 1.xlsx:Sheet1:B4:B6,G4:G6` |
| Fig. 1e uninfected tissues | `Sheet1:C15:E24` |
| Fig. 1j/k baselines | `Sheet1:C59:H59,C64:H64` |
| Fig. 1l empty vector | `Sheet1:C69:C81,H69:H81` |
| Fig. 2h all uninfected values | `Source Data Fig 2.xlsx:Sheet1:B50:C52,F50:G52,B57:C60,F57:G60` |
| Fig. 3a/b PBS | `Source Data Fig 3.xlsx:Sheet1:D3:K3,D6:K6,D11:K11,D14:K14` |
| Fig. 7a/b empty vector | `Source Data Fig 7.xlsx:Sheet1:C3:C8,D11:D35` |

**Details** — Setting a calibrator to 1 is **normal for `2^-ΔΔCt` reporting** and is not evidence of
fraudulent normalization. But fixing *every* control replicate at exactly 1 removes visible
control-group variance, and testing fold-change values rather than the underlying ΔCt values can
understate uncertainty. Raw Ct/ΔCt and raw Firefly/Renilla readings are unavailable, so those
analyses are not independently reproducible. Absolute ELISA/plaque/FACS measurements are present for
some panels, which prevents a blanket normalization FAIL.

### C. Result File Existence: FAIL

**Reconciliations that PASS** (sample SD, Excel-style equal-variance two-tailed unpaired *t*-test):

| # | Panel | Recomputed | Reported | Evidence |
|---|---|---|---|---|
| 1 | Fig. 1f ZNFX1/HIV | ctrl 0.0000006 ± 0.19350 (n=9) vs HIV 0.45465 ± 0.47008 (n=14) → *P* = 0.012325 | 0.0123 | `Fig 1.xlsx:Sheet1:B28:C41`; `manuscript_extracted.txt:443,594-595` |
| 2 | Fig. 1g SIV ZNFX1 | 7.96237 ± 0.23385 vs 9.32450 ± 0.36133 (n=18) → *P* = 3.7716×10⁻¹⁵ | 3.77×10⁻¹⁵ | `Sheet1:H28:I45`; `:444,596` |
| 3 | Fig. 1j, 4 h | untreated 6.6927 ± 0.5718 vs ruxolitinib 3.9106 ± 0.5972 → *P* = 0.004318 | 0.0043 | `Sheet1:C60:H60`; `:529` |
| 4 | Fig. 2a A549 6 h | 23.685 ± 3.628 % vs 42.383 ± 6.770 % → *P* = 0.002799 | 0.0028 | `Fig 2.xlsx:Sheet1:E3:E6,G3:G6`; `:843-847` |
| 5 | Fig. 2h VSV | WT 1618.11 ± 215.98 vs KO 5634.90 ± 1163.84 → *P* = 0.0041869 | 0.0042 | `Sheet1:D50:E53`; `:862-869` |
| 6 | Fig. 3a lung | WT 3531.86 ± 599.13 vs KO 9756.33 ± 666.99 → *P* = 8.6907×10⁻⁶ | 8.69×10⁻⁶ | `Fig 3.xlsx:Sheet1:D4:K4`; `:1067` |
| 7 | Fig. 3c VSV IFN-β | WT 1376.8 ± 215.89 vs KO 269.05 ± 104.48 (n=8) → *P* = 3.1219×10⁻⁹ | matches | `Sheet1:D20:S20`; `:1071` |
| 8 | Fig. 7i / 7j | 22.65 ± 0.86 vs 32.97 ± 3.10 % → *P* = 0.005121; 30.95 ± 1.81 vs 40.20 ± 1.56 % → *P* = 0.002555 | 0.0051 / 0.0026 | `Fig 7.xlsx:Sheet1:F98:G100,F103:G105`; `:2524-2525` |

**Demonstrated or material correspondence failures:**

1. **Fig. 3f survival sample-size conflict** — legend states *n* = 10 mice/group (`manuscript_extracted.txt:1083-1085`), but deposited values never exceed 5 animals and appear as survival counts `5,5,…,3` and `5,5,…,1` (`Source Data Fig 3.xlsx:Sheet1:B32:C41`). Individual event/censoring records are absent, so the stated Gehan–Breslow–Wilcoxon *P* = 0.0283 **cannot be recomputed**.
2. **Fig. 2h replication mismatch** — legend says *n* = 3 (`:910`), but H1N1 and HSV-1 each contain **four** values per group (`Source Data Fig 2.xlsx:Sheet1:D57:E60,H57:I60`). The reported H1N1 *P* ≈ 4.24×10⁻⁵ requires all four values, so this is not merely an unused extra row.
3. **Fig. 7c label conflict** — legend says "wild-type or *Mda5*−/−" (`:2537`), whereas deposited groups are *Rig-I*−/− and *Mda5*−/− (`Source Data Fig 7.xlsx:Sheet1:B38:K43`). The first source-data group cannot be unambiguously mapped to the stated WT panel.
4. **Fig. 7e incomplete** — described as statistical analysis of repeated FACS for EV, ZNFX1, RIG-I and MDA5 conditions (`:2538-2540`), but source data contain only EV/uninfected and EV+VSV values for WT, *Rig-I*−/− and *Mda5*−/− (`Sheet1:I48:K58`). Treatment-group means, SDs and *P* values cannot be reproduced.
5. **Fig. 7g incomplete** — the EV, infection and ZNFX1 conditions (`:2475-2495,2541-2542`) are represented by only EV and EV+VSV columns (`Sheet1:I61:K67`); the ZNFX1 condition is **missing**.
6. **Whole quantitative panel families absent** — no replicate-level source for Fig. 4a–e/i, Fig. 5b–f, or Fig. 6j. The Fig. 4–6 PDFs provide uncropped images, not the numbers needed to reproduce means, SDs or *P* values.
7. **Extended Data source data absent from this package**, despite the availability statement asserting source data for Figs. 1–7 **and Extended Data Figs. 1–7** (`:2859-2863`).
8. **Fig. 3d "80 % conjunctivitis" has no animal-level source table** (`:219`).

### D. Dead Code Detection: WARN

No statistical scripts, analysis/evaluation code, experiment tracker, configuration files or
machine-readable run records exist anywhere in the supplied package. Function invocation, versioned
analysis state and "DONE" status therefore **cannot be checked at all**.

Potential orphan / unresolvable data:
- Second "HSV-1 high" row in Fig. 2g (`Source Data Fig 2.xlsx:Sheet1:B45:L46`) is not distinguishable in the extracted panel labels.
- Anomalous Fig. 7c value `Source Data Fig 7.xlsx:Sheet1:G40 = 4176.8590572`, roughly **tenfold below** its neighbouring replicates 45,515 and 42,553. May be genuine or a dropped digit; not resolvable without raw records.

### E. Scope Assessment: WARN

Evidence spans four cell lines, primary macrophages/PBMCs, mouse cohorts, HIV/SIV observational
datasets and several viruses (`manuscript_extracted.txt:165-219,2715-2730`) — broader than a
single-assay study.

Nevertheless, most mechanistic estimates use only *n* = 3 independent experiments; **one** mouse
strain and **one** main in-vivo RNA-virus challenge; HSV-1 is the principal DNA-virus negative
comparator. Therefore "essential", "specifically restricts RNA viruses", "broad anti-RNA-viral
spectrum", "immediately", and the therapeutic extrapolation (`:80-84,165,194,614,2197-2202`) require
qualification. "Conserved" rests primarily on sequence analysis (`:2173-2181`), not conserved
functional tests across species.

### F. Evaluation Type: mixed — `real_gt` + `self_supervised_proxy` + `human_eval` + `simulation_only` (PASS)

| Class | Assays |
|---|---|
| `real_gt` | Plaque titres, calibrated ELISA concentrations, FACS percentages, animal survival |
| `self_supervised_proxy` | Relative qPCR, reporter ratios, normalized RIP-seq/heatmaps, qualitative blot comparisons |
| `human_eval` | Unblinded conjunctivitis / histopathology interpretation; no blinding performed (`:3033-3037`) |
| `simulation_only` | Promoter/site prediction, phylogenetic / in-silico analyses |
| `synthetic_proxy` | **Not identified** |

---

## Action Items

1. Release raw Ct/ΔCt values, Firefly and Renilla readings, ELISA absorbances/standard curves, plaque counts, and FCS files with gates.
2. Correct or explain the Fig. 2h *n* = 3 statement versus four deposited replicates.
3. Supply individual survival times/censoring for all claimed Fig. 3f *n* = 10 animals and rerun the stated survival test.
4. Resolve the Fig. 7c WT versus *Rig-I*−/− label conflict, and verify cell `G40`.
5. Deposit complete Fig. 7e/7g treatment groups and numerical data for Figs. 4–6.
6. Supply the Extended Data statistical source data promised by the availability statement.
7. Release the Excel/Prism analysis tables or scripts, software settings, multiple-comparison decisions, and an experiment/run ledger.
8. Analyse qPCR on ΔCt values; report fold changes for presentation only.
9. Run a separate blinded pixel-level blot/image forensics pass.

---

## Claim Impact

| ID | Claim | Manuscript ref | Impact |
|---|---|---|---|
| C1 | ZNFX1 is induced by viral infection / IFN | `:112-147` | **supported** (raw Ct unavailable) |
| C2 | ZNFX1 deficiency enhances RNA-virus replication in vitro | `:165-194` | **supported** for tested systems/viruses |
| C3 | ZNFX1 has a broad, RNA-virus-specific antiviral spectrum | `:194,614` | **needs_qualifier** — 3 RNA viruses, principally 1 DNA-virus comparator |
| C4 | ZNFX1 is essential for host defence in mice | `:1078` | **needs_qualifier** — one strain/challenge, incomplete survival records, *n* conflict |
| C5 | 80 % of knockout mice developed conjunctivitis | `:219` | **not_verifiable** — animal-level observations absent |
| C6 | ZNFX1 directly binds viral RNA and prefers long RNA | `:921-953` | **needs_qualifier** — Fig. 5b–f quantitative source missing; "direct" strongest only for purified-protein competition |
| C7 | ZNFX1 localizes to mitochondria and interacts with MAVS | `:2048-2094` | **supported** qualitatively; no image forensics performed |
| C8 | Signalling is independent of RIG-I / MDA5 | `:2095-2122` | **needs_qualifier** — Fig. 7c label conflict, Fig. 7e/g incomplete |
| C9 | ZNFX1 acts "immediately" as an early sensor | `:81-84,2163-2169` | **needs_qualifier** — limited time-course; temporal primacy not established |
| C10 | ZNFX1 may provide an early therapeutic strategy | `:2197-2202` | **unsupported** as a therapeutic claim — no intervention/efficacy/toxicity experiment |

---

## Limits of This Audit

Covers only the supplied text, spreadsheets and PDF text/image inventories. It does **not**
authenticate biological samples, establish whether replicates were truly independent, inspect
laboratory notebooks, retrieve GEO accessions, reanalyse raw sequencing, inspect FCS files, validate
antibody specificity, or perform **pixel-level image forensics**. Plot means/error bars could not
always be read numerically from text extraction. Missing data make several findings
**"not verifiable", not demonstrated false**. Nothing here asserts misconduct or intent.

Backend caveat: the canonical `codex` / `manual-review` MCP reviewer backends were unavailable; see
the *Reviewer Backend Note* above.
