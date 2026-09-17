# Research Package Integrity Audit: Comprehensive Technical Audit

**Package:** ZNFX1 mitochondrial dsRNA sensor — Wang Y., Yuan S., Jia X., Ge Y., Ling T., Nie M., Lan X., Chen S. & Xu A., *Nature Cell Biology* **21**, 1346–1356 (2019). DOI 10.1038/s41556-019-0416-0
**Audit ID:** URPA-ZNFX1-2019-001
**Skill:** `universal-research-package-audit`
**Ledger:** `audit-ledger.json` (source of truth for every status in this document)
**Output validation:** **PASS** — `scripts/validate_audit.py` returned `{"status":"PASS","errors":[],"warnings":[]}`

> This audit reports evidence, scope and uncertainty. It does not infer fabrication, falsification, deception or intent, and it makes no recommendation about acceptance, rejection, retraction, or whether readers should rely on the paper.

---

## 1. Execution-mode disclosure

| Item | Value |
|---|---|
| Execution status | `EXECUTION_NOT_ATTEMPTED` |
| Basis | No analysis code, notebook, pipeline or workflow was supplied with the package. There is nothing to execute; this is the expected shape of a wet-lab source-data deposit, not a failed run. |
| Substitute method | Independent recomputation from the deposited replicate values using deterministic scripts written by this audit and retained in `audit-evidence/scripts/`. |
| Recomputation environment | Python 3.12, `openpyxl`, `numpy`, `scipy`, `pdfplumber` (Windows). |
| Specialist method validation | `SPECIALIST_METHOD_VALIDATION: NOT_ASSESSED` — image forensics on the Figure 4–6 blot scans was not performed and no validated tooling for it was available. |
| Reviewer/tooling caveat | The cross-model reviewer MCP backends some sibling skills expect (`mcp__codex__codex`, `mcp__manual_review__review`) are not configured in this environment. This audit does not depend on them; all determinations here are script-based and locally reproducible. |

## 2. Executive summary

The package supplied to this audit contains the manuscript text plus seven author-deposited Source Data files. Twenty-three canonical claims were registered across 31 manuscript occurrences.

Six claims were verified as matching the deposited evidence, four are robust mismatches against it, three are mapping ambiguities that the deposited data cannot resolve, three are blocked by absent numeric evidence, and seven deposited-but-unchecked claims are recorded openly as audit limitations rather than being presented as clean.

The strongest positive result is that where the deposited workbooks store the authors' own p-values, an equal-variance two-tailed Student's *t*-test recomputed from the deposited replicates reproduces them to within 5 × 10⁻¹⁵, while the Welch variant does not. The stated test is therefore demonstrably the test used for those cells.

The four demonstrated discrepancies are correspondence problems between the manuscript's descriptions and the deposited data: a replicate count (Fig. 2h), a survival group size (Fig. 3f), a genotype label (Fig. 7c), and the scope of the data-availability statement. None of them, on this evidence, establishes that a published result is wrong; each has `result_correctness_impact: NOT_DETERMINED`, and each is stated with the reason its impact was not evaluated.

One earlier-suspected problem did **not** survive reconciliation and is explicitly *not* raised as a finding — see § 16.

## 3. Preflight and scope

| Item | Value |
|---|---|
| Package scope status | `PARTIALLY_COMPLETE` |
| Supplied | Manuscript text (extracted, 3,128 lines); Source Data Fig. 1, 2, 3, 7 (`.xlsx`); Source Data Fig. 4, 5, 6 (`.pdf`, uncropped blots) |
| Not supplied | Analysis code; raw instrument output; numeric data for Fig. 4–6; Extended Data source data; Supplementary Fig. 1–6 source data; per-animal survival records |
| Evidence profiles detected | group comparisons; repeated measurements / time series; counted observations; laboratory measurements; image evidence; aggregate-only evidence |
| Absent-artifact rule applied | Absent artifacts are treated as unavailable evidence, never as proof of error. |

## 4. File inventory and version register

Produced by `scripts/inventory_package.py`; full record in `audit-evidence/inventory.json`. All 8 files readable; 0 unclassified.

