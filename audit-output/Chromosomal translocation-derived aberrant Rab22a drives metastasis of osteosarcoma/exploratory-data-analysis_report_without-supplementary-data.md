# EDA: Rab22a Osteosarcoma Manuscript — Text Artifact (no local scientific dataset)

**File analyzed**: `supporting-files/manuscript_extracted.txt` (PyMuPDF-extracted
text from the published PDF "Chromosomal translocation-derived aberrant
Rab22a drives metastasis of osteosarcoma", Liao et al., *Nature Cell Biology*,
2020)
**Analysis date**: session date (2026)

## Skill/Target Mismatch Disclosure (read this first)

The `exploratory-data-analysis` skill is built to analyze **scientific data
files** — tabular data, sequence data, images, spectra, arrays — using
format-specific loaders (pandas, Biopython, tifffile, etc.) to compute
dimensions, missingness, distributions, and quality metrics.

**No such data file exists locally for this paper.** This is a wet-lab
biology manuscript whose primary evidence (RNA-seq, whole-genome sequencing)
is deposited externally at **SRA accession SRP181860** — it was not
downloaded for this audit (multi-GB raw sequencing data, outside this
session's scope). Locally, this paper's folder contains only:
- The manuscript PDF (extracted to text, not kept as a binary per this
  repo's convention — see other audit folders)
- Two prior review reports (`academic-paper-review_review.md`,
  `academic-paper-reviewer_review.md`)
- The `experiment-audit_report.md` completed earlier in this session

There is **no CSV/Excel/FASTQ/imaging/spectra file to run a "real" EDA on**.
To still provide a useful artifact under this skill, the following treats
the **extracted manuscript text itself** as a general-format text document
(closest analog: `references/general_scientific_formats.md` §"plain text /
unstructured text corpus") and reports structural/content statistics on it,
rather than fabricating a tabular analysis that has no underlying file.

## Basic Information

| Property | Value |
|---|---|
| Source | Published PDF, 39 pages, extracted via PyMuPDF |
| Extracted text size | 117,795 characters |
| Word count | 17,634 |
| Line count (as extracted) | 3,088 |
| Approx. unique word forms | 3,275 |
| Format category | General/unstructured text (not a structured scientific data format) |

## File Type Details

- **Description**: Plain-text extraction of a peer-reviewed journal article
  PDF. Column-based PDF layout means body text, figure legends, and
  Methods/Statistics sections are interleaved non-linearly in the extraction
  (a known PyMuPDF column-order artifact), so line order does not always
  match logical reading order.
- **Typical data**: Prose (Abstract, Introduction, Results, Discussion,
  Methods), figure/table legends, references, and a Reporting Summary /
  Statistics-and-reproducibility section — not measurement data itself.
- **Use cases**: Text-mining for claim extraction, citation analysis,
  reporting-standard compliance checks (as done for the earlier
  `experiment-audit` and `academic-paper-reviewer` outputs on this same
  paper) — not the numerical/statistical EDA this skill normally targets.
- **Python libraries used**: `re` (regex) for structural/content counting;
  no domain-specific scientific-format library applies here since this is
  not a structured data file.

## Data Analysis (structural/content statistics on the extracted text)

| Pattern | Count | Notes |
|---|---|---|
| `Fig.`/`Figure` + number mentions | 127 | High figure-citation density typical of a data-rich Nature-family paper |
| "Extended Data" mentions | 73 | Indicates substantial supplementary evidence not in the main-text figures |
| "Supplementary" mentions | 14 | Additional supplementary material referenced |
| `P` value expressions (`P = 0.0x` / `P < 0.0x`) | 269 | Very high density of individual statistical tests reported in text/legends |
| Percentage expressions (`\d+%`) | 14 | Relatively few — most quantitative claims are figure-embedded rather than percentage-stated in prose |
| `n = <number>` replicate/sample-size statements | 65 | Consistent with the small-n wet-lab replicate reporting style (n=3 in vitro, n=6-8 animals) already flagged in the `experiment-audit_report.md` for this paper |

**Key ratios**: with 269 distinct P-value mentions against only ~127
figure-number citations, this manuscript reports substantially more
individual statistical comparisons than headline figures — consistent with
many within-figure sub-panel comparisons, and reinforcing the
`experiment-audit_report.md` finding that no multiple-comparison correction
is disclosed for this volume of pairwise testing.

## Key Findings

1. **No structured/tabular scientific data file is available locally** for
   this paper — a genuine EDA (missingness, distributions, outlier
   detection) cannot be performed without retrieving the deposited
   SRP181860 sequencing data, which is out of scope for this session.
2. The manuscript text itself is dense with statistical claims (269 P-value
   mentions) relative to its figure count (127), a pattern worth flagging
   for readers assessing multiple-comparison risk — this corroborates
   (rather than duplicates) the independent finding already made in
   `experiment-audit_report.md` Check B.
3. High "Extended Data" reference density (73 mentions) indicates most of
   the primary evidence supporting the paper's claims lives outside the
   main-text figures — readers should consult Extended Data directly rather
   than relying on the main text/abstract summary alone.
4. Low percentage-expression count (14) relative to the paper's headline
   "5.4%" prevalence claim suggests that specific number is reported once
   or twice in prose and is not restated/cross-referenced elsewhere in the
   running text — consistent with the internal-consistency check already
   done in `experiment-audit_report.md` Check C, but worth independent
   confirmation if the raw cohort table becomes available.

## Recommendations

- **To perform a genuine EDA on this paper's primary data**: retrieve the
  RNA-seq/WGS FASTQ or processed-count files from SRA accession SRP181860
  and run this skill against those files directly (e.g.
  `references/bioinformatics_genomics_formats.md` for `.fastq`/`.bam`/count
  matrices) — this was outside the scope of the current session.
  - Expected quality checks: FASTQ read-quality distributions, alignment
    rate, fusion-transcript breakpoint read support, variant-caller
    confidence scores for the reported translocation.
- **For the currently-available text artifact**: no further preprocessing
  is recommended beyond what has already been done — the structural
  statistics above are best interpreted alongside the existing
  `experiment-audit_report.md` and `academic-paper-reviewer_review.md` in
  this same folder, which already substantively cover statistical-rigor and
  claim-consistency concerns for this manuscript.
- If a future session obtains the Extended Data / Source Data files (often
  distributed as an Excel workbook by *Nature* journals), re-run this skill
  against that spreadsheet directly — it would be the correct target for a
  genuine tabular EDA (missingness, per-panel replicate counts, and outlier
  checks against the values quoted in the main text).
