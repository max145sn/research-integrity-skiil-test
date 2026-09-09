---
name: research-package-integrity-audit2
description: >
  Audit a complete research package containing a manuscript, supplementary
  information, raw or processed data, source-data workbooks, analysis code,
  configurations, result files, tables, and figures. Build a study-to-file and
  claim-to-evidence map before checking data integrity, computational
  reproducibility, numerical correspondence, internal consistency, and
  reporting accuracy. Report only evidence-backed findings, classify blocked
  checks explicitly, preserve study-level granularity, and never infer
  misconduct from missing or inconsistent evidence.
---

# Research Package Integrity Audit

## Purpose

Perform a study-aware, evidence-calibrated, executable audit of a complete research package. The central requirement is to build and verify an evidence graph for each study and claim before performing integrity checks or issuing conclusions.

This skill is not a generic manuscript reviewer, a methodological quality assessment, or a publication-decision tool. It traces reported results through the supplied manuscript, supplementary information, data, code, configurations, outputs, tables, and figures.

## Use This Skill When

Use this skill when the user asks to:

- audit a manuscript and its data;
- verify a paper against source data;
- check whether reported results reproduce;
- compare a manuscript, supplementary information, code, and data;
- inspect a reproducibility bundle;
- check a research package for inconsistencies;
- validate tables or figures against source data and code;
- investigate whether reported numbers add up;
- identify unsupported claims;
- review code, configuration, result, or figure provenance;
- perform a research-integrity or complete-package audit.

Do not use this skill for a manuscript-only peer review unless the user explicitly requests package-level tracing and sufficient package materials are available. If only part of the package is supplied, run the applicable phases and mark the remainder as `BLOCKED` or `NOT_CHECKED`.

## Non-Negotiable Principles

1. **Map before measuring.** Do not recompute a statistic until the relevant chain has been mapped:

   `claim -> study -> experiment -> analysis -> data -> code -> output -> table/figure -> reported value`

2. **Inventory first.** The first substantive output must be a complete file inventory. Do not make an integrity conclusion while files remain unclassified without documented investigation.

3. **Attach an evidence status to every check and conclusion.** Never convert inspection or inference into verification.

4. **Preserve study-level granularity.** One missing or failed study must not invalidate a separate study that was successfully checked.

5. **Missing does not mean wrong.** Missing evidence limits verifiability. It does not establish invalidity.

6. **Static inspection is not reproduction.** Reserve “reproduced” for outputs that were regenerated or independently recomputed.

7. **Search broadly, report narrowly.** Examine the full supplied package, but raise only demonstrated contradictions, reproducible numerical mismatches, verified provenance failures, execution failures, and clearly blocked checks.

8. **No misconduct inference.** Never infer fabrication, falsification, deception, or intent solely from missing files, mismatches, duplicated records, broken code, undocumented exclusions, or incomplete documentation.

9. **No publication verdicts.** Do not recommend accept, reject, approve, retract, desk reject, or “do not rely on the paper.” Report evidence and separate statuses. The editor or user decides what the findings mean.

10. **Separate integrity, reproducibility, consistency, and methodology.** Methodological review notes must be reported separately from integrity findings.

11. **Apply discipline-specific checks only when applicable.** Do not mechanically apply GRIM, Benford analysis, multiple-testing rules, clinical risk-of-bias tools, terminal-digit analysis, or similar frameworks without evidence that they fit the study design and data.

12. **Do not silently modify the source package.** Preserve originals. Record every temporary transformation or environmental adaptation.

## Accepted Inputs

Inspect any supplied combination of:

- PDF, DOCX, LaTeX, or Markdown manuscripts;
- supplementary information;
- CSV, TSV, XLSX, or XLS files;
- R, R Markdown, or Quarto files;
- Python scripts or notebooks;
- Stata, SPSS, SAS, MATLAB, or Julia files where tooling permits;
- YAML, JSON, or TOML configurations;
- result files, logs, serialized objects, and cached outputs;
- figure images and source-data workbooks;
- README files, data dictionaries, preregistrations, protocols, rebuttal letters, and reporting checklists.

## Central Evidence Model

Construct an evidence graph whose nodes and links include:

