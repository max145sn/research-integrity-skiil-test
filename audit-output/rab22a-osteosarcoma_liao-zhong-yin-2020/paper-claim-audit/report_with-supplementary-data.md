# Paper Claim Audit Report (with supplementary data)

**Date**: 2026-09-10
**Skill**: paper-claim-audit (`.github/skills/paper-claim-audit/skill.md`)
**Auditor**: Fresh zero-context reviewer sub-agent, no prior conversation and
no prior audit outputs supplied as context — substituting for the skill's
specified `mcp__codex__codex` (gpt-6-astra, ultra reasoning) backend, which
is unavailable in this environment. Same substitution pattern used for the
prior `report_without-supplementary-data.md` in this folder and for the
other skill outputs in this paper's folder.
**Inputs supplied to this run**:
1. `../supporting-files/manuscript_extracted.txt` — the manuscript, Liao,
   Y. et al., "Chromosomal translocation-derived aberrant Rab22a drives
   metastasis of osteosarcoma", *Nature Cell Biology* (2020).
2. `../supporting-files/supplementary_data_extracted.txt` — the
   "supplementary data.pdf" file supplied by the user for this paper,
   extracted text of a "Supplementary Materials" document (Figures S1–S9).

## Overall Verdict: 🚫 BLOCKED

Per the skill's verdict decision table: *"Numeric claims detected, no raw
result files found → `BLOCKED`, reason_code: `no_raw_evidence`."* Adding the
supplementary document does not change this: it contains only figure
captions (assay descriptions, sample sizes, ratios, percentages), not raw
result files (no `results/*.json|csv`, `outputs/*`, or `config.yaml`
equivalents) — so, as with the manuscript-only run, the core claim-to-raw-
evidence trace this skill exists to perform remains blocked for both
documents.

### ⚠️ Identity check (carried over from prior audits in this folder, re-confirmed here)

Before extracting claims, this run re-ran the skill's Step 0-equivalent
identity check on the two supplied documents, since a "supplementary data"
file is only actually evidence *for this manuscript* if it is that
manuscript's own supplementary information:

| | Manuscript | Supplied "supplementary data.pdf" |
|---|---|---|
| Title | "Chromosomal translocation-derived aberrant Rab22a drives metastasis of osteosarcoma" | "Rab22a-NeoF1 fusion protein promotes osteosarcoma lung metastasis through its secretion into exosomes" |
| Authors (order) | Dan Liao, Li Zhong, Junqiang Yin, Cuiling Zeng, Xin Wang, Xingchuan Huang, Jinna Chen, Hong Zhang, Ruhua Zhang, Xin-Yuan Guan, Xintao Shuai, Jianhua Sui, Song Gao, Wuguo Deng, Yi-Xin Zeng, Jing-Nan Shen, Jian Chen, Tiebang Kang | Li Zhong, Dan Liao, Jingjing Li, Wenqiang Liu, Jingxuan Wang, Cuiling Zeng, Xin Wang, Zhiliang Cao, Ruhua Zhang, Miao Li, Kuntai Jiang, Yi-Xin Zeng, Jianhua Sui, Tiebang Kang |
| Correspondence authors | Jing-Nan Shen, Jian Chen, Tiebang Kang | Tiebang Kang, Jianhua Sui |

**Verdict: `DIFFERENT_PUBLICATION`.** Titles, author rosters, and
correspondence-author sets all differ. The two documents share overlapping
authors (Liao, Zhong, Zeng, Wang, Zhang, Sui, Zeng, Kang appear in both) and
identical fusion-protein/cell-line nomenclature (RAB22A-NeoF1, 143B, ZOS-M,
U2OS), consistent with a closely related follow-on paper from an overlapping
author group — but it is not this manuscript's own Supplementary
Information. This is the same finding already logged as **F-05** in
`../research-package-integrity-audit2/integrity-audit_with-supplementary-data.md`;
it is repeated here because it directly limits what this audit can claim
about the supplementary document's evidentiary relationship to the
manuscript's claims (they cannot be used to cross-verify each other's
numbers as main-text/supplement pairs, only compared as two independent
documents).

## Claims Verified: 45 total (32 manuscript + 13 supplementary)

| Status | Count |
|---|---|
| exact_match | 14 |
| rounding_ok | 1 |
| ambiguous_mapping | 4 |
| missing_evidence | 21 |
| number_mismatch | 1 |
| scope_overclaim | 2 |
| not_applicable | 2 |

The manuscript-only rows (C01–C32) are unchanged from
`report_without-supplementary-data.md`, reproduced here for a single
consolidated ledger. New rows (S01–S13) cover the supplementary document.

## Issues Found

### [WARN] Claim #C30: Unit inconsistency in iRGD dosing (mg/kg vs mg/ml)
- **Location**: Methods (in-vivo drug administration) vs. Extended Data
  Figure 10 caption (manuscript)
