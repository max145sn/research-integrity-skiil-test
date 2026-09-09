---
name: universal-research-package-audit
description: >
  Universally audit research packages containing arbitrary combinations of manuscripts,
  supplements, data, code, configurations, models, figures, tables, laboratory records,
  qualitative materials, and repository metadata. Always run the universal evidence audit,
  dynamically activate compatible evidence-type modules, and explicitly mark unsupported
  specialist validation. Produce a technical audit, an accessible review brief, a validated
  machine-readable ledger, and a reproducible audit-evidence bundle. Never infer misconduct
  or make publication decisions.
---

# Universal Research Package Audit

## Governing rule

Build and validate this evidence chain before issuing a conclusion:

`claim -> study -> experiment -> analysis -> code/workflow -> input -> population -> transformation -> result -> table/figure -> reported statement`

## Required inputs

Accept any files supplied by the user. Do not require a specific discipline or file type. Treat absent artifacts as unavailable evidence, not proof of error.

## Required outputs

Create all four outputs:

1. `technical-audit.md`: complete evidence, calculations, findings, coverage, and limitations.
2. `review-brief.md`: accessible, table-first summary using POSITIVE, CONCERN, LIMITATION, NOT ASSESSED, NOT APPLICABLE, and UNRESOLVED.
3. `audit-ledger.json`: source of truth conforming to `schemas/audit-ledger.schema.json`.
4. `audit-evidence/`: inventory, hashes, calculation records, scripts, logs, and validation result.

Do not deliver unless all four outputs exist. If validation cannot run, label validation `MANUAL_CHECK_ONLY`, never `PASS`.

## Mandatory execution order

1. Run `scripts/inventory_package.py` on the supplied package.
2. Classify artifacts by evidence structure, not merely by discipline.
3. Extract manuscript sections and claim occurrences.
4. Build canonical claims and link repeated occurrences.
5. Build study, experiment, analysis, artifact, and evidence-graph records.
6. Create a population record before every count, percentage, rate, ratio, richness value, model metric, or grouped calculation.
7. Run compatible universal and optional module checks.
8. Execute supplied workflows where feasible, preserving originals and logging adaptations.
9. Independently recompute feasible claims using deterministic scripts.
10. Separate research-package findings, verification limitations, and audit limitations.
11. Generate both reports from the validated ledger using `scripts/build_reports.py`.
12. Run `scripts/validate_audit.py`. Its result governs the reported validation status.

## Universal audit core

Always perform:

- file inventory, hashing, readability, and version identification;
- artifact-role and evidence-role classification;
- study and experiment registry;
- manuscript-section coverage;
- canonical claim ledger with occurrence mapping;
- claim centrality and dependency mapping;
- study-to-file and claim-to-evidence graph;
- provenance and transformation tracing;
- population and denominator definition;
- cross-document and cross-file consistency checks;
- execution-state assessment;
- independent recomputation where feasible;
- table and figure provenance assessment;
- coverage reconciliation;
- detailed and accessible reporting;
- deterministic output validation.

## Evidence-profile detection

Detect one or more evidence profiles:

- counted observations;
- repeated measurements or time series;
- group comparisons;
- hierarchical or clustered data;
- predictive evaluation;
- numerical or simulation models;
- spatial evidence;
- image evidence;
- audio or video evidence;
- qualitative coding;
- laboratory measurements;
- documentary or archival evidence;
- aggregate-only evidence;
- unknown evidence structure.

Activate only checks whose requirements are met. If a specialist method cannot be validated, continue the universal audit and report `SPECIALIST_METHOD_VALIDATION: NOT_ASSESSED`.

## Evidence and mapping statuses

Evidence statuses: `EXECUTED`, `RECOMPUTED`, `DIRECTLY_INSPECTED`, `CROSS_DOCUMENT_MATCH`, `INFERRED`, `NOT_APPLICABLE`, `BLOCKED`, `NOT_CHECKED`, `FAILED`.

Mapping statuses: `CONFIRMED`, `PROBABLE`, `UNRESOLVED`.

Execution statuses: `ENVIRONMENT_READY`, `ENVIRONMENT_PARTIAL`, `ENVIRONMENT_CHECK_FAILED`, `EXECUTION_NOT_ATTEMPTED`, `EXECUTION_ATTEMPTED_FAILED`, `EXECUTION_SUCCEEDED`, `EXECUTION_SUCCEEDED_WITH_WARNINGS`, `REPRODUCED_WITH_ENVIRONMENTAL_ADAPTATION`, `EXECUTION_BLOCKED`.

Validation statuses: `PASS`, `CONDITIONAL_PASS`, `MANUAL_CHECK_ONLY`, `FAILED`, `NOT_RUN`.