```text
Manuscript claim
-> study
-> experiment
-> analysis
-> code entry point
-> input data
-> transformation
-> result object
-> table or figure
-> final reported value
```

Each mapping must be one of:

- `CONFIRMED`
- `PROBABLE`
- `UNRESOLVED`

A probable mapping must not be treated as confirmed. Record the evidence for filenames, variable names, code references, captions, output paths, hashes, metadata, and manuscript cross-references used to establish a mapping.

## Evidence Status Taxonomy

Assign one or more statuses to every check, claim decision, and finding:

- `EXECUTED`: supplied code or an identified entry point was run;
- `RECOMPUTED`: a result was independently calculated from mapped inputs;
- `DIRECTLY_INSPECTED`: the relevant source, formula, code, file, or value was directly read;
- `CROSS_DOCUMENT_MATCH`: corresponding content was matched across independent package artifacts;
- `INFERRED`: the conclusion depends on interpretation not directly established by supplied evidence;
- `NOT_APPLICABLE`: the check does not fit the study or evidence type;
- `BLOCKED`: a required dependency or artifact was unavailable or unreadable;
- `NOT_CHECKED`: the check was within possible scope but was not performed;
- `FAILED`: the attempted check or execution failed.

Use the most specific applicable label. If multiple labels apply, retain all of them and explain the sequence. Never describe an `INFERRED` or `DIRECTLY_INSPECTED` item as verified or reproduced.

## Error and Gap Taxonomy

Keep these conditions distinct:

- `MISSING_FILE`
- `UNREADABLE_FILE`
- `WRONG_FILE`
- `FILE_VERSION_MISMATCH`
- `CODE_DATA_SCHEMA_MISMATCH`
- `EXECUTION_FAILURE`
- `NUMERICAL_MISMATCH`
- `IMPLEMENTATION_ERROR`
- `REPORTING_ERROR`
- `METHODOLOGICAL_CONCERN`

Do not collapse missing evidence, contradictory evidence, execution failure, and analytical error into a single category.

## Workflow

### Phase 0: Preflight and Scope Declaration

Record:

- supplied files;
- readable files;
- unsupported formats;
- execution environment and available software;
- missing or unavailable dependencies;
- internet or external-service requirements;
- expected study types;
- user-requested scope;
- planned exclusions from the audit.

Set `Preflight status` to `READY`, `PARTIAL`, or `BLOCKED`.

Do not ask the user to map files unless automatic inspection cannot resolve the relationship. Investigate filenames, internal metadata, code I/O, captions, section names, variable schemas, and README instructions first.

### Phase 1: File Inventory and Package Extraction

Produce the file inventory before any integrity conclusion. Classify each file as:

- manuscript;
- supplementary information;
- raw data;
- processed or cleaned data;
- source data;
- code;
- configuration;
- result or cached output;
- figure;
- documentation;
- unknown or unclassified.

For every file, record path, type, size, readability, hash when feasible, likely study, likely role, and classification confidence.

#### Manuscripts and supplements

- Extract complete text, not isolated snippets.
- Preserve page, section, paragraph, table, figure, and line references where possible.
- Extract tables separately.
- Extract captions, cross-references, equations, and supplementary references.
- Record extraction confidence and unreadable regions.

#### Spreadsheets

Inspect:

- sheet names and used ranges;
- hidden or very hidden sheets;
- formulas and cached displayed values;
- named ranges and external links;
- merged cells, comments, filters, and hidden rows or columns;
- missing-value codes;
- cells presented as replicates that contain formulas;
- presentation-only formatting versus evidence-bearing cells.

Read formula views and cached-value views separately. A formula-derived value must not be treated as an observed replicate.

#### Code and notebooks

Identify:

- entry points and execution order;
- files read and written;
- libraries and package versions;
- seeds and random-state handling;
- working directories and absolute paths;
- environment dependencies;
- command-line arguments;
- configurations and values actually consumed;
- commented, dead, alternate, or inactive branches;
- hardcoded reported values;
- output filenames and serialization paths.

### Phase 2: Study, Experiment, and File Map

Create a formal study registry. Distinguish study, experiment, dataset, analysis, model, run, configuration, result file, figure or table, and manuscript claim.

