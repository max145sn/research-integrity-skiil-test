# EDA Re-run — Verification and Extension

**Generated:** 2026-09-16
**Skill:** `exploratory-data-analysis` (Option B — custom analysis)
**Inputs:** `s41556-019-0416-0.pdf` + the 7-item attached `source data` folder
**Extends:** `s41556-019-0416-0_eda_report.md` · `source-data_eda_report.md`
**Paper:** Wang, Yuan, Jia, Ge, Ling, Nie, Lan, Chen & Xu, *Nature Cell Biology* 21:1346–1356 (2019), doi:10.1038/s41556-019-0416-0

---

## 0. Purpose of this document

The skill had already been run against this package. This re-run was executed **independently and from scratch** — the source data were re-resolved from the `.url` shortcuts, re-downloaded, and re-profiled with freshly written scripts, without reading the prior reports until afterwards.

Two things follow:

1. **§ 1 is a reproducibility check** on the earlier reports. Every quantity that both runs measure is compared.
2. **§§ 2–6 are new material** that the earlier reports do not contain: file provenance, a panel-level coverage map, reproduction of the workbook's two stored *p*-values, and first-digit distribution testing.

This report does not restate the earlier findings. Read it alongside them, not instead of them.

---

## 1. Reproducibility check against the prior run

The attached folder again resolved to **seven 164–166 byte `.url` shortcuts**, not data. All seven targets were re-downloaded from `media.springernature.com` (7/7 succeeded) and re-profiled.

| Quantity | Prior report | This run | Agreement |
|---|---:|---:|:--:|
| Fig 1 — numeric / text / blank cells | 400 / 102 / 389 | 400 / 102 / 389 | ✅ |
| Fig 2 — numeric / text / blank cells | 353 / 128 / 455 | 353 / 128 / 455 | ✅ |
| Fig 3 — numeric / text / blank cells | 180 / 47 / 593 | 180 / 47 / 593 | ✅ |
| Fig 7 — numeric / text / blank cells | 424 / 124 / 607 | 424 / 124 / 607 | ✅ |
| Cells holding exactly 1.0 (all files) | 199 | 199 (81+28+36+54) | ✅ |
| Fig 1 min / max | −0.345583 / 117.95 | −0.3456 / 118 | ✅ |
| Fig 7 max | 69,738.32 | 69,738.32 | ✅ |
| Precision histograms (per file, all bins) | § 3 table | identical, bin for bin | ✅ |
| Fig 2 cells at 18–19 dp | 2 | 2 | ✅ |
| Fig 4/5/6 — embedded rasters per page | 17 / 16 / 36 | 17 / 16 / 36 | ✅ |
| Fig 4/5/6 — text-layer characters | 326 / 317 / 574 | 328 / 318 / 576 | ⚠️ ±2 |

**Result: full agreement on every numeric profile.** The only divergence is a ±2-character difference in the PDF text layers, which is a whitespace-handling difference between `pdfplumber` (prior run) and `pymupdf` (this run), not a data difference.

One item in the prior report is **corrected** below: it recorded Fig 2 as having no formulas. Re-reading the workbooks with `data_only=False` shows **Fig 2 contains 2 formula cells** — the two stored *p*-values are live formulas, not pasted constants (see § 4). The other three workbooks contain none.

---

## 2. File provenance (new)

Neither prior report examined the embedded authoring metadata. It is informative.

| File | Creator / producer | Created | Last modified |
|---|---|---|---|
| Source Data Fig 1.xlsx | `WangYao` | 2019-08-29 06:30:46 | **2019-10-22 13:46:52** |
| Source Data Fig 2.xlsx | `WangYao` | 2019-08-29 06:32:53 | 2019-08-29 06:42:29 |
| Source Data Fig 3.xlsx | `WangYao` | 2019-08-29 06:33:47 | 2019-08-29 06:42:45 |
| Source Data Fig 7.xlsx | `WangYao` | 2019-08-29 06:36:49 | 2019-08-29 06:45:03 |
| Source Data Fig 4.pdf | Adobe Illustrator CC 2017 (Macintosh) | 2019-08-31 16:46:10 +08:00 | same |
| Source Data Fig 5.pdf | Adobe Illustrator CC 2017 (Macintosh) | 2019-08-31 16:53:56 +08:00 | same |
| Source Data Fig 6.pdf | Adobe Illustrator CC 2017 (Macintosh) | 2019-08-31 17:14:59 +08:00 | same |

