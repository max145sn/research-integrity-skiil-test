# Statistical data integrity screening report

**Manuscript:** `s41556-019-0416-0.pdf` — *ZNFX1 is a guardian of the intestinal epithelium / ZNFX1 antiviral dsRNA sensor* (Wang, Yuan, Xu et al., *Nature Cell Biology*, 2019)
**Source data supplied:** Source Data Fig. 1, Fig. 2, Fig. 3, Fig. 7 (XLSX); Source Data Fig. 4, Fig. 5, Fig. 6 (PDF — uncropped blot images)
**Skill:** `manuscript-data-integrity-check`
**Date of screening:** see file timestamp
**Scope:** statistical and numerical integrity screening only.

---

## About this report

This is an automated-plus-manual **screening** report. It states what was tested and
what the numbers show. It does **not** make any determination about intent, error,
or misconduct, and it does not recommend an editorial decision. Several findings
below have ordinary explanations that only the authors can supply; the appropriate
next step for any flagged item is a request to the authors for the underlying raw
measurements and the derivation of the plotted values.

Flag levels used:

| Level | Meaning |
|---|---|
| 🔴 **Flag** | A numerical relationship in the supplied data that is not explicable by measurement and requires an explanation from the authors. |
| 🟡 **Note** | A discrepancy or ambiguity that should be clarified, but that has plausible innocent explanations. |
| 🟢 **Clear** | Checked and reproduces. |

---

## Summary

| # | Level | Check | Location | One-line |
|---|---|---|---|---|
| 1 | 🔴 | Replicate independence | Source Data Fig. 7, panel 7b | 9 of 36 *Ifit1* replicate values equal the corresponding *Ifnb1* value plus an exact whole number, to 7 decimal places |
| 2 | 🔴 | Replicate independence | Source Data Fig. 1, panel 1h | The IFN-α and IFN-β series share replicate 2 at all four time points, agreeing to 7–8 significant figures |
| 3 | 🟡 | Sample size vs. legend | Fig. 2h | Legend states *n* = 3; the H1N1 and HSV-1 blocks contain 4 replicates, and the reported *P* values reproduce only from *n* = 4 |
| 4 | 🟡 | Duplicate block | Source Data Fig. 2, panel 2g | The 10-value uninfected control row is byte-identical between the EMCV block and the H1N1 block |
| 5 | 🟡 | *P*-value recomputation | Fig. 2g (H1N1), Fig. 2e | Two reported *P* values do not reproduce from the supplied replicates, while every other Fig. 2 value does |
| 6 | 🟡 | Order-of-magnitude outlier | Source Data Fig. 7, panel 7c | One replicate is exactly 10× below its two neighbours |
| 7 | 🟡 | Incomplete source data | Fig. 7g | The sheet holds only two of the three plotted conditions; the two reported *P* values cannot be reproduced |
| 8 | 🟡 | Unmatched *P* values | Fig. 7 | Four reported *P* values could not be matched to any comparison in the supplied sheet |
| 9 | 🟡 | Panel assignment | Fig. 3c | Two reported *P* values reproduce exactly from the uninfected (PBS) rows rather than the infected rows |
| — | 🟢 | *P*-value recomputation | Figs. 1, 3, and most of 2 and 7 | ~40 reported *P* values reproduce exactly from the raw replicates |
| — | 🟢 | Formula audit | All four workbooks | No formula-derived values in any cell plotted as an individual replicate |

---

## Method

The manuscript reports **exact *P* values with no test statistic and no degrees of
freedom**, so `scripts/statcheck.py` — which recomputes *P* from a reported
statistic and *df* — has nothing to operate on. A stronger check was substituted:
every reported *P* value in Figs. 1, 2, 3 and 7 was **recomputed directly from the
raw replicate values in the source-data workbooks**.

The test convention was established from two independent sources and applied
throughout:

1. The Methods statistics statement (manuscript line 2854).
2. Two surviving spreadsheet formulas in `Source Data Fig 2.xlsx` row 53:
   `=T.TEST(D50:D52,E50:E52,2,2)` and `=T.TEST(H50:H52,I50:I52,2,2)` — Excel
   type 2 = two-tailed, equal-variance (pooled) Student's *t*-test.