| file_id | Path | Bytes | SHA-256 (first 16) | Classification | Evidence role |
|---|---|---:|---|---|---|
| FILE-0001 | `manuscript_extracted.txt` | 96,827 | `9145a5dc89c2f816` | NARRATIVE_OR_DOCUMENTATION | Reported-statement source |
| FILE-0002 | `source-data/Source Data Fig 1.xlsx` | 15,724 | `948c4974e337469f` | STRUCTURED_DATA | Result object |
| FILE-0003 | `source-data/Source Data Fig 2.xlsx` | 15,179 | `b3f7a518a3a1ccd1` | STRUCTURED_DATA | Result object |
| FILE-0004 | `source-data/Source Data Fig 3.xlsx` | 12,688 | `f77eed0f8466ebba` | STRUCTURED_DATA | Result object |
| FILE-0005 | `source-data/Source Data Fig 4.pdf` | 19,569,773 | `5c0f777759eda965` | IMAGE_OR_FIGURE † | Published-artifact support |
| FILE-0006 | `source-data/Source Data Fig 5.pdf` | 13,040,249 | `6bd3c1ec2376c1fd` | IMAGE_OR_FIGURE † | Published-artifact support |
| FILE-0007 | `source-data/Source Data Fig 6.pdf` | 6,693,658 | `f49239f09a4d8b05` | IMAGE_OR_FIGURE † | Published-artifact support |
| FILE-0008 | `source-data/Source Data Fig 7.xlsx` | 16,447 | `b4ca4c544660c71f` | STRUCTURED_DATA | Result object |

† Classified by the inventory script as `NARRATIVE_OR_DOCUMENTATION` on file extension; reclassified by **evidence structure** (skill step 2) to `IMAGE_OR_FIGURE`, because each is a scan set of uncropped immunoblots whose text layer carries labels only.

**Version identification:** none of the deposited files carries an internal version marker, revision date or changelog. Version state is therefore established only by the SHA-256 digests recorded above.

## 5. Manuscript-section coverage

| Section | Status | Claims identified | Claims classified |
|---|---|---:|---:|
| Abstract | REVIEWED | 4 | 4 |
| Introduction | REVIEWED | 0 | 0 |
| Results — ZNFX1 induction (Fig. 1) | REVIEWED | 6 | 6 |
| Results — antiviral restriction (Fig. 2) | REVIEWED | 4 | 4 |
| Results — in vivo (Fig. 3) | REVIEWED | 3 | 3 |
| Results — localisation / RNA binding / MAVS (Fig. 4–6) | REVIEWED_EVIDENCE_BLOCKED | 3 | 3 |
| Results — RLR independence (Fig. 7) | REVIEWED | 5 | 5 |
| Discussion | REVIEWED | 0 | 0 |
| Methods / Statistics | REVIEWED | 1 | 1 |
| Data availability | REVIEWED | 1 | 1 |
| Extended Data / Supplementary | NOT_SUPPLIED | 0 | 0 |

Introduction and Discussion contribute no *new* verifiable claims: their assertions are restatements of claims registered from the Abstract and Results, and are captured as additional occurrences rather than as separate claim IDs.

## 6. Study and evidence graph

| study_id | Description | Files |
|---|---|---|
| S-001 | Cell-culture loss-/gain-of-function virology (A549, L929, HEK293T, MEF) | FILE-0003, FILE-0004, FILE-0008 |
| S-002 | Mouse in vivo VSV/HSV-1 infection and survival | FILE-0004 |
| S-003 | Human/macaque clinical sample expression (HIV, SIV encephalitis) | FILE-0002 |
| S-004 | Biochemistry: localisation, RNA binding, protein–protein interaction | FILE-0005, FILE-0006, FILE-0007 |

Governing chain, instantiated for the one fully traversable case (C-008):

`claim (Znfx1 loss raises RNA-virus load) -> study S-001 -> experiment (qRT–PCR, wt vs Znfx1−/−, VSV/EMCV) -> analysis (two-tailed unpaired Student's t) -> code/workflow (NOT SUPPLIED; substituted by audit recomputation) -> input (Source Data Fig 2.xlsx!Sheet1!B50:I52) -> population P-001 -> transformation (fold-change normalisation to uninfected = 1) -> result (stored p-values E53, I53) -> figure (Fig. 2h) -> reported statement (manuscript_extracted.txt:910)`