Observations:

- **The four workbooks were created within a 6-minute window** (06:30:46 → 06:36:49) by a single user account, and three of them were last saved within a further 3-minute window (06:42–06:45). This is consistent with a single sitting in which a pre-existing set of panel values was assembled into deposit files.
- **Figure 1's workbook is the outlier: last saved 2019-10-22, eight weeks after the other three.** The paper was published 2019-11-05 (from the manuscript PDF's own `/CreationDate`). A late edit confined to one file is the expected signature of a revision-round change to Figure 1 — routine, but it means Fig 1's contents and the other three files are **not** from the same snapshot.
- **The three blot PDFs are Illustrator exports, not scanner output.** Each is a single Illustrator artboard with 16–36 rasters placed on it, exported two days after the workbooks. Uncropped-blot deposits are normally assembled this way; it is recorded here because it means each embedded raster is a *placed* image whose relationship to an original scan file is not captured in the deposit.
- The `+08:00` offset on all three PDFs is consistent with the authors' stated China-based affiliations.

---

## 3. Panel coverage map (new)

Parsing every `Figure Xy` block label across all seven files gives the deposit's actual panel coverage:

| Source file | Panels represented | Modality |
|---|---|---|
| Fig 1.xlsx | 1b, 1e, 1f, 1g, 1h, 1j, 1k, 1l | numeric (8 panels) |
| Fig 2.xlsx | 2a, 2b, 2d, 2e, 2g, 2h, 2i, 2j | numeric (8 panels) |
| Fig 3.xlsx | 3a, 3b, 3c, 3f | numeric (4 panels) |
| Fig 4.pdf | 4b, 4c, 4f, 4g, 4h | image (5 panels, 17 rasters) |
| Fig 5.pdf | 5b, 5g, 5h, 5i, 5j, 5k, 5l | image (7 panels, 16 rasters) |
| Fig 6.pdf | 6a, 6c, 6d, 6e, 6f, 6g, 6i, 6j, 6k | image (9 panels, 36 rasters) |
| Fig 7.xlsx | 7a, 7b, 7c, 7e, 7f, 7g, 7h, 7i, 7j | numeric (9 panels) |

**50 panels are represented: 29 numerically, 21 as images. The overlap is empty.**

That empty overlap is the structurally important result. No panel in this deposit has *both* a numeric series and its image evidence. In particular, Figures 4, 5 and 6 are represented **only** as uncropped blots — the deposit contains no densitometry values, and therefore no numeric trail for any quantitative statement derived from those three figures. Conversely, Figures 1–3 and 7 have values with no corresponding raw-image deposit.

Lettering gaps are visible within each figure (e.g. 1a/1c/1d/1i, 2c/2f, 3d/3e, 4a/4d/4e, 6b/6h, 7d). Most correspond to schematics, micrographs or survival curves for which a numeric or blot deposit is not expected — **these gaps are listed as observations only and would need checking against the figure legends before any of them is called a genuine omission.**

### Parsing hazard: panels share rows

Two panel pairs are laid out **side by side in the same rows**, not stacked: `Figure 1f` / `Figure 1g` (both begin at row 26 of Fig 1) and `Figure 7e` / `Figure 7f` (both at row 47 of Fig 7). A row-delimited block parser — the approach the prior report recommends — silently assigns 0 rows to the second panel of each pair.

**Any block-parsing of these workbooks must be column-aware as well as row-aware.** This is a concrete, reproducible failure mode; it was hit by this run's own first-pass parser and is documented so the next consumer does not hit it too.

---

