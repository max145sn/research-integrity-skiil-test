# Repository assets

This repository includes several document bundles and one installed skill.

## Skill

- `.github/skills/paper-claim-audit/skill.md`
- `.github/skills/claim-grounding/skill.md`
- `.github/skills/citation-management/skill.md`
- `.github/skills/exploratory-data-analysis/skill.md`
  - `.github/skills/exploratory-data-analysis/assets/` — report_template.md
  - `.github/skills/exploratory-data-analysis/fixtures/` — proteomics_fixture.mztab, mass_spectrometry_fixture.mgf, structure_fixture.pdb
  - `.github/skills/exploratory-data-analysis/references/` — README.md
  - `.github/skills/exploratory-data-analysis/scripts/` — eda_analyzer.py
- `.github/skills/academic-paper-review/skill.md`
- `.github/skills/academic-paper-reviewer/skill.md`
  - `.github/skills/academic-paper-reviewer/agents/` — field-analyst-agent.md, eic-agent.md, methodology-reviewer-agent.md, domain-reviewer-agent.md, perspective-reviewer-agent.md, editorial-synthesizer-agent.md, devils-advocate-reviewer-agent.md
  - `.github/skills/academic-paper-reviewer/examples/` — hei_paper_review_example.md, interdisciplinary_review_example.md, subclaim_decomposition_example.md
  - `.github/skills/academic-paper-reviewer/references/` — calibration_mode_protocol.md, editorial_decision_standards.md, review_quality_thinking_framework.md
  - `.github/skills/academic-paper-reviewer/templates/` — editorial_decision_template.md, peer_review_report_template.md, revision_response_template.md
- `.github/skills/research-package-integrity-audit2/skill.md`
- `.github/skills/universal-research-package-audit/skill.md`
  - `.github/skills/universal-research-package-audit/modules/` — registry.yaml
  - `.github/skills/universal-research-package-audit/references/` — module-contract.md, population-and-denominator-rules.md, tolerance-rules.md
  - `.github/skills/universal-research-package-audit/schemas/` — audit-ledger.schema.json, finding.schema.json, population-record.schema.json
  - `.github/skills/universal-research-package-audit/scripts/` — build_reports.py, inspect_tabular_data.py, inventory_package.py, validate_audit.py
  - `.github/skills/universal-research-package-audit/templates/` — accessible-review-brief.md, technical-audit.md
  - `.github/skills/universal-research-package-audit/tests/` — test_validation.py, fixtures/
- `.github/skills/manuscript-consistency-audit/skill.md`
  - `.github/skills/manuscript-consistency-audit/references/` — cross-check-checklist.md, query-style.md
  - `.github/skills/manuscript-consistency-audit/scripts/` — dump_sheet.py, extract_package.py, scan_workbook.py
- `.github/skills/manuscript-data-integrity/skill.md`
  - `.github/skills/manuscript-data-integrity/references/` — discipline_checks.md
  - `.github/skills/manuscript-data-integrity/scripts/` — digit_analysis.py, duplicate_scan.py, grim_check.py, statcheck.py

## Core documents

- `paper/Manuscript.pdf`
- `results/Data.csv`
- `code/Code.R`

## Trial packages

- `trial/controlled_synthetic_claim_audit_package.zip`
- `trial/controlled_synthetic_claim_audit_package/`
- `trial/compact_tabular_benchmark_package.zip`
- `trial/compact_tabular_benchmark_package/`

## Notes

- The `.github/` folder is hidden in many file explorers, so the skill file may not be obvious at first glance.
- The `trial/` folder contains separate, isolated fixtures for trial runs.
