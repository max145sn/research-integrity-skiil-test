# Exploratory Data Analysis Report: Source Data (7 files)

**Generated:** 2026-09-16
**Skill:** `exploratory-data-analysis` — multi-file analysis
**Companion to:** `s41556-019-0416-0_eda_report.md`
**Paper:** Wang, Yuan, Jia, Ge, Ling, Nie, Lan, Chen & Xu, *Nature Cell Biology* 21:1346–1356 (2019)

---

## 0. Input resolution

The attached folder (`…/Integrity checks/Nature cell biology/WangXu et al. 2019 - 1/source data`) contains **seven 164–166 byte `.url` shortcut files, not the data itself**. Each points at a Springer Nature media endpoint, e.g.:

```
URL=https://media.springernature.com/original/springer-static/esm/
    art%3A10.1038%2Fs41556-019-0416-0/MediaObjects/41556_2019_416_MOESM4_ESM.xlsx
```

`.url` is a Windows shortcut format and carries no scientific content. This report therefore profiles the **resolved downloads** already present and hash-verified in the repository at `supporting-files/source-data/`. File identity is fixed by the SHA-256 digests in § 1; if the remote objects ever change, these digests will not match and the report should be regenerated.

**Skill-execution note:** as documented in the companion report, this skill ships `skill.md` only — `scripts/eda_analyzer.py`, `references/*.md` and `assets/report_template.md` are absent from the repository. Analysis follows the skill's Option B (custom analysis) path. Both `.xlsx` and `.pdf` fall in the skill's *General Scientific Data Formats* category.

## 1. File inventory

| File | Format | Size | SHA-256 (16) | Readable |
|---|---|---:|---|---|
| Source Data Fig 1.xlsx | Office Open XML workbook | 15,724 B | `948c4974e337469f` | Yes |
| Source Data Fig 2.xlsx | Office Open XML workbook | 15,179 B | `b3f7a518a3a1ccd1` | Yes |
| Source Data Fig 3.xlsx | Office Open XML workbook | 12,688 B | `f77eed0f8466ebba` | Yes |
| Source Data Fig 4.pdf | PDF raster container | 19,569,773 B | `5c0f777759eda965` | Yes |
| Source Data Fig 5.pdf | PDF raster container | 13,040,249 B | `6bd3c1ec2376c1fd` | Yes |
| Source Data Fig 6.pdf | PDF raster container | 6,693,658 B | `f49239f09a4d8b05` | Yes |
| Source Data Fig 7.xlsx | Office Open XML workbook | 16,447 B | `b4ca4c544660c71f` | Yes |

**Two distinct data modalities**, with a 1,000-fold size split: four small numeric workbooks (12–17 KB) and three large raster PDFs (6.7–19.6 MB). Notably, **Figures 4, 5 and 6 have no numeric deposit at all** — those panels are represented only as images.

## 2. Tabular files — structure

All four workbooks share an identical, unusual layout: **one sheet named `Sheet1`, containing multiple figure-panel blocks stacked vertically**, separated by label rows (`A2=Figure 1b`, `A8=Figure 1e`, …). This is *not* tidy/rectangular data — there is no single header row, and column meaning changes down the sheet.

| File | Dims | Rows × Cols | Total cells | Numeric | Text | Empty | % empty |
|---|---|---|---:|---:|---:|---:|---:|
| Fig 1 | A1:K81 | 81 × 11 | 891 | 400 | 102 | 389 | 43.7% |
| Fig 2 | A1:M72 | 72 × 13 | 936 | 353 | 128 | 455 | 48.6% |
| Fig 3 | A1:T41 | 41 × 20 | 820 | 180 | 47 | 593 | 72.3% |
| Fig 7 | A1:K105 | 105 × 11 | 1,155 | 424 | 124 | 607 | 52.6% |
| **Total** | — | — | **3,802** | **1,357** | **401** | **2,044** | **53.8%** |

**The 44–72% "missing" rate is a layout artifact, not missing data.** Empty cells are the padding between panel blocks. A naive `pandas.read_excel()` will produce a mostly-NaN frame with meaningless column names — these files must be parsed block-by-block, not as a table.

### Value ranges

