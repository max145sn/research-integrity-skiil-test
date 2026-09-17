# Peer Review Report

## Manuscript Information

**Title:** Mitochondria-localised ZNFX1 functions as a dsRNA sensor to initiate antiviral responses through MAVS  
**Manuscript ID:** DOI 10.1038/s41556-019-0416-0  
**Review Date:** 2026-09-16  
**Review Round:** Round 1

## Reviewer Information

**Reviewer Role:** Peer Reviewer 3 (Perspective / cross-disciplinary)  
**Reviewer Identity:** Mitochondrial cell biologist and RNA biologist, outside the innate-immunity community.  
**Review Focus:** I focus on whether the mitochondrial/sub-mitochondrial localization claim is established to cell-biological standards, whether the proposed sensor topology plausibly permits access to viral dsRNA, whether endogenous mitochondrial dsRNA is considered as a ligand class, and how far the conclusions generalize across the tested cell and animal systems. I do not attempt to serve as the primary statistics or innate-immunity-literature reviewer.

## Scoring Plan

Before reading the manuscript, I will score this paper from a mitochondrial/RNA-cell-biology perspective using the following criteria. (1) A title-level "mitochondria-localised" claim requires evidence beyond diffraction-limited colocalisation: at minimum endogenous-protein fractionation with multiple purity markers for nucleus, cytosol, ER/light membranes and mitochondria; protease-protection or selective permeabilization to distinguish cytosolic exposure from IMS/matrix protection; carbonate extraction or equivalent membrane-association testing; and controls showing that the result is not overexpression-, infection-, or crude-mitochondrial-contamination-driven. (2) A submitochondrial claim must specify the location/topology: OMM integral, OMM peripheral cytosolic face, IMS-facing, IMM, or matrix, and the proposed ligand-access route must be physically compatible with that topology. (3) For a mitochondrial dsRNA sensor claim, I will look for consideration of endogenous mitochondrial dsRNA/mtRNA as possible ligands or confounders, especially under infection or IFN stress. (4) I will distinguish functional antiviral evidence from localization evidence: broad antiviral phenotypes do not rescue weak submitochondrial assignment. (5) I will assess whether claims generalize across A549, HEK293T, MEF, PBMC/MDM, macrophage, and mouse experiments or are mainly inferred from one cell context. (6) Translational claims require at least a plausible therapeutic modality, selectivity/safety rationale, or disease-context evidence; otherwise they should be framed as speculative.

Pre-committed fatal triggers forcing Reject from this seat: (a) the central mitochondrial localization claim rests only on overexpressed fluorescence colocalisation without endogenous biochemical support; (b) the proposed topology is physically incompatible with viral dsRNA access and the manuscript offers no plausible bridge; (c) the paper's main conclusion requires broad mammalian generality but all decisive evidence is confined to one transformed cell line; or (d) source-data/manuscript correspondence for the localization or interaction panels is so incomplete that the relevant evidence cannot be interpreted.

## Overall Assessment

**Recommendation:** Major Revision  
**Confidence Score:** 4 ? mitochondrial localization/RNA biology competence, not innate-immunity specialist

**Summary Assessment:** This is an interesting and potentially important study identifying ZNFX1 as an IFN-stimulated antiviral factor with MAVS-linked signaling and viral-RNA binding. From my cross-disciplinary perspective, the functional antiviral story is broad enough to merit serious consideration: the authors test knockdown, knockout, overexpression, several RNA viruses, primary immune cells/macrophages, MEFs, A549/293T systems, and VSV infection in mice. The manuscript also does more than simple colocalisation for localization, using mitochondrial fractionation, proteinase K sensitivity and carbonate extraction. However, the title-level and Discussion-level phrasing overstate what the mitochondrial evidence establishes. The data support mitochondrial association, likely with the outer surface/peripheral OMM fraction, but topology and purity controls are incomplete for a field-standard submitochondrial assignment. More importantly, the mechanism by which a mitochondria-associated protein encounters viral dsRNA in intact cells is not demonstrated, and the paper does not address endogenous mitochondrial dsRNA/mtRNA as either a ligand, competitor, or stress-related confounder. These issues are repairable by stronger framing and additional targeted controls/experiments, so I do not recommend rejection. I would require major revision before accepting the strongest claims.

## Strengths