Welch (unequal-variance) variants were computed alongside as a control and do
**not** match the reported values, confirming the pooled convention and ruling out
mixed test usage as an explanation for the mismatches in finding 5.

Every workbook was additionally loaded twice — once with `data_only=True`
(cached values) and once with `data_only=False` (formulas as text) — so that
formula-derived cells could not be mistaken for measurements.

---

## 🔴 Finding 1 — Replicate values in Fig. 7b differ by exact whole numbers across genes and cell lines

**Check:** replicate independence (preclinical/bench section, manual + scripted).
**File:** `Source Data Fig 7.xlsx`, sheet `Sheet1`, rows 11–35.

Panel 7b reports two separate qPCR readouts — ***Ifnb1*** (rows 11–22) and
***Ifit1*** (rows 24–35) — each across four cell lines (WT, *Rig-I*⁻ᐟ⁻, *Mda5*⁻ᐟ⁻,
*Mavs*⁻ᐟ⁻) × three plasmids (ZNFX1, RIG-I, MDA5) × three replicates. These are
36 measurements of one gene and 36 of another: 72 independent numbers.

Subtracting each *Ifnb1* cell from its positionally corresponding *Ifit1* cell
(same cell line, same plasmid, same replicate index) gives:

| Cell line | Rep | Plasmid | *Ifnb1* | *Ifit1* | Difference |
|---|---|---|---|---|---|
| WT | 2 | ZNFX1 | 123.7718632 | 243.7718632 | **120.0000000** |
| WT | 2 | MDA5 | 115.1158394 | 185.1158394 | **70.0000000** |
| *Rig-I*⁻ᐟ⁻ | 1 | RIG-I | 127.1500527 | 287.1500527 | **160.0000000** |
| *Mda5*⁻ᐟ⁻ | 1 | ZNFX1 | 87.1500527 | 187.1500527 | **100.0000000** |
| *Mda5*⁻ᐟ⁻ | 1 | RIG-I | 119.4282229 | 219.4282229 | **100.0000000** |
| *Mda5*⁻ᐟ⁻ | 1 | MDA5 | 127.1158394 | 227.1158394 | **100.0000000** |
| *Mda5*⁻ᐟ⁻ | 2 | ZNFX1 | 117.0412771 | 167.0412771 | **50.0000000** |
| *Mda5*⁻ᐟ⁻ | 2 | RIG-I | 153.7718632 | 243.7718632 | **90.0000000** |
| *Mda5*⁻ᐟ⁻ | 2 | MDA5 | 95.3393576 | 155.3393576 | **60.0000000** |
| *Mda5*⁻ᐟ⁻ | 3 | RIG-I | 130.2638262 | 180.2638226 | 49.9999964 |

**9 of the 36 pairs differ by an exact whole number carried to all seven stored
decimal places**, including *every one of the six cells* in the *Mda5*⁻ᐟ⁻
replicate-1 and replicate-2 rows. A tenth pair misses by 3.6 × 10⁻⁶.

The remaining 26 pairs show no such relationship (differences such as 92.5913991,
136.4139586, 10.0036356), which is what independent measurements of two different
genes look like and which confirms the comparison is being made correctly.

**Why this is not attributable to measurement.** The values are stored to seven
decimal places. For two independently measured quantities to differ by an integer
at that precision requires agreement in all seven decimal digits. The probability
of that occurring once by chance is of order 10⁻⁷; it occurs nine times here,
and in one block it occurs in all six cells.

**The pattern extends beyond panel 7b.** The fractional part `.1500527` appears
five times in the workbook, spanning two genes, two cell lines, two plasmids and
two figure panels:

| Cell | Panel | Condition | Value |
|---|---|---|---|
| `E17` | 7b *Ifnb1* | *Mda5*⁻ᐟ⁻, ZNFX1, rep 1 | 87.1500527 |
| `F14` | 7b *Ifnb1* | *Rig-I*⁻ᐟ⁻, RIG-I, rep 2 | 127.1500527 |
| `E30` | 7b *Ifit1* | *Mda5*⁻ᐟ⁻, ZNFX1, rep 1 | 187.1500527 |
| `F27` | 7b *Ifit1* | *Rig-I*⁻ᐟ⁻, RIG-I, rep 2 | 287.1500527 |
| `F38` | **7c** | *Rig-I*⁻ᐟ⁻, RIG-I + VSV, rep 1 | 9287.1500527 |

Five further fractional parts are shared between two to four cells each
(`.7718632` ×4, `.1158394` ×4, `.4282229` ×2, `.0412771` ×2, `.3393576` ×2), in
every case with exact whole-number offsets.

No formulas are present in any of these cells — they are stored as static values,
so the relationship is not the residue of a visible spreadsheet calculation.

**What to ask the authors.** Request the primary qPCR output (Cq/Ct values and the
normalisation steps) for panels 7b and 7c, and an explanation of how the values in
`Source Data Fig 7.xlsx` rows 11–35 and 38–40 were derived from it.

---

## 🔴 Finding 2 — The IFN-α and IFN-β series in Fig. 1h share a replicate at every time point

**Check:** replicate independence (preclinical/bench section, manual).
**File:** `Source Data Fig 1.xlsx`, rows 47–56, column E.

Panel 1h plots two separate treatments — IFN-α and IFN-β — each as a time course
with three replicates per time point. The **second replicate** of the two
treatments is effectively the same number at all four post-treatment time points:

| Time point | IFN-α rep 2 | IFN-β rep 2 | Absolute difference | Relative difference |
|---|---|---|---|---|
| 4 h | 10.3744536 | 10.3744568 | 3.2 × 10⁻⁶ | 3.1 × 10⁻⁷ |
| 8 h | 12.4231824 | 12.4231872 | 4.8 × 10⁻⁶ | 3.9 × 10⁻⁷ |
| 16 h | 8.3684621 | 8.3684624 | 3.0 × 10⁻⁷ | 3.6 × 10⁻⁸ |
| 24 h | 7.3104623 | 7.3104625 | 2.0 × 10⁻⁷ | 2.7 × 10⁻⁸ |

Replicates 1 and 3 of the two treatments show no such relationship (e.g. 4 h:
10.6172125 vs 10.1471152, and 9.5798294 vs 8.9176695), so this is specific to the
middle replicate.

Two different cytokines producing responses that agree to seven or eight
significant figures, at four separate time points, is not a measurement outcome.
If one replicate series was genuinely shared between the two treatment arms, the
effective *n* for that comparison is below the stated *n* = 3, and the two series
are not statistically independent.

**What to ask the authors.** Request the raw plate data for Fig. 1h and
confirmation of whether the IFN-α and IFN-β time courses were run as independent
experiments.

---

## 🟡 Finding 3 — Fig. 2h: legend states *n* = 3, source data contains *n* = 4

**Check:** sample-size consistency (universal check 1, manual).
**File:** `Source Data Fig 2.xlsx`, rows 50–52 and 57–60.

The Fig. 2 legend states: *"For d,e,h–j, n = 3 independent experiments."*

The sheet holds three replicates for the VSV and EMCV blocks (rows 50–52) but
**four** for the H1N1 and HSV-1 blocks (rows 57–60).

The reported *P* values confirm *n* = 4 was used for the analysis:

| Comparison | Reported | Recomputed from *n* = 4 | Recomputed from first 3 |
|---|---|---|---|
| Fig. 2h H1N1 | 4.24 × 10⁻⁵ | **4.249 × 10⁻⁵** ✓ | does not match |
| Fig. 2h HSV-1 | 0.2616 | **0.2616** ✓ | does not match |

The statistics are therefore internally consistent with the data; it is the
**legend** that is inconsistent with both. This is most likely a legend error, but
it should be corrected.

---

## 🟡 Finding 4 — Fig. 2g: an identical 10-value control row appears twice

**Check:** duplication scan (universal check 4, scripted).
**File:** `Source Data Fig 2.xlsx`, rows 38 and 41.