| File | Min | Max | Dynamic range | Exact 1.0 cells | Negatives | Zeros |
|---|---:|---:|---|---:|---:|---:|
| Fig 1 | −0.345583 | 117.95 | ~3 orders | 81 | 10 | 0 |
| Fig 2 | 0.00185 | 9,512.43 | ~6 orders | 28 | 0 | 0 |
| Fig 3 | 0.4 | 12,359.51 | ~4 orders | 36 | 0 | 0 |
| Fig 7 | 0 | 69,738.32 | ~6 orders | 54 | 0 | 5 |

Observations:
- **199 cells hold exactly 1.0** across the four files. These are fold-change normalisation references (control arms set to unity), not measurements. Any distributional summary that pools them with real measurements is meaningless.
- **Figure 1 is the only file with negative values** (10 cells, min −0.35) — consistent with log-ratio expression data in the clinical-sample panels, a different measurement scale from the fold-change panels elsewhere.
- **Figure 2's minimum (0.00185) is not a measurement** — it is a stored *p*-value sitting in the same sheet as the data (see § 3).
- **Figure 7 contains five exact zeros** (`C61`, `E61`, `C67`, `E67`, `E70`), in the Fig 7f heat-map region. Zero in a fold-change matrix is worth confirming as a true zero rather than an empty-cell placeholder.

## 3. Data quality assessment

### Numeric precision — a bimodal signature

| File | 0 dp | 1 dp | 2 dp | 4 dp | 5 dp | 6 dp | 7 dp | 8 dp | 18–19 dp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Fig 1 | 81 | — | — | 6 | 141 | 34 | 137 | 1 | — |
| Fig 2 | 28 | 25 | 270 | — | — | — | 28 | — | **2** |
| Fig 3 | 52 | 64 | 32 | — | — | 30 | 2 | — | — |
| Fig 7 | 59 | — | 54 | 1 | 10 | 155 | 144 | 1 | — |

The distribution is strikingly **bimodal**: values cluster either at ≤2 decimal places or at ≥5, with little in between.

| File | ≤2 dp | ≥6 dp |
|---|---:|---:|
| Fig 1 | 81 | 172 |
| Fig 2 | 323 | 30 |
| Fig 3 | 148 | 32 |
| Fig 7 | 113 | 300 |

This is the signature of **mixed provenance within a single sheet** — some blocks appear machine-exported at full float precision, others hand-entered or rounded before entry. Figure 2 is predominantly low-precision; Figure 7 predominantly high-precision. This is a normal consequence of assembling source data by hand from several instruments, and is recorded here as a structural characteristic rather than a defect.

**Two cells in Figure 2 carry 18–19 decimal places.** These are full-float *p*-values (`E53`, `I53`) stored alongside the raw replicates — i.e. the workbook contains both inputs and a derived statistic in the same sheet, with no separation between them.

### Duplicate values

| File | Duplicate value groups (excl. 0 and 1) | Duplicate numeric rows |
|---|---:|---:|
| Fig 1 | 1 | 2 |
| Fig 2 | 24 | 1 |
| Fig 3 | 15 | 1 |
| Fig 7 | 5 | 0 |

Most duplicates are unremarkable: they occur in the low-precision (≤2 dp) blocks, where repeated values are expected simply because there are few possible values (e.g. `0.86` at `J4`, `C21`, `F72` in Fig 2). The count tracks precision, not anomaly — Fig 2 and Fig 3, the two lowest-precision files, have the most duplicates.

One case is different in kind and worth noting: **`0.249075` appears three times in Figure 1** at `E34`, `E38`, `E41` — a 6-decimal value repeated exactly within one column. Exact repetition at that precision is far less likely to arise by rounding than the 2-dp cases. This is flagged as an **observation for confirmation**, not a finding; legitimate explanations include a repeated measurement, a carried-forward value, or a copy-paste during sheet assembly.

### Structural quality summary

| Check | Result |
|---|---|
| All files open without error | ✅ 4/4 workbooks, 3/3 PDFs |
| Formulas preserved | ❌ None — values only, no computation trail |
| Single sheet per workbook | ⚠️ Yes — multiple panels crammed into `Sheet1` |
| Machine-readable header row | ❌ No — block labels only |
| Units recorded | ❌ Not stated anywhere in the workbooks |
| Replicate structure explicit | ❌ Implicit in row position only |
| Inputs separated from derived statistics | ❌ *p*-values stored beside raw data (Fig 2) |
| Codebook / README | ❌ Absent |

## 4. Image files — Figures 4, 5, 6

