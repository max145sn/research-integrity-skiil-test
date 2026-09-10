# Universal Research Package Audit

A packaged, cross-disciplinary audit capability consisting of instructions, schemas, deterministic scripts, templates, references, fixtures, and tests.

## Quick start

```bash
python scripts/inventory_package.py PACKAGE_DIR --output audit-evidence/inventory.json
python scripts/inspect_tabular_data.py PACKAGE_DIR --output audit-evidence/tabular-profile.json
# Build or complete audit-ledger.json using the schemas and audit workflow.
python scripts/validate_audit.py audit-ledger.json
python scripts/build_reports.py audit-ledger.json --technical technical-audit.md --brief review-brief.md
```

## Framework

1. Universal evidence core runs on every package.
2. Evidence-profile detection selects compatible modules.
3. Population contracts govern all calculations.
4. Canonical claims link repeated manuscript occurrences.
5. Findings, verification limitations, and audit limitations are separate.
6. Deterministic scripts preserve arithmetic and report consistency.
7. The ledger is the source of truth.
8. Validation status is determined by the validator, not prose judgment.

## Extension contract

A module declares its required evidence profiles, checks, outputs, and not-applicable conditions. Modules must not override universal safeguards.