The chain breaks at `code/workflow` for every claim in the package, and additionally at `input` for S-004 (C-014/C-015/C-016), where no numeric input exists.

## 7. Canonical claim ledger and occurrences

23 unique claims / 31 occurrences. Full text and per-claim basis in `audit-ledger.json`.

| claim_id | Canonical claim (abbreviated) | Centrality | Outcome |
|---|---|---|---|
| C-001 | ZNFX1 is an ISG induced by RNA virus and poly(I:C) | CENTRAL | NOT_CHECKED |
| C-002 | Znfx1 rises across mouse tissues after infection | SUPPORTING | NOT_CHECKED |
| C-003 | ZNFX1 elevated in HIV samples (n = 9 / 14) | SUPPORTING | **MATCH** |
| C-004 | ZNFX1 elevated in SIV encephalitis (n = 18) | SUPPORTING | **MATCH** |
| C-005 | Znfx1 induction requires JAK/STAT and IFNAR | SUPPORTING | NOT_CHECKED |
| C-006 | STAT1/2, IRF1/9 drive the Znfx1 promoter | SUPPORTING | NOT_CHECKED |
| C-007 | ZNFX1 knockdown enhances VSV replication | CENTRAL | NOT_CHECKED |
| C-008 | Znfx1 deficiency raises VSV/EMCV load | CENTRAL | **MATCH** |
| C-009 | Figure 2h comprises n = 3 independent experiments | DESCRIPTIVE | **ROBUST_MISMATCH** |
| C-010 | ZNFX1 restricts RNA but not DNA virus | CENTRAL | NOT_CHECKED |
| C-011 | Znfx1−/− mice: higher VSV load (n = 4/group) | CENTRAL | **MATCH** |
| C-012 | Serum IFN differs (8 or 4 mice per group) | SUPPORTING | **MATCH** |
| C-013 | Survival assessed with n = 10 mice per group | CENTRAL | **ROBUST_MISMATCH** |
| C-014 | ZNFX1 is mitochondrially localised | CENTRAL | BLOCKED |
| C-015 | ZNFX1 binds viral RNA via ARM and P-loop | CENTRAL | BLOCKED |
| C-016 | ZNFX1 interacts with MAVS | CENTRAL | BLOCKED |
| C-017 | ZNFX1 induces Ifnb1 independently of RIG-I/MDA5 | CENTRAL | NOT_CHECKED |
| C-018 | Fig. 7c uses wild-type or Mda5−/− cells | DESCRIPTIVE | **ROBUST_MISMATCH** |
| C-019 | Fig. 7c replicates internally consistent | DESCRIPTIVE | MAPPING_AMBIGUITY |
| C-020 | Fig. 7g printed P values derive from deposited data | SUPPORTING | MAPPING_AMBIGUITY |
| C-021 | Fig. 7e analyses the repeated FACS data of 7d | SUPPORTING | MAPPING_AMBIGUITY |
| C-022 | Two-tailed unpaired Student's t-test used | DESCRIPTIVE | **MATCH** |
| C-023 | Source data provided for Fig. 1–7 and Suppl. Fig. 1–6 | DESCRIPTIVE | **ROBUST_MISMATCH** |

## 8. Population and denominator records

Six population records (P-001 … P-006) were created before any count, ratio or grouped calculation, per the population contract. Full fields in `audit-ledger.json`.

| population_id | Unit of analysis | Source locator | Mapping confidence | Alternatives tested |
|---|---|---|---|---|
| P-001 | Independent experiment (relative viral RNA) | `Fig 2.xlsx!Sheet1` rows 50–52, 57–60 | CONFIRMED | Student vs Welch |
| P-002 | Mouse at risk per timepoint | `Fig 3.xlsx!Sheet1!B32:C41` | PROBABLE | at-risk count; percent survival; two pooled cohorts |
| P-003 | Independent experiment (Ifnb1/Ifit1 in DKO) | `Fig 7.xlsx!Sheet1!J62:K67` | **UNRESOLVED** | printed P as EV-vs-EV+VSV; printed P as ±ZNFX1 within +VSV |
| P-004 | Independent clinical sample | `Fig 1.xlsx!Sheet1!B28:E41`, `H28:K45` | CONFIRMED | counting with/without trailing blanks |
| P-005 | Mouse | `Fig 3.xlsx!Sheet1` rows 3–29 | CONFIRMED | per-tissue vs pooled |
| P-006 | Independent experiment (cellular viral load) | `Fig 7.xlsx!Sheet1!C38:K43` | **UNRESOLVED** | deposited labels authoritative; legend authoritative |