**S1. Multi-system functional evidence for an antiviral role**  
The manuscript does not rely on a single perturbation or cell type: ZNFX1 is assessed by siRNA, CRISPR knockout, overexpression, mouse infection, and macrophage/MEF/A549/293T contexts.  
**Evidence Anchor**: text: "Znfx1?/? BMDMs exhibited lower IFN-? or IFN-? secretion" Results/manuscript_extracted.txt:202-204; figure: Fig. 2g-j; figure: Fig. 3a-f

**S2. Endogenous viral-RNA association is tested, not only tagged overexpression**  
The authors include endogenous ZNFX1 RIP from infected A549 cells and map ZNFX1-associated sequences to the VSV genome, strengthening the sensor claim relative to overexpression-only pulldowns.  
**Evidence Anchor**: text: "binding ability of endogenous ZNFX1 to VSV, EMCV and Senda virus" Results/manuscript_extracted.txt:928-930; figure: Fig. 5c-e

**S3. Localization analysis includes biochemical topology assays**  
The localization section includes mitochondrial fractionation, proteinase K sensitivity and carbonate extraction, which is the correct experimental family for asking submitochondrial questions.  
**Evidence Anchor**: text: "protease protection assays were performed" Results/manuscript_extracted.txt:2057-2058; figure: Fig. 6a,c

**S4. MAVS interaction is examined with endogenous and specificity controls**  
The manuscript tests candidate adaptors and reports selective MAVS association, including endogenous co-immunoprecipitation and knockout-control contexts.  
**Evidence Anchor**: text: "associated with Flag-tagged MAVS but not with TRIF, MyD88 and STING" Results/manuscript_extracted.txt:2077-2080; figure: Fig. 6d-g

## Weaknesses

**W1. Submitochondrial localization is over-interpreted relative to topology controls**  
**Problem:** The data support mitochondrial association, but the manuscript elevates this to a title-level "mitochondria-localised" and Discussion-level "outer membrane" claim without enough purity/topology resolution. Proteinase K digestion shows exposure, and carbonate extraction places much ZNFX1 in the soluble/peripheral fraction, but this does not by itself distinguish cytosolic-face OMM association from post-lysis association with crude mitochondria or mitochondria-associated membranes. ER/MAM/light-membrane markers and orientation-specific epitope controls are not apparent in the submitted figure/source data text layers.  
**Evidence Anchor:** text: "most of the ZNFX1 protein were digested" Results/manuscript_extracted.txt:2059-2062; text: "ZNFX1 was largely recovered in the supernatant" Results/manuscript_extracted.txt:2070-2072; dataset: Source Data Fig 6.pdf ? text layer lists Fig. 6a/6c blot labels including ZNFX1, Lamin B, ?-actin, MAVS and COX IV but no ER/MAM marker label.  
**Why it matters:** The paper's title and mechanistic model depend on where ZNFX1 sits. In mitochondrial cell biology, crude mitochondrial enrichment plus protease sensitivity is not sufficient to define a stable OMM sensor topology.  
**Suggestion:** Add or cite experiments using purified mitochondria versus MAM/light-membrane fractions with ER/MAM markers (for example calnexin/VDAC/TOM20 as appropriate), selective permeabilization or epitope orientation mapping, and endogenous immunofluorescence/super-resolution or proximity labeling. If not available, soften the claim to "mitochondria-associated peripheral protein."  
**Severity:** Major  
**Confidence:** 5 ? direct mitochondrial localization expertise

**W2. The ligand-access mechanism is not physically resolved**  
**Problem:** The model requires a mitochondria-associated ZNFX1 molecule to encounter cytosolic viral dsRNA and signal to MAVS. The manuscript demonstrates RNA binding after immunoprecipitation or lysate-based pulldown and separately demonstrates mitochondrial association, but it does not show in intact cells that viral RNA is bound at the mitochondrial surface, nor whether infection-induced ZNFX1 specks are the RNA-bound signaling compartment.  
**Evidence Anchor:** text: "overexpressed ZNFX1 in 293T cells and then performed pull-down" Results/manuscript_extracted.txt:925-928; text: "ZNFX1 is localised to the outer membrane of mitochondria" Discussion/manuscript_extracted.txt:2147-2151; figure: Fig. 5a-f and Fig. 6a-c,h  
**Why it matters:** A sensor can bind RNA in lysate but still fail to access that ligand at the proposed subcellular site in living cells. This is especially important for a peripheral OMM protein whose ligand is described as viral dsRNA.  
**Suggestion:** Provide in situ evidence linking ZNFX1, viral RNA and mitochondria/MAVS: RNA-FISH plus endogenous ZNFX1/MAVS proximity, mitochondrial-fraction RIP under nuclease-protected conditions, proximity ligation, or biochemical fractionation showing viral RNA enrichment with ZNFX1-positive mitochondrial fractions before lysis mixing.  
**Severity:** Major  
**Confidence:** 4 ? strong cell-biological competence; viral-RNA biogenesis details outside my core field

