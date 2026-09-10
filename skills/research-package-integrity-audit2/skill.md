---
name: research-package-integrity-audit2
description: >
  Audit complete research packages by mapping manuscript claims to studies,
  data, code, configurations, outputs, tables, and figures before checking
  integrity, reproducibility, and reporting correspondence. Produce a detailed
  technical audit, an accessible issue-focused review brief, and a shared
  machine-readable ledger. The accessible brief remains factual and serious,
  uses plain language and table-first presentation, and clearly labels each
  result as positive, concerning, limiting, neutral, or not assessed without
  inferring misconduct or making publication decisions.
---

# Research Package Integrity Audit

## Governing Rule

Build a verified evidence graph for every study and claim before performing checks or issuing conclusions:

`claim -> study -> experiment -> analysis -> code entry point -> input -> configuration -> transformation -> result object -> table or figure -> reported value`

This skill audits evidence correspondence. It does not detect intent, infer misconduct, or make publication decisions.

## Trigger Conditions

Use this skill when the user asks to audit a manuscript and its data or code, verify reported results, inspect a reproducibility package, validate tables or figures, investigate numerical consistency, identify unsupported claims, or trace code and result provenance.

If only part of the package is supplied, complete the feasible work and label the remaining checks `BLOCKED` or `NOT_CHECKED`. Never present a partial audit as a complete audit.

## Non-Negotiable Principles

1. Inventory first.
2. Map before measuring.
3. Preserve study-level granularity.
4. Missing evidence limits verification but does not establish error.
5. Static inspection is not execution or reproduction.
6. Source execution and independent recomputation are separate.
7. Every conclusion carries an evidence status.
8. Every severity has a tested impact basis or is `UNDETERMINED`.
9. Coverage categories are mutually exclusive and arithmetically reconcile.
10. Methodological quality, reporting consistency, reproducibility, and integrity evidence receive separate statuses.
11. No fabrication, falsification, deception, or motive inference.
12. No accept, reject, approve, retract, or reliance recommendation.
13. Both human-readable reports are generated from one validated ledger.
14. Accessibility must not reduce factual precision, scope qualifications, or evidentiary seriousness.

## Evidence Statuses

Use:

- `EXECUTED`
- `RECOMPUTED`
- `DIRECTLY_INSPECTED`
- `CROSS_DOCUMENT_MATCH`
- `INFERRED`
- `NOT_APPLICABLE`
- `BLOCKED`
- `NOT_CHECKED`
- `FAILED`

Never describe `DIRECTLY_INSPECTED` or `INFERRED` evidence as reproduced.

## Mapping Statuses

Use:

- `CONFIRMED`
- `PROBABLE`
- `UNRESOLVED`

A caption or matching code heading can confirm intended code mapping. It cannot verify that the published figure was produced by that exact code version.

## Finding Categories

Use precise primary categories:

- `FILE_OR_PACKAGE_GAP`
- `MAPPING_AMBIGUITY`
- `DATA_PROVENANCE_GAP`
- `DATA_STRUCTURE_ERROR`
- `REPLICATE_COUNT_MISMATCH`
- `FORMULA_ERROR`
- `CODE_DATA_MISMATCH`
- `CODE_MANUSCRIPT_MISMATCH`
- `EXECUTION_FAILURE`
- `NUMERICAL_MISMATCH`
- `FIGURE_TABLE_MISMATCH`
- `REPORTING_INCONSISTENCY`
- `CONFIGURATION_MISMATCH`
- `UNSUPPORTED_SCOPE_CLAIM`
- `REPRODUCIBILITY_LIMITATION`
- `METHODOLOGICAL_REVIEW_NOTE`

Use `CODE_DATA_MISMATCH` only for a conflict between code and data. Use `CODE_MANUSCRIPT_MISMATCH` for manuscript-to-code constants or model definitions.

## Reader-Facing Assessment Labels