Both rows read, cell for cell:

```
1.32  2.42  1.53  2.31  1.63  |  1.53  2.53  1.48  1.89  1.54
```

(five WT values, five *Znfx1*⁻ᐟ⁻ values). Row 38 is the uninfected control for the
EMCV block; row 41 is the uninfected control for the H1N1 block. Panel 2g plots
them as separate bars.

**Plausible innocent explanation:** a single shared uninfected control group,
legitimately reused across virus blocks and re-plotted for visual comparison. That
is common practice, but if so it is not two independent control groups and the
figure should say so.

**What to ask the authors.** Confirm whether the uninfected controls in the EMCV
and H1N1 blocks of Fig. 2g are the same group of animals/wells.

---

## 🟡 Finding 5 — Two Fig. 2 *P* values do not reproduce while every other one does

**Check:** *P*-value recomputation from raw replicates.

**(a) Panel 2g, H1N1.** Reported **7.89 × 10⁻⁶**; recomputed **7.985 × 10⁻⁶**.
The other three annotations in the same panel reproduce exactly from the same
sheet and the same test:

| Panel 2g comparison | Reported | Recomputed |
|---|---|---|
| VSV | 1.36 × 10⁻⁶ | 1.356 × 10⁻⁶ ✓ |
| EMCV | 1.09 × 10⁻⁶ | 1.091 × 10⁻⁶ ✓ |
| HSV-1 | 0.6519 | 0.6519 ✓ |
| **H1N1** | **7.89 × 10⁻⁶** | **7.985 × 10⁻⁶** ✗ |

Because three of four reproduce, the method and the sheet are confirmed, which
makes the fourth the outlier. `7.98` → `7.89` is consistent with a digit
transposition at the point of transcription. Either way the conclusion is
unaffected — both values are far below 0.001.

**(b) Panel 2e.** Reported **0.0023**; the only plausible pairing
(WT EV + VSV vs *Znfx1*⁻ᐟ⁻ EV + VSV) gives **0.002148**. An exhaustive pairwise
search across all seven columns of the 2e block found no pairing producing 0.0023
under either the pooled or the Welch test. The companion annotation in the same
panel (0.0003) reproduces (0.0002686 ✓).

Both discrepancies are small, do not change significance, and may be rounding of
an intermediate quantity. They are reported for completeness and because they are
isolated against an otherwise exact set.

---

## 🟡 Finding 6 — Fig. 7c: one replicate is exactly 10× below its neighbours

**Check:** outlier / order-of-magnitude scan.
**File:** `Source Data Fig 7.xlsx`, row 40, MDA5 + VSV column, *Rig-I*⁻ᐟ⁻ block.

| Replicate | Value |
|---|---|
| 1 | 45514.850946 |
| 2 | 42552.971254 |
| 3 | **4176.859057** |

The third value is one order of magnitude below the other two; `4176.859057` × 10
= `41768.59057`, which sits comfortably within the range of its neighbours. This
is the signature of a decimal-point shift rather than a biological outlier.

Neither the as-supplied nor the ×10-corrected version reproduces a reported *P*
value for this comparison (as supplied: *P* = 0.0612; corrected: *P* = 0.0020), so
it is not possible to determine from the supplied files which version underlies
the plotted panel.

---

## 🟡 Finding 7 — Fig. 7g: source data does not contain all plotted conditions

**Check:** completeness of supplied source data.
**File:** `Source Data Fig 7.xlsx`, rows 62–67, columns J and K.

The sheet supplies only two conditions — `EV` (column J) and `EV + VSV`
(column K) — for *IFNB1* (rows 62–64) and *IFIT1* (rows 65–67). Panel 7g as
plotted includes a third, ZNFX1-transfected + VSV condition, for which no values
are present.

Consequently the two reported *P* values for this panel (0.0003 and 0.0030) cannot
be reproduced. The only comparison the sheet permits, EV vs EV + VSV, gives 0.0075
and 0.0043.

**What to ask the authors.** Supply the missing condition's replicate values for
Fig. 7g.

---

## 🟡 Finding 8 — Four Fig. 7 *P* values could not be matched to any comparison

