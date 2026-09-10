# Paper Claim Audit Report

**Date**: 2026-09-10
**Skill**: paper-claim-audit (`.github/skills/paper-claim-audit/skill.md`)
**Auditor**: GPT-5.3-Codex, high reasoning effort (fresh, zero-context thread
— no prior conversation, no prior audit outputs, only the extracted
manuscript text), substituting for the skill's specified
`mcp__codex__codex` (gpt-6-astra, ultra reasoning) reviewer backend, which is
unavailable in this environment. Same substitution pattern used for the
prior `experiment-audit_report.md` and `academic-paper-reviewer_review.md`
in this folder.
**Paper**: Liao, Y. et al., "Chromosomal translocation-derived aberrant
Rab22a drives metastasis of osteosarcoma", *Nature Cell Biology* (2020) —
text extracted from the manuscript PDF to
`supporting-files/manuscript_extracted.txt`.

## Overall Verdict: 🚫 BLOCKED

Per the skill's verdict decision table: *"Numeric claims detected, no raw
result files found → `BLOCKED`, reason_code: `no_raw_evidence`."* This
paper's primary quantitative evidence (RNA-seq, WGS, per-sample
fusion-validation calls, per-mouse tumor-volume/survival records) is
deposited externally at **SRA accession SRP181860** and was not retrieved
for this audit — there is no local `results/*.json|csv`, `outputs/*`, or
`config.yaml`-equivalent file to trace any claim against. This is **not**
itself evidence of misconduct — it reflects that this skill's design target
(a paper + adjacent raw-result files in the same repository) does not exist
for this externally-deposited wet-lab dataset. It does, however, mean the
core claim-to-raw-evidence verification this skill exists to perform could
not be completed, and the paper's numeric claims remain formally unverified
against primary data as far as this audit package is concerned.

Within that constraint, the reviewer still performed the one check that
*is* possible from text alone — **internal cross-referencing**: does a
number restated in a different section of the same manuscript agree with
itself, and does stated arithmetic (subgroup counts, percentages, unit
conversions) hold up. Two internal issues surfaced from that check (see
below) that are independent of the missing-raw-evidence limitation.

## Claims Verified: 32 total

| Status | Count |
|---|---|
| exact_match | 14 |
| rounding_ok | 1 |
| ambiguous_mapping | 2 |
| missing_evidence | 12 |
| number_mismatch | 1 |
| scope_overclaim | 2 |
| not_applicable | 0 |

## Issues Found

### [WARN] Claim #C30: Unit inconsistency in iRGD dosing (mg/kg vs mg/ml)
- **Location**: Methods (in-vivo drug administration) vs. Extended Data
  Figure 10 caption
- **Paper says**: Methods states iRGD peptide was administered at
  "1 mg kg⁻¹ or 10 mg kg⁻¹"; the Extended Data Fig. 10 caption instead
  states "1 mg/ml and 10 mg/ml" for what appears to be the same treatment
  arms.
- **Evidence shows**: mg/kg (a dose per body weight) and mg/ml (a solution
  concentration) are not interchangeable units — this is either a
  typographical error in one location or an underspecified dosing protocol
  (concentration of stock solution vs. administered dose per animal weight
  are both needed and are not the same number).
- **Status**: `number_mismatch` (unit-level, not necessarily a numeric
  fabrication)
- **Fix**: Reconcile the two passages — confirm whether 1/10 refers to
  mg/kg dose, mg/ml stock concentration, or both (in which case both units
  should be stated together, e.g. "X mg/ml stock administered at Y mg/kg").

### [INFO] Claim #C22: Replicate-count variation across a related assay set
- **Location**: Extended Data Fig. 10 legend, panels c–f (n=3) vs. panel g
  (n=4)
- **Paper says**: Panels within the same figure, testing closely related
  migration/invasion outcomes, report n=3 for most panels and n=4 for one.
- **Evidence shows**: This is not inherently wrong (an extra replicate can
  legitimately be added to one assay), but the manuscript text does not
  explain why one panel in an otherwise-matched set has a different
  replicate count.
- **Status**: `ambiguous_mapping`
- **Fix**: Add a one-line clarification in the legend or Methods for why
  panel g used n=4 while adjacent panels used n=3.