Every item in the accessible brief must explicitly explain whether it is good, bad, limiting, neutral, or unresolved. Do not force a binary good/bad label when the evidence supports a more precise interpretation.

Use these labels:

| Label | Meaning | Reader-facing wording |
|---|---|---|
| **POSITIVE** | A completed check supports correspondence or reproducibility within its stated scope. | “Good: the checked values agree.” |
| **CONCERN** | A demonstrated discrepancy, error, or provenance failure exists. | “Concern: the manuscript and code use different values.” |
| **LIMITATION** | Verification could not be completed because evidence, tooling, or scope was unavailable. | “Limitation: this result could not be checked.” |
| **NEUTRAL** | A factual condition is neither evidence for nor against correctness. | “Neutral: this figure is a conceptual diagram and was not expected to be code-generated.” |
| **NOT ASSESSED** | The item was within possible scope but was not evaluated. | “Not assessed: the analysis was technically feasible but not completed.” |
| **NOT APPLICABLE** | The check does not fit the study or artifact. | “Not applicable: there are no participant records in this simulation study.” |
| **UNRESOLVED** | Available evidence does not support a determinate classification. | “Unresolved: the relationship between these files is uncertain.” |

### Assessment-label rules

- Always pair the label with a one-sentence reason.
- `POSITIVE` means only that a specific completed check passed. It does not establish that the entire paper is correct.
- `CONCERN` must be tied to demonstrated evidence, not suspicion.
- `LIMITATION` is not a negative finding about the research. It is a limitation of verifiability.
- `NOT ASSESSED` is not the same as `BLOCKED`. Explain why the check was not completed.
- Never mark missing evidence as `CONCERN` about research correctness unless a reporting requirement itself is demonstrably unmet. Otherwise use `LIMITATION`.
- Avoid traffic-light color as the only signal. Always show the text label and explanation.

## Mandatory Completion Gates

### Gate 1: Inventory

Inventory every supplied file. Investigate unclassified files. List manuscript-referenced and inferred required artifacts separately. State the denominator and scope behind completeness claims.

### Gate 2: Study and evidence mapping

Map every checked claim to its study, analysis, inputs, code, configuration, result, and reported artifact. Separate intended code mapping, actual output provenance, numerical correspondence, and published-artifact correspondence.

### Gate 3: Claim ledger

Assign stable IDs to every independently verifiable claim, including claims that will end as `BLOCKED`, `NOT_CHECKED`, or `NOT_APPLICABLE`.

Include numerical claims, model behavior, comparisons, figure-derived claims, exclusions, scope statements, and words such as “all,” “most,” “best,” and “consistent.”

A parameter ledger is not a manuscript-wide claim ledger. If extraction is incomplete, state:

```text
Claim ledger status: INCOMPLETE
Reporting correspondence: PARTIALLY_VERIFIED or BLOCKED
```

### Gate 4: Execution-state precision

Distinguish:

- `ENVIRONMENT_READY`
- `ENVIRONMENT_PARTIAL`
- `ENVIRONMENT_CHECK_FAILED`
- `EXECUTION_NOT_ATTEMPTED`
- `EXECUTION_ATTEMPTED_FAILED`
- `EXECUTION_SUCCEEDED`
- `EXECUTION_SUCCEEDED_WITH_WARNINGS`
- `REPRODUCED_WITH_ENVIRONMENTAL_ADAPTATION`
- `EXECUTION_BLOCKED`

A missing runtime does not mean the code failed.

### Gate 5: Independent recomputation

A missing source runtime does not automatically block independent computation. Where feasible, use an available environment to evaluate formulas, recompute statistics, quantify discrepancies, verify dimensions, or independently implement selected calculations.

Report source execution, independent recomputation, and figure regeneration separately. Feasible but omitted work is `NOT_CHECKED`, not `BLOCKED`.

### Gate 6: Evidence-backed severity

Assign `MINOR`, `MAJOR`, or `CRITICAL` only after testing impact on values, conclusions, figures, tables, studies, samples, denominators, or evaluation integrity.