- Unchanged from the manuscript-only audit — see
  `report_without-supplementary-data.md` for full detail. Not present in,
  or resolved by, the supplementary document (which does not discuss iRGD
  dosing at all).

### [INFO] Claim #C22: Replicate-count variation across a related assay set (manuscript)
- Unchanged from the manuscript-only audit.

### [ADVISORY] Claim #C03 / #C12: Scope-overclaim language (manuscript)
- Unchanged from the manuscript-only audit.

### [ADVISORY] Claim #S05a: Unexplained mouse-count variation within Figure S1
- **Location**: Supplementary Figure S1, panels (a) and (c–f)
- **Supplementary document says**: Panel (a) "n = 5 biologically independent
  mice"; panels (c–f) "n = 5 biologically independent mice" — these agree.
  However, Figure S5 (below) shows the same kind of pattern with a real
  discrepancy.
- **Status**: `not_applicable` (checked, no discrepancy found in S1 itself;
  listed for completeness since it was the comparison point for the S5
  finding below)

### [WARN] Claim #S05: Unexplained mouse-count variation within Figure S5
- **Location**: Supplementary Figure S5, panel (a) vs. panels (b) and (c–f)
- **Supplementary document says**: Panel (a): "n = 4 biologically
  independent mice"; panel (b): "n = 5 biologically independent mice";
  panels (c–f): "n = 3 biologically independent mice." All three panel
  groups describe closely related orthotopic/tail-vein lung-metastasis
  pre-education experiments using the same cell lines and readout
  (bioluminescence / IVIS / H&E / nodule counts).
- **Evidence shows**: Three different sample sizes (n=3, 4, 5) appear across
  panels of what reads as one coherent experimental series in a single
  figure, with no stated reason for the difference (e.g., attrition,
  a priori power calculation, or a deliberately smaller pilot group).
- **Status**: `ambiguous_mapping`
- **Fix (author question)**: Clarify why panel (a) used n=4, panel (b) used
  n=5, and panels (c–f) used n=3 mice for what appear to be parallel arms of
  the same pre-education/metastasis assay.

### [ADVISORY] Claim #S03/S08: KFERQ-like motif position differs between NeoF1 and NeoF2-6 without explanation
- **Location**: Supplementary Figure S3(d) vs. Figure S8(a)
- **Supplementary document says**: Fig. S3(d), for RAB22A-NeoF1: "four
  KFERQ-like motifs (aa52-56, aa59-63, aa102-106 and aa137-142)". Fig.
  S8(a), for RAB22A-NeoF2-6: "the KFERQ-like motif (aa52-57)" (singular,
  one motif, and a different residue span — 52-57 rather than 52-56 — from
  the first motif listed for NeoF1).
- **Evidence shows**: This is plausible (NeoF1 and NeoF2-6 are described
  elsewhere as distinct fusion transcripts with different sequences past
  the shared Rab22a portion, so a differing motif count/position is not
  inherently an error), but the text does not explain the discrepancy
  between "52-56" (NeoF1) and "52-57" (NeoF2-6) for what is otherwise
  labelled as the same type of degradation-targeting motif.
- **Status**: `ambiguous_mapping`
- **Fix (author question)**: Confirm whether the one-residue difference in
  motif boundary (52-56 vs 52-57) between Fig. S3d and Fig. S8a is
  intentional (reflecting true sequence differences between the fusion
  variants) or a transcription/labelling inconsistency.

### [ADVISORY] Claim #S01g: Multiple co-injection ratios reported without a stated rationale
- **Location**: Supplementary Figure S1(g)
- **Supplementary document says**: "mice orthotopically injected
  U2OS/MTX300-Luc cells alone or with either ZOS-M-shNC cells or
  ZOS-M-shRAB22A-NeoF1 cells at the indicated 10:1 and 10:2 ratios."
- **Evidence shows**: Two different co-injection ratios (10:1 and 10:2) are
  used within the same panel without the caption stating why both were
  tested (e.g., a dose-response design) — plausible but not stated.
- **Status**: `ambiguous_mapping`
- **Fix (author question)**: State whether 10:1 and 10:2 were tested as a
  dose-response series and, if so, whether both ratios are shown or only
  one was carried forward to later figures.

## Internal Arithmetic / Consistency Checks

**Manuscript (unchanged from prior run, all passed):**
- 2/37 = 5.4054% → correctly rounds to the stated "5.4%". ✅
- 37 (metastatic) + 60 (non-metastatic) = 97 (total screened cohort). ✅
- 2 (fusion-positive) + 35 (fusion-negative) = 37 (metastatic subgroup). ✅
- 1.5 cm³ = 1,500 mm³ tumor-volume cutoff, consistent across 4 mentions. ✅
- Epitope span "residues 68–82" = 15 amino acids, consistent with "15-mer" label. ✅