### [ADVISORY] Claim #C03 / #C12: Scope-overclaim language
- **Location**: Title/Abstract ("drives metastasis of osteosarcoma");
  Results, cross-cancer generalization sentence ("occur and drive
  metastasis in multiple cancer types")
- **Paper says**: General, disease-wide and pan-cancer causal framing.
- **Evidence shows**: The clinical-positive evidence base cited elsewhere in
  the same text is a 2/37 (5.4%) fusion-positive metastatic-osteosarcoma
  subgroup, and the cross-cancer claim is supported by only 2 clinical
  cases plus 2 cell lines in Results. This corroborates the identical
  scope-vs-claim finding already documented independently in this folder's
  `experiment-audit_report.md` (Check E).
- **Status**: `scope_overclaim` (advisory — a framing/precision issue, not a
  numeric error)
- **Fix**: Qualify the general claim to specify it is based on a rare
  fusion event found in a small subset of screened patients, consistent
  with the wording already recommended in `experiment-audit_report.md`.

## Internal Arithmetic Checks (all passed)
- 2/37 = 5.4054% → correctly rounds to the stated "5.4%". ✅
- 37 (metastatic subgroup) + 60 (non-metastatic subgroup) = 97 (total
  screened cohort) — consistent everywhere the total is restated. ✅
- 2 (fusion-positive) + 35 (fusion-negative) = 37 (metastatic subgroup) —
  consistent. ✅
- 1.5 cm³ = 1,500 mm³ tumor-volume cutoff — correct unit conversion,
  consistent across all four locations where it is restated. ✅
- Epitope span "residues 68–82" = 15 amino acids (82 − 68 + 1 = 15),
  consistent with the manuscript's own "15-mer synthesized peptide" label. ✅

## All Claims (detailed)

| # | Location | Paper Value | Evidence Check | Status |
|---|----------|-------------|-----------------|--------|
| C01 | Intro | 60–70% 5-yr survival; 20% metastatic | external epidemiology, no local file | missing_evidence |
| C02 | Abstract | fusion breakpoint aa 1–38; chr20 | needs sequence file | missing_evidence |
| C03 | Title/Abstract | "drives metastasis of osteosarcoma" (general claim) | vs. 2/37 clinical-positive subgroup | scope_overclaim |
| C04 | Results | 6 fusion transcripts identified (NeoF1–6) | needs fusion-caller output | missing_evidence |
| C05 | Results + Methods | 97 clinical samples screened | restated identically in Methods | exact_match |
| C06 | Results | 1 NeoF1-positive + 1 NeoF6-positive case | needs per-sample validation record | missing_evidence |
| C07 | Results | 2/37 = 5.4% | internal arithmetic | rounding_ok |
| C08 | Results | 60/60 non-metastatic samples negative | internal cross-check | exact_match |
| C09 | Results | 37 + 60 = 97 | internal arithmetic | exact_match |
| C10 | Results | median survival 9.5 vs 19 months | needs patient-level survival data | missing_evidence |
| C11 | Results | 2 + 35 = 37 | internal arithmetic | exact_match |
| C12 | Results | "occur and drive metastasis in multiple cancer types" | vs. 2 cases + 2 cell lines cited | scope_overclaim |
| C13 | Results vs Methods | "two cases of breast cancer" vs "four tumour samples" | not explicitly reconciled in text | ambiguous_mapping |
| C14 | Results | coding sequence 186 amino acids | needs ORF/sequence file | missing_evidence |
| C15 | Results + Methods | epitope residues 68–82 = 15-mer peptide | internal arithmetic (15 aa) | exact_match |
| C16 | Fig. 1–7 legends | n=3 biologically independent experiments (repeated) | consistent across comparable panels | exact_match |
| C17 | Fig. 1 legend + Methods | orthotopic model n=6 mice | matches Methods "six mice per group" | exact_match |
| C18 | Fig. 2 legend + Methods | in-vivo groups n=6 | matches Methods | exact_match |
| C19 | Fig. 2 legend | RT-qPCR/WB/migration n=3 | consistent with same-class assays | exact_match |
| C20 | Fig. 3 legend + Methods | in vitro n=3; orthotopic n=6 | matches Methods | exact_match |
| C21 | Fig. 8 legend + Methods | 143B-Luc n=8; ZOS-M-Luc n=6 | within Methods' stated "6–8 mice per group" range | exact_match |
| C22 | Ext. Data Fig. 10 | panels c–f n=3; panel g n=4 | unexplained within-figure variation | ambiguous_mapping |
| C23 | Methods | specimens collected 2014–2017 | no local file to check | missing_evidence |
| C24 | Methods + Reporting Summary | 6 GB / 90 GB clean sequencing data per sample | restated identically | exact_match |
| C25 | Methods + Reporting Summary | TopHat parameters (p8, stdev80, max-intron 100000, min-dist 100000, anchor-length 13) | restated identically | exact_match |
| C26 | Methods | 50 nM siRNA, 48 h harvest | no local raw protocol log | missing_evidence |
| C27 | Methods | RT-qPCR 10 μl reaction, triplicate | no local raw run sheet | missing_evidence |
| C28 | Methods | 2,000 cells/well, 24 h readout | no local raw assay output | missing_evidence |
| C29 | Methods | inocula doses + n=6 mice/group | no local animal-run sheet | missing_evidence |
| C30 | Methods vs Ext. Data Fig. 10 | iRGD "mg/kg" (Methods) vs "mg/ml" (caption) | unit inconsistency between two mentions | number_mismatch |
| C31 | Methods + Ext. Data (×4 locations) | cutoff 1,500 mm³ = 1.5 cm³ | correct unit conversion, consistent everywhere | exact_match |
| C32 | Data Availability | SRA accession SRP181860; per-figure source data pointer | external data, not provided to this audit | missing_evidence |

## Files in this audit

- `paper-claim-audit_report.md` — this report
- `paper-claim-audit_report.json` — machine-readable version
- `supporting-files/manuscript_extracted.txt` — full extracted manuscript
  text (evidence trail), already present in this folder from the earlier
  `experiment-audit` and `exploratory-data-analysis` runs

## Note on Skill/Target Fit

Consistent with the other two skills already run against this paper
(`experiment-audit`, `exploratory-data-analysis`), this is a repository-wide
pattern for this particular target: `paper-claim-audit`, `experiment-audit`,
and `exploratory-data-analysis` are all designed around a *local
computational research package* (paper `.tex`/PDF + adjacent raw result
files in the same repo). This paper only has the manuscript itself locally
available; its raw evidence lives in an external public archive (SRA). All
three audits reach the same underlying conclusion through their own
lens — data provenance cannot be independently re-verified locally, so each
audit is scoped to (a) disclosing that limitation explicitly and (b)
performing the maximum verification actually possible from the manuscript
text alone (internal arithmetic/consistency checks here; structural/content
statistics in the EDA report; scope and statistical-rigor assessment in the
experiment audit).