Otherwise use:

```text
Severity: UNDETERMINED
Reason: The discrepancy is demonstrated, but its effect was not evaluated.
```

### Gate 7: Coverage reconciliation

All categories sharing a denominator must be mutually exclusive and sum to the denominator. Distinguish affected cells from distinct findings.

```text
Parameter cells: 38
Matched or acceptable: 29
Not applicable: 6
Mismatching cells: 3
Total classified: 38
Reconciliation: PASS

Distinct discrepancies: 2
Distinct findings: 2
```

### Gate 8: Verdict scope

Use `MATCHES`, `MINOR_DISCREPANCIES`, or `MATERIAL_DISCREPANCIES` only when coverage is broad enough to characterize the stated domain. Otherwise use `PARTIALLY_VERIFIED`, `BLOCKED`, or `NOT_ASSESSED` and name the checked subset.

### Gate 9: Dual-output validation

Before delivery verify that:

- both human-readable outputs exist;
- both use the same finding IDs and facts;
- the concise report never strengthens the detailed report;
- all counts reconcile;
- every brief assessment label agrees with the technical evidence state;
- code syntax, YAML, JSON, and raw implementation logs are absent from the accessible brief unless indispensable;
- the machine-readable ledger remains separate from the brief.

## Audit Workflow

### Phase 0: Preflight

Record supplied files, readable files, unsupported formats, environment, available software, dependencies, expected study types, internet needs, user scope, and exclusions. Set `READY`, `PARTIAL`, or `BLOCKED`.

### Phase 1: Extraction and inventory

Extract complete manuscript and supplement text with page, section, table, figure, caption, equation, and cross-reference locations. Record extraction confidence.

For spreadsheets inspect sheet visibility, used ranges, formulas, cached values, names, links, comments, filters, missing codes, and formula-derived replicate cells.

For code inspect entry points, I/O, libraries, versions, seeds, paths, arguments, configurations, dead branches, overwritten variables, hardcoded outputs, and result objects.

### Phase 2: Study registry and evidence graph

Create nodes for studies, experiments, analyses, models, runs, configurations, datasets, results, tables, figures, and claims. Record confirmed, probable, and unresolved links.

### Phase 3: Claim ledger

Every independently verifiable claim receives an ID, exact location, type, reported proposition, expected support, mapping status, evidence status, and outcome. Identification is required even when verification is blocked.

### Phase 4: Data provenance and structural integrity

Classify data as `RAW_OBSERVED`, `RAW_SIMULATED`, `CLEANED`, `DERIVED`, `IMPUTED`, `MODEL_INPUT`, `MODEL_OUTPUT`, `PREDICTION`, `GROUND_TRUTH`, `PRESENTATION_ONLY`, or `UNKNOWN`.

Apply relevant checks for IDs, duplicates, overlap, missingness, ranges, coding, dates, denominators, formulas, exclusions, transformations, labels, and overwritten outcomes.

### Phase 5: Code, configuration, and domain checks

Check file existence, schemas, joins, filters, score construction, missing-value handling, labels, seeds, consumed configurations, generated outputs, hardcoded values, overwritten provenance, inactive branches, and stale outputs.

For machine learning inspect leakage, split overlap, tuning reuse, thresholds, denominators, seed selection, failed-run exclusion, fold duplication, and prediction-to-ground-truth joins.

For simulations inspect parameter sources, units, initial conditions, numerical methods, solver settings, convergence, sweeps, uncertainty, seeds, dimensions, and configuration-to-output correspondence.

### Phase 6: Controlled execution

Execute only after mapping. Preserve originals. Record environment, versions, entry point, seed state, hashes, warnings, errors, and every adaptation.

### Phase 7: Independent recomputation

Independently calculate applicable statistics, formulas, model quantities, prediction metrics, summary formulas, and figure values. Set tolerances from reported precision, not a universal percentage.