Never convert inspection into execution, missing evidence into contradiction, or absence of detected problems into proof of integrity.

## Population contract

Before calculating, record:

- unit of analysis;
- source file and source columns;
- numerator and denominator;
- inclusion and exclusion rules;
- positive-count requirements;
- placeholder handling;
- missing-value handling;
- weighting;
- grouping and aggregation;
- mapping confidence.

Test plausible alternatives when any element is ambiguous. Zero-count placeholders, empty categories, aggregate count columns, duplicate records, and mixed data types must be explicitly tested.

If an unresolved population choice can change a result, assign `DEPENDENCY_UNRESOLVED` to that claim and every dependent claim.

## Claim contract

Every identifiable claim receives a stable ID even when blocked. Record:

- canonical claim and all manuscript occurrences;
- exact location;
- study and analysis;
- type and centrality (`CENTRAL`, `SUPPORTING`, `DESCRIPTIVE`, `CONTEXTUAL`);
- dependencies;
- expected evidence;
- mapping and evidence status;
- population record where applicable;
- verification outcome.

Report both unique claims and claim occurrences. A parameter ledger is not a complete claim ledger.

## Finding and limitation separation

Use three registers:

1. `RESEARCH_PACKAGE_FINDING`: demonstrated discrepancy or structural condition in supplied evidence.
2. `VERIFICATION_LIMITATION`: missing artifact, inaccessible runtime, unresolved provenance, or other blocker.
3. `AUDIT_LIMITATION`: feasible audit work not completed or unsupported specialist validation.

For missing code or evidence, report both:

- `verification_impact`: how much verification is blocked;
- `result_correctness_impact`: normally `NOT_DETERMINED` unless evidence establishes an effect.

Do not treat a verification limitation as proof that a research result is wrong.

## Severity and assessment

Assign `MINOR`, `MAJOR`, or `CRITICAL` only when impact has been tested. Otherwise use `UNDETERMINED`.

Accessible assessment labels:

- `POSITIVE`: a completed check supports correspondence within its scope;
- `CONCERN`: a demonstrated discrepancy or provenance problem;
- `LIMITATION`: verification could not be completed;
- `NOT_ASSESSED`: feasible or specialist work was not completed;
- `NOT_APPLICABLE`: check does not fit the evidence;
- `UNRESOLVED`: evidence does not support a determinate classification;
- `NEUTRAL`: factual condition neither supports nor contradicts correctness.

Always explain the label in plain language. Never use color alone.

## Reconciliation and sensitivity

Before raising a contradiction, test applicable alternatives including rounding, unit of analysis, positive-count filtering, placeholders, full versus filtered population, weighted versus unweighted analysis, available versus complete cases, subgroup differences, adjusted versus unadjusted analysis, single run versus aggregate, observed versus simulated evidence, alternate denominators, versions, software differences, caches, and transcription.

Classify outcomes as `MATCH`, `ROBUST_MISMATCH`, `SPECIFICATION_DEPENDENT`, `MAPPING_AMBIGUITY`, `BLOCKED`, `NOT_CHECKED`, or `NOT_APPLICABLE`.

## Figures and tables

Separate:

- intended code mapping;
- source-data mapping;
- result-object mapping;
- published-artifact provenance;
- published-value comparison;
- regeneration.

Do not use `FIGURE_NUMERICALLY_MATCHED` unless published or supplied figure values were actually compared.

## Coverage and validation stop conditions

Coverage categories sharing a denominator must be mutually exclusive and sum exactly. Distinguish claims, claim occurrences, affected cells, distinct discrepancies, findings, verification limitations, and audit limitations.

`PASS` is allowed only when `scripts/validate_audit.py` returns PASS with no unresolved errors. Use `CONDITIONAL_PASS` when structure and arithmetic pass but material assumptions remain unresolved. Use `MANUAL_CHECK_ONLY` when deterministic validation was not run.

## Output A: technical audit

Follow `templates/technical-audit.md`. Include execution disclosure, inventory, section coverage, evidence graph, claims, population records, computations, figures/tables, findings, limitations, checked-but-not-raised items, reconciled coverage, separate statuses, author queries, and validation result.

## Output B: accessible review brief

Follow `templates/accessible-review-brief.md`. Use descriptive headings and tables instead of raw code, YAML, JSON, hashes, or tool logs. Include:

- review at a glance;
- issues requiring attention;
- what checked out well;
- what could not be verified;
- paper navigation guide;
- author questions;
- what is good, what needs attention, what remains unknown, and what this does not mean.

The brief may simplify phrasing but must not remove qualifications or strengthen conclusions.

## Prohibited conclusions

Never infer fabrication, falsification, deception, or intent. Never recommend acceptance, rejection, approval, retraction, or whether readers should rely on the paper. Report evidence, scope, and uncertainty only.
