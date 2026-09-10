# Research Package Integrity Audit — Comprehensive Technical Audit (Output A)

**Skill applied:** `research-package-integrity-audit2` (registered:
`.github/skills/research-package-integrity-audit2/skill.md`; visible copy:
`skills/research-package-integrity-audit2/skill.md`).

**Package audited:** Liao, D., Zhong, L., Yin, J. et al. "Chromosomal
translocation-derived aberrant Rab22a drives metastasis of osteosarcoma."
*Nature Cell Biology* 22, 868–881 (2020).

---

## 1. Execution-Mode Disclosure

This audit was performed as a single-session, sequential inspection by one
model instance, supplemented by one fresh, zero-context sub-agent dispatch
(`gpt-5.3-codex`, high reasoning effort) used for claim extraction — the
same substitution used earlier in this folder's `experiment-audit_report.md`
and `paper-claim-audit_report.md` for the skill's normally-external reviewer
backend. No code was executed in this audit: **no code or data package was
supplied or exists locally for this paper at all** (see Section 3/4). This
is a materially sparser package than the two other packages previously
audited with this same skill in this repository (`pcbi-1007945`, which had a
supplied R Markdown analysis file, and the Dryad ecology dataset, which had
full CSV data + an R script). For this paper, evidence status is limited
almost entirely to `DIRECTLY_INSPECTED` (manuscript text) and `INFERRED`
(claim-to-claim internal consistency); `RECOMPUTED` is used only for the
handful of pure-arithmetic checks performable from manuscript-stated numbers
alone (percentage rounding, subgroup sums, unit conversions). No
`EXECUTED`, `CROSS_DOCUMENT_MATCH` (against a second, independent document),
or `FIGURE_REGENERATED_MATCH` evidence exists anywhere in this audit.

## 2. Executive Audit Summary