### Phase 8: Figures and tables

For each figure or table locate its caption, source, output object, code, and configuration. Compare values, labels, units, legends, panels, and aggregation type.

Use precise statuses such as:

- `FIGURE_CODE_SECTION_MAPPED`
- `FIGURE_UNDERLYING_FORMULA_RECOMPUTED`
- `PUBLISHED_FIGURE_PROVENANCE_VERIFIED`
- `FIGURE_REGENERATED_MATCH`
- `FIGURE_PUBLISHED_VALUES_COMPARED`
- `FIGURE_LABEL_MISMATCH`
- `FIGURE_EXECUTION_NOT_ATTEMPTED`
- `FIGURE_CHECK_BLOCKED`

Do not use `FIGURE_NUMERICALLY_MATCHED` unless published or supplied figure values were actually compared.

### Phase 9: Reconciliation

Before raising a mismatch, test rounding, population differences, exclusions, adjustment, weighting, aggregation, observed versus simulated values, denominators, subgroups, versions, software differences, caches, and transcription.

### Phase 10: Findings and statuses

Each finding records its ID, category, locations, claim IDs, evidence, reported and observed values, tolerance, reconciliation attempts, impact, severity basis, certainty, misconduct inference `NONE`, reviewer action, and author question.

### Phase 11: Generate and validate outputs

Build Output A, Output B, and the ledger from the same structured records. Run arithmetic and cross-output validation before declaring `PASS`.

## Required Output A: Comprehensive Technical Audit

Produce a detailed technical report containing:

1. Execution-mode disclosure
2. Executive summary
3. Preflight and scope
4. File inventory and missing-artifact register
5. Study and evidence map
6. Complete claim ledger or explicit incomplete status
7. Data-provenance checks
8. Code, configuration, and domain checks
9. Source-execution report
10. Independent-recomputation report
11. Figure, table, and source-data correspondence
12. Detailed findings
13. Checked but not raised
14. Reconciled coverage
15. Separate status architecture
16. Author queries
17. Blocked and not-checked register
18. Limitations
19. Output-validation result

Technical code snippets and machine-readable details may appear here when necessary, but explain their meaning in prose.

## Required Output B: Accessible Issue-Focused Review Brief

### Purpose and tone

Create a serious, factual, plain-language brief for researchers, reviewers, editors, and authors. It must help a reader locate issues and understand their significance without reading code or audit implementation details.

Use short sections, descriptive headings, concise paragraphs, and tables. Prefer tables over code blocks, YAML, JSON, raw vectors, formulas, file dumps, and long status lists.

Do not reduce scientific precision. Expand technical terms on first use and retain exact values, locations, evidence levels, and scope limitations.

### Accessibility rules

1. **Table-first presentation.** Use tables for findings, blocked checks, coverage, figure status, and author questions.
2. **No raw code by default.** Translate code into a readable description. For example, write “the code sets the human population to 624” rather than displaying a parameter vector.
3. **No YAML or JSON.** Keep the machine-readable ledger outside Output B.
4. **Define technical terms.** Introduce terms such as “independent recomputation” in plain language.
5. **Use descriptive headings.** Prefer “Two parameter values differ between Table 1 and the code” over “Findings.”
6. **State the practical meaning.** Every item answers: What happened? Is it positive, concerning, limiting, neutral, or not assessed? Why does it matter? What should the reviewer do?
7. **Use exact locations.** Include page, table, figure, section, supplement, or code-file reference without requiring the reader to interpret code syntax.
8. **Separate research issues from audit limitations.** Never place missing software in the same table as demonstrated manuscript errors without a clear type column.
9. **Prioritize actionable information.** Put demonstrated concerns first, then central limitations, then positive checks.
10. **Avoid implementation metadata in the opening.** Skill hashes, repository commits, tool-loading messages, and internal paths belong in an appendix or ledger, not the review snapshot.
11. **Avoid unexplained status codes.** If a code is shown, add a plain-language translation.
12. **Do not use color alone.** Labels must be readable in text and accessible to screen readers.