**Placeholder handling, explicitly tested:** control arms in P-001, P-003 and P-006 are deposited as the exact constant `1` in every replicate. These are normalisation references, not zero-count placeholders and not missing values; they were retained as data. Their zero variance is recorded as a structural condition in F-008.

**Unresolved population choices:** P-003 and P-006 carry `mapping_confidence: UNRESOLVED`. Per the population contract, the dependent claims are *not* reported as contradictions — C-020 and C-019 are classified `MAPPING_AMBIGUITY`.

## 9. Provenance and structural checks

| Check | Result |
|---|---|
| File readability | 8/8 readable |
| Hash register | 8/8 hashed (SHA-256), § 4 |
| Internal version markers | None present in any deposited file |
| Sheet structure | Each `.xlsx` contains a single `Sheet1` with figure-panel blocks delimited by label rows |
| Cross-document consistency (legend *n* vs deposited rows) | 5 correspond (Fig. 1f, 1g, 2a, 2b, 2g, 3a–c); 2 do not (Fig. 2h block 2, Fig. 3f) |
| Cross-document consistency (legend genotype vs deposited labels) | 1 does not correspond (Fig. 7c) |
| Group-coverage completeness (deposited arms vs displayed arms) | Incomplete for Fig. 7e and Fig. 7g |
| Outlier screen within replicate groups | 1 flagged (`Fig 7.xlsx!Sheet1!G40`) |
| Transformation tracing | Fold-change normalisation to a control fixed at 1.0 is the only transformation evidenced; no intermediate files were supplied to trace it from raw Ct values |

## 10. Source execution

No executable artifact was supplied. Status `EXECUTION_NOT_ATTEMPTED` (§ 1). No originals were modified; the audit wrote only to `audit-output/.../universal-research-package-audit/`. Per the skill's status rules, inspection has **not** been converted into execution anywhere in this document.

## 11. Independent recomputation

Records in `audit-evidence/calculations/calculations.json`; script `audit-evidence/scripts/recompute.py`.

| calc_id | Panel | What was recomputed | Reported / stored value | Recomputed | Outcome |
|---|---|---|---|---|---|
| CALC-VSV-2h | Fig. 2h | Student's *t*, wt vs *Znfx1*−/−, VSV | `E53` = 0.004186885624489595 | 0.004186885624489591 | **MATCH** (Δ ≈ 4 × 10⁻¹⁸) |
| CALC-EMCV-2h | Fig. 2h | Student's *t*, wt vs *Znfx1*−/−, EMCV | `I53` = 0.0018500638904232246 | 0.001850063890423224 | **MATCH** |
| — | Fig. 2h | Welch variant, same data | — | 0.02371 / 0.01102 | Does **not** match stored — confirms the equal-variance test was used |
| CALC-2h-n | Fig. 2h | Deposited replicate rows per arm | legend n = 3 | block 1 = 3 rows; block 2 = **4 rows** | **ROBUST_MISMATCH** |
| CALC-7g-IFNB1 | Fig. 7g | Student's *t*, only deposited contrast | printed 0.0004 | 0.007486 | **MAPPING_AMBIGUITY** (see § 16) |
| CALC-7g-IFIT1 | Fig. 7g | Student's *t*, only deposited contrast | printed 0.0001 | 0.004337 | **MAPPING_AMBIGUITY** (see § 16) |
| CALC-3f-n | Fig. 3f | Maximum at-risk per group | legend n = 10 | wt max 5, KO max 5 | **ROBUST_MISMATCH** |
| CALC-3f-events | Fig. 3f | Event reconstruction from at-risk series | — | wt 2 deaths / 3 censored; KO 4 deaths / 1 censored | Reported as reconstruction only; timepoint units not deposited |
| CALC-1f-n | Fig. 1f/1g | Column lengths vs legend *n* | 9 / 14 / 18 | 9 / 14 / 18 | **MATCH** |
| CALC-7c-labels | Fig. 7c | Legend genotype vs deposited row labels; outlier screen | legend "wild-type or Mda5−/−" | deposited "Rig-i −/−", "Mda5 −/−"; `G40` 10.54× below sibling mean | **ROBUST_MISMATCH** + outlier flag |