**W3. Endogenous mitochondrial dsRNA/mtRNA is not considered as a ligand or confounder**  
**Problem:** ZNFX1 is proposed as a mitochondrial dsRNA sensor and preferentially binds HMW poly(I:C), yet the manuscript frames ligand identity almost exclusively as viral RNA. It does not test whether ZNFX1 binds mitochondrial transcripts/dsRNA, whether viral infection changes mtRNA release, or whether endogenous mtRNA contributes to basal or infection-induced ZNFX1-MAVS signaling.  
**Evidence Anchor:** absence: Results/Discussion and Fig. 5 RIP/RIP-seq ? expected assessment of endogenous mitochondrial dsRNA/mitochondrial transcript ligands; checked manuscript_extracted.txt lines 921-955, 2034-2088, 2123-2202 and Source Data Fig 5/6 text layers.  
**Why it matters:** Mitochondria produce immunostimulatory RNAs, including dsRNA species, and mitochondrial stress can release RNA to cytosol. Without excluding or incorporating this ligand class, the interpretation "viral dsRNA sensor" may be incomplete.  
**Suggestion:** Screen ZNFX1 RIP/RIP-seq for mitochondrial reads in mock and infected cells, test RNase III/J2-sensitive mitochondrial dsRNA colocalization or binding, and determine whether perturbing mitochondrial RNA degradation/release changes ZNFX1-MAVS signaling. At minimum, discuss this limitation.  
**Severity:** Major  
**Confidence:** 5 ? direct mitochondrial RNA biology expertise

**W4. Localization generality lags behind functional generality**  
**Problem:** Antiviral phenotypes are shown across several systems, but decisive localization/topology experiments are mainly A549 fractionation/protease assays and tagged A549/293T imaging/interaction contexts. The manuscript does not show endogenous ZNFX1 localization in PBMC/MDM/BMDM/MEF or infected mouse tissues, even though these systems support the broader physiological claims.  
**Evidence Anchor:** text: "Mitochondrial fraction isolated from A549 cells" Fig. 6 legend/manuscript_extracted.txt:2037-2039; text: "Confocal microscopy of 293T cells transfected with Flag-ZNFX1" Fig. 6 legend/manuscript_extracted.txt:2042-2043  
**Why it matters:** The claim that a mitochondrial ZNFX1-MAVS mechanism explains broad antiviral defense is stronger if the same localization is endogenous and conserved in the key primary/animal systems.  
**Suggestion:** Add endogenous fractionation or imaging in at least one primary immune/macrophage system and one mouse-derived cell type, or explicitly state that submitochondrial localization was established in A549/293T-derived experiments and remains to be generalized.  
**Severity:** Major  
**Confidence:** 4 ? generalizability assessment within my cell-biology scope

**W5. dsRNA specificity is blurred by the poly(dA:dT) response**  
**Problem:** The manuscript's title and abstract call ZNFX1 a dsRNA sensor, but reporter assays state that ZNFX1 enhances responses to poly(dA:dT) as well as poly(I:C). Later pulldown/competition data argue against direct DNA binding. The manuscript does not clearly reconcile whether poly(dA:dT) is an indirect effect, transfection/stress artifact, or evidence of broader nucleic-acid pathway modulation.  
**Evidence Anchor:** text: "poly(I:C) or poly(dA:dT) in a dose-dependent manner" Results/manuscript_extracted.txt:623-624; text: "cGAS but not ZNFX1 binds to both single- and double-stranded DNA" Results/manuscript_extracted.txt:942-944  
**Why it matters:** From a ligand-biology perspective, specificity is central to calling ZNFX1 a dsRNA sensor rather than a broader amplifier of nucleic-acid-triggered IFN signaling.  
**Suggestion:** Clarify the poly(dA:dT) result mechanistically, preferably by testing STING/cGAS dependence and direct DNA binding under matched conditions, or narrow the claim to viral-RNA-biased sensing plus pathway amplification.  
**Severity:** Major  
**Confidence:** 4 ? RNA-ligand specificity expertise; innate DNA pathway details partly outside my lane