### B1. Review at a glance

Begin with a compact summary table:

| Area | Assessment | What this means |
|---|---|---|
| Package completeness | LIMITATION | Some material needed to verify central outputs was not supplied. |
| Checked manuscript-to-code values | CONCERN | Two values differ between the manuscript and code. |
| Independently recalculated results | POSITIVE | The selected formula was recalculated in a separate implementation. |
| Full source-code execution | LIMITATION | The original analysis was not run in its native environment. |
| Misconduct inference | NEUTRAL | The audit does not assess or infer intent. |

Use the actual audit facts, not these example outcomes.

Follow with no more than six plain-language bullets covering the most important facts.

### B2. Issues requiring attention

Use one row per finding:

| Priority | Assessment | Issue | Where to look | What the evidence shows | Why it matters | Recommended reviewer action |
|---:|---|---|---|---|---|---|
| 1 | CONCERN | Different value used for a model parameter | Table 1; Figure 3 analysis | The manuscript reports one value and the code uses another. | The effect was measured as ... | Ask which value generated the published figure. |

Rules:

- Put the finding ID in the issue title, such as `[F-02] Different latent-probability value`.
- Replace code syntax with prose.
- Exact values must remain visible.
- State “impact not yet determined” when impact was not tested.
- Do not call an issue minor or major without an evidence-backed impact assessment.
- Explain whether the item is a research concern or an audit limitation.

### B3. What checked out well

Always include a positive-results section so readers can distinguish passed checks from unchecked work.

Use a table:

| Assessment | Check completed | Result | Scope limitation |
|---|---|---|---|
| POSITIVE | Selected model parameters compared with the manuscript | The checked values agreed except for F-01 and F-02. | This does not cover untested simulation claims. |

Only include completed checks. Never convert “no issue found” into proof that the full package is correct.

### B4. What could not be verified

Use a separate table for blocked and not-assessed work:

| Assessment | Item | Why it could not be verified | Effect on the review | What would resolve it |
|---|---|---|---|---|
| LIMITATION | Figure 5 sensitivity analysis | Supporting analysis files were not supplied. | The figure and related claims remain unverified. | Supply the analysis code and outputs. |
| NOT ASSESSED | A feasible independent simulation | It was outside the completed audit scope. | No conclusion can be drawn from this audit. | Complete a follow-up calculation. |

Do not present these rows as evidence that the research is wrong.

### B5. Paper navigation guide

Use a short table to help the reviewer move through the paper:

| Paper location | What to check | Related item |
|---|---|---|
| Table 1 | Compare reported and coded parameter values | F-01, F-02 |
| Figure 3 | Confirm which values generated the published curves | F-01, F-02 |
| Figure 5 | Locate the missing sensitivity-analysis support | B-01 |

Only include locations with an issue, limitation, or high-value positive verification.

### B6. Author questions

Use a numbered table:

| # | Location | Question for the authors | Why this question is needed |
|---:|---|---|---|
| 1 | Table 1 and Figure 3 | Which value was used to generate the published figure? | The manuscript and code differ. |

Questions must remain neutral and must not speculate about intent.

### B7. Bottom line

End with four clearly labelled statements:

- **What is good:** summarize the strongest completed positive check.
- **What needs attention:** summarize the demonstrated concerns.
- **What remains unknown:** summarize the central blocked and not-assessed work.
- **What this does not mean:** state that the audit does not infer misconduct and that unchecked claims have not been validated or invalidated.

Use plain language and no more than 150 words.

### B8. Scope note

End with:

> This brief lists demonstrated issues, completed positive checks, and central verification limitations. A concern indicates an evidence-backed discrepancy, while a limitation indicates that verification could not be completed. Neither label implies misconduct. Absence from this brief does not mean every other claim was independently reproduced. See the comprehensive technical audit for the full evidence, coverage, and limitations.

