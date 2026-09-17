# Manuscript Consistency Audit — Findings Report (for the editor)

**Manuscript:** *Mitochondria-localised ZNFX1 functions as a dsRNA sensor to initiate antiviral responses through MAVS*
Wang Y., Yuan S., Jia X., Ge Y., Ling T., Nie M., Lan X., Chen S., Xu A.
*Nature Cell Biology* **21**, 1346–1356 (November 2019). DOI 10.1038/s41556-019-0416-0
File audited: `s41556-019-0416-0.pdf` (24 pp.)

**Package audited**

| Item | File | Notes |
|---|---|---|
| Main text + figure legends + Methods + Extended Data legends + Reporting Summary | `s41556-019-0416-0.pdf` | Text extracted with PyMuPDF; 3,129 lines |
| Source Data Fig. 1 | `Source Data Fig 1.xlsx` | `Sheet1` A1:K81 |
| Source Data Fig. 2 | `Source Data Fig 2.xlsx` | `Sheet1` A2:M72 |
| Source Data Fig. 3 | `Source Data Fig 3.xlsx` | `Sheet1` A2:T41 |
| Source Data Fig. 4 | `Source Data Fig 4.pdf` | 1 p., 17 embedded images (uncropped blots) |
| Source Data Fig. 5 | `Source Data Fig 5.pdf` | 1 p., 16 embedded images |
| Source Data Fig. 6 | `Source Data Fig 6.pdf` | 1 p., 36 embedded images |
| Source Data Fig. 7 | `Source Data Fig 7.xlsx` | `Sheet1` A2:K105 |

**Scope.** This audit asks only whether the package is internally consistent — whether the numbers, labels and cross-references in the manuscript agree with each other and with the source data supplied. It does not assess novelty, biological interpretation, or journal house style, and it does not draw any conclusion about intent.

**Headline.** Fourteen items survived verification. Items 1 and 4 are the substantive ones: the Fig. 7b/7c and Fig. 1h worksheets contain values that repeat across experimental groups to seven decimal places, and repeat in patterns (identical fractional parts, integer-valued differences) that independent measurement would not be expected to produce. Items 2, 3, 5, 6 and 7 are label, replicate-count and panel-coverage conflicts that the authors should be able to resolve from their records. The remainder are cross-reference and wording corrections.

---

## Part 1 — Findings

### 1. In the Fig. 7b/7c source data, values in different genotypes, different transfections and different genes share identical seven-decimal fractional parts and differ from one another by whole integers

**Location:** `Source Data Fig 7.xlsx`, `Sheet1` rows 10–43 (Fig. 7b and Fig. 7c).

Fig. 7b reports *IFNB1* and *IFIT1* transcript levels in wild-type, *Rig-I<sup>−/−</sup>*, *Mda5<sup>−/−</sup>* and *Mavs<sup>−/−</sup>* A549 cells transfected with EV, ZNFX1, RIG-I or MDA5. The legend states:

> **b**, qRT–PCR analysis of *Ifnb1* and *Ifit1* in wild-type, *Rig-I*<sup>−/−</sup>, *Mda5*<sup>−/−</sup> or *Mavs*<sup>−/−</sup> A549 cells transfected with the indicated expressing plasmids. … For **a–c,e,g–j**, *n* = 3 independent experiments.

These are therefore 3 independent biological replicates per gene × genotype × plasmid cell.

**First: one value appears twice, exactly, in two unrelated groups.**

| Cell | Gene | Genotype | Plasmid | Replicate | Value |
|---|---|---|---|---|---|
| `E25` | *IFIT1* | wild-type | ZNFX1 | 2 | **243.7718632** |
| `F31` | *IFIT1* | *Mda5*<sup>−/−</sup> | RIG-I | 2 | **243.7718632** |

**Second: the repetition is systematic.** Scanning all four workbooks, 534 stored values carry six or more decimal places. Of those, 30 values fall into 11 families that share an identical six-decimal fractional part — and all but two of those families sit inside `Source Data Fig 7.xlsx`. Within each family the members differ from one another by whole integers:

| Shared fractional part | Cells (gene / genotype / plasmid / replicate) | Values |
|---|---|---|
| `.1500527` | `F14` *IFNB1*/*Rig-I*<sup>−/−</sup>/RIG-I/1; `E17` *IFNB1*/*Mda5*<sup>−/−</sup>/ZNFX1/1; `F27` *IFIT1*/*Rig-I*<sup>−/−</sup>/RIG-I/1; `E30` *IFIT1*/*Mda5*<sup>−/−</sup>/ZNFX1/1; `F38` Fig. 7c *Rig-I*<sup>−/−</sup>/ZNFX1+VSV/1 | 127.1500527; 87.1500527; 287.1500527; 187.1500527; 9287.1500527 |
| `.7718632` | `E12` *IFNB1*/WT/ZNFX1/2; `F18` *IFNB1*/*Mda5*<sup>−/−</sup>/RIG-I/2; `E25` *IFIT1*/WT/ZNFX1/2; `F31` *IFIT1*/*Mda5*<sup>−/−</sup>/RIG-I/2 | 123.7718632; 153.7718632; 243.7718632; 243.7718632 |
| `.1158394` | `G12` *IFNB1*/WT/MDA5/2; `G17` *IFNB1*/*Mda5*<sup>−/−</sup>/MDA5/1; `G25` *IFIT1*/WT/MDA5/2; `G30` *IFIT1*/*Mda5*<sup>−/−</sup>/MDA5/1 | 115.1158394; 127.1158394; 185.1158394; 227.1158394 |
| `.4282229` | `F17` *IFNB1*/*Mda5*<sup>−/−</sup>/RIG-I/1; `F30` *IFIT1*/*Mda5*<sup>−/−</sup>/RIG-I/1 | 119.4282229; 219.4282229 |
| `.0412771` | `E18` *IFNB1*/*Mda5*<sup>−/−</sup>/ZNFX1/2; `E31` *IFIT1*/*Mda5*<sup>−/−</sup>/ZNFX1/2 | 117.0412771; 167.0412771 |
| `.3393576` | `G18` *IFNB1*/*Mda5*<sup>−/−</sup>/MDA5/2; `G31` *IFIT1*/*Mda5*<sup>−/−</sup>/MDA5/2 | 95.3393576; 155.3393576 |

Reading down the `.1500527` family: 87.1500527 → 127.1500527 → 187.1500527 → 287.1500527. The differences are exactly 40, 60 and 100. The `.4282229` pair differs by exactly 100.000000; the `.0412771` pair by exactly 50.000000; the `.3393576` pair by exactly 60.000000.

**Third: the same structure appears in the Fig. 7c block, at a different order of magnitude.** Row 41 (*Mda5*<sup>−/−</sup>, replicate 1) contains 9235.5383942, 29235.5307294, 40235.5333627 and 56235.5374922 — four of its six non-unity values agree to `235.53` and differ from one another by 20,000, 11,000 and 16,000 to within 0.008. Row 42 (replicate 2) contains 11563.8973829, 31563.8902421, 36563.8969814 and 48563.8900729 — four values agreeing to `563.89`, differing by 20,000, 5,000 and 12,000 to within 0.008. These four values per row span both viruses (VSV and EMCV) and both plasmid conditions (EV and ZNFX1), which the legend presents as separate measurements.

**Question for the author.** These cells are presented as independent qRT–PCR measurements from separate biological replicates in different cell lines, with different plasmids, and for two different transcripts. Can the authors explain how the same seven-digit decimal tails, and differences that are exact whole numbers, arose across them, and supply the primary instrument export (Ct values or equivalent) from which these relative-expression values were calculated?

---

### 2. The Fig. 7c legend names the wrong cell lines: it says wild-type, the source data contains *Rig-I<sup>−/−</sup>*, and the main text names only *Mda5<sup>−/−</sup>*

**Location:** Fig. 7 legend, panel c; Results, "ZNFX1-mediated signalling is independent of RIG-I and MDA5"; `Source Data Fig 7.xlsx` `Sheet1` rows 37–43.

Legend:

> **c**, qRT–PCR analysis of cellular VSV and EMCV loads in **wild-type or *Mda5*<sup>−/−</sup>** A549 cells transfected with the indicated expressing plasmids for 24 h followed by viral infection for another 12 h.

Main text:

> The qRT–PCR results also showed reduced viral loads of VSV and EMCV in ***Mda5*<sup>−/−</sup> cells** when cells were transfected with ZNFX1, RIG-I and MDA5 expressing plasmids, respectively (Fig. 7c).

Source data, column A of the Fig. 7c block:

| Row | Label |
|---|---|
| 38–40 | `Rig-i -/-` |
| 41–43 | `Mda5 -/-` |

The source data contains no wild-type group at all, and contains a *Rig-I<sup>−/−</sup>* group that neither the legend nor the main text mentions. All three descriptions disagree with each other.

**Question for the author.** Which two cell lines are plotted in Fig. 7c, and should the legend and the corresponding sentence in the Results be corrected to match?

---

### 3. One replicate in Fig. 7c is roughly ten-fold below the other two in its own group

**Location:** `Source Data Fig 7.xlsx` `Sheet1` cells `F38:F40` (Fig. 7c, *Rig-I<sup>−/−</sup>*, MDA5+VSV).

| Replicate | Value |
|---|---|
| 1 | 45514.8509464 |
| 2 | 42552.9712536 |
| 3 | **4176.8590572** |

Replicates 1 and 2 agree to within 7%. Replicate 3 is 10.9-fold lower than replicate 1 and 10.2-fold lower than replicate 2. With *n* = 3 and the data plotted as mean ± s.d., this single value moves the group mean from ~44,034 (replicates 1 and 2) to 30,748 and inflates the s.d. from ~2,095 to ~23,166. The neighbouring group in the same row, `E38:E40` (ZNFX1+VSV: 9287.15, 12345.86, 8765.64), shows no comparable spread. The pattern is consistent with a lost leading digit (41,768.6 would sit within the group), but that is a hypothesis, not a finding.

**Question for the author.** Can the authors confirm the third replicate value for the *Rig-I<sup>−/−</sup>*, MDA5+VSV condition in Fig. 7c against the original run?

---

### 4. In Fig. 1h, the second replicate of the IFN-α series and the second replicate of the IFN-β series agree to six decimal places at every time point

**Location:** `Source Data Fig 1.xlsx` `Sheet1` column E, rows 47–56.

The legend describes two separate treatments:

> **h**, *Znfx1* expression was measured by qRT–PCR in A549 cells after IFN-α or IFN-β treatment for the indicated time points. … For **b,e,h,j–l**, *n* = 3 independent experiments.

| Time point | IFN-α, replicate 2 | IFN-β, replicate 2 | Difference |
|---|---|---|---|
| 4 h | `E48` 10.374**4536** | `E53` 10.374**4568** | 0.0000032 |
| 8 h | `E49` 12.423**1824** | `E54` 12.423**1872** | 0.0000048 |
| 16 h | `E50` 8.368462**1** | `E55` 8.368462**4** | 0.0000003 |
| 24 h | `E51` 7.310462**3** | `E56` 7.310462**5** | 0.0000002 |

The first and third replicates behave normally — for example at 4 h, replicate 1 is 10.6172 (IFN-α) versus 10.1471 (IFN-β), and replicate 3 is 9.57983 versus 8.91767. Only the middle replicate series coincides, and it coincides at all four time points, in both directions of rounding, with discrepancies confined to the seventh or eighth significant digit.

**Question for the author.** Fig. 1h presents IFN-α and IFN-β stimulation as separate experiments. Can the authors account for the second replicate of each series being numerically identical to six decimal places at all four time points, and supply the underlying Ct values for both series?

---

### 5. Two of the four blocks behind Fig. 2h contain four replicates, although the legend states *n* = 3

**Location:** Fig. 2 legend; `Source Data Fig 2.xlsx` `Sheet1` rows 48–60.

Legend:

> For **d,e,h–j**, *n* = 3 independent experiments.

| Fig. 2h block | Source-data rows | Replicates present |
|---|---|---|
| uninfected / VSV | 50–52 | 3 |
| uninfected / EMCV | 50–52 | 3 |
| uninfected / H1N1 | 57–60 | **4** |
| uninfected / HSV-1 | 57–60 | **4** |

The two *P* values stored in the sheet (`E53` = 0.00418689 for VSV, `I53` = 0.00185006 for EMCV) are the only formulas in the whole package; both are `T.TEST` calls over the correct three-row ranges and both reproduce the values shown in the figure. No stored *P* value accompanies the four-replicate H1N1 and HSV-1 blocks.

**Question for the author.** How many independent experiments underlie each panel of Fig. 2h, and should the legend distinguish the H1N1 and HSV-1 panels from the VSV and EMCV panels?

---

### 6. The Fig. 7e and Fig. 7g source data contain only the empty-vector conditions, although both panels and their legends describe several transfections

**Location:** `Source Data Fig 7.xlsx` `Sheet1` rows 47–58 (cols. H–K) and rows 61–67 (cols. H–K); Fig. 7 legend, panels d, e, g, h.

Legend:

> **d**, FACS analysis of WT, *Rig-I*<sup>−/−</sup> and *Mda5*<sup>−/−</sup> A549 cells transfected with **ZNFX1, RIG-I or MDA5 expressing plasmids or EV** … **e**, Statistical analysis of the data from the multiple repeated FACS experiments in **d**. … **g,h**, *Ifnb1* and *Ifit1* mRNA transcripts were analysed by qRT–PCR in *Rig-I*<sup>−/−</sup> and *Znfx1*<sup>−/−</sup> DKO cells transfected with **the indicated expressing plasmids** followed by VSV or poly(I:C) stimulation.

The Fig. 7e block supplies only two columns, headed `EV` and `EV+VSV-GFP`, for each of `WT`, `Rig-i -/-` and `Mda5 -/-` — three values per column. The ZNFX1, RIG-I and MDA5 transfections that panel d displays, and that panel e is stated to quantify, are absent. The same applies to Fig. 7g, which supplies only `EV` and `EV+VSV` for *IFNB1* and *IFIT1*, with no genotype label and none of the plasmid conditions; the adjacent Fig. 7h block, by contrast, does carry the full `EV / ZNFX1 / RIG-I` × `± poly(I:C)` design.

For reference, the EV+VSV-GFP values that are present do reconcile with the percentages printed on the panel d flow plots (for example `EV+ 40.43%` for wild-type matches the first WT value, 40.43).

**Question for the author.** Can the authors supply the remaining source data for Fig. 7e and Fig. 7g, covering the ZNFX1, RIG-I and MDA5 transfections and the poly(I:C) conditions, and add the missing genotype label to the Fig. 7g block?

---

### 7. The uncropped-blot files carry panel labels for panels their legends describe as luciferase or qRT–PCR assays, and the Fig. 4 labels do not line up with the Fig. 4 legend

**Location:** `Source Data Fig 4.pdf`, `Source Data Fig 5.pdf`, `Source Data Fig 6.pdf`; Fig. 4, Fig. 5 and Fig. 6 legends.

The Fig. 4 legend assigns immunoblots to three panels only:

> **a,b**, A549 cells were transfected with IFN-β-Luc or ISRE-Luc … before **luciferase assays** (**b**). **c**, **Luciferase activity analysis** … **f**, **Immunoblot** analysis of ISGs level in wild-type and *Znfx1*<sup>−/−</sup> A549 cells or **RIG-I** expression in wild-type and *Znfx1*<sup>−/−</sup> MEFs … **g**, **Immunoblot** analysis of phosphorylated (p-) IRF3 and (p-) TBK1 in peritoneal macrophages … **h**, **Immunoblot** analysis of IRF3 dimerization … with **native PAGE**.

`Source Data Fig 4.pdf` contains five labelled blocks — `Figure 4 b`, `Figure 4c`, `Figure 4f`, `Figure 4g`, `Figure 4h` — i.e. uncropped blots for two panels the legend describes as luciferase assays. Within the file the antibody labels also sit under the wrong panel letters relative to the legend:

| Label in source-data file | Antibodies listed under it | Legend panel those antibodies belong to |
|---|---|---|
| `Figure 4f` | Native Page, SDS Page, IRF3, IRF3, GAPDH, ZNFX1 | **h** (IRF3 dimerization, native PAGE) |
| `Figure 4g` | GAPDH, RIG-I, ZNFX1-flag, GAPDH, TBK1 | **f** (ISGs / RIG-I immunoblot) |
| `Figure 4h` | p-IRF3, p-TBK1, GAPDH, IRF3 | **g** (p-IRF3 and p-TBK1) |

The same class of mismatch appears in the other two files. `Source Data Fig 5.pdf` contains a block labelled `Figure 5b` (bands: ZNFX1, MDA5, RIG-I), but the legend describes panel 5b as "immunoprecipitated and analysed by **qRT–PCR** to detect bound VSV-RNA". `Source Data Fig 6.pdf` contains a block labelled `Figure 6j`, but the legend describes 6j as "**qRT–PCR** analysis of *Ifnb1* and ISGs in A549 cells transfected with ZNFX1 and its truncated versions".

**Question for the author.** Can the authors confirm which published panel each uncropped blot in Source Data Figs. 4, 5 and 6 belongs to, and relabel the files so that the panel letters match the figure legends?

---

### 8. The Fig. 1e left panel plots nine tissues; its source data lists ten

**Location:** Fig. 1e (left), published axis; `Source Data Fig 1.xlsx` `Sheet1` row 9.

The source-data header row for the Fig. 1e left panel lists ten tissues:

> Muscle | Brain | Lymph node | Thymus | **liver** | Bowel | Heart | Kideny | Lung | Spleen

The tissue labels extracted from the published Fig. 1e left panel are: Muscle, Brain, Lymph node, Thymus, Bowel, Heart, Kideny, Lung, Spleen — nine categories, with liver absent. The right-hand panel of the same figure does plot Liver (its source-data block, rows 15–24, lists ten tissues beginning with `Liver`), so the omission is specific to the left panel.

**Question for the author.** Does the published Fig. 1e left panel omit the liver measurement that appears in the source data, and if so, should the panel or the source data be corrected?

---

### 9. Two columns of the Fig. 7i source data carry no genotype label

**Location:** `Source Data Fig 7.xlsx` `Sheet1` rows 96–100.

| Row 96 (genotype) | `WT` | `Rig-i-/-` | *(blank)* | `WT` | `Rig-i-/-` | *(blank)* |
|---|---|---|---|---|---|---|
| **Row 97 (treatment)** | siCtrl | siCtrl | siZNFX1 | siCtrl+VSV | siCtrl+VSV | siZNFX1+VSV |

The legend states:

> **i**, FACS analysis of **WT and *Rig-I*<sup>−/−</sup>** A549 cells transfected with siRNAs of control or *Znfx1* for 48 h followed by VSV-eGFP infection.

The two siZNFX1 columns cannot be assigned to a genotype, so the panel cannot be reconciled with its legend. The main text describes this experiment as knockdown "in *Rig-I*<sup>−/−</sup> cells":

> Moreover, siRNA knockdown of ZNFX1 could further enhance the viral loads of VSV-eGFP in *Rig-I*<sup>−/−</sup> cells (Fig. 7i).

**Question for the author.** Which genotype do the siZNFX1 and siZNFX1+VSV columns of the Fig. 7i source data correspond to?

---

### 10. The Data Availability statement and the Reporting Summary describe different source-data coverage and different locations

**Location:** Data availability section; Reporting Summary, "Data" section.

Data availability:

> Source data for **Figs. 1–7 and Extended Data Figs. 1–7** have been provided as **Statistics Source Data**.

Reporting Summary:

> Statistical source data for **Fig. 1-7 and Supplementary Fig. 1-6** are provided in **Supplementary Table**. Uncropped blots are provided in supplement figure.

The two statements disagree on which supplementary figures are covered (Extended Data Figs. 1–7 versus Supplementary Figs. 1–6) and on where the data sit (Statistics Source Data versus Supplementary Table). Separately, the Data Availability statement promises source data for Figs. 1–7 without distinguishing that the files supplied for Figs. 4, 5 and 6 are uncropped blots only and contain no numeric values, even though Fig. 4a–e,i, Fig. 5b,c,e,f and Fig. 6j are quantitative panels plotted as mean ± s.d. with *P* values.

**Question for the author.** Can the two statements be reconciled, and can numeric source data be supplied for the quantitative panels of Figs. 4, 5 and 6?

---

### 11. The Discussion's constitutive-expression claim cites three references, two of which show something else

**Location:** Discussion; Fig. 1 legend panel i; Extended Data Fig. 1 legend panel f; Extended Data Fig. 2 legend panel f.

> First, although RIG-I, MDA5 and ZNFX1 are commonly expressed ISGs regulated by the Jak-STAT pathway, the **constitutive** mRNA or protein levels of ZNFX1 are much higher than those of RIG-I and MDA5 in various tissues and cell types (**Fig. 1i and Extended Data Figs. 1f, 2f and 5a–c**).

Of the four references:

- **Fig. 1i** is "Immunoblot analysis of ZNFX1 and RIG-I expression in A549 cells **treated with human recombinant IFN-α or IFN-β** for the indicated time points" — a stimulated time course in one cell line, showing ZNFX1 and RIG-I only, not MDA5.
- **Extended Data Fig. 1f** is "RNA levels of *Znfx1* and *Rig-I* are significantly **increased after different virial infection** in different cell types" — again induced rather than constitutive, and again without MDA5.
- **Extended Data Fig. 2f** is "*Znfx1*<sup>−/−</sup> 293T and A549 clones were generated by the CRISPR-Cas9 method. **Deficiency of target genes in the KO clones were confirmed by immunoblotting** analysis" — knockout validation blots, which do not compare constitutive levels of the three sensors.
- **Extended Data Fig. 5a–c** is "The expression of *Znfx1*, *Rig-I* and *Mda5* in different tissues and cell types as per BioGPS" — this reference does support the claim.

The following sentence then cites Fig. 1i a second time, for a different property ("the induced expression of ZNFX1 is primed and reaches a peak much earlier than RIG-I upon IFN-α and IFN-β stimulation (Fig.1i)"), which is what Fig. 1i actually shows.

**Question for the author.** Should the constitutive-expression claim cite Extended Data Fig. 5a–c alone, or are Fig. 1i, Extended Data Fig. 1f and Extended Data Fig. 2f intended to support a different part of the sentence?

---

### 12. The Methods give a single infection condition for the knockdown FACS experiments; the Fig. 2a source data contains four

**Location:** Methods, "Flow cytometry"; `Source Data Fig 2.xlsx` `Sheet1` rows 2–10.

Methods:

> For gene knockdown, A549 and L929 cells were transiently transfected with siRNAs for 48 h and then challenged with VSV-eGFP for **6 h at 2 MOI**.

The Fig. 2a source-data block carries four condition labels:

| Cell line | Conditions in source data |
|---|---|
| A549 | `2 MOI (6h)`, `0.5 MOI (12h)` |
| L929 | `5 MOI (6h)`, `1 MOI (12h)` |

Three of the four are not described anywhere in the Methods. The sentence immediately following does allow variable conditions, but only for overexpression: "For gene overexpression, cells were transfected with the indicated expression plasmids for 24 h following VSV-eGFP infection at the indicated MOI for 6 h or 12 h."

**Question for the author.** Should the Methods be amended to cover the 0.5 MOI (12 h) A549 and the 5 MOI (6 h) and 1 MOI (12 h) L929 knockdown conditions shown in Fig. 2a?

---

### 13. The Fig. 2g source data contains two HSV-1 doses; the legend and main text mention one

**Location:** Fig. 2 legend; Results; `Source Data Fig 2.xlsx` `Sheet1` rows 43–46.

The Fig. 2g source data contains two separate HSV-1 rows, `HSV-1 low` (row 45) and `HSV-1 high` (row 46), each with five wild-type and five *Znfx1*<sup>−/−</sup> values. Neither the legend nor the Results text distinguishes two doses; the text reads:

> *Znfx1*<sup>−/−</sup> BMDMs exhibited lower IFN-α or IFN-β secretion after RNA virus infection, including VSV, EMCV and H1N1 **but not HSV-1**.

The negative conclusion for HSV-1 is drawn without stating which dose, or whether both, it refers to.

**Question for the author.** Does Fig. 2g plot both HSV-1 doses, and should the legend and the corresponding sentence specify the doses used?

---

### 14. The Author Contributions statement names joint co-first authors who are not first in the author list, and no equal-contribution footnote appears

**Location:** Author contributions; title page.

> **S.Y. and X.J. are joint co first authors.**

The author list begins Yao Wang (Y.W.), Shaochun Yuan (S.Y.), Xin Jia (X.J.). S.Y. and X.J. are the second and third authors. The title page carries no "These authors contributed equally" footnote of the kind that normally accompanies such a statement, and Y.W. — the listed first author — is not included in it. S.Y. is also credited as a supervising and corresponding author in the same paragraph ("S.Y. and A.X. supervised the research and wrote the paper").

**Question for the author.** Which authors are intended as joint first authors, and should a corresponding footnote be added to the title page?

---

## Smaller corrections

These are presented together because each is a single wording or spelling error with no consequence for the data.

| Location | Text as published | Note |
|---|---|---|
| Fig. 1e axis label; `Source Data Fig 1.xlsx` `H9` | `Kideny` | Misspelling of "Kidney". The Fig. 1e right-panel source-data block spells it `kidney` (row 18). |
| Fig. 1l legend; `Source Data Fig 1.xlsx` `A72`, `F72`, `A79`, `F79` | legend: `ΔZnfx1 **promotor**-Luc`; source data: `△Znfx1 **promoter**-Luc` | The legend and the source data spell the same construct differently; "promotor" is the misspelling. |
| Fig. 5e legend | "the x axis corresponds to the positions in the VSV genome, **includeing** of five coding genes" | Misspelling of "including"; the phrase also reads as if a word is missing. |
| Results, ZNFX1-RNA binding section | "binding ability of endogenous ZNFX1 to VSV, EMCV and **Senda**" | The virus is Sendai virus; the Fig. 5c legend spells it correctly as "SeV". |
| Discussion | "the antiviral immunity mediated by RLRs and MAVS. **ZFNX1**, …" | Transposition of ZNFX1. |
| Results, RLR-independence section | "we first performed endogenous co-immunoprecipitation assays and found that ZNFX1 interacts with neither RIG-I nor MDA5 in resting or VSV-infected cells." | No figure is cited for this experimental result, unlike every other claim in the paragraph. |

---

## Checked and not raised

Recording these so the editor can see the sweep was complete and know why certain patterns were left out.

**Replicate counts that reconcile.** Fig. 1b, 1e, 1j, 1k, 1l: *n* = 3 as stated. Fig. 1f: 9 uninfected-control and 14 HIV values, matching "*n* = 9 … *n* = 14". Fig. 1g: 18 values per group, matching "*n* = 18". Fig. 2a and 2b: *n* = 4 as stated; Fig. 2d, 2e, 2i, 2j: *n* = 3; Fig. 2g: *n* = 5. Fig. 3a and 3b: 4 mice per group; Fig. 3c: 8 (VSV) and 4 (HSV-1) per group, matching "8 or 4 mice per group"; Fig. 3f: 10 per group. Fig. 7a, 7b, 7c, 7g, 7h, 7i, 7j: *n* = 3.

**Arithmetic that reproduces.** The only two formulas in the whole package, `Sheet1!E53` and `Sheet1!I53` of `Source Data Fig 2.xlsx`, are `T.TEST` calls over the correct replicate ranges; the computed values 0.00418689 and 0.00185006 round to the 0.0042 and 0.0019 printed on Fig. 2h. A second pass over all four workbooks with cached values disabled found no other formulas, so no replicate cell is a calculated value masquerading as a measurement.

**Directional claims that hold.** The Fig. 7b claim that ZNFX1 overexpression induces *Ifnb1* and *Ifit1* "intensely in wild-type and *Mda5*<sup>−/−</sup> cells, slightly in *Rig-I*<sup>−/−</sup>, but not in *Mavs*<sup>−/−</sup> cells" reproduces from the source data in both the *IFNB1* and *IFIT1* blocks. The Fig. 2a MOI and time-point labels match the panel labels.

**Fig. 2g shared uninfected control.** The uninfected rows of the EMCV panel (row 38) and the H1N1 panel (row 41) are identical value for value: 1.32, 2.42, 1.53, 2.31, 1.63 (wild-type) and 1.53, 2.53, 1.48, 1.89, 1.54 (*Znfx1*<sup>−/−</sup>). Reusing a single set of uninfected wells as the baseline for two infections assayed in the same experiment is ordinary practice, and the legend does not claim these were separate controls. Not raised.

**Fig. 1f repeated value.** `0.249075` occurs three times in the RIG-I HIV-treated column (rows 34, 38, 41 of 14 values). Fig. 1f is a re-analysis of public GEO microarray datasets (accessions GDS4231/4214/1271/3210/6082/6063, cited in the Results and the Reporting Summary), where processed expression values can legitimately tie. Noted but not raised as a finding; it is worth one line in the query letter only because it is cheap to resolve.

**Fig. 7d flow percentages.** The percentages printed on the panel d plots and the values in the Fig. 7e source-data block appear in a different order in the text layer of the PDF, which would suggest a genotype/label swap. The text extraction of that figure is unreliable — figure text comes out as unordered fragments — so the apparent mismatch is an artefact of the extraction method, not evidence. Not raised.

**Screens run but not reported as findings.** Terminal-digit distribution, Benford-style leading-digit checks, and within-group correlation across the four workbooks were run as search tools to locate candidates. They found nothing beyond the exact-value duplications already reported at items 1 and 4, and no distributional result appears anywhere above or in the author-query letter.

---

*Findings 1–4 rest on exact values reproduced above and can be verified directly in the supplied workbooks. Findings 5–14 rest on quoted text set against quoted labels. This report describes what the package does and does not say; it makes no assessment of intent and no recommendation on the manuscript's disposition.*
