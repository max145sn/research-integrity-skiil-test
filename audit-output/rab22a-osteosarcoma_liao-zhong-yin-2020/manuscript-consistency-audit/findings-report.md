# Manuscript Consistency Audit — Findings Report (for the editor)

**Manuscript:** "Chromosomal translocation-derived aberrant Rab22a drives metastasis of osteosarcoma"
**Journal / DOI:** Nature Cell Biology, https://doi.org/10.1038/s41556-020-0522-z
**Package supplied for this audit:** the manuscript PDF (main text, methods, Extended Data Figs. 1–10, and an appended Reporting Summary) and a file named `supplementary data.pdf`.

## Package scope note (read before the findings)

This skill checks whether a paper contradicts **itself** — across abstract, results, discussion, SI, tables and source data. That check depends on having a genuine, matching set of those documents. Two scope limitations apply here and bound everything below:

1. **No genuine supplementary information for this manuscript was available.** The supplied `supplementary data.pdf` was already established (in a separate `research-package-integrity-audit2` run on this same paper) to be titled, authored, and themed differently from this manuscript — it documents an exosome-secretion mechanism that this manuscript's main text never mentions, and most plausibly belongs to a related, later publication by an overlapping author group. Because of this, none of the manuscript's own Supplementary Tables 1–8 (cited 14 times in-text) or any genuine supplementary figures could be cross-checked against the main text. This is a package-identity question, not a manuscript-consistency finding, and it is not repeated as an author query here — it was already raised as an author question in the prior integrity-audit run.
2. **No source-data workbook and no rebuttal letter were supplied.** Categories of this audit that depend on a spreadsheet (recomputing means/SDs, checking replicate formulas, workbook hygiene, units-in-data) or on a rebuttal (checking promised revisions landed) could not be performed at all.

What **was** checkable, and was checked exhaustively: the main text, Methods, Extended Data figure legends, and the appended Reporting Summary — reading start to finish rather than sampling, per the skill's search step.

## What was searched

- **Headline metrics across the main text.** Traced every restated instance of the cohort figures (97 clinical samples; 61 male / 36 female; 37 with metastasis / 60 without; 2/37 = 5.4% RAB22A-NeoF-positive among metastatic cases; median survival 9.5 vs 19 months) from the Results section, the Methods section, the Discussion, and the appended Reporting Summary's "Population characteristics" field.
- **Figure and Extended Data figure numbering.** Confirmed the eight main-text figure legends (Fig. 1–8) and ten Extended Data figure legends (Extended Data Fig. 1–10) are sequential with no gaps, repeats, or numbers exceeding what exists.
- **In-text figure citations.** Searched for any citation to a main figure or Extended Data figure number that does not exist (for example, "Fig. 9", "Extended Data Fig. 11").
- **Panel-letter sequencing.** Read the panel-letter runs in the main-text figure legends for gaps or repeated letters.
- **Cross-reference targets.** Spot-checked several in-text figure citations against the content of the legend they point to (for example, the Fig. 1b/c citation for the RT–PCR/Sanger validation of RAB22A-NeoF1 and RAB22A-NeoF6).

## Findings

**None of the candidates found in this sweep clear the certainty bar for a demonstrable, self-contained contradiction.** Specifically:

- The cohort numbers reconcile exactly and consistently everywhere they appear: 61 + 36 = 97 (Reporting Summary vs Results' "97 clinical samples"); 37 + 60 = 97 (metastatic vs non-metastatic subgroup vs total screened); 2/37 = 5.4% is restated identically in the Results and again in the Discussion.
- The eight main-text figures and ten Extended Data figures are numbered sequentially with no gaps or repeats, and panel letters in the checked legends (for example, Fig. 1's a, b, c, d, e–g) run without repeats or gaps.
- One apparent cross-reference anomaly was investigated and **dismissed as a false lead**: a text search for "Fig. 9" and "Fig. 10" (numbers that do not exist among the eight main figures) initially returned several hits. On inspection, every one of these is a PDF-text-extraction artefact: the phrase "Extended Data Fig. 9b" (a real, correctly numbered citation) was split across a line wrap in the PDF-to-text conversion, so "Extended Data" and "Fig. 9b" landed on separate extracted lines and a naive search matched only the second fragment. Reading the surrounding sentence in full confirms the citation is "Extended Data Fig. 9b" (or "10a", "10c–f", etc.) throughout, not a bare "Fig. 9"/"Fig. 10". This is reported here only to show it was checked and ruled out — it is not a finding.

No headline metric, figure citation, or panel sequence in the checkable portion of this package (main text, Methods, Extended Data legends, Reporting Summary) was found to disagree with itself.

## Checked but not raised

| Candidate | Why it was not raised |
|---|---|
| "Fig. 9b" / "Fig. 9f" / "Fig. 10a" appearing to cite non-existent main figures | Confirmed to be a PDF-extraction line-wrap of "Extended Data Fig. 9b/9f/10a", not a manuscript error. See Findings above. |
| 60–70% / 20% five-year survival figures in the introduction | These appear once, sourced to external citations (refs. 1–5) rather than this study's own data, and are not restated or contradicted elsewhere in the manuscript. Nothing to compare them against internally. |
| Median survival of 9.5 vs 19 months (RAB22A-NeoF-positive vs -negative metastatic patients) | Internally consistent with the 2/37 vs 35/37 subgroup split; not restated elsewhere to check against. |

## Blocked and not-checked register

| Sweep category (skill's numbering) | Status | Reason |
|---|---|---|
| 3. Prose against source data | BLOCKED | No source-data workbook was supplied. |
| 4. Derived quantities requiring a workbook | BLOCKED | No source-data workbook was supplied. |
| 6. Tables against their own source data | BLOCKED | No source-data workbook was supplied. |
| 7. Legends against text against SI data | PARTIALLY BLOCKED | Legend-vs-text checked; legend-vs-SI-data could not be, since no genuine SI was supplied (see scope note). |
| 8–9. Source-data workbook hygiene / in-workbook summary statistics | NOT_APPLICABLE | No workbook exists in this package. |
| 15. The rebuttal as a source | NOT_APPLICABLE | No rebuttal letter was supplied. |
| 16. Replicate counts / derived-replicate formulas | BLOCKED | Requires the source-data workbook, which is absent; the manuscript text states replicate counts (e.g., "n = 3 biologically independent experiments") but the underlying replicate values are not available to verify. |

## Output validation

This findings report and the accompanying author-queries document were produced together; the author-queries document reflects that no consistency finding cleared the reporting bar, so it contains no queries of its own (see that document for detail on why, and for the one procedural note it does carry forward).