A `scipy` catastrophic-cancellation precision warning is raised for the Fig. 7g computations because one arm has zero variance. The *t* statistic remains well defined; the warning is recorded here for completeness and does not affect the classification, which rests on group coverage rather than on the numeric value.

## 12. Figures and tables

Separated per the skill's figure/table rules. **`FIGURE_NUMERICALLY_MATCHED` is not claimed anywhere in this audit**, because no published figure pixel values or plotted values were compared — only deposited source-data values.

| Figure | Intended code mapping | Source-data mapping | Result-object mapping | Published-artifact provenance | Published-value comparison | Regeneration |
|---|---|---|---|---|---|---|
| Fig. 1 | NOT_APPLICABLE (no code) | Blocks 1b,1e,1f,1g,1h,1j,1k,1l present | CONFIRMED | Not assessed | Sample counts only | Not attempted |
| Fig. 2 | NOT_APPLICABLE | Blocks 2a,2b,2d,2e,2g,2h,2i,2j present | CONFIRMED | Not assessed | Stored p-values reproduced (2h) | Not attempted |
| Fig. 3 | NOT_APPLICABLE | Blocks 3a,3b,3c,3f present | PROBABLE (3f) | Not assessed | Group counts only | Not attempted |
| Fig. 4 | NOT_APPLICABLE | **Absent** (blot scans only) | BLOCKED | Uncropped scans supplied | Not possible | Not attempted |
| Fig. 5 | NOT_APPLICABLE | **Absent** (blot scans only) | BLOCKED | Uncropped scans supplied | Not possible | Not attempted |
| Fig. 6 | NOT_APPLICABLE | **Absent** (blot scans only) | BLOCKED | Uncropped scans supplied | Not possible | Not attempted |
| Fig. 7 | NOT_APPLICABLE | Blocks 7a,7b,7c,7e,7f,7g,7h,7i,7j present; 7d absent | UNRESOLVED (7c, 7e, 7g) | Not assessed | Attempted; not attributable | Not attempted |

No tables were present in the package.

## 13. Research-package findings

| finding_id | Title | Assessment | Severity | Verification impact | Result-correctness impact |
|---|---|---|---|---|---|
| F-001 | Fig. 2h H1N1/HSV-1 block deposits 4 replicate rows while legend states n = 3 | CONCERN | UNDETERMINED | MINOR | NOT_DETERMINED |
| F-002 | Fig. 3f legend n = 10/group; deposited series describe at most 5/group | CONCERN | UNDETERMINED | MAJOR | NOT_DETERMINED |
| F-003 | Fig. 7c legend names wild-type; deposited block labelled *Rig-i*−/− and *Mda5*−/− | CONCERN | UNDETERMINED | MAJOR | NOT_DETERMINED |
| F-004 | One Fig. 7c replicate ~10.5× below its two siblings (`G40`) | UNRESOLVED | UNDETERMINED | MINOR | NOT_DETERMINED |
| F-005 | Data-availability statement promises broader source data than supplied | CONCERN | UNDETERMINED | MAJOR | NOT_DETERMINED |
| F-006 | Fig. 2h VSV/EMCV p-values reproduce exactly using the stated test | **POSITIVE** | NOT_APPLICABLE | NONE | NONE_DEMONSTRATED |
| F-007 | Clinical-sample and mouse group sizes match legend n where deposited | **POSITIVE** | NOT_APPLICABLE | NONE | NONE_DEMONSTRATED |
| F-008 | Control arms deposited as the exact constant 1 (zero variance) | NEUTRAL | UNDETERMINED | MINOR | NOT_DETERMINED |

**Why every concern carries `severity: UNDETERMINED`.** The skill permits MINOR/MAJOR/CRITICAL only when impact has been *tested*. For F-001, F-002 and F-003 the printed panel statistic could not be tied to the affected block (F-001), the survival statistic and event times are not deposited (F-002), or the package contains no evidence establishing which genotype was actually run (F-003). Each is a demonstrated correspondence discrepancy whose consequence for the published result has deliberately not been guessed.