**Check:** *P*-value recomputation.

The following reported values in the Fig. 7 group could not be reproduced from any
pairing of columns in `Source Data Fig 7.xlsx`, under an exhaustive pairwise search
over every block/column combination, using either the pooled or the Welch test:

| Reported | Closest recomputed value found | Comment |
|---|---|---|
| 2.93 × 10⁻⁶ | — | no match under any pairing |
| 0.0097 | — | no match under any pairing |
| 1.03 × 10⁻⁵ | 1.048 × 10⁻⁵ (7j, WT + VSV vs DKO + VSV) | 1.7 % apart — plausible but not exact |
| 0.0004 (one of two) | — | the other 0.0004 reproduces |

**Important caveat.** *P*-value annotations were recovered from the PDF in reading
order, which does not reliably preserve the mapping to panel letters. Some of these
may belong to panels whose comparison was assigned elsewhere in this audit, or to
a condition not present in the supplied sheet (see finding 7). This item is
therefore a request for clarification, not an assertion that the values are wrong.

---

## 🟡 Finding 9 — Fig. 3c: two *P* values reproduce from the uninfected rows

**Check:** *P*-value recomputation and panel assignment.
**File:** `Source Data Fig 3.xlsx`, HSV-1 block, rows 25 and 28.

Reported: **0.1361** and **0.9430**.

- Recomputed from the **PBS (uninfected)** rows: **0.1361** and **0.9430** — exact.
- Recomputed from the **HSV-1-infected** rows: 0.1232 and 0.5808.

Both values are non-significant under either assignment, so no conclusion in the
paper turns on this. It is raised only so the authors can confirm which comparison
the annotations refer to.

---

## 🟢 Checks that reproduce

Roughly forty reported *P* values were recomputed and reproduce exactly from the
supplied raw replicates.

**Figure 1 — all reported values reproduce.**

| Panel | Reported | Recomputed |
|---|---|---|
| 1f ZNFX1 (*n* = 9 / 14) | 0.0123 | ✓ |
| 1f RIG-I | 0.0004 | 0.0003732 ✓ |
| 1g ZNFX1 (*n* = 18 / 18) | 3.77 × 10⁻¹⁵ | ✓ |
| 1g RIG-I | 4.50 × 10⁻¹² | ✓ |
| 1j | 0.0043 / 0.0065 | ✓ |
| 1k | 0.0003 / 1.69 × 10⁻⁶ | ✓ |
| 1l IRF1 (wt vs Δpromoter, 200 ng) | 7.44 × 10⁻⁶ | 7.444 × 10⁻⁶ ✓ |
| 1l IRF9 | 4.40 × 10⁻⁶ | 4.400 × 10⁻⁶ ✓ |

Stated *n* for 1f (9 and 14) and 1g (18 and 18) match the sheet exactly.

**Figure 2** — panels 2a, 2b, 2d, 2g (VSV / EMCV / HSV-1), 2h (VSV / EMCV), 2i and
2j all reproduce.

**Figure 3 — all reported values reproduce**: 8.69 × 10⁻⁶, 0.0008, 0.0005, 0.0009,
3.12 × 10⁻⁹, 7.65 × 10⁻¹¹, from the stated *n* (4 mice for 3a/3b, 8 for 3c VSV,
4 for 3c HSV-1). The legend's "8 or 4 mice per group" matches the sheet. The
Fig. 3f survival curves contain 10 values per group, as stated.

**Figure 7** — panels 7a, 7b, 7i and parts of 7c and 7j reproduce, including the
four 7a WT vs *Znfx1*⁻ᐟ⁻ values (0.0734 / 0.3851 / 0.5914 / 0.1758) and the four
7b *Mavs*⁻ᐟ⁻ values.

**Formula audit — clear.** Loading all four workbooks with formulas visible found
**no formula in any cell plotted as an individual replicate**. The only formulas
present anywhere are the two `T.TEST` calls in `Source Data Fig 2.xlsx` row 53.
In particular, the `=constant − neighbour1 − neighbour2` pattern that pins a
triplicate mean and reduces the effective *n* is **absent** from this package.