**W6. The therapeutic-target claim is premature**  
**Problem:** The Introduction and final paragraph move from a mechanistic antiviral factor to therapeutic targeting without evidence for druggability, selectivity, timing, tissue safety, or whether activating ZNFX1 would be beneficial versus inflammatory.  
**Evidence Anchor:** text: "provides a target for antiviral therapy" Introduction/manuscript_extracted.txt:59-61; text: "may serve as a strategy for early therapeutic intervention" Discussion/manuscript_extracted.txt:2199-2201  
**Why it matters:** ZNFX1 is an IFN-linked mitochondrial/RNA-binding factor. Therapeutic activation could have mitochondrial-stress or autoinflammatory liabilities, and the current data do not define an intervention route.  
**Suggestion:** Reframe as a biological pathway that may inform future antiviral strategies, or add disease-relevant pharmacologic/genetic modulation and safety data.  
**Severity:** Minor  
**Confidence:** 4 ? translational plausibility assessment from mitochondrial stress biology

## Detailed Comments

**Introduction and framing.** The opening rationale is clear: SF1 helicases are understudied relative to SF2 helicases, and ZNFX1 emerges from VSV-infected MDM expression data. However, the manuscript introduces ZNFX1 immediately as an "ISG and mitochondrial-localised dsRNA sensor" before the localization evidence is presented (manuscript_extracted.txt:54-61). I would prefer more cautious first framing, because the mitochondrial evidence later supports association but not fully resolved topology.

**Results: expression and antiviral phenotypes.** The breadth of systems is a real strength. The manuscript uses A549, L929, 293T, MEF, PBMC expression, BMDM infection, and mice. The RNA-virus versus HSV-1 contrast is useful for scoping the claim. From my seat, these data support an antiviral role but do not by themselves specify mitochondrial mechanism.

**Results: viral-RNA binding.** The endogenous RIP and VSV-genome mapping are stronger than tagged overexpression alone. Still, the cell-biological question remains open: the RIP workflow extracts from infected cells and therefore demonstrates association recoverable after lysis, not necessarily the compartment in which recognition occurs. The preference for HMW poly(I:C) is consistent with dsRNA-biased binding, but the manuscript should explicitly reconcile the poly(dA:dT)-responsive reporter result.

**Results: localization and MAVS interaction.** Figure 6 is the key section for my review. The authors use the right classes of assays: fractionation, proteinase K, carbonate extraction, adaptor co-IP, endogenous co-IP, and confocal microscopy. The interpretation should be tightened. Proteinase K digestion of most ZNFX1 argues cytosolic exposure; carbonate supernatant argues peripheral association; together these are compatible with a peripheral cytosolic-face OMM-associated protein. They are less definitive for a stable outer mitochondrial membrane protein, especially without ER/MAM/light-membrane controls and without topology-specific epitope mapping. The confocal data are supportive but are overexpressed, diffraction-limited, and cannot establish submitochondrial localization.

**Discussion and model.** The discussion appropriately distinguishes ZNFX1 from RIG-I/MDA5 and proposes an early priming role. The model would be substantially stronger if it addressed two mitochondrial-RNA issues: how cytosolic viral dsRNA reaches mitochondria-associated ZNFX1 in intact cells, and whether endogenous mitochondrial dsRNA or mtRNA release participates in basal/viral ZNFX1-MAVS signaling. The discussion should also state the localization limitation plainly if no further experiments are added.

**Methods and source data.** The Methods provide useful details for RIP, confocal microscopy, fractionation, proteinase K, and carbonate-associated procedures. The source-data PDFs for Figs. 4-6 appear to carry only label text layers for blot panels, which is adequate for identifying which blots are present but not for quantitative or image-integrity evaluation. I did not perform pixel-level image forensics.

## Questions for Authors

1. Does endogenous ZNFX1 bind mitochondrial transcripts or J2-positive mitochondrial dsRNA in mock or virally infected cells, and were mitochondrial reads present in the ZNFX1 RIP-seq data?
2. Can the authors define ZNFX1 topology more precisely: cytosolic-face OMM peripheral protein, IMS-facing peripheral protein, or another mitochondria-associated compartment?
3. Are ER/MAM/light-membrane markers available for the mitochondrial fractions used in Fig. 6a,c to exclude contamination by membranes that co-purify with crude mitochondria?
4. How do the authors reconcile ZNFX1-enhanced poly(dA:dT)-triggered reporter activity with the conclusion that ZNFX1 is specifically a dsRNA sensor?