Example:

```yaml
studies:
  - study_id: S1
    manuscript_sections:
      - "Results: Study 1"
    data_files:
      - path: Study1_raw.csv
        mapping_status: CONFIRMED
    code_sections:
      - path: analysis.R
        lines: 120-410
        mapping_status: CONFIRMED
    outputs:
      - table_s1.csv
      - figure_2.png

  - study_id: S2
    manuscript_sections:
      - "Results: Study 2"
    expected_data_files:
      - Study2_raw.csv
    status: BLOCKED_MISSING_DATA
```

Before linking files, determine whether they refer to the same population, subgroup, exclusions, weighting, adjustment, run aggregation, observed or simulated data, and analysis version.

### Phase 3: Quantitative and Verifiable Claim Ledger

Extract every verifiable claim and assign a stable unique ID. Define a claim unit as one independently checkable proposition. Split a sentence or paragraph into separate claim units when it contains distinct reported values, comparisons, populations, analyses, or scope statements.

Example:

```yaml
claim_id: C-014
study_id: S1
location: "manuscript.pdf, page 8, paragraph 2"
claim_type: group_mean
reported_value: 4.83
reported_precision: 2
population: female respondents
outcome: Use_F
analysis: descriptive mean
support_expected:
  - study1_data.csv
  - analysis.R
  - table_2
mapping_status: CONFIRMED
```

Include:

- sample sizes and exclusions;
- means, medians, dispersion, percentages, and ratios;
- test statistics, p-values, confidence intervals, and effect sizes;
- model coefficients and classification metrics;
- simulation outputs;
- comparative statements;
- “all,” “most,” “best,” and “consistent” claims;
- figure-derived statements;
- scope and generalization claims.

### Phase 4: Data Provenance and Structural Integrity

Assign each data-bearing file or object one role:

- `RAW_OBSERVED`
- `RAW_SIMULATED`
- `CLEANED`
- `DERIVED`
- `IMPUTED`
- `MODEL_INPUT`
- `MODEL_OUTPUT`
- `PREDICTION`
- `GROUND_TRUTH`
- `PRESENTATION_ONLY`
- `UNKNOWN`

Check, where applicable:

- IDs, row uniqueness, participant uniqueness, and duplicate records;
- overlap across studies, splits, folds, waves, or conditions;
- missingness and structural versus unexpected missingness;
- impossible values, range violations, and inconsistent coding;
- date or event ordering;
- group-size and denominator consistency;
- logical constraints defined by the manuscript or data dictionary;
- formulas in purported raw-data or replicate cells;
- hidden exclusions and undocumented filters;
- transformed columns and label provenance;
- overwritten outcomes or labels;
- derived or simulated values presented as observations.

Activate domain-specific constraints only when supported by a data dictionary, manuscript definition, protocol, preregistration, or appropriate subject-specific guide.

### Phase 5: Code-to-Data and Configuration Audit

Check whether:

- each imported file exists and is mapped to the intended study;
- imported columns exist and variable types match expectations;
- joins preserve intended cardinality and do not duplicate participants;
- filters correspond to reported exclusions;
- scores, reverse coding, and composite variables match the Methods;
- missing-value handling matches the manuscript;
- labels and group definitions correspond to manuscript terminology;
- seeds are set and reused appropriately;
- declared configurations are actually consumed;
- the code writes the claimed result or figure;
- supplied result files are generated rather than manually substituted;
- variables are overwritten in ways that change provenance;
- inactive code is described as executed;
- hardcoded metrics or reported values appear in outputs;
- result files originate from the mapped inputs and configuration;
- figures are generated from final rather than stale intermediate results.

#### Machine-learning module, when applicable

Check:

- train, validation, tuning, and test split integrity;
- leakage and label leakage;
- train/test or cross-fold overlap;
- duplicate samples across folds;
- validation or test data reused during tuning;
- evaluation on training data;
- metric denominators and threshold selection;
- inconsistent random split regeneration;
- selective seed retention;
- excluded failures or phantom result files;
- predictions joined to the correct ground truth;
- configuration values declared but ignored.

#### Simulation and computational-model module, when applicable

Check:

- parameter-source mapping;
- initial conditions and units;
- numerical method and solver settings;
- tolerance and convergence checks;
- parameter sweeps and uncertainty propagation;
- stochastic seeds and sample generation;
- matrix dimensions and model structure;
- whether outputs were generated from the reported parameter configuration.

Do not make biological or domain-plausibility conclusions unless the user explicitly requests methodological review and appropriate evidence is available. Keep such notes separate.

### Phase 6: Controlled Execution

Execute only after study mapping and dependency inspection. Use a clean or isolated environment where feasible. Preserve logs.

For each execution, record:

```yaml
execution_id: E-01
entry_point: analysis.R
environment: R 4.x
status: SUCCESS_WITH_WARNINGS
inputs_confirmed: true
input_hashes: {}
outputs_created:
  - table1.csv
  - figure2.png
output_hashes: {}
warnings:
  - random seed not set
adaptations: []
```

Record package versions, entry point, working directory, seed state, input hashes, output hashes, stdout, stderr, warnings, and exit status.

Permitted temporary interventions include changing a working-directory path, installing a declared dependency, converting an unsupported format, or replacing an unavailable absolute path with the supplied local file. Record each intervention. If an intervention was required, use `REPRODUCED_WITH_ENVIRONMENTAL_ADAPTATION`, not “fully reproduced.”

A branch that looks correct but was not executed remains `DIRECTLY_INSPECTED`, not `EXECUTED`.

### Phase 7: Independent Recomputation

Do not rely solely on supplied code. Independently calculate mapped claims where feasible, including:

- counts, missingness, and group sizes;
- means, medians, SDs, and SEs;
- confidence intervals and percentages;
- effect sizes and conventional test statistics or p-values;
- confusion matrices and prediction metrics;
- summary-table formulas;
- figure values where extractable.

Set tolerances from reported precision and statistic type, not a universal percentage threshold. Default rules:

```yaml
exact_integer: 0
percentage_tolerance: "0.05 percentage points unless reported precision implies a tighter rule"
rounded_value_tolerance: "half of the final reported unit"
p_value_rule: "compare at reported precision and account for inequality notation"
```

Document formulas, software, population, exclusions, denominator, weighting, and rounding used in every recomputation.

### Phase 8: Figures, Tables, and Source-Data Correspondence

For each figure and table:

- locate the manuscript caption and cross-references;
- locate the source-data sheet or output object;
- identify the exact code and configuration that generate it;
- compare labels, units, conditions, legends, panel letters, and ordering;
- compare table values with mapped source data;
- determine whether the display represents one run, an aggregate, observed data, or model predictions;
- regenerate it where feasible;
- inspect image metadata only as supporting evidence;
- report manual edits only when demonstrable.

Use statuses such as:

- `FIGURE_REGENERATED_MATCH`
- `FIGURE_NUMERICALLY_MATCHED`
- `FIGURE_LABEL_MISMATCH`
- `FIGURE_SOURCE_UNAVAILABLE`
- `FIGURE_CHECK_BLOCKED`

A nearby code block labelled with a figure number is not proof of correspondence.

### Phase 9: Contradiction Reconciliation

When manuscript, table, code, configuration, and data disagree, test plausible explanations before raising a mismatch:

1. rounding;
2. filtered versus full sample;
3. adjusted versus unadjusted analysis;
4. weighted versus unweighted estimate;
5. single run versus aggregate;
6. observed versus simulated value;
7. alternate denominator;
8. different study or subgroup;
9. online-first versus print version;
10. software-version difference;
11. stale cached result;
12. transcription error.

Record each tested explanation and its outcome. Raise a numerical inconsistency only after the relevant alternatives have been evaluated or explicitly marked blocked.

### Phase 10: Findings Classification

Use these finding categories:

- `FILE_OR_PACKAGE_GAP`
- `MAPPING_AMBIGUITY`
- `DATA_PROVENANCE_GAP`
- `DATA_STRUCTURE_ERROR`
- `REPLICATE_COUNT_MISMATCH`
- `FORMULA_ERROR`
- `CODE_DATA_MISMATCH`
- `EXECUTION_FAILURE`
- `NUMERICAL_MISMATCH`
- `FIGURE_TABLE_MISMATCH`
- `REPORTING_INCONSISTENCY`
- `CONFIGURATION_MISMATCH`
- `UNSUPPORTED_SCOPE_CLAIM`
- `REPRODUCIBILITY_LIMITATION`
- `METHODOLOGICAL_REVIEW_NOTE`