## 4. The two stored *p*-values reproduce exactly (new)

Fig 2 stores two *p*-values (`E53`, `I53`) beside the raw replicates in the Figure 2h block. They are live formulas, so the test used is recoverable. Recomputing from the replicates in the same sheet:

**Figure 2h — viral titre, wt vs *Znfx1*<sup>−/−</sup>**

| Comparison | wt (n, mean ± sd) | KO (n, mean ± sd) | Fold | Student's *t* | Recomputed *p* | Stored *p* |
|---|---|---|---:|---|---:|---:|
| VSV | 3, 1618.11 ± 215.98 | 3, 5634.90 ± 1163.84 | 3.48 | t = −5.8775, df = 4 | **0.004187** | 0.004187 |
| EMCV | 3, 546.09 ± 114.86 | 3, 2188.70 ± 371.13 | 4.01 | t = −7.3233, df = 4 | **0.001850** | 0.001850 |

Both stored values reproduce **to all six significant figures** under a two-sided, equal-variance (Student) two-sample *t*-test. Welch's correction does not reproduce them (0.0237 and 0.0110 respectively), so the test in use is identified unambiguously as Student's *t*.

This is a positive reproducibility signal: for the two places in this deposit where a derived statistic can be checked against its own inputs, the derivation is exact and the method is identifiable.

It also gives a method baseline for the two Fig 2h comparisons that carry **no** stored *p*-value:

| Comparison | wt (n = 4) | KO (n = 4) | Fold | Student's *p* |
|---|---|---|---:|---:|
| H1N1 | 498.95 ± 92.61 | 1355.93 ± 133.35 | 2.72 | 0.000042 |
| HSV-1 | 6303.05 ± 1258.19 | 7500.76 ± 1467.89 | 1.19 | 0.262 |

The HSV-1 arm is the one non-significant comparison in this block — consistent with the paper's own position that ZNFX1 acts on RNA viruses, HSV-1 being a DNA virus. Recorded as a descriptive observation; **whether this matches what the figure and legend state is a claim-level question and is out of scope here.**

Note the unequal replicate structure *within a single panel*: n = 3 for the VSV and EMCV arms, n = 4 for H1N1 and HSV-1.

---

## 5. Distributional screening (new)

### First significant digit — Benford conformity

Pooled over all 1,048 non-integer, non-normalisation values in the four workbooks:

| Digit | Observed | % | Benford % |
|---:|---:|---:|---:|
| 1 | 317 | 30.2 | 30.1 |
| 2 | 160 | 15.3 | 17.6 |
| 3 | 135 | 12.9 | 12.5 |
| 4 | 112 | 10.7 | 9.7 |
| 5 | 84 | 8.0 | 7.9 |
| 6 | 60 | 5.7 | 6.7 |
| 7 | 65 | 6.2 | 5.8 |
| 8 | 58 | 5.5 | 5.1 |
| 9 | 57 | 5.4 | 4.6 |

χ²(8) = 8.31, *p* ≈ 0.40. **The pooled first-digit distribution is fully consistent with Benford's law.** No deviation is detectable.

This is a weak screen and should be read as such: Benford conformity is a necessary-not-sufficient property, the data span several orders of magnitude which favours conformity, and pooling across heterogeneous panels blurs any localised effect. It is reported because it is a standard screen and it came back clean, not because a clean result licenses any conclusion.

### Terminal-digit testing — not interpretable here

A terminal-digit uniformity test was attempted and is **withdrawn**. Excel stores numbers as IEEE-754 doubles and does not preserve trailing zeros: a value typed as `1.20` is indistinguishable from `1.2` once stored. Any last-digit extraction from these files therefore misassigns every value whose typed final digit was 0, and the resulting χ² is an artifact of that misassignment rather than a property of the data.

This is stated explicitly because the test is a common integrity screen and would otherwise be run on these files and over-read. **Terminal-digit analysis on `.xlsx` deposits requires access to the number-format-rendered strings, not the stored doubles, and should not be reported from `openpyxl` values alone.**