### Detail — F-002 (highest-priority concern)

Deposited `Fig 3.xlsx!Sheet1!B32:C41`:

```
wt        : 5 5 5 5 5 5 5 5 3 3
Znfx1-/-  : 5 5 5 5 2 2 1 1 1 1
```

Legend (`manuscript_extracted.txt:1083`): "*Survival of wild-type and Znfx1−/− mice (n = 10 mice per group)*".

Alternatives tested before raising the contradiction, per the reconciliation rule:
1. **Number at risk per timepoint** — consistent internally; yields 5 per group, not 10.
2. **Percent survival** — rejected: values are integers 1–5, not a 0–100 scale.
3. **Two pooled cohorts of 5** — would reach n = 10, but requires a second cohort that is not deposited.

No reading of the deposited data yields 10 animals per group. Classified `ROBUST_MISMATCH` on the denominator; impact on the reported survival difference **not evaluated** (L-006).

## 14. Verification limitations

| id | Title | Assessment | Verification impact | Result-correctness impact |
|---|---|---|---|---|
| L-001 | No numeric source data for Fig. 4, 5, 6 | LIMITATION | COMPLETE_BLOCK | NOT_DETERMINED |
| L-002 | Fig. 7g deposits 2 of 4 displayed groups | LIMITATION | MAJOR | NOT_DETERMINED |
| L-003 | Fig. 7e deposits only the empty-vector arms | LIMITATION | MAJOR | NOT_DETERMINED |
| L-004 | No analysis code, scripts or workflow supplied | LIMITATION | MAJOR | NOT_DETERMINED |
| L-005 | Extended Data / Supplementary source data absent | LIMITATION | MAJOR | NOT_DETERMINED |
| L-006 | Fig. 3f timepoint units and per-animal records absent | LIMITATION | MAJOR | NOT_DETERMINED |

L-001 blocks three CENTRAL claims (C-014 mitochondrial localisation, C-015 RNA binding, C-016 MAVS interaction) — that is, the three claims carrying the title's mechanistic weight are the three this package cannot verify numerically. **This is a statement about verifiability, not about correctness.**

## 15. Audit limitations

| id | Title | Assessment |
|---|---|---|
| B-001 | Image forensics on the blot scans not performed — `SPECIALIST_METHOD_VALIDATION: NOT_ASSESSED` | NOT_ASSESSED |
| B-002 | Seven deposited claims not independently recomputed (C-001, C-002, C-005, C-006, C-007, C-010, C-017) | NOT_ASSESSED |
| B-003 | Panel-to-P-value mapping relies on the manuscript text layer and is positional for some panels | NOT_ASSESSED |

B-002 is feasible work this audit did not complete. It is recorded so that "not checked" is never read as "checked and clean".

## 16. Checked but not raised

This section exists so that suppressed contradictions are visible.

**Figure 7g printed P values — checked, deliberately NOT raised as a discrepancy.**
Recomputing the only deposited Fig. 7g contrast (EV vs EV+VSV) gives *P* = 0.00749 (Ifnb1) and *P* = 0.00434 (Ifit1), against printed values of 0.0004 and 0.0001 — superficially an 18× and 43× divergence. It would have been easy, and wrong, to report that as a numeric mismatch.

The deposited block contains only two columns, `EV` and `EV+VSV`, whereas the published panel displays four arms (EV, ZNFX1, EV+VSV, ZNFX1+VSV) in *Rig-I*−/−;*Znfx1*−/− DKO cells. The panel design implies the printed P values compare the +VSV arms **with versus without ZNFX1** — and those ZNFX1 arms are not deposited. The printed values therefore can be neither attributed to nor refuted by the deposited contrast. Recorded as `MAPPING_AMBIGUITY` (C-020) plus a verification limitation (L-002), not as a finding.

**Also checked, nothing raised:**
- Fig. 1f/1g, 2a, 2b, 2g, 3a, 3b, 3c replicate and animal counts — all correspond to the legends (F-007).
- The stated statistical test — reproduces the stored p-values exactly (F-006).
- Outlier screen across the deposited replicate groups — only `G40` flagged; all other groups were internally consistent.
- Readability and hash integrity of all 8 files — no anomaly.