Use `METHODOLOGICAL_REVIEW_NOTE` only in a separate section. Do not present it as an established integrity issue.

Each finding must contain:

```yaml
finding_id: F-007
category: NUMERICAL_MISMATCH
study_id: S1
claim_id: C-014
location: "manuscript.pdf, page 8, paragraph 2"
severity: MAJOR
certainty: DEMONSTRATED
evidence_status:
  - RECOMPUTED
evidence_method:
  - INDEPENDENT_RECOMPUTATION
reported: 4.83
recomputed: 4.51
tolerance: 0.005
innocent_explanations_tested:
  - rounding
  - subgroup filtering
  - missing-value denominator
impact:
  - affects Table 2
  - affects Results paragraph
misconduct_inference: NONE
author_question: "Please check ..."
```

Use conservative severity and certainty labels. A blocked check is not a finding that the reported result is wrong.

## Verdict Architecture

Never issue one binary verdict for the paper. Report separate dimensions.

### Package completeness

- `COMPLETE`
- `PARTIALLY_COMPLETE`
- `INCOMPLETE`
- `UNDETERMINED`

### Computational reproducibility

- `FULLY_REPRODUCED`
- `SUBSTANTIALLY_REPRODUCED`
- `PARTIALLY_REPRODUCED`
- `BLOCKED`
- `FAILED`
- `NOT_APPLICABLE`

### Reporting correspondence

- `MATCHES`
- `MINOR_DISCREPANCIES`
- `MATERIAL_DISCREPANCIES`
- `PARTIALLY_VERIFIED`
- `BLOCKED`

### Data-integrity evidence

- `NO_DEMONSTRATED_ISSUES`
- `DEMONSTRATED_ISSUES`
- `INSUFFICIENT_EVIDENCE`
- `NOT_ASSESSED`

Provide these statuses for the package and, where applicable, for each study. `NO_DEMONSTRATED_ISSUES` means only that no issue was demonstrated within the completed checks. It does not establish absence of all possible issues.

## Required Deliverables

### Part 1: Executive Audit Summary

Keep this concise. Include:

- package completeness;
- studies checked and blocked;
- reproduced outputs;
- material findings;
- limitations;
- neutral overall status.

Example neutral language:

> The supplied package is partially complete. Study 1 was substantially reproduced, with two minor reporting discrepancies. Study 2 could not be verified because its raw data were not supplied. No conclusion about Study 2's correctness or research misconduct follows from that absence.

### Part 2: File Inventory and Study Map

Show relationships among manuscript sections, datasets, code, configurations, results, tables, and figures. Include unresolved and probable mappings.

### Part 3: Coverage Report

Report complete denominators, not only successful checks. Include at minimum:

```text
Claims identified: 53
Recomputed: 34
Cross-checked only: 9
Blocked: 7
Not applicable: 3
Not checked: 0

Figures identified: 6
Regenerated: 4
Numerically checked only: 1
Blocked: 1
```

Also report files inventoried, files classified, studies mapped, executions attempted, tables checked, and spreadsheet sheets inspected where applicable.

### Part 4: Detailed Findings

For each finding include exact location, claim, evidence, calculation, tolerance, reconciliation attempts, impact, certainty, evidence status, and a neutral author question.

### Part 5: Checked but Not Raised

List meaningful candidate issues that were investigated and not raised, with the reason. This demonstrates search breadth and application of the certainty threshold.

### Part 6: Ready-to-Send Author Queries

Each query must:

- identify the location;
- ask the author to check or clarify;
- avoid accusation and motive attribution;
- avoid speculative diagnoses;
- use one paragraph per bullet.

### Part 7: Machine-Readable Audit Ledger

Produce JSON or YAML containing:

- file inventory;
- study mappings;
- claims;
- evidence graph edges;
- executions;
- findings;
- coverage;
- blocked checks;
- tolerances;
- transformations and environmental adaptations made during auditing.

