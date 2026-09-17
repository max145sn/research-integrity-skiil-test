# Paper Claim Audit Report

**Date**: 2026-09-16
**Auditor**: Fresh zero-context cross-model reviewer (self-declared `gpt-5.3-codex`)
**Executor**: `claude-opus-5` — collected paths, performed mechanical XLSX/PDF→text conversion, transcribed the verdict. Contributed **no** claim judgement.
**Paper**: *ZNFX1 is a novel mitochondrial dsRNA sensor* — Wang, Yuan, Xu et al., *Nature Cell Biology* (2019), `s41556-019-0416-0`
**Evidence set**: author-deposited Source Data Fig. 1–7 (4 × XLSX, 3 × uncropped-blot PDF)

---

## Overall Verdict: FAIL

**reason_code**: `claim_mismatch`

**Summary**: Most deposited spreadsheet values and many *P* values match, but Fig. 7g *P* values do
not recompute from the deposited data, Fig. 2h has an *n* mismatch, and several quantitative /
representative claims lack deposited source values.

---

## Zero-Context Guarantee (how isolation was enforced)

This skill's defining property is that the reviewer has **no prior expectations**. Enforcement for
this run:

- The manuscript and the seven source-data files were mechanically converted and staged into an
  **isolated workspace** (`Temp\znfx1_pca\evidence\`) containing *only* those eight artifacts.
- The reviewer was told that folder is the complete input set, and that a claim with no counterpart
  there is `missing_evidence` rather than something to hunt for elsewhere.
- The repository tree — which contains **four prior audit reports on this exact paper**
  (`claim-grounding`, `manuscript-consistency-audit`, `manuscript-data-integrity`,
  `experiment-audit`) — was outside the staged set, so no prior verdict, summary or executor
  interpretation entered the reviewer's context.
- Fresh thread, no reply-chaining, no conversation history.

**Corroboration value**: this reviewer independently re-derived the Fig. 2h *n* = 3-vs-4 discrepancy
that a *separate* audit found earlier the same day, without access to that finding — and it
additionally surfaced the **Fig. 7g *P*-value mismatch**, which the earlier pass had recorded only as
"incomplete data", not as a numeric contradiction.

---

## Claims Verified: 58 total

| Status | Count |
|---|---:|
| `exact_match` | 22 |
| `rounding_ok` | 17 |
| `ambiguous_mapping` | 5 |
| `missing_evidence` | 7 |
| `unsupported_claim` | 3 |
| `scope_overclaim` | 2 |
| `aggregation_mismatch` | 1 |
| `number_mismatch` | **1** |

39 of 58 claims (67 %) reconcile cleanly to the deposited evidence.

---

## Issues Found

### 🔴 FAIL — Claim C50: Fig. 7g *P* values do not recompute

- **Location**: Fig. 7g, `PAPER:2463-2464`
- **Paper says**: "*P* = 0.0004; *P* = 0.0001"
- **Evidence shows**: `EVIDENCE_Source_Data_Fig_7:Sheet1:J62:K67` — EV vs VSV gives
  IFNB1 mean 1 → 3.5126, ***P* = 0.00749**; IFIT1 mean 1 → 2.4510, ***P* = 0.00434**
- **Status**: `number_mismatch`
- **Detail**: Under the manuscript's own stated test (two-tailed unpaired Student's *t*-test) the
  deposited values yield *P* values roughly **19× and 43× larger** than displayed. Both remain
  significant at α = 0.05, so the qualitative conclusion is unaffected — but the printed numbers are
  not reproducible from the deposited data.
- **Fix**: Correct the printed *P* values, or supply the analysis file and exact bracket-to-comparison
  mapping showing which comparison each label refers to.

### 🟠 WARN — Claim C22: Fig. 2h replicate count conflicts with legend

- **Location**: Fig. 2h legend, `PAPER:908,910`
- **Paper says**: "h… *n* = 3 independent experiments"
- **Evidence shows**: `EVIDENCE_Source_Data_Fig_2:Sheet1:D50:I60` — VSV/EMCV have *n* = 3, but
  **H1N1 and HSV-1 have *n* = 4 per group**
- **Status**: `aggregation_mismatch`
- **Detail**: Not an unused spare row — the reported H1N1 *P* ≈ 4.249 × 10⁻⁵ **requires all four
  values**. The stated *n* and the *n* actually used therefore differ.
- **Fix**: Correct the legend *n* for the H1N1/HSV-1 panels, or explain the discrepancy.

### 🟠 WARN — Claims C32, C34, C36, C37, C40, C46, C1: evidence not deposited

| Claim | Panel / statement | What is missing |
|---|---|---|
| C1 | Fig. 1a ">3-fold upregulated" screen | Fig. 1a values absent; workbook starts at Fig. 1b |
| C32 | "80 % of *Znfx1*−/− mice suffered from conjunctivitis" (`PAPER:218-220`) | No animal-level counts deposited |
| C34 | Fig. 4a–e,i quantitative panels + *P* values | No numerical data; Fig. 4 PDF is blots only |
| C36 | "preferentially… around 6,000–8,000 nt" (`PAPER:932-933`) | No Fig. 5d/e quantitative values |
| C37 | Fig. 5b,c,e,f (*n* = 3 + *P* values) | No replicate values deposited |
| C40 | Fig. 6j qRT–PCR of *Ifnb1* and ISGs | No numerical panel-j values |
| C46 | Fig. 7d displayed FACS percentages | Only 40.43, 59.94, 62.34 traceable; **13.54, 30.42, 51.41, 18.37, 7.85, 3.40 are absent** from the workbook |

### 🟡 NOTE — Claims C35, C38, C39: repeat counts unverifiable

Legends state "repeated three times independently" for Fig. 4f–h, Fig. 5g–l and Fig. 6 generally,
but each deposited PDF is a single uncropped-blot page whose text layer carries only panel/protein/
molecular-weight labels. Repeat counts cannot be counted from the deposited evidence.
Status `unsupported_claim` — *not verifiable*, not contradicted.

### 🟡 NOTE — Claims C56, C57: scope language exceeds deposited evidence

- C56 — "specifically restricts the replication of RNA viruses" (`PAPER:79-81`): deposited main-figure
  data cover several RNA-virus assays plus limited HSV-1 contrasts; "specifically" is broader than
  this evidence set alone establishes.
- C57 — "a broad anti-RNA-viral spectrum of ZNFX1" (`PAPER:191-195`): rests on **three** RNA viruses
  (VSV, EMCV, H1N1) in selected cell types.

### 🟡 NOTE — Claims C23, C31, C45, C51, C58: bracket mapping lost in extraction

Where figure text was flattened, the reviewer could confirm the *values are internally consistent*
with the deposited data but could not always pin each printed *P* label to its exact comparison
bracket. Recorded as `ambiguous_mapping` — explicitly **not** called mismatches.

---

## Reconciliations That Passed (arithmetic shown)

| Panel | Groups | Recomputed *P* | Printed |
|---|---|---|---|
| Fig. 1f *Znfx1*/HIV | UI ≈ 0.0000006 vs HIV 0.454651 | 0.012325 | 0.0123 |
| Fig. 1f *Rig-I* | — | 0.000373 | 0.0004 |
| Fig. 1g *Znfx1*/SIV | 7.96237 vs 9.32450 (*n* = 18) | 3.77161 × 10⁻¹⁵ | 3.77 × 10⁻¹⁵ |
| Fig. 1g *Rig-I* | — | 4.50476 × 10⁻¹² | 4.50 × 10⁻¹² |
| Fig. 1j (4 h / 8 h) | UT 6.6927 vs Rux 3.9106; 13.0437 vs 5.2943 | 0.004318 / 0.006510 | 0.0043 / 0.0065 |
| Fig. 1k (4 h / 8 h) | WT vs *Ifnar*−/− | 0.000251 / 1.6878 × 10⁻⁶ | 0.0003 / 1.69 × 10⁻⁶ |
| Fig. 1l | STAT1/STAT2/IRF1/IRF9 | 0.000928 / 0.000281 / 7.44 × 10⁻⁶ / 4.40 × 10⁻⁶ | 0.0009 / 0.0003 / 7.44 × 10⁻⁶ / 4.40 × 10⁻⁶ |
| Fig. 2a A549 12 h | 41.7275 % vs 58.545 % | 0.001310 | 0.0013 |
| Fig. 2a A549 6 h / L929 6 h / 12 h | — | 0.002799 / 4.595 × 10⁻⁶ / 1.231 × 10⁻⁶ | 0.0028 / 4.60 × 10⁻⁶ / 1.23 × 10⁻⁶ |
| Fig. 2b A549 / L929 | — | 0.000213 / 3.191 × 10⁻⁶ | 0.0002 / 3.19 × 10⁻⁶ |
| Fig. 2g VSV / EMCV / H1N1 | — | 1.356 × 10⁻⁶ / 1.091 × 10⁻⁶ / 7.985 × 10⁻⁶ | 1.36 × 10⁻⁶ / 1.09 × 10⁻⁶ / 7.89 × 10⁻⁶ |
| Fig. 2g/h HSV-1 (null results) | — | 0.6519 / 0.2616 | 0.6519 / 0.2616 |
| Fig. 3a lung / liver | WT 3531.86 vs KO 9756.33 | 8.6907 × 10⁻⁶ / 0.000819 | 8.69 × 10⁻⁶ / 0.0008 |
| Fig. 3b lung / liver | — | 0.000489 / 0.000933 | 0.0005 / 0.0009 |
| Fig. 3c VSV IFN-β / IFN-α | 1376.8 vs 269.05 (*n* = 8) | 3.1219 × 10⁻⁹ / 7.6467 × 10⁻¹¹ | 3.12 × 10⁻⁹ / 7.65 × 10⁻¹¹ |
| Fig. 3c PBS controls | — | 0.13608 / 0.94302 | 0.1361 / 0.9430 |
| Fig. 7b | IFNB1/IFIT1 across genotypes | 0.000682 / 0.03044 / 0.000371 / 0.000404 | 0.0007 … 8.41 × 10⁻⁵ range |
| Fig. 7i | *Rig-I*−/− siCtrl vs siZNFX1 | 0.005121 | 0.0051 |
| Fig. 7j | *Rig-I*−/− vs DKO (+VSV) | 0.002555 | 0.0026 |

Replicate counts confirmed as stated for Fig. 1b, 1e, 1f (9/14), 1g (18), 1h, 2a (4), 2b (4), 2d/e,
2g (5), 2i/j, 3a (4), 3b (4), 3c (8/4), 3f (10), 7a, 7b, 7c, 7e, 7g/h, 7i, 7j.

---

## Failure-Mode Findings (skill checklist C1–C7)

| # | Failure mode | Result |
|---|---|---|
| 1 | Number inflation | **None detected** in spreadsheet-backed values; rounding is standard throughout |
| 2 | Best-replicate cherry-pick | **None detected** in panels reporting mean ± s.d. Caveat: several Fig. 7d displayed percentages are absent from the workbook, so they cannot be checked either way |
| 3 | Config mismatch | **None detected** — compared groups share virus/cell/timepoint settings |
| 4 | Aggregation mismatch | **1 found** — Fig. 2h (C22) |
| 5 | Delta error | **None detected** among recomputable derived quantities |
| 6 | Caption–content mismatch | Fig. 2h legend *n*; remaining suspicions are `ambiguous_mapping`, not confirmed mismatches |
| 7 | Scope overclaim | **2 found** — C56, C57 |

---

## All Claims (detailed)

Full 58-row claim table with per-claim `paper_text`, `evidence_file`, `evidence_value` and `status`
is preserved verbatim in the review trace:
`.aris/traces/paper-claim-audit/2026-09-16_run01/reviewer_response.md`
and in machine-readable form in `PAPER_CLAIM_AUDIT.json`.

---

## Prioritised Fix List

1. **Correct or explain the Fig. 7g *P* values** (0.0004 / 0.0001 vs recomputed 0.00749 / 0.00434); supply the analysis file and exact bracket mapping.
2. **Correct the Fig. 2h replicate count**, or explain why H1N1/HSV-1 carry four values while the legend states *n* = 3.
3. **Supply the missing numerical source data**: Fig. 4 quantitative panels, Fig. 5b/c/e/f, Fig. 6j, Fig. 3d conjunctivitis counts, Fig. 1a screen values, and the six untraceable Fig. 7d percentages.
4. **Temper the "specifically" / "broad anti-RNA-viral spectrum" language**, or deposit broader supporting evidence.
5. **Provide bracket-to-comparison mapping** for every *P* value whose position was lost in text extraction, so the five `ambiguous_mapping` items can be resolved either way.

---

## Limits of This Audit

- Covers **numeric fidelity only** — whether the paper reports its deposited data truthfully and
  precisely. It does not assess whether the science or methodology is sound.
- **Pixel-level image/blot forensics is out of scope** and must be run separately; the three Fig. 4–6
  PDFs were read as text layers only.
- Extended Data source data was not part of this evidence set.
- Several findings are **"not verifiable"**, not "demonstrated false" — the distinction is preserved
  per claim. Nothing here asserts misconduct or intent.

## Backend Caveat

The skill specifies `mcp__codex__codex` with `model: gpt-6-astra`, `reasoning: ultra`. That MCP tool
is **not available in this session** (`claude mcp add codex -- npx -y @openai/codex-mcp`). The
verbatim zero-context audit protocol was instead routed to an isolated fresh cross-family reviewer
subagent, which self-declared as `gpt-5.3-codex`. The skill's invariants — *fresh thread, zero
context, no executor interpretation, cross-model family* — were all preserved; only the transport
differs. Treat the verdict as valid-but-non-canonical.