## 17. Reconciled coverage

Categories sharing a denominator are mutually exclusive and sum exactly.

**Claims (denominator = 23):**

| Outcome | Count |
|---|---:|
| MATCH | 6 |
| ROBUST_MISMATCH | 4 |
| SPECIFICATION_DEPENDENT | 0 |
| MAPPING_AMBIGUITY | 3 |
| BLOCKED | 3 |
| NOT_CHECKED | 7 |
| NOT_APPLICABLE | 0 |
| DEPENDENCY_UNRESOLVED | 0 |
| **Total** | **23** ✓ |

**Distinct registers (not summed with claims):** claim occurrences 31; distinct discrepancies 4; research-package findings 8; verification limitations 6; audit limitations 3; files inventoried 8, readable 8.

Validator confirmation: `claims_total` = 23 equals the sum of `claim_outcomes` = 23; `reconciliation: PASS`.

## 18. Separate status architecture

| Register | Meaning | Count |
|---|---|---:|
| `RESEARCH_PACKAGE_FINDING` | Demonstrated discrepancy or structural condition in the supplied evidence | 8 |
| `VERIFICATION_LIMITATION` | Missing artifact, inaccessible runtime, or unresolved provenance blocking verification | 6 |
| `AUDIT_LIMITATION` | Feasible or specialist audit work not completed | 3 |

For every missing-evidence item, both impacts are reported separately: `verification_impact` describes how much verification is blocked, while `result_correctness_impact` remains `NOT_DETERMINED`. **No verification limitation in this audit is treated as evidence that a research result is wrong.**

## 19. Author queries

| # | Location | Query |
|---:|---|---|
| 1 | Fig. 3f | Please supply the per-animal survival table (one row per mouse, with time of death or censoring) and confirm the number of animals per group, which the deposited series places at 5 rather than the legend's 10. |
| 2 | Fig. 7c | Please confirm which host genotypes were used. The legend names "wild-type or *Mda5*−/−"; the deposited rows are labelled "*Rig-i* −/−" and "*Mda5* −/−". |
| 3 | Fig. 2h | Please confirm the number of independent experiments for each sub-panel: the H1N1/HSV-1 block deposits four replicate rows where the legend states n = 3. |
| 4 | Fig. 7g | Please indicate which pair of groups each printed P value compares, and supply the ZNFX1 and ZNFX1+VSV replicate values, which are not in the deposited block. |
| 5 | Fig. 7e / 7d | Please supply the ZNFX1, RIG-I and MDA5 transfection arms for the FACS quantification; only the empty-vector arms are deposited. |
| 6 | `Fig 7.xlsx!Sheet1!G40` | Please confirm this value (4,176.86) against the original qPCR output; its two sibling replicates are 45,514.85 and 42,552.97. |
| 7 | Fig. 4–6 | Please confirm whether quantification tables underlying these panels exist and can be supplied. |
| 8 | Data availability | Please confirm whether source data for the Extended Data figures and Supplementary Figs 1–6 exist, as the statement indicates. |

## 20. Validation result

```json
{"status": "PASS", "errors": [], "warnings": []}
```

| Item | Value |
|---|---|
| Validator | `scripts/validate_audit.py` (schema `audit-ledger.schema.json`, Draft 2020-12) |
| Status | **PASS** |
| Errors | 0 |
| Warnings | 0 |
| Log | `audit-evidence/logs/validation.log` |
| Schema conformance | `audit-ledger.json` validates, including the `finding.schema.json` and `population-record.schema.json` sub-schemas |
| ID uniqueness | No duplicate claim, finding or limitation IDs |
| Cross-reference integrity | Every `claim_ids` entry in findings and limitations resolves to a registered claim |
| Coverage arithmetic | 23 = 23 |

`PASS` here certifies the **structure and arithmetic of this audit's own output**. It does not certify the research package, and it is not a statement that the paper is correct.

---

### Scope statement

This audit examined correspondence between the manuscript and the evidence supplied to it. It did not assess biological plausibility, experimental design quality, novelty, or the published figures as rendered. Claims marked `NOT_CHECKED` were not examined and must not be read as verified. No finding in this document infers fabrication, falsification, deception or intent, and no publication decision is offered or implied.