Validate that identifiers and references are internally consistent.

## Required Language Discipline

Prefer:

- “The supplied evidence does not reproduce the reported value.”
- “This check was blocked because the mapped raw-data file was not supplied.”
- “The code was inspected but not successfully executed.”
- “No issue was demonstrated within the completed checks.”

Do not say:

- “The value was fabricated.”
- “The study is invalid” solely because evidence is missing.
- “The package is reproducible” after static inspection only.
- “No integrity concerns exist.”
- “Approve for publication.”

## Output Validation Checklist

Before finalizing the audit, verify that:

- every supplied file appears in the inventory;
- every unclassified file was investigated and remains explicitly unresolved if necessary;
- every study has its own status;
- every claim has a stable ID and location;
- every conclusion has an evidence status;
- probable mappings were not silently promoted to confirmed;
- recomputations use the correct study, population, exclusions, denominator, configuration, and precision;
- formulas and cached spreadsheet values were distinguished;
- static inspection was not reported as execution or reproduction;
- missing evidence was not reported as contradictory evidence;
- blocked checks are explicitly listed;
- methodological notes are separated from integrity findings;
- no misconduct inference or publication recommendation appears;
- coverage counts reconcile with the detailed ledgers;
- machine-readable identifiers and references are valid;
- temporary adaptations and transformations are fully logged.

If any validation item fails, correct the report or mark the relevant output as `FAILED` or `BLOCKED` rather than overstating completion.

## Implementation Guidance

Use deterministic scripts for inventory, extraction, formula inspection, code I/O scanning, calculations, figure comparisons, and ledger validation. Use model reasoning for study mapping, claim interpretation, contradiction reconciliation, applicability decisions, and report writing.

A recommended implementation can include:

```text
research-package-integrity-audit/
├── SKILL.md
├── README.md
├── references/
│   ├── evidence-status-taxonomy.md
│   ├── finding-categories.md
│   ├── tolerance-rules.md
│   ├── statistical-checks.md
│   ├── spreadsheet-audit.md
│   ├── code-provenance.md
│   ├── ml-integrity-checks.md
│   └── simulation-model-checks.md
├── templates/
│   ├── executive-summary.md
│   ├── findings-report.md
│   ├── author-queries.md
│   ├── claim-ledger.yaml
│   ├── study-map.yaml
│   └── audit-ledger.schema.json
├── scripts/
│   ├── inventory_package.py
│   ├── extract_manuscript.py
│   ├── inspect_workbook.py
│   ├── scan_code_io.py
│   ├── build_claim_ledger.py
│   ├── compare_statistics.py
│   ├── validate_figures.py
│   └── validate_audit_output.py
└── tests/
    ├── clean_control/
    ├── missing_study_data/
    ├── spreadsheet_formula_error/
    ├── manuscript_number_mismatch/
    ├── ml_leakage/
    ├── simulation_seed_issue/
    └── multi_study_mapping/
```

## Development Priorities

1. Build the evidence model: inventory, study map, claim ledger, status taxonomy, and completeness classification.
2. Add deterministic checkers: workbook formulas, descriptive and inferential recomputation, file I/O mapping, configuration comparison, prediction-label joins, and duplicate or ID checks.
3. Add controlled execution with dependency, version, seed, entry-point, hash, and adaptation logging.
4. Add discipline modules initially for survey or behavioral data, machine learning, computational ODE models, and laboratory replicate workbooks.
5. Test against clean controls, subtle planted errors, incomplete packages, misleading filenames, multi-study packages, simulated studies, computational models, machine-learning experiments, and spreadsheet-only packages.
6. Calibrate severity and author-query wording with domain experts.

Suggested acceptance targets:

```text
Clean-control false positives: 0 major findings
Planted major-error recall: at least 90%
Study-to-file mapping accuracy: 100% on benchmark packages
Blocked-check accuracy: at least 95%
Misconduct inferences: 0
Unsupported publication recommendations: 0
```

## Final Governing Rule

Build a verified evidence graph for every study and claim before performing integrity checks or issuing conclusions. The target is a study-aware, evidence-calibrated, executable research-package audit, not a broad manuscript review.