---

## 6. What this re-run adds

| # | Item | Status |
|---|---|---|
| 1 | Prior reports reproduce exactly on every numeric profile | ✅ verified |
| 2 | Fig 2 contains 2 formula cells (prior report said none) | ⚠️ correction |
| 3 | All four workbooks authored by one account in a 6-minute window | new |
| 4 | Fig 1's workbook last saved 8 weeks after the other three | new |
| 5 | Blot PDFs are Illustrator exports, not scans; no link to originals | new |
| 6 | 50 panels covered — 29 numeric, 21 image, **zero overlap** | new |
| 7 | Figs 4–6 have no numeric deposit of any kind | confirmed, quantified |
| 8 | Side-by-side panels break row-delimited parsing (1f/1g, 7e/7f) | new |
| 9 | Both stored *p*-values reproduce exactly; test = Student's *t* | new |
| 10 | Unequal *n* within Fig 2h (3 vs 4) | new |
| 11 | Benford first-digit conformity, χ²(8) = 8.31, *p* ≈ 0.40 | new |
| 12 | Terminal-digit screening is invalid on `.xlsx` and is withdrawn | new |

## 7. Recommendations (additional to the prior reports)

**For anyone consuming these workbooks**
- Parse blocks with **column awareness**; row delimiters alone will drop Fig 1g and Fig 7f.
- Read with `data_only=False` as well as `data_only=True` — the formula layer identifies which cells are derived.
- Do not run terminal-digit screens on the stored values (§ 5).

**For the deposit itself**
- Deposit densitometry tables for Figures 4–6, so that quantitative statements from those figures have a numeric trail.
- Deposit original scan files, or record the placed-image filenames, alongside the Illustrator artboards.
- Record *n* explicitly per arm; the within-panel n = 3 / n = 4 split in Fig 2h is recoverable only by counting rows.
- State the statistical test per panel in the workbook. It happens to be recoverable for the two Fig 2h comparisons because the formulas survived; nowhere else in the deposit is it recoverable at all.

---

## 8. Scope and limitations

- **Structural and descriptive only.** This report characterises the deposit. It does not evaluate whether the values are correct, whether they support the paper's claims, or whether figure-reported statistics reproduce — those are handled by the other skills in this repository (`paper-claim-audit`, `manuscript-data-integrity`, `manuscript-consistency-audit`, `universal-research-package-audit`), whose outputs sit alongside this one.
- The §§ 4–5 computations are **reproductions of statistics stored in the deposit**, not an audit of the paper's reported statistics.
- Every gap, duplicate and anomaly noted here is an **observation for confirmation**. None is asserted to be an error, and nothing here implies misconduct.
- No pixel-level image forensics was performed on the blot PDFs; that is outside this skill.
- The source data are profiled from re-downloaded copies of the `.url` targets. Identity is pinned by the SHA-256 digests in `source-data_eda_report.md` § 1, which this run's downloads match.

---

**Artifacts**

| Script | Log | Produces |
|---|---|---|
| `scripts/eda_rerun_workbooks.py` | `logs/rerun_workbook_dump.txt` | Full cell-by-cell dump of all four workbooks |
| `scripts/eda_rerun_pdfs.py` | `logs/rerun_pdf_dump.txt` | Per-raster inventory and text layer of the three blot PDFs |
| `scripts/eda_rerun_stats.py` | `logs/rerun_distribution.txt` | Cell inventory, precision histograms, Benford (§ 5) |
| `scripts/eda_rerun_pcheck.py` | `logs/rerun_pvalue_recompute.txt` | *p*-value reproduction (§ 4) |
| `scripts/eda_rerun_coverage.py` | `logs/rerun_provenance_coverage.txt` | Provenance table and panel coverage map (§§ 2–3) |

All scripts read from `../../supporting-files/source-data` by default and honour the `EDA_DATA_DIR` environment variable. Every log in the table was regenerated by running the script from that location; all seven archived files hash-match the freshly downloaded `.url` targets.