| File | Pages | Embedded images | Text-layer chars | Chars/page | MB per page |
|---|---:|---:|---:|---:|---:|
| Fig 4.pdf | 1 | 17 | 326 | 326 | 18.7 |
| Fig 5.pdf | 1 | 16 | 317 | 317 | 12.4 |
| Fig 6.pdf | 1 | 36 | 574 | 574 | 6.4 |

Each is a **single page carrying 16–36 separate embedded rasters** — uncropped immunoblot scans tiled onto one sheet. The text layer is tiny (317–574 characters) and contains only panel labels and molecular-weight annotations.

**These files contain no numeric data.** They are image evidence. Densitometry values, band quantifications and the statistics derived from them are not present in any deposited file. The very high bytes-per-page (up to 18.7 MB) indicates minimally compressed, high-resolution scans — good practice for blot transparency.

Pixel-level image-integrity analysis is **out of scope for this skill** and was not performed.

## 5. Key findings

1. **Two incompatible data modalities.** Four numeric workbooks and three image-only PDFs. Figures 4–6 have no numeric deposit whatsoever.
2. **The workbooks are not tidy data.** Multi-panel blocks in a single sheet, no header row, 54% padding cells. Naive `read_excel()` will fail meaningfully.
3. **Bimodal precision within single sheets** points to mixed provenance — part machine export, part manual entry.
4. **199 cells are exactly 1.0** — normalisation references, not measurements; they must be excluded from any pooled statistical summary.
5. **Derived statistics are stored beside raw inputs** (Fig 2 `E53`, `I53` at 18–19 dp), with nothing marking them as derived.
6. **No formulas, units, codebook or explicit replicate labelling** — the computation trail from raw values to published statistics is not preserved.
7. **Five exact zeros in Figure 7** in a fold-change region, worth confirming as true zeros.
8. **One 6-decimal value repeated three times in Figure 1** (`E34`/`E38`/`E41`), flagged for confirmation.

## 6. Recommendations

### Preprocessing
- Parse workbooks **block-by-block** using the `A<n>="Figure Xy"` label rows as delimiters. Do not load as a flat table.
- Build an explicit long-format frame: `figure, panel, group, replicate, value`, with normalisation references marked by a boolean flag rather than being mixed into the value column.
- Exclude the two stored *p*-value cells from any measurement series.
- Treat empty cells as structural padding, not as missing observations — do not impute.
- Confirm the five Fig 7 zeros and the repeated Fig 1 value against original records before analysis.

### Appropriate analyses
- Per-panel group comparison with the replicate structure recovered from row position.
- Recomputation of reported statistics from the raw replicate blocks (the two stored *p*-values give a ground-truth check on method choice).
- Precision profiling by block, to identify which panels were machine-exported.

### Improving the deposit
| Gap | Fix |
|---|---|
| Multi-panel single sheet | One sheet per panel, or a tidy long-format table |
| No header row | Explicit column names: group, replicate, value, units |
| Units unrecorded | State units/normalisation per panel |
| Statistics mixed with inputs | Separate sheet, or clearly labelled derived block |
| No codebook | Add a README sheet defining every block |
| No numeric data for Figs 4–6 | Deposit densitometry tables alongside the blot scans |

### Tooling
| Task | Tool |
|---|---|
| Block-aware workbook parsing | `openpyxl` (`load_workbook(..., data_only=True)`) |
| Tidy reshaping | `pandas` |
| Recomputation | `scipy.stats` |
| Blot PDF image extraction | `pymupdf` `get_images()` / `pdfimages` |

### Visualisation
- Per-panel replicate dot plots with the normalisation reference shown explicitly at 1.0.
- Precision histogram per file (tabulated in § 3) to expose the provenance split.
- Sheet occupancy heat map to make the block layout legible.

---

## 7. Limitations of this report

- Profiles the resolved downloads, not the attached `.url` shortcuts; identity is pinned by the § 1 digests.
- The skill's analyzer script, format catalogue and report template were absent (§ 0); analysis was custom-written.
- **Structural and descriptive only.** Nothing here evaluates whether values are correct, whether they support the paper's claims, or whether reported statistics reproduce — that is the province of other skills in this repository, and this report deliberately makes no such claim.
- Duplicate and zero observations are flagged for confirmation; none is asserted to be an error.
- No pixel-level image forensics was performed on the blot PDFs.

**Artifacts:** `logs/sourcedata_profile.json` · `logs/quality_profile.json` · `scripts/eda_sourcedata.py` · `scripts/eda_quality.py`