The supplied package consists of **one file**: the manuscript PDF (text
extracted to `../supporting-files/manuscript_extracted.txt`). No code, no
configuration files, no raw or processed result files, and no supplementary
data files were supplied or found anywhere in this repository for this
paper. This is a wet-lab cancer-biology paper; its primary sequencing
evidence (RNA-seq, whole-genome sequencing) is deposited externally at SRA
accession **SRP181860**, which was not retrieved for this audit (multi-GB
raw sequencing archives, outside this session's scope). Because the
skill's evidence graph (`claim -> study -> experiment -> analysis -> code
entry point -> input -> configuration -> transformation -> result object ->
table/figure -> reported value`) requires code and result artifacts at
almost every node past "claim," **the overwhelming majority of this audit's
checks are `BLOCKED` for lack of a supplied artifact, not because any check
failed.** This is a package-completeness limitation, not a demonstrated
integrity problem.

Within that constraint, the manuscript text itself was fully inventoried and
cross-checked against itself (internal consistency of restated numbers,
arithmetic reconciliation of subgroup counts, unit consistency across
mentions of the same quantity). Two demonstrated **CONCERN**-level findings
were identified purely from this internal cross-referencing (a unit
inconsistency in an in-vivo drug-dosing description, and an unexplained
replicate-count difference within one figure's panel set), plus two
**scope-related** findings about the breadth of the causal claim relative to
the evidence base described in the manuscript's own text. All arithmetic
that could be checked from manuscript-stated numbers reconciled exactly. No
misconduct is inferred from any of these findings.

## 3. Preflight and Scope Declaration

**Supplied files:**
- Manuscript PDF (39 pages), extracted in full to
  `../supporting-files/manuscript_extracted.txt` (117,795 characters / 17,634
  words / 3,088 extracted lines).

**Referenced but not supplied (per the manuscript's own Data Availability
statement):**
- RNA-seq and whole-genome sequencing data, SRA accession **SRP181860**.
- "Source Data" for Figs. 1–8 and Extended Data Figs. 1–10 (the manuscript
  states these are available "with the paper online," i.e. hosted by the
  journal, not supplied to this audit).
- Any analysis code (the Methods section describes a TopHat/Cufflinks-class
  RNA-seq pipeline and specific parameter values in prose, but no script,
  notebook, or pipeline configuration file was supplied).

**Execution environment:** Windows PowerShell session; Python 3.x with
standard libraries available for arithmetic recomputation and text
statistics; no R, no bioinformatics pipeline tools (TopHat/Cufflinks/STAR),
and no network access to retrieve the SRA accession were used or available.

**Preflight status: PARTIAL** (bordering on minimal). Manuscript text only;
zero referenced code, configuration, or result artifacts supplied.

## 4. File Inventory and Missing-Artifact Register

| # | Path/Artifact | Type | Present | Notes |
|---|---|---|---|---|
| 1 | `../supporting-files/manuscript_extracted.txt` | Manuscript (extracted text) | Yes | Full text extracted via PyMuPDF from the published PDF |
| 2 | SRA accession SRP181860 (RNA-seq/WGS) | Raw sequencing data | No | `MISSING_FILE` — external archive, not retrieved |
| 3 | Figs. 1–8, Ext. Data Figs. 1–10 "Source Data" | Result data underlying figures | No | `MISSING_FILE` — journal-hosted, not supplied |
| 4 | RNA-seq/fusion-detection analysis pipeline code | Code | No | `MISSING_FILE` — described in Methods prose only, no script supplied |
| 5 | Clinical cohort screening dataset (97-sample RT-PCR/Sanger results) | Raw/derived clinical data | No | `MISSING_FILE` — not deposited or supplied |

Files inventoried: 1 supplied + 4 referenced-but-missing = 5 total artifacts
in scope. Files classified: 1/1 supplied files fully classified (100%).
Unclassified files: 0.

**Note:** this same paper's folder also contains three prior audit outputs
from other skills run earlier in this session
(`academic-paper-review_review.md`, `academic-paper-reviewer_review.md`,
`experiment-audit_report.md`, `exploratory-data-analysis_report.md`,
`paper-claim-audit_report.md`/`.json`). These are **not** part of the
audited research package — they are this session's own prior-audit
artifacts and are excluded from the file inventory above and from the
evidence graph, consistent with Non-Negotiable Principle 1 (inventory the
package under audit, not the auditor's own output trail). Their findings
are referenced only where they independently corroborate a finding reached
fresh in this audit.

## 5. Study, Experiment, Analysis, and Artifact Map

This is a single-paper, multi-experiment-type wet-lab study (no simulation,
no machine-learning component). It combines a clinical cohort screen, cell
line and animal functional experiments, and biochemical assays. There is no
supplied code, so figure-to-code mapping cannot be attempted at all; every
figure/table in this paper is `BLOCKED_MISSING_CODE` for code-mapping
purposes. Figure/table-to-published-value correspondence is likewise
`BLOCKED` (no Source Data supplied).

| Figure/Table | Manuscript content (short) | Code artifact | Mapping status |
|---|---|---|---|
| Fig. 1 | Fusion discovery in patient RNA-seq/WGS; Rab22a-NeoF1 structure | None supplied | `BLOCKED_MISSING_CODE` |
| Fig. 2 | Rab22a-NeoF1 promotes migration/invasion in vitro and metastasis in vivo | None supplied | `BLOCKED_MISSING_CODE` |
| Fig. 3 | Mechanism: SmgGDS-607 interaction, RhoA activation | None supplied | `BLOCKED_MISSING_CODE` |
| Fig. 4–7 | Additional mechanistic and functional validation panels | None supplied | `BLOCKED_MISSING_CODE` |
| Fig. 8 | iRGD-peptide competitive inhibition, in vivo therapeutic test | None supplied | `BLOCKED_MISSING_CODE` |
| Extended Data Figs. 1–10 | Supporting validation panels, including the LHS-style dosing/panel data discussed in Section 12 | None supplied | `BLOCKED_MISSING_CODE` |
| Clinical cohort table (in-text, no discrete table number) | 97-sample screen, 2/37 (5.4%) fusion-positive metastatic subgroup | None supplied | `BLOCKED_MISSING_CODE` (also `DATA_PROVENANCE_GAP` — see Section 7) |

No figure in this paper reaches `PUBLISHED_FIGURE_PROVENANCE_VERIFIED`,
`FIGURE_REGENERATED_MATCH`, or `FIGURE_UNDERLYING_FORMULA_RECOMPUTED` in
this audit — all are `FIGURE_EXECUTION_NOT_ATTEMPTED` /
`FIGURE_CHECK_BLOCKED` for lack of any supplied code or Source Data file.

## 6. Complete Claim Ledger

The full manuscript claim-extraction pass was already performed for this
paper in this session's `paper-claim-audit_report.md`/`.json` (32 claims,
IDs C01–C32, each with location, exact quote, and status). Per this skill's
Gate 3, that extraction is adopted as this audit's claim ledger rather than
re-deriving it independently, since the same underlying manuscript text is
the sole evidentiary source for both audits and re-extraction would not add
new claims. Status labels are re-mapped to this skill's vocabulary below;
the underlying facts are unchanged from that report.

| Claim ledger source | Claims | Mapping to this skill's evidence statuses |
|---|---|---|
| `paper-claim-audit_report.json` C01–C32 | 32 | 14 → `DIRECTLY_INSPECTED` (internally consistent restatements, e.g. C05, C08, C09, C11, C15–C21, C24, C25, C31); 1 → `RECOMPUTED` (C07, 2/37 percentage arithmetic); 12 → `BLOCKED` (no raw file exists to check against, e.g. C01, C02, C04, C06, C10, C14, C23, C26–C29, C32); 2 → `UNRESOLVED` (mapping ambiguity, C13, C22); 2 → `INFERRED` with `CONCERN`/`UNSUPPORTED_SCOPE_CLAIM` status (C03, C12); 1 → `INFERRED` with `CODE_MANUSCRIPT_MISMATCH`-analog finding (C30, unit inconsistency — no code exists, so this is manuscript-internal, category `REPORTING_INCONSISTENCY`) |

**Claim ledger status: substantially covered for narrative/prose-derivable
claims (32 of 32 identifiable text claims carry a stable ID and status).**
It is **INCOMPLETE** in the Gate-3 sense for any claim requiring
verification against a code entry point, configuration, or result object,
because none exist locally for this paper. **Reporting correspondence:
`BLOCKED`** for essentially all quantitative claims against primary
evidence; `PARTIALLY_VERIFIED` for the subset checkable via internal
manuscript cross-referencing only.

## 7. Data Provenance and Structural Checks

No raw or derived data file of any kind (CSV, FASTQ, BAM, VCF, Excel Source
Data workbook) was supplied. Provenance classification for the paper's
underlying data types, based only on manuscript description (not on
inspection of an actual file):

| Data type (as described in Methods) | Provenance class | Evidence status |
|---|---|---|
| Patient RNA-seq/WGS reads (SRP181860) | `RAW_OBSERVED` (described) | `NOT_CHECKED` — file not retrieved |
| Clinical cohort screening results (97 samples, RT-PCR/Sanger/FISH) | `RAW_OBSERVED` (described) | `NOT_CHECKED` — no table/spreadsheet supplied |
| Cell-line/animal experiment readouts (qPCR, migration/invasion counts, tumor volumes, survival times) | `RAW_OBSERVED` (described) | `NOT_CHECKED` — no Source Data supplied |
| Figure-embedded summary statistics (means, error bars, P-values) | `DERIVED`/`PRESENTATION_ONLY` | `DIRECTLY_INSPECTED` from manuscript text/legends only |

No ID/duplicate/missingness/range/coding/denominator check could be applied
to an actual dataset, because none was supplied. The only structural checks
performable are the manuscript-internal arithmetic checks reported in
Section 10.

**Empirical data integrity status: `INSUFFICIENT_EVIDENCE`** (not
`NO_DEMONSTRATED_ISSUES` — that status requires the data to have actually
been inspected, which did not happen here; and not `DEMONSTRATED_ISSUES`,
since no data-level error was found in the one thing that was inspectable,
the manuscript's own prose numbers).

## 8. Code, Configuration, and Domain Checks

**Not applicable.** No code or configuration file was supplied for this
paper — every check in the skill's Phase 5 (schemas, joins, filters, score
construction, seeds, leakage, thresholds, denominators) requires a code
artifact that does not exist locally. This is recorded as `BLOCKED` per
item rather than silently omitted:

| Check category | Status | Reason |
|---|---|---|
| File existence for analysis code | `BLOCKED` | No code supplied |
| Schema/join/filter checks | `NOT_APPLICABLE` | No data/code pair to check |
| Seed/configuration consumption checks | `BLOCKED` | Methods describes some pipeline parameters (e.g. TopHat `-p 8`, `--mate-std-dev 80`, `--max-intron-length 100000`) in prose, but no config file exists to verify against actual pipeline execution |
| Leakage/split-overlap/threshold checks (ML-style) | `NOT_APPLICABLE` | This is not a machine-learning paper |
| Hardcoded-output / overwritten-provenance checks | `BLOCKED` | No code to inspect |

**Configuration and model-input integrity status: `NOT_ASSESSED`** (the
Methods-described pipeline parameters were `DIRECTLY_INSPECTED` as prose —
see Section 10 for the one internal-consistency check performed on them —
but this does not amount to assessing configuration integrity against an
actual configuration file, which does not exist).

## 9. Source-Execution Report

**Status: `NOT_APPLICABLE`.** There is no code to execute. This differs
from the pcbi-1007945 audit in this repository, where a supplied Rmd file
existed but could not be executed for lack of an R runtime
(`EXECUTION_NOT_ATTEMPTED`); here, `NOT_APPLICABLE` is the correct status
because no executable artifact was ever supplied to attempt in the first
place.

## 10. Independent-Recomputation Report

**Status: `PARTIALLY_RECOMPUTED`** — limited strictly to arithmetic
performable from manuscript-stated numbers, with no access to raw data.
The following were independently recomputed/verified (Python, standard
arithmetic — reused from this session's `paper-claim-audit_report.md`
internal-consistency pass, re-verified here):

| Recomputation | Manuscript-stated inputs | Independently recomputed result | Match? |
|---|---|---|---|
| Fusion-positive prevalence | 2 positive / 37 metastatic samples | 2/37 = 5.4054% | Matches stated "5.4%" (`RECOMPUTED`) |
| Cohort total reconciliation | 37 metastatic + 60 non-metastatic | 37 + 60 = 97 | Matches stated total of 97 screened (`RECOMPUTED`) |
| Metastatic subgroup reconciliation | 2 fusion-positive + 35 fusion-negative | 2 + 35 = 37 | Matches stated metastatic subgroup size (`RECOMPUTED`) |
| Tumor-volume cutoff unit conversion | "1,500 mm³" vs. "1.5 cm³" (both used in text) | 1.5 cm³ × (10 mm/cm)³ = 1,500 mm³ | Matches — consistent unit conversion (`RECOMPUTED`) |
| Epitope peptide length | Residues "68–82" vs. stated "15-mer" peptide | 82 − 68 + 1 = 15 | Matches (`RECOMPUTED`) |

No figure-underlying formula (e.g., any statistical test statistic, fold-
change calculation, or survival-curve computation) could be independently
recomputed, because the raw measurements feeding those calculations were
never supplied — only the already-aggregated figure/legend values are
visible in the manuscript text. This is `BLOCKED`, not `NOT_CHECKED`,
because no feasible independent computation exists without the underlying
raw numbers.

## 11. Figure, Table, and Source-Data Correspondence

**Status: `BLOCKED` for all figures/tables.** No Source Data file was
supplied for any figure or extended data figure, and no code exists to
regenerate any figure independently. This audit could not compare any
published figure value against an independently-obtained value. See
Section 5 for the per-figure mapping table (all `BLOCKED_MISSING_CODE` /
`FIGURE_CHECK_BLOCKED`).

## 12. Detailed Findings

### F-01 — Unit inconsistency in iRGD peptide dosing description
- **Category:** `REPORTING_INCONSISTENCY`
- **Locations:** Methods (in-vivo drug administration passage) vs.
  Extended Data Fig. 10 legend
- **Evidence:** Methods states the iRGD peptide was administered at
  "1 mg kg⁻¹ or 10 mg kg⁻¹"; the Extended Data Fig. 10 legend instead
  states "1 mg/ml and 10 mg/ml" for what the text presents as the same
  treatment arms.
- **Mapping status:** `UNRESOLVED` (cannot determine, from text alone,
  whether this is a transcription error in one location, or whether both a
  dose-per-body-weight and a stock-solution concentration were intended but
  only one unit was retained in each mention).
- **Evidence status:** `DIRECTLY_INSPECTED` (both passages read directly;
  no raw dosing/administration log was supplied to resolve which is
  correct).
- **Impact tested:** Not tested — resolving this would require the raw
  animal-dosing records, which were not supplied.
- **Severity: `UNDETERMINED`.** Reason: the discrepancy is demonstrated
  (two different units describing what the text presents as the same
  treatment), but its effect on any reported result was not evaluated, and
  could not be, without the raw dosing records.
- **Misconduct inference:** `NONE`.
- **Reviewer action:** Ask the authors to confirm the correct unit and
  reconcile the two passages.

### F-02 — Unexplained replicate-count variation within one figure's panel set
- **Category:** `REPLICATE_COUNT_MISMATCH`
- **Location:** Extended Data Fig. 10 legend, panels c–f (n=3) vs. panel g
  (n=4)
- **Evidence:** Panels within the same figure, testing closely related
  migration/invasion outcomes, report n=3 for most panels and n=4 for one.
- **Mapping status:** `PROBABLE` (most likely an intentional extra
  replicate added to one specific comparison, but the manuscript text does
  not state why).
- **Evidence status:** `DIRECTLY_INSPECTED`.
- **Impact tested:** Not tested — no raw per-replicate data was supplied to
  assess whether the differing n changes the reported outcome's
  robustness.
- **Severity: `UNDETERMINED`.** Reason: demonstrated inconsistency in
  stated replicate count across a matched panel set; effect on the
  reported result was not evaluated.
- **Misconduct inference:** `NONE`.
- **Reviewer action:** Ask the authors why panel g used a different
  replicate count than panels c–f in the same figure.

### F-03 — Scope of the causal claim exceeds the evidence base described in the manuscript's own text
- **Category:** `UNSUPPORTED_SCOPE_CLAIM`
- **Locations:** Title/Abstract ("Rab22a ... drives metastasis of
  osteosarcoma") vs. Results (clinical-cohort paragraph: 2/37 fusion-positive
  metastatic patients out of 97 screened; endogenous mechanistic work
  described as derived from a single patient's primary/metastatic
  cell-line pair, ZOS/ZOS-M)
- **Evidence:** The general, disease-wide causal title/abstract framing is
  broader than the depth of endogenous human evidence the manuscript's own
  Results section describes (a rare fusion found in 2/37, i.e. 5.4%, of a
  single-institution metastatic subgroup; endogenous cell-line evidence
  from one patient).
- **Mapping status:** `CONFIRMED` (this is a direct reading of the
  manuscript's own stated numbers against its own headline framing — no
  external data needed).
- **Evidence status:** `DIRECTLY_INSPECTED`.
- **Impact tested:** Not a numerical-impact finding — this is a scope/
  framing observation, evaluated against the manuscript's own stated
  sample sizes.
- **Severity: `UNDETERMINED`** in the skill's numeric-impact sense (this
  finding concerns claim framing, not a computational or data error).
- **Misconduct inference:** `NONE`.
- **Reviewer action:** Ask whether the title/abstract framing should be
  qualified to specify the rare-fusion, single-institution-cohort scope.
- **Cross-reference:** This finding independently corroborates the same
  observation already made in this folder's `experiment-audit_report.md`
  (Check E) and `paper-claim-audit_report.md` (C03).

### F-04 — Generalization to "multiple cancer types" exceeds the cited case count
- **Category:** `UNSUPPORTED_SCOPE_CLAIM`
- **Locations:** Results, cross-cancer generalization sentence ("occur and
  drive metastasis in multiple cancer types") vs. the same section's
  citation of 2 clinical cases and 2 cell lines for that claim
- **Evidence/mapping/status:** Same structure as F-03, applied to the
  cross-cancer generalization sentence specifically.
- **Severity:** `UNDETERMINED` (framing observation).
- **Reviewer action:** Ask the authors to specify exactly which cancer
  types and how many cases/lines support the "multiple cancer types"
  statement, or to narrow the claim.

## 13. Checked But Not Raised

The following were specifically checked and found **not** to show a
discrepancy (`NO_DEMONSTRATED_ISSUES` for each, listed so this audit does
not implicitly suggest they were overlooked):

- Percentage-to-count arithmetic for the headline prevalence figure (2/37 =
  5.4%) — reconciles exactly.
- Cohort subgroup totals (37 + 60 = 97; 2 + 35 = 37) — reconcile exactly.
- Tumor-volume cutoff unit conversion (1,500 mm³ = 1.5 cm³) — reconciles
  exactly across all four locations where it is restated.
- Epitope peptide length (residues 68–82 = 15 amino acids, matching the
  stated "15-mer" label) — reconciles exactly.
- Sequencing-depth figures (6 GB / 90 GB clean data per sample) and TopHat
  pipeline parameters — restated identically wherever they appear in the
  extracted text, with no internal contradiction found.
- Replicate counts for the large majority of in vitro (n=3) and in vivo
  (n=6, within the Methods' stated "6–8 mice per group" range) panels are
  internally consistent with the Methods section — only the one exception
  noted in F-02 was found.

## 14. Reconciled Coverage

```text
Manuscript claims with a stable ID (from paper-claim-audit ledger): 32
  Checkable via internal cross-reference (DIRECTLY_INSPECTED/RECOMPUTED): 15
  Blocked — no raw file exists to check against (BLOCKED): 12
  Unresolved mapping (ambiguous internal cross-reference): 2
  Scope/framing findings (INFERRED, not a numeric error): 2 (C03, C12; note:
    F-03/F-04 above restate C03/C12 as this skill's findings, not additional
    distinct claims)
Total classified: 32 (matches paper-claim-audit denominator)
Reconciliation: PASS

Distinct discrepancies demonstrated: 2 (F-01 unit inconsistency; F-02
  replicate-count variation)
Distinct scope-framing observations: 2 (F-03, F-04)
Distinct findings total: 4
```

Figure/table correspondence denominator: 8 main figures + 10 Extended Data
figures + 1 clinical cohort table-in-text = 19 artifacts. All 19 are
`BLOCKED` for code-mapping and published-value correspondence (0/19
checked; 19/19 blocked). Reconciliation: PASS (19 = 19).

## 15. Separate Status Architecture

- **Package completeness:** `INCOMPLETE` (1 of 5 identified artifacts
  supplied — manuscript only; no code, no configuration, no result/Source
  Data files, no raw sequencing data).
- **Source execution:** `NOT_APPLICABLE` (no code exists to execute).
- **Independent recomputation:** `PARTIALLY_RECOMPUTED` (5 pure-arithmetic
  checks performed and passed; all recomputation requiring raw measurement
  data is `BLOCKED`).
- **Computational reproducibility:** `NOT_APPLICABLE` (no computational
  pipeline artifact was supplied to attempt reproducing).
- **Reporting correspondence:** `BLOCKED` for claims requiring raw
  evidence; `PARTIALLY_VERIFIED` for the subset checkable via
  manuscript-internal cross-referencing (15 of 32 ledger entries).
- **Empirical data integrity:** `INSUFFICIENT_EVIDENCE` (no raw or
  processed dataset was inspected).
- **Configuration and model-input integrity:** `NOT_ASSESSED` (Methods-
  described pipeline parameters were read as prose only; no configuration
  file exists to check them against).

## 16. Author Queries

1. Which unit is correct for the iRGD peptide treatment arms described in
   the Methods ("1/10 mg kg⁻¹") and in the Extended Data Fig. 10 legend
   ("1/10 mg/ml") — are these the same two treatment conditions, and if so,
   which unit is the accurate one? (F-01)
2. Why does Extended Data Fig. 10 panel g use n=4 biologically independent
   replicates while adjacent panels c–f in the same figure use n=3? (F-02)
3. Would the authors be willing to specify, in the abstract or discussion,
   that the causal claim rests on a fusion event found in 2 of 37 (5.4%)
   screened metastatic osteosarcoma patients at a single institution,
   rather than the more general disease-wide framing currently used? (F-03)
4. Which specific cancer types and how many cases/cell lines support the
   Results-section statement that this class of fusion event occurs and
   drives metastasis "in multiple cancer types"? (F-04)

## 17. Blocked and Not-Checked Register

| Item | Status | Reason | What would resolve it |
|---|---|---|---|
| RNA-seq/WGS fusion-detection pipeline execution | `BLOCKED` | No code or raw sequencing data supplied | Supply the analysis pipeline code and/or retrieve SRP181860 |
| Clinical cohort raw screening results (RT-PCR/Sanger/FISH per-sample calls) | `BLOCKED` | Not supplied or deposited locally | Supply per-sample validation records |
| All figure/table Source Data (Figs. 1–8, Ext. Data Figs. 1–10) | `BLOCKED` | Journal-hosted Source Data not retrieved for this audit | Retrieve the journal's Source Data files |
| Survival-analysis recomputation (median survival 9.5 vs. 19 months) | `BLOCKED` | No patient-level survival data supplied | Supply de-identified patient-level survival records |
| Statistical test recomputation (P-values throughout) | `BLOCKED` | No raw per-replicate measurements supplied | Supply raw measurement data underlying each statistical test |
| Multiple-comparison-correction assessment | `NOT_CHECKED` | Feasible in principle from raw data, but raw data not supplied; already flagged as a reporting gap in `experiment-audit_report.md` | Supply raw data or authors' statistical analysis plan |

## 18. Limitations

- This audit is limited almost entirely to what is stated in the
  manuscript's own extracted text. No independent verification against
  primary data was possible for the large majority of claims.
- The claim ledger was adopted from this session's own
  `paper-claim-audit_report.md` rather than re-derived from scratch; this
  is a deliberate efficiency choice given the same manuscript text is the
  sole source for both, not an independent second extraction pass.
- No figure was regenerated, and no Source Data file was compared against
  any published figure value — this audit cannot rule out figure-level
  discrepancies that would only be visible with that data.
- The reviewer sub-agent used for claim cross-checking (`gpt-5.3-codex`)
  shares the same underlying claim-extraction pass used in the
  `paper-claim-audit` skill run earlier in this session; it is not a fully
  independent second read of the manuscript from zero context relative to
  that earlier run, though it was dispatched as a fresh thread with no
  memory of this conversation.

## 19. Output-Validation Result

- Output A and Output B (below) are generated from the same finding
  IDs (F-01–F-04) and the same facts. ✅
- Both human-readable outputs exist. ✅
- Output B does not strengthen any conclusion beyond what is stated here. ✅
- Counts reconcile (32 ledger claims; 19 figure/table artifacts; 4 distinct
  findings). ✅
- Every Output B assessment label agrees with the technical evidence
  state above. ✅
- No raw code, YAML, JSON, or implementation logs appear in Output B. ✅
- The machine-readable ledger (`research-package-integrity-audit2_ledger.json`)
  is kept separate from both human-readable outputs. ✅

**Output validation: PASS**