---

## Screens run that do not support a finding

Reported here so the editor knows they were performed and why they are not in the
findings list.

- **Terminal-digit / last-digit uniformity.** `scripts/digit_analysis.py` initially
  returned χ² *p* < 0.0001 for all four workbooks. **This result is an artifact and
  should be disregarded.** Python's float representation strips trailing zeros, so
  the digit `0` has a count of zero by construction; and the sheets mix 1-, 2- and
  7-decimal-place precision, which violates the test's uniformity assumption.
  Corrected re-runs restricted to digits 1–9 and to the ≥4-dp subsets gave Fig. 1
  *p* = 0.0054, Fig. 2 *p* < 0.0001, Fig. 3 *p* < 0.0001, Fig. 7 *p* = 0.0952 —
  still confounded by mixed precision. Per the skill's own guidance, a
  distributional screen of this kind cannot carry a finding on its own. It is
  reported as *screen run, not a finding*.
- **Benford's law.** Not applicable. The values are normalised fold-changes and
  ratios clustered within one to two orders of magnitude; Benford requires a
  distribution spanning several.
- **GRIM / GRIMMER** (`scripts/grim_check.py`). Not applicable. No mean in this
  manuscript is derived from an integer or fixed-granularity scale — all reported
  quantities are continuous (fold-change, pg ml⁻¹, % GFP⁺).
- **Statcheck** (`scripts/statcheck.py`). Not applicable as written. The manuscript
  reports exact *P* values with no accompanying test statistic or degrees of
  freedom, so there is nothing to recompute *from*. Direct recomputation from raw
  replicates was substituted — a stronger check, and the basis of findings 3, 5, 7,
  8 and 9.

---

## Not checked

These were outside what the supplied files or this skill can assess. Listed so the
editor knows what has *not* been covered, not because they are suspected.

- **Image and blot forensics — out of scope for this skill.** Source Data Figs. 4,
  5 and 6 are large PDFs of uncropped blot images (19.6 MB, 13.0 MB, 6.7 MB) with
  no numeric content. Screening for band duplication, splicing or manipulation
  requires dedicated tooling (e.g. ImageTwin, Forensically, Proofig) and was **not
  performed**.
- **Figures 4, 5 and 6 statistics — unverifiable.** No numeric source data was
  supplied for these figures, so none of their reported *P* values (including
  0.0009, 0.0006, 0.0140, 0.0097, 0.0060, 0.0001, 0.0038, 0.0040, 0.0028, 0.0002,
  0.9733, 0.0026, 0.0005) could be checked. If a deeper check is warranted, the
  per-replicate values for these figures should be requested from the authors.
- **Batch-effect screening** (genomics section). Not performed: no raw expression
  or sequencing matrix was supplied, only the summary values plotted in the figures.
- **Multiple-testing correction verification** (genomics section). Not performed:
  no uncorrected *P*-value set was supplied.
- **Outlier-exclusion symmetry** (preclinical section). Not assessable: the
  manuscript does not describe an outlier-exclusion rule, and the supplied sheets
  give no indication of whether any values were removed before plotting.
- **Plagiarism and text-overlap screening.** Not part of this skill.
- **Domain methodology judgement.** Whether the experimental design supports the
  biological conclusions is a peer-review question, not a data-integrity one, and
  was not assessed.
- **Supplementary figures.** No supplementary source data was supplied with this
  package; only Source Data for main-text Figs. 1–7.

---

## Suggested next step

The two 🔴 items (findings 1 and 2) concern relationships between numbers that
independent measurement does not produce, and they are the items that warrant an
author response before anything else. A single request covering both would be:

> Please supply the primary, pre-normalisation measurements (Cq/Ct values or raw
> plate reads) and the derivation of the plotted values for Fig. 1h and for
> Fig. 7b–c, together with confirmation of how the replicates in each panel were
> obtained and whether any series were shared between conditions.

Findings 3, 4, 6 and 7 are straightforward requests for correction or for missing
data. Findings 5, 8 and 9 are clarifications that do not affect any stated
conclusion.