## Shared Machine-Readable Ledger

Produce a separate JSON or YAML ledger as the source of truth. Include inventory, completeness denominators, study mappings, evidence-graph edges, claims, executions, independent recomputations, findings, assessment labels, severity bases, coverage, blocked and not-checked records, transformations, report-inclusion flags, and validation results.

Do not paste the ledger into the accessible brief unless the user explicitly requests it.

## Dual-Output Consistency Rules

- Output B may simplify wording but may not remove qualifications or strengthen conclusions.
- Every concern in Output B must exist in Output A and the ledger.
- Finding IDs, values, locations, categories, impact, severity, and evidence must agree.
- Every Output B item includes an assessment label and plain-language reason.
- `LIMITATION` and `NOT ASSESSED` must never be rewritten as research errors.
- `POSITIVE` must never imply whole-paper validation.
- Output B must include both concerns and positive completed checks.
- Output B must not contain raw code, YAML, JSON, hashes, commits, or tool-loading detail unless essential to the scientific finding.

## Status Architecture

Report separately:

- package completeness: `COMPLETE`, `PARTIALLY_COMPLETE`, `INCOMPLETE`, `UNDETERMINED`;
- source execution: `EXECUTION_SUCCEEDED`, `EXECUTION_SUCCEEDED_WITH_WARNINGS`, `REPRODUCED_WITH_ENVIRONMENTAL_ADAPTATION`, `EXECUTION_ATTEMPTED_FAILED`, `EXECUTION_NOT_ATTEMPTED`, `BLOCKED`, `NOT_APPLICABLE`;
- independent recomputation: `FULLY_RECOMPUTED`, `PARTIALLY_RECOMPUTED`, `BLOCKED`, `NOT_CHECKED`, `NOT_APPLICABLE`;
- computational reproducibility: `FULLY_REPRODUCED`, `SUBSTANTIALLY_REPRODUCED`, `PARTIALLY_REPRODUCED`, `BLOCKED`, `FAILED`, `NOT_APPLICABLE`;
- reporting correspondence: `MATCHES`, `MINOR_DISCREPANCIES`, `MATERIAL_DISCREPANCIES`, `PARTIALLY_VERIFIED`, `BLOCKED`, `NOT_ASSESSED`;
- empirical data integrity: `NO_DEMONSTRATED_ISSUES`, `DEMONSTRATED_ISSUES`, `INSUFFICIENT_EVIDENCE`, `NOT_ASSESSED`, `NOT_APPLICABLE_FOR_EMPIRICAL_DATA`;
- configuration and model-input integrity: `NO_DEMONSTRATED_ISSUES`, `DEMONSTRATED_ISSUES`, `PARTIALLY_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_ASSESSED`, `NOT_APPLICABLE`.

## Final Validation Checklist

Before delivery confirm:

- every supplied file is inventoried;
- completeness denominators are documented;
- every identifiable claim has a stable ID, even if blocked or not checked;
- mappings are evidence-backed;
- source execution and independent recomputation are separate;
- figure-code mapping is separate from published-figure provenance;
- every severity has a tested impact basis or is undetermined;
- coverage counts reconcile programmatically where possible;
- affected cells and distinct findings use separate denominators;
- methodological notes are separate;
- no misconduct inference or publication verdict appears;
- Output A and Output B agree;
- Output B contains assessment labels, plain-language reasons, tables, positive checks, concerns, limitations, navigation guidance, and author questions;
- Output B contains no unnecessary raw code or machine-readable blocks;
- `Output validation: PASS` is used only if every applicable item passes.

If any validation item fails, correct it or report `Output validation: FAILED` with the specific failures.

## Final Governing Rule

Produce a rigorous technical audit and an accessible review brief from the same validated evidence. The brief must be easier to read, not less factual. It must show readers what is positive, what is concerning, what limits verification, what was not assessed, why each classification applies, and what action to take next.
