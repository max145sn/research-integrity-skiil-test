# Experiment Audit Report — "Chromosomal translocation-derived aberrant Rab22a drives metastasis of osteosarcoma"

**Date**: 2026 (session date)
**Auditor**: External reviewer backend, fresh zero-context cross-model reviewer
(`gpt-5.3-codex`, high reasoning effort, sandboxed, no prior conversation
context), substituting for `mcp__codex__codex` per the `experiment-audit`
skill's reviewer-independence requirement (that MCP tool is unavailable in
this environment).
**Manuscript**: Liao, Y. et al., *Nature Cell Biology* (2020) — attached PDF
"Chromosomal translocation-derived aberrant Rab22a drives metastasis of
osteosarcoma", text extracted via PyMuPDF to
`../supporting-files/manuscript_extracted.txt` (122,750 characters, ~39 pages) for
read-only auditing.

## Skill/Target Mismatch Disclosure (read this first)

The `experiment-audit` skill's checklist (A. Ground Truth Provenance, B. Score
Normalization, C. Result File Existence, D. Dead Code Detection, E. Scope
Assessment, F. Eval Type Classification) is built for **local computational
ML/data-science experiment packages** — eval scripts, ground-truth generation
code, JSON/CSV result files, and an experiment tracker that can be
independently re-executed or recomputed from raw files.

This paper is a **wet-lab cancer-biology manuscript**, not a computational
repro package. There is:
- **No local eval/analysis code** (no `code/`, `scripts/`, or notebook of any
  kind for this paper anywhere in the repository or session files).
- **No local result files** (no CSV/JSON of raw measurements, no run logs).
- **No local ground-truth dataset** — the paper's RNA-seq/WGS data is
  deposited externally at SRA accession **SRP181860**, which was not fetched
  or provided to this audit.

Because of this, checks A-D **cannot be executed as literally specified**
(there is no code to recompute a number from, and no result file to diff
against a manuscript claim). Rather than mark them silently "PASS" or skip
them, this audit reports what **is** verifiable from the manuscript text
alone (internal arithmetic consistency, claim-to-evidence traceability,
statistical-reporting patterns) and explicitly discloses the residual
`NOT_ASSESSABLE` gap for anything that would require the missing raw files.
Checks E and F map onto this paper reasonably well and are executed at full
strength.

## Overall Verdict: FAIL

## Integrity Status: fail

The paper's own internal arithmetic (patient counts, percentages, survival
subgroup sizes) is self-consistent everywhere it could be checked. The FAIL
verdict is **not** a "fabricated data" finding (that would require the
externally-deposited raw sequencing files, which are `NOT_ASSESSABLE` here) —
it reflects a **scope-vs-claim mismatch**: the title/abstract-level causal
claim ("drives metastasis of osteosarcoma") is stated more broadly than the
depth of endogenous human evidence actually supports (a 2-patient positive
subgroup within a 97-sample cohort, with endogenous mechanistic work
concentrated in a single patient-derived cell-line pair), compounded by the
absence of any disclosed multiple-comparison correction across a large volume
of pairwise statistical tests.

## Checks

### A. Ground Truth / Reference Provenance: WARN
- **Evidence**: "we screened 97 clinical samples ... 2 out of 37 (5.4%) ...
  all 60 ... without metastasis were negative" (Results, clinical-cohort
  paragraph); "RNA-seq and WGS ... deposited ... SRP181860" (Data
  Availability); "hFOB1.19 ... used as control"; repeated "vector-only",
  "negative control shRNA/siRNA" (Results/Figure legends).
- **Details**: Provenance of the sequencing/patient data is declared (SRA
  accession) but the raw files were not fetched for this audit — see
  `NOT_ASSESSABLE` below. Comparator/control framework in the functional
  assays is internal (vector-only, scrambled shRNA) rather than an
  independent second cohort; no independent replication cohort is described.
- **NOT_ASSESSABLE**: whether the raw deposited SRA data (SRP181860)
  reproduce the reported cohort/genomic numbers — those files were not
  retrieved.

### B. Score/Metric Normalization and Statistical Red Flags: WARN
- **Evidence**: "P values were obtained by two-tailed Student's t-test ...
  Kaplan-Meier ... log-rank test" (Statistics and Reproducibility section);
  numerous panels reporting very small P-values across many pairwise
  comparisons; Reporting Summary contains a multiplicity-disclosure checklist
  item but the Methods text itself does not describe an implemented
  multiple-comparison correction (e.g., Bonferroni/FDR).
- **Details**: No self-referential/circular normalization was identified
  (percentages and fold-changes are stated against external denominators —
  e.g., 2/37 patients, not against the manipulated system's own baseline in a
  way that inflates the ratio). However, given the large number of pairwise
  statistical tests across figures, the absence of a disclosed
  multiple-comparison correction is a reporting-rigor gap, and per-panel
  replicate counts (n=3 in vitro, n=6-8 animals per group) are not
  cross-checked against raw source data here.
- **NOT_ASSESSABLE**: exact underlying numeric values behind each P-value
  (raw measurements, source-data spreadsheets) were not provided locally.

### C. Result File Existence & Claim-to-Text Consistency: WARN
- **Evidence**: Title/Abstract claim: "Rab22a ... drives metastasis of
  osteosarcoma"; Results: "Rab22a-NeoF1 ... promoted lung metastases ...
  decreased survival time of mice"; cohort figures "2 out of 37 (5.4%)",
  "60 ... without metastasis", 37+60 = 97 total screened.
- **Details**: All disclosed patient-cohort arithmetic checked out internally
  consistent (2/37 = 5.4%; 37 + 60 = 97 total). No local result CSV/JSON
  exists to independently re-derive these numbers from raw records, so this
  check is limited to **internal** consistency of the manuscript's own
  numbers, not independent recomputation from source data.
