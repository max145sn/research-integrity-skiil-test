# Research Package Integrity Audit — Technical Report
## Manuscript + Supplied Supplementary Data

**Manuscript:** "Chromosomal translocation-derived aberrant Rab22a drives metastasis of osteosarcoma"
**Journal / DOI:** Nature Cell Biology, https://doi.org/10.1038/s41556-020-0522-z
**Run scope:** This run adds a user-supplied file, `supplementary data.pdf`, to the package previously audited (manuscript text only). It supersedes nothing about the prior findings on the manuscript itself; those are preserved verbatim in `research-package-integrity-audit2_integrity-audit_without-supplementary-data.md` and are only summarized here where the new file affects their status.

---

## 1. Execution-mode disclosure

This audit performed **static inspection** of two documents (the manuscript's extracted text, already produced in the prior run, and the newly supplied supplementary PDF, extracted for this run). **No code was run, no runtime environment was used, and no source data files were present to recompute.** All evidence statuses in this report are `DIRECTLY_INSPECTED`, `CROSS_DOCUMENT_MATCH`, or `BLOCKED`; none are `EXECUTED` or `RECOMPUTED`.

## 2. Executive summary

The central result of this run is not a numerical discrepancy inside the manuscript, but a **package-composition finding**: the file supplied to this audit as "the supplementary data" for this manuscript does not appear to be this manuscript's own supplementary information.

- The manuscript's title, co-first-author order (Dan Liao, Li Zhong, Junqiang Yin), and corresponding authors (J.-N. Shen, Jian Chen, T. Kang) do not match the supplied PDF's title page ("Rab22a-NeoF1 fusion protein promotes osteosarcoma lung metastasis through its secretion into exosomes"; co-first authors Li Zhong, Dan Liao, Jingjing Li; correspondence Jianhua Sui and Tiebang Kang).
- The word "exosome" occurs **zero times** in the audited manuscript's full extracted text, yet it is the subject of all nine supplementary figures (S1–S9) in the supplied PDF.
- The supplied PDF does, however, reuse the exact fusion-protein name (RAB22A-NeoF1) and cell-line panel (143B, ZOS-M, U2OS) that this manuscript establishes, and shares a corresponding author (Tiebang Kang) with the manuscript.

The most defensible reading of this evidence is that the supplied document is supplementary material for a **separate, related follow-on publication** by an overlapping author/lab group studying the same fusion protein, not the official Nature Cell Biology supplementary information for this manuscript. This is stated as a directly-inspected observation, not an accusation of wrongdoing by either paper; no misconduct inference is made about either document.

**Practical consequence:** none of the manuscript's previously logged 32 claims or 19 figures/extended-data figures gain new verification evidence from this file. The manuscript-only findings (F-01 through F-04) and blocked/unresolved items from the prior run are unchanged. Two new items are logged for this run (F-05, F-06).

## 3. Preflight and scope

| Item | Status |
|---|---|
| Manuscript text | Available (from prior extraction) |
| Supplied supplementary_data.pdf | Available (17 pages, ~12.7k extracted characters; figure captions only, no data tables, no code) |
| Environment/tooling | Python + PyMuPDF for text extraction only; no execution environment needed or used |
| Scope of this run | Cross-check the newly supplied file against the manuscript; the manuscript-only claim/figure ledger from the prior run is carried forward unchanged |
| User scope/exclusions | No source files, code, or configuration were supplied for either document |

Preflight status: **PARTIAL** (a document was supplied, but it does not extend verification coverage of the manuscript).

## 4. File inventory and missing-artifact register

| Path | Type | Present |
|---|---|---|
| `../supporting-files/manuscript_extracted.txt` | Manuscript extracted text | Yes |
| `../supporting-files/supplementary_data.pdf` | User-supplied supplementary document | Yes |
| `../supporting-files/supplementary_data_extracted.txt` | Extracted text of the above | Yes |

Missing, manuscript-referenced artifacts (unchanged from the prior run, still absent):

| Artifact | Type | Status |
|---|---|---|
| SRA accession SRP181860 (RNA-seq/WGS) | Raw sequencing data | MISSING_FILE |
| Source Data for Figs. 1–8 and Extended Data Figs. 1–10 | Result data | MISSING_FILE |
| RNA-seq/fusion-detection analysis pipeline code | Code | MISSING_FILE |
| Clinical cohort screening dataset (97-sample RT-PCR/Sanger/FISH results) | Raw/derived clinical data | MISSING_FILE |
| Official Nature Cell Biology Supplementary Information for this DOI (Supplementary Tables 1–8) | Supplementary information | MISSING_FILE — see Section 6 |

Completeness denominator: 6 identified required/expected artifact categories; 3 classified as present, 3 absent (unchanged proportionally from the prior run, since the newly supplied document does not fill any of the manuscript's own gaps).

## 5. Study and evidence map

No new edges could be added between the manuscript's claim/figure nodes and the supplied supplementary document. The supplied document forms an **isolated node** in the evidence graph: 9 figures (S1–S9), each with a caption describing exosome-related experiments, none of which cite or are cited by any node in the manuscript's own evidence graph (built in the prior run).

## 6. Cross-document identity check (new in this run)

This section documents the direct comparison between the manuscript and the supplied supplementary file.

| ID | Proposition | Location | Evidence status |
|---|---|---|---|
| SC-01 | The manuscript states its own supplementary information is hosted at its own DOI (10.1038/s41556-020-0522-z). | manuscript text, "Additional information" section | DIRECTLY_INSPECTED |
| SC-02 | The supplied PDF's title page reads "Supplementary Materials for Rab22a-NeoF1 fusion protein promotes osteosarcoma lung metastasis through its secretion into exosomes," authored by Li Zhong, Dan Liao, Jingjing Li (co-first) et al., correspondence Jianhua Sui and Tiebang Kang. | supplementary_data_extracted.txt, lines 1–12 | DIRECTLY_INSPECTED |
| SC-03 | The manuscript's own title is "Chromosomal translocation-derived aberrant Rab22a drives metastasis of osteosarcoma," with a different co-first-author list (Dan Liao, Li Zhong, Junqiang Yin) and additional corresponding authors (J.-N. Shen, Jian Chen) absent from the supplied document. | manuscript text, header | DIRECTLY_INSPECTED |
| SC-04 | "Exosome" occurs 0 times in the manuscript's full extracted text, while it is the subject of all 9 figures in the supplied document. | full-text search of both documents | DIRECTLY_INSPECTED |
| SC-05 | The supplied document reuses the manuscript's fusion-protein name (RAB22A-NeoF1) and cell-line panel (143B, ZOS-M, U2OS). | 433 combined term matches in the manuscript; consistent terminology in every supplementary figure legend | CROSS_DOCUMENT_MATCH |

**Interpretation:** SC-01 through SC-04 directly demonstrate that the supplied file's title, authorship, and subject matter differ from the audited manuscript. SC-05 shows enough shared terminology and cell-line identity that the supplied document is very unlikely to be an unrelated or mismatched upload; it most plausibly documents a separate, related publication by an overlapping research group building on the fusion protein this manuscript first reports. This interpretation is offered with the certainty level stated in Finding F-05 below, not as a confirmed bibliographic fact (no external bibliographic database lookup was performed as part of this static audit).

## 7. Claim ledger

Claim-ledger status: **INCOMPLETE**, unchanged from the prior run. The full 32-item ledger for the manuscript's own claims is preserved in `research-package-integrity-audit2_ledger_without-supplementary-data.json`. This run adds five new, narrowly scoped claims (SC-01–SC-05, Section 6 above) concerning the identity of the supplied supplementary document; none of the original 32 manuscript claims change evidence status as a result.

## 8. Data-provenance checks

Not applicable in this run — no data files (raw, derived, or otherwise) were supplied in either the manuscript package or the newly added supplementary document. The supplementary document contains only figure images and their prose captions.

## 9. Code, configuration, and domain checks

Not applicable — no code or configuration files were supplied in either document.

## 10. Source-execution report

Status: `NOT_APPLICABLE`. No executable analysis artifacts exist in this package.

## 11. Independent-recomputation report

Status: `NOT_APPLICABLE`. No numerical claim in the supplied supplementary document maps to a manuscript-reported value, so there is nothing available to recompute against the manuscript.

## 12. Figure, table, and source-data correspondence

| Item | Correspondence status |
|---|---|
| Manuscript Figs. 1–8 and Extended Data Figs. 1–10 (19 figures, from prior run) | Still `FIGURE_EXECUTION_NOT_ATTEMPTED` / `FIGURE_CHECK_BLOCKED` — unchanged; the supplied supplementary document does not depict any of them. |
| Supplementary Figs. S1–S9 (in the newly supplied document) | `NOT_APPLICABLE_TO_THIS_MANUSCRIPT` — these figures document exosome-secretion experiments not referenced anywhere in the audited manuscript, so there is no manuscript claim or table for them to correspond to. |

## 13. Detailed findings

### F-05 — MAPPING_AMBIGUITY (new)
**Title:** Supplied "supplementary data.pdf" does not correspond to the audited manuscript's own supplementary information.
**Claim IDs:** SC-01, SC-02, SC-03, SC-04, SC-05
**Evidence status:** DIRECTLY_INSPECTED / CROSS_DOCUMENT_MATCH
**Description:** See Section 6 for the full comparison. Title, author correspondence, co-first-author order, and subject matter (exosome secretion) differ from the manuscript; the same fusion-protein name and cell-line panel are reused.
**Impact:** No manuscript claim or figure gains verification coverage from this file. Coverage is unchanged from the manuscript-only run.
**Severity:** `NOT_APPLICABLE` — this is a package-composition/file-provenance observation, not a discrepancy in a manuscript-reported value, so the impact-tested severity scale does not apply.
**Certainty:** High for the observed title/author/subject-matter mismatch; the true identity of the supplied document's source publication is not independently confirmed (no bibliographic database lookup was performed) and is offered as the most plausible interpretation, not a verified fact.
**Misconduct inference:** NONE.
**Reviewer action:** Confirm which document is intended as this manuscript's official supplementary information before relying on the supplied file for verification purposes.
**Author question:** Which document constitutes the official supplementary information for doi:10.1038/s41556-020-0522-z, and is the supplied exosome-focused document supplementary material for a separate, later publication?

### F-06 — REPRODUCIBILITY_LIMITATION (new)
**Title:** Manuscript's own declared supplementary material (Supplementary Tables 1–8) remains unsupplied.
**Evidence status:** BLOCKED
**Description:** The manuscript cites Supplementary Tables 1–8 fourteen times as the basis for cohort characteristics, fusion candidates, primers, siRNAs, and sgRNAs. Neither audit run received these tables.
**Impact:** All claims resting on these tables remain unverifiable.
**Severity:** UNDETERMINED — impact on any specific value was not tested because the tables were never available.
**Certainty:** High.
**Misconduct inference:** NONE.
**Reviewer action:** Request Supplementary Tables 1–8 directly from the publisher or authors.
**Author question:** Can Supplementary Tables 1–8 be supplied to allow verification of cohort size, fusion-candidate, primer, siRNA, and sgRNA claims?

### F-01 through F-04 (carried over, unchanged)
These findings concern the manuscript's own internal reporting consistency and scope claims and are unaffected by the newly supplied file. Full detail is preserved in `research-package-integrity-audit2_integrity-audit_without-supplementary-data.md`, Section "Detailed findings."

## 14. Checked but not raised

| Check | Result | Assessment |
|---|---|---|
| Whether the manuscript's own claims rely on, cite, or borrow support from any exosome-related result in the supplied document | No such reliance found; "exosome" occurs 0 times in the manuscript, and none of Figures S1–S9 are cited in the manuscript text. | POSITIVE — this is a completed check confirming the two documents are not improperly conflated within the manuscript's own argument. It does not confirm the supplied document's true source paper (see F-05). |

## 15. Reconciled coverage

```text
Manuscript claims total: 32
  Checkable via internal cross-reference: 15
  Blocked: 12
  Unresolved mapping: 2
  Scope findings: 2
  Reconciliation: PASS (unchanged from prior run)

Manuscript figures/extended-data figures total: 19
  Blocked: 19
  Checked: 0
  Reconciliation: PASS (unchanged from prior run)

Supplementary-document identity claims (new, this run): 5
  Directly inspected: 4
  Cross-document match: 1
  Reconciliation: PASS

Distinct findings this run: 2 (F-05, F-06)
Distinct findings cumulative: 6 (F-01–F-06)
```

## 16. Separate status architecture

| Dimension | Status |
|---|---|
| Package completeness | INCOMPLETE |
| Source execution | NOT_APPLICABLE |
| Independent recomputation | NOT_APPLICABLE |
| Computational reproducibility | NOT_APPLICABLE |
| Reporting correspondence | PARTIALLY_VERIFIED |
| Empirical data integrity | NOT_ASSESSED |
| Configuration/model-input integrity | NOT_APPLICABLE_FOR_EMPIRICAL_DATA |

## 17. Author queries

1. Which document constitutes the official supplementary information for doi:10.1038/s41556-020-0522-z, and is the supplied exosome-focused document supplementary material for a separate, later publication?
2. Can Supplementary Tables 1–8 be supplied to allow verification of cohort size, fusion-candidate, primer, siRNA, and sgRNA claims?

## 18. Blocked and not-checked register

| Item | Status | Reason |
|---|---|---|
| All 19 manuscript figures/extended-data figures | BLOCKED | No source data, code, or the manuscript's own supplementary figures were supplied; the new document does not depict them. |
| Supplementary Tables 1–8 | BLOCKED | Not supplied in either run. |
| Supplementary Figures S1–S9 (supplied document) | NOT_APPLICABLE_TO_THIS_MANUSCRIPT | Do not correspond to any manuscript claim, figure, or table. |

## 19. Limitations

- This audit is static inspection only; no execution or recomputation was possible or attempted.
- The claim that the supplied document belongs to a different, related publication is the most defensible reading of the internal textual evidence but was not confirmed against an external bibliographic source (e.g., a publisher database or DOI registry lookup), which was outside this audit's static-inspection scope.
- No new manuscript claims became verifiable as a result of this run; all limitations documented in the manuscript-only run persist unchanged.

## 20. Output-validation result

- Both Output A (this document) and Output B were generated from the same ledger (`research-package-integrity-audit2_ledger_with-supplementary-data.json`).
- Finding IDs, values, and locations agree between outputs.
- Output B does not strengthen any conclusion beyond what is stated here.
- All coverage counts reconcile (Section 15).

**Output validation: PASS**