**Supplementary document (new, internal to the S1–S9 figure set only):**
- Replicate counts of "n = 3 biologically independent experiments" recur
  consistently for in-vitro biochemistry/imaging panels across Figs.
  S2–S4, S6, S7, S9 — internally consistent. ✅
- Replicate counts of "n = 5 biologically independent mice" recur
  consistently for most in-vivo bioluminescence panels across Figs. S1,
  S3, S4, S6, S7 — internally consistent, **except** Fig. S5 (see finding
  S05 above) and Fig. S6(f,g) which use "n = 4 biologically independent
  mice" without explanation for the difference from the more common n=5. ⚠️
- Density-gradient percentages "12–36%" and "5%–40%" (Fig. S2e,f) are
  distinct, clearly-labelled gradient protocols for two different panels —
  no internal conflict. ✅

## All Claims (detailed)

### Manuscript claims (C01–C32) — unchanged, see `report_without-supplementary-data.md` for the full table.

### Supplementary-document claims (new, S01–S13)

| # | Location | Claim | Evidence Check | Status |
|---|----------|-------|-----------------|--------|
| S01 | Title/authors | Title and author list of supplied "supplementary data.pdf" | Compared to manuscript title/authors | `not_applicable` (identity check, not a numeric claim — see verdict above: `DIFFERENT_PUBLICATION`) |
| S02 | Fig. S1(a) | n = 5 biologically independent mice (bioluminescence) | No raw result file; internally consistent with other S1 panels | missing_evidence |
| S03 | Fig. S1(b) | n = 3 biologically independent experiments (migration/invasion) | No raw result file | missing_evidence |
| S04 | Fig. S1(c–f) | n = 5 biologically independent mice; 1:1 co-injection ratio | No raw result file; consistent with S1(a) | missing_evidence |
| S05 | Fig. S1(g) | 10:1 and 10:2 co-injection ratios | No stated rationale for two ratios | ambiguous_mapping |
| S06 | Fig. S2(b) | n = 8 fields (Pearson correlation coefficients) | No raw result file | missing_evidence |
| S07 | Fig. S2(e,f) | 12–36% and 5%–40% iodixanol density gradients; n = 3 experiments | Two distinct, clearly-labelled protocols, no conflict | exact_match (internally self-consistent) |
| S08 | Fig. S3(d) | KFERQ-like motifs at aa52-56, aa59-63, aa102-106, aa137-142 (NeoF1) | Compared to Fig. S8(a) motif position for NeoF2-6 | ambiguous_mapping |
| S09 | Fig. S3(g) | n = 5 biologically independent mice | Consistent with other n=5 panels | exact_match |
| S10 | Fig. S5(a) vs (b) vs (c–f) | n = 4 vs n = 5 vs n = 3 mice, same experimental series | Unexplained replicate-count variation | ambiguous_mapping |
| S11 | Fig. S6(f,g) | n = 4 biologically independent mice | Differs from the more common n=5 elsewhere in the document, unexplained | ambiguous_mapping |
| S12 | Fig. S8(a) | KFERQ-like motif at aa52-57 (NeoF2-6) | Compared to Fig. S3(d) motif position for NeoF1 | ambiguous_mapping (same pair as S08) |
| S13 | Figs. S2–S4, S6, S7, S9 | n = 3 biologically independent experiments (recurring) | Internally consistent across all in-vitro panels checked | exact_match |

## Files in this audit

- `report_with-supplementary-data.md` — this report
- `report_with-supplementary-data.json` — machine-readable version
- `../paper-claim-audit/report_without-supplementary-data.md` /
  `.json` — the prior manuscript-only run, reused verbatim for the
  C01–C32 rows above
- `../supporting-files/manuscript_extracted.txt` — full extracted
  manuscript text
- `../supporting-files/supplementary_data_extracted.txt` — full extracted
  text of the supplied "supplementary data.pdf"

## Note on Skill/Target Fit and Scope

As with the manuscript-only run and the other skills already run against
this paper, this skill is designed around a local computational research
package (paper + adjacent raw result files in the same repository). Neither
document supplied here contains raw result files — the manuscript's primary
evidence is deposited externally (SRA accession SRP181860), and the
supplementary document is itself only figure captions with no underlying
data table, spreadsheet, or code. Adding the supplementary document
therefore does not change the verdict from `BLOCKED`; what it adds is (a) a
second, larger set of numeric claims that could be checked for **internal**
consistency (the S01–S13 rows above), and (b) confirmation, independent of
the earlier `research-package-integrity-audit2` run, that the supplied
supplementary document is not actually this manuscript's own Supplementary
Information (`DIFFERENT_PUBLICATION`).