- **NOT_ASSESSABLE**: independent recomputation against raw/source-data files
  (not provided).

### D. Dead / Unused Experimental Elements: WARN
- **Evidence**: Data Availability/Reporting Summary references a genomic
  mutation database cross-reference (COSMIC/cBioPortal-style listing) that is
  not clearly tied back to a specific Results-section claim.
- **Details**: The large majority of Methods reagents/assays are referenced
  again in Results with specific figure anchors. At least one listed
  data-availability element does not clearly connect to a narrative claim —
  a minor "described but not visibly used" flag, not evidence of fabrication.
- **NOT_ASSESSABLE**: whether any locally-absent code/scripts contain dead
  logic — no code exists to inspect for this paper.

### E. Scope Assessment: FAIL
- **Evidence**: 97-patient screening cohort with only **2** fusion-positive
  metastatic patients; in vitro assays predominantly n=3 biologically
  independent replicates; in vivo cohorts predominantly n=6 (some n=8) per
  group; endogenous patient-derived material described as isolated "from a
  patient" (ZOS/ZOS-M primary/metastatic pair); title states the general
  claim "drives metastasis of osteosarcoma."
- **Details**: The headline causal/generality claim is broader than the
  empirical breadth actually tested. The clinical prevalence/survival signal
  rests on **2** fusion-positive patients out of 97 screened, and the
  endogenous (non-overexpression) mechanistic evidence in osteosarcoma is
  concentrated in cell lines derived from a **single** patient. This is a
  classic small-n-to-general-claim scope mismatch.

### F. Evaluation Type Classification: WARN
This paper uses five distinct wet-lab evidence types, each with different
adequacy for the strength of claim it supports:
- **clinical_cohort_correlational**: 97-sample screening + survival subgroup
  comparison (2 fusion-positive vs. 35 fusion-negative-metastatic patients).
  Adequate for a prevalence/association signal; **not adequate alone** for
  the paper's population-level causal framing.
- **cell_line_overexpression_system**: gain-of-function Rab22a-NeoF1
  overexpression plus orthotopic/tail-vein xenograft metastasis models.
  Adequate for mechanistic plausibility; does not by itself establish
  endogenous, patient-relevant causality.
- **cell_line_endogenous**: knockdown/rescue in the ZOS/ZOS-M
  patient-derived pair, plus fusion knockdown in additional lines. Useful
  corroboration, but narrow (single-patient origin for the primary
  endogenous pair).
- **animal_model_in_vivo**: xenograft metastatic burden and survival-time
  effects. Supports in vivo metastatic potential within the engineered
  model system.
- **biochemical_in_vitro**: SmgGDS-607 interaction, pull-down/co-IP, RhoA
  activation assays. Supports the proposed mechanism at the molecular level.

No individual evidence type is inadequate on its own terms — the issue is
that the **combination** is used to support a broader, general causal title
claim than any single evidence stream (or their combination, given the small
patient-positive n) fully carries.

## Action Items
- Qualify the title/abstract-level generalization ("drives metastasis of
  osteosarcoma") to explicitly note the finding is based on a rare fusion
  event (2/37 metastatic patients, 5.4% of the screened cohort) rather than a
  general osteosarcoma mechanism.
- Disclose whether any multiple-comparison correction was applied across the
  large number of pairwise statistical tests reported across figures; if
  none was applied, state this explicitly as a limitation.
- Explicitly state, in the Discussion or Limitations, that endogenous
  (non-overexpression) mechanistic evidence for this fusion in osteosarcoma
  derives from a single patient-derived cell-line pair, and that broader
  replication in additional patient-derived material is needed.
- Clarify the data-availability element (genomic mutation database
  cross-reference) that does not appear to connect to a specific Results
  claim, or remove it if unused.
- To fully close checks A-D, the raw SRA-deposited sequencing data
  (SRP181860) and any underlying source-data spreadsheets for the
  statistical panels would need to be retrieved and independently
  recomputed — this was outside the scope of files available to this audit.

## Claim Impact
- "Rab22a ... drives metastasis of osteosarcoma" (general/title-level claim):
  **needs qualifier** — supported mechanistically in engineered/model
  systems, but the human endogenous evidence base is a single positive
  fusion subgroup (2/37 patients) and a single patient-derived cell-line
  pair; the general framing overstates this scope.
- Clinical cohort arithmetic (2/37 = 5.4%; 37 + 60 = 97 total screened):
  **supported** — internally consistent throughout the text.
- Statistical significance claims (multiple P<0.0001-type results across
  many panels): **needs qualifier** — no disclosed multiple-comparison
  correction found despite a high volume of pairwise tests.
- Underlying raw sequencing/genomic data supporting cohort claims:
  **NOT_ASSESSABLE** — deposited externally (SRP181860), not retrieved for
  this audit.

## Reviewer Backend Note

As with the prior audits in this repository, `mcp__codex__codex` and
`mcp__manual_review__review` (the skill's specified reviewer backends) are
unavailable in this environment. The executor (Claude, this session)
collected the manuscript file path only and dispatched a separate, stateless
`task`-tool agent (`agent_type: general-purpose`, `model: gpt-5.3-codex`,
high reasoning effort, a single self-contained prompt with no reference to
this conversation or to the earlier `academic-paper-review` /
`academic-paper-reviewer` outputs already produced for this same paper) to
perform the actual A-F integrity judgment, preserving the skill's
reviewer-independence requirement. This report additionally documents, up
front, the fundamental mismatch between the skill's computational-package
checklist and this paper's wet-lab evidence base — a mismatch that does not
arise in this repository's other (computational) audit targets.