## Minor Issues

- The manuscript alternates between "localises" and "localizes" in different parts of the extracted text/source captions; standardize style.
- "includeing" appears in the Fig. 5 legend and should be corrected to "including."
- The final paragraph spells "ZFNX1" instead of "ZNFX1."
- "nucleic fractions" in the Fig. 6 legend likely means "nuclear fractions."
- The phrase "as is the case with interferon-stimulated genes alone" in the abstract is difficult to parse.

## Criterion-Bound Judgements

Calibration status: `NOT_CALIBRATED`

| Dimension | Criterion source | Judgement (EXCEEDS/MEETS/PARTLY_MEETS/DOES_NOT_MEET/NOT_ASSESSED) | Evidence anchor(s) | Rationale | Uncertainty / scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Originality | Cross-disciplinary novelty of a mitochondria-associated SF1 helicase/RNA sensor | MEETS | text: "helicase SF1 is rarely characterized in sensing pathogenic nucleic acids" Introduction/manuscript_extracted.txt:24-28 | The ZNFX1-MAVS viral-RNA sensor model is novel and biologically interesting. | I did not adjudicate innate-immunity priority beyond the manuscript's framing. | Yes |
| Methodological Rigor | Mitochondrial localization and RNA-cell-biology evidence standards | PARTLY_MEETS | figure: Fig. 6a,c; text: "protease protection assays were performed" Results/manuscript_extracted.txt:2057-2058 | The authors use relevant assays, but topology, purity and in situ ligand-access controls are incomplete. | Pixel-level blot assessment was out of scope. | Yes |
| Evidence Sufficiency | Sufficiency for title-level mitochondrial dsRNA sensor claim | PARTLY_MEETS | text: "ZNFX1 was largely recovered in the supernatant" Results/manuscript_extracted.txt:2070-2072; absence: Results/Discussion ? expected endogenous mitochondrial dsRNA assessment; checked manuscript_extracted.txt lines 921-955 and 2123-2202 | Functional antiviral evidence is broad, but localization/topology and ligand identity are not fully sufficient for the strongest wording. | Other reviewers may judge antiviral signaling sufficiency differently. | Yes |
| Argument Coherence | Physical coherence between location, ligand access and MAVS signaling | PARTLY_MEETS | text: "ZNFX1 is localised to the outer membrane of mitochondria" Discussion/manuscript_extracted.txt:2147-2151; figure: Fig. 5a-f | The MAVS link is coherent, but the route of viral dsRNA access to mitochondrial ZNFX1 is not demonstrated. | Exact viral replication compartment biology is partly outside my specialist lane. | Yes |
| Writing Quality | Clarity, precision and claim calibration | PARTLY_MEETS | text: "may serve as a strategy for early therapeutic intervention" Discussion/manuscript_extracted.txt:2199-2201 | The manuscript is readable, but some central terms are over-broad and several copyediting issues remain. | I assessed extracted text, not typeset proof corrections beyond it. | No |
| Literature Integration | Integration with mitochondrial RNA biology and localization standards | PARTLY_MEETS | absence: Introduction/Discussion ? expected mitochondrial dsRNA/mtRNA-release context; checked manuscript_extracted.txt lines 1-61 and 2123-2202 | The innate-sensing literature is discussed, but mitochondrial RNA ligand biology and submitochondrial-localization standards are underdeveloped. | I did not run a full post-publication literature review. | Yes |
| Significance & Impact | Biological and translational significance | MEETS | text: "restrict the replication of RNA viruses" Abstract/manuscript_extracted.txt:80-82; text: "may serve as a strategy" Discussion/manuscript_extracted.txt:2200-2201 | The biological significance is substantial if the mechanism is refined; translational impact is speculative. | Therapeutic feasibility was not experimentally assessed. | Yes |

Unresolved decision-bearing criteria are localization/topology rigor, ligand-access coherence, mitochondrial-endogenous RNA exclusion/integration, and the breadth of localization generality across physiological systems. These are repairable: some require new targeted experiments, while others could be addressed by claim narrowing and transparent discussion. Without repair, I would not accept the title-level wording or the strongest mechanistic/translational claims, but the functional antiviral findings remain promising enough for major revision rather than rejection.
