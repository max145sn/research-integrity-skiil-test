# Claim-grounding report — *Mitochondria-localised ZNFX1 functions as a dsRNA sensor to initiate antiviral responses through MAVS*

**Manuscript.** Wang, Y., Yuan, S., Jia, X., Ge, Y., Ling, T., Nie, M., Lan, X., Chen, S. & Xu, A. *Nature Cell Biology* **21**, 1346–1356 (2019). DOI [10.1038/s41556-019-0416-0](https://doi.org/10.1038/s41556-019-0416-0). Source file `s41556-019-0416-0.pdf`.

**Skill.** `claim-grounding` — does every citation-backed claim actually say what its cited source says?

**Machine-readable companion.** [`claim_grounding_report_v1.json`](claim_grounding_report_v1.json)

---

## Summary

| | |
|---|---|
| Citation-backed claims graded | **24** |
| `substantiated` | 13 |
| `partial` | 7 |
| `not_substantiated` | 4 |
| `conflicting` | 0 |
| `source_unavailable` | 0 |
| Distinct citations identity-checked | 43 |
| Citation-identity mismatches | **1** (ref 43) |
| **Grounding risk score** | **0.3125** (0 = fully grounded, 1 = wholly ungrounded) |

Of the 51 references, 43 carry a graded claim. The remainder are methods citations or members of congruent background bundles.

### How the verdicts were reached

Three rules, applied mechanically rather than by judgement:

- **Span rule.** `substantiated` and `partial` require at least one *verbatim* quote from the fetched source, with a locator, drawn from one of that claim's own `evidence_uris`. A claim I believed but could not quote is `not_substantiated`, not "probably fine".
- **Identity gate.** Every `evidence_uri` was bound to a canonical record (Crossref + OpenAlex + Europe PMC) before any content was read. A displayed citation that does not match its canonical record downgrades an otherwise positive verdict.
- **Source content.** Europe PMC `resultType=core` abstracts, keyed by canonical DOI. Most of the cited literature is paywalled; where a claim's specific content could only be confirmed from a full text, that is stated rather than graded as though the full text had been read.

Resolver note: Crossref's bibliographic query returned F1000/"Faculty Opinions recommendation of …" stub DOIs (`10.3410/…`) as the top hit for thirteen references. Those are resolver artefacts, not citation defects, and were discarded before identity comparison. Page-range formatting differences (`639–649` vs `639–649.e6`), erratum page numbers and online-first vs issue year (ref 45: 2012 vs 2013) were likewise treated as non-diagnostic.

---

## Findings, ordered by severity

### 1. `not_substantiated` — the DHX9 sentence describes a different paper's result

> **Introduction, p.1346:** "DHX9 mediates NLRP9b recognition of dsRNA stretches and forms inflammasome complexes to promote the maturation of interleukin (IL)-18 and gasdermin D-induced pyroptosis¹⁰"

**Ref 10 as displayed:** Zhang, Z. et al. *J. Immunol.* **187**, 4501–4508 (2011).
**Canonical record:** "DHX9 pairs with IPS-1 to sense double-stranded RNA in myeloid dendritic cells", [10.4049/jimmunol.1101307](https://doi.org/10.4049/jimmunol.1101307). Identity: **matched**.

The cited paper's own summary is: *"these results suggest that DHX9 is an important RNA sensor that is dependent on IPS-1 to sense pathogenic RNA."* The words NLRP9b, inflammasome, IL-18, gasdermin D and pyroptosis appear nowhere in it. Every element of the manuscript's sentence except "DHX9" and "dsRNA" is unsupported.

The result described does exist in the literature — Zhu, S. et al., "Nlrp9b inflammasome restricts rotavirus infection in intestinal epithelial cells", *Nature* **546**, 667–670 (2017) — but that work is not in this reference list. This reads as a citation attached to the wrong sentence, or a sentence written from memory of a different paper.

**No span could be quoted. Verdict: `not_substantiated`.**

---

### 2. `not_substantiated` — the Discussion's quantitative premise is not in either cited source

> **Discussion, p.1354:** "However, expression of RIG-I and MDA5 is rare in resting cells and becomes detectable until 7 h in viral infection⁴²,⁴³."

This is the load-bearing sentence of the paper's argument: it creates the gap ("how the type I IFN is primed to initiate the early expression of a series of ISG genes … remains unanswered") that ZNFX1 is then proposed to fill. It carries two checkable components — a claim about basal expression, and a specific 7-hour threshold.

**Ref 42:** "DHX15 senses double-stranded RNA in myeloid dendritic cells", *J. Immunol.* **193**, 1364–1372 (2014), [10.4049/jimmunol.1303322](https://doi.org/10.4049/jimmunol.1303322). Subject: DHX15 as a MAVS-dependent RNA sensor. No statement about RIG-I/MDA5 basal expression or induction kinetics.

**Ref 43:** ZCCHC3 as an RLR co-receptor, [10.1016/j.immuni.2018.08.014](https://doi.org/10.1016/j.immuni.2018.08.014). Subject: ZCCHC3 enhancing RIG-I/MDA5 dsRNA binding and TRIM25 recruitment. Again nothing on basal expression or a time threshold.

Neither the "rare in resting cells" component nor the "7 h" figure can be quoted from either source. **Verdict: `not_substantiated`.**

**This claim also fails the identity gate independently — see finding 6.**

---

### 3. `not_substantiated` — three RLR-activation papers cited for a statement about ZNFX1 deficiency

> **Discussion, p.1354:** "Although ZNFX1 binds to virus RNA and interacts with MAVS in a fashion independent of RIG-I and MDA5, the deficiency of ZNFX1 could impair the induced expression of a series of ISGs, including RIG-I or MDA5, leading to antiviral defect in the early stage of virus infection⁴⁷⁻⁴⁹."

| Ref | Canonical record | Subject |
|---|---|---|
| 47 | Hou, F. et al., *Cell* **146**, 448–461 (2011) | MAVS forms prion-like aggregates |
| 48 | Gack, M. U. et al., *Nature* **446**, 916–920 (2007) | TRIM25 ubiquitinates RIG-I |
| 49 | Jiang, X. et al., *Immunity* **36**, 959–973 (2012) | K63-ubiquitin oligomerises RIG-I and MDA5 |

All three identity-match their displayed citations. All three predate the identification of ZNFX1 as an antiviral factor, and none of them contains any ZNFX1 content whatsoever. No span can be quoted for a consequence of ZNFX1 deficiency.

The proposition is in fact supported by this manuscript's own data. The three citations appear either to have migrated from an adjacent sentence or to have been intended as generic RLR-activation background — in which case they are attached to a claim they cannot carry.

**Verdict: `not_substantiated`.**

---

### 4. `not_substantiated` — the PKR sentence, and an error in the sentence independent of the citation

> **Introduction, p.1346:** "PKR impedes viral translation through phosphorylation of eIF2a elongation factors²⁷"

**Ref 27:** Munir, M. & Berg, M., "The multiple faces of proteinkinase R in antiviral defense", *Virulence* **4**, 85–89 (2013), [10.4161/viru.23134](https://doi.org/10.4161/viru.23134). Identity: **matched**.

The cited mini-review's stated subject is a *different* PKR function: *"a novel role of PKR has been unveiled, as it was shown that, upon the infection with certain viruses, PKR is crucial for the integrity of newly synthesized IFN mRNA."* Neither eIF2α nor translational shutdown is mentioned. No span supports the claim. **Verdict: `not_substantiated`.**

Separately, and independent of any citation: **eIF2α is a translation *initiation* factor**, not an elongation factor. The manuscript's descriptor is incorrect on its own terms.

---

### 5. `partial` — MOV10's function is inverted relative to the paper cited for it

> **Discussion, p.1354:** "In addition to ZNFX1, another representative of RNA helicase SF1, MOV10, is well conserved during evolution and shown to be a co-factor to enhance the nuclear export of viral mRNA³⁴."

**Ref 34:** Goodier, J. L., Cheung, L. E. & Kazazian, H. H. Jr., "MOV10 RNA helicase is a potent inhibitor of retrotransposition in cells", *PLoS Genet.* **8**, e1002941 (2012). Identity: **matched**. Open access.

The conservation half is groundable:

> "With homologs in other vertebrates, insects, and plants, MOV10 may represent an ancient and innate form of immunity against both infective viruses and endogenous retroelements."

The functional half is not. The source's subject is MOV10 as an *inhibitor*: *"MOV10 protein … inhibits retrovirus replication"* and *"severely restricts human LINE1 (L1), Alu, and SVA retrotransposons."* Nuclear export of viral mRNA is not discussed. The manuscript describes MOV10 as a **co-factor that enhances** a viral process; the cited work describes it as a **restriction factor**.

Graded `partial` rather than `conflicting` because the source is silent on nuclear export rather than contradicting that specific mechanism — but the polarity of MOV10's role is inverted relative to its own citation.

---

### 6. Citation-identity mismatch — ref 43 has a garbled volume and page

| | |
|---|---|
| **Displayed** | Lian, H. et al. … *Immunity* **18**, 49 (2018) |
| **Canonical** | "The Zinc-Finger Protein ZCCHC3 Binds RNA and Facilitates Viral RNA Sensing and Activation of the RIG-I-like Receptors", *Immunity* **49**, 438–448.e5 (2018), [10.1016/j.immuni.2018.08.014](https://doi.org/10.1016/j.immuni.2018.08.014) |

The displayed volume (18) and page (49) look like a transposition: the true volume is 49, and "18" is plausibly the trailing digits of the year or the issue. As printed, the citation does not resolve to the work it names.

This is the only identity failure among 43 citations checked. Per the identity gate it would downgrade any positive verdict resting solely on ref 43; claim C20 (finding 2) was already `not_substantiated` on content.

---

### 7. `partial` — UPF1 is cited for an antiviral role its own reference disclaims

> **Results, p.1346–1347 (lines 111–115):** "MOV10, UPF1 and SEXT have been implicated previously in antiviral immunity, validating our screening approach based on RNAi and viral infection³⁴⁻³⁶"

- **Ref 36** (SETX) supports its half cleanly: *"Here we identified a role for SETX in controlling the antiviral response."*
- **Ref 34** (MOV10) supports its half: *"MOV10 protein … inhibits retrovirus replication."*
- **Ref 35** (UPF1) states the opposite polarity: *"whereas ectopic MOV10 restricts HIV-1 replication, the related UPF1 helicase functions as a cofactor at an early postentry step."* UPF1 is characterised there as **proviral**, not antiviral.

Also: the protein is written **"SEXT"** in the manuscript. The gene is **SETX** (senataxin), as in the title of ref 36. The same spelling appears at line 110 ("SEXT knockdown").

---

### 8. `partial` — the ARM-domain inference outruns the five papers cited for it

> **Discussion, p.1354:** "functional studies of the ARM domain containing proteins ALEX3 and SARM suggest that the ARM in ZNFX1 may be responsible for its mitochondrial localisation³⁷,³⁸,⁴⁴⁻⁴⁶"

Four of the five sources support the *premises* — that these are ARM-repeat proteins and that they localise to mitochondria:

- ref 44: *"The Armcx3 gene encodes a mitochondrial-targeted protein (Alex3) that contains several arm-like domains."*
- ref 37: *"a new protein family that localizes to the mitochondria … encoded by an array of armadillo (Arm) repeat-containing genes"*
- ref 45: *"The mitochondria-localized SARM triggers intrinsic apoptosis…"*
- ref 46: *"B. belcheri tsingtauense SARM was localized in mitochondria…"*

None supports the *causal* step the sentence infers — that the ARM domain is responsible for the localisation. Ref 45 in fact attributes SARM's functional activity to its SAM and TIR domains. Ref 38 (MAVS-driven SARM1 upregulation and neuronal death) contributes nothing to a localisation argument and is carried by the bundle.

The manuscript hedges with "may be responsible", which is appropriate; the grading reflects that the citations support the premises but not the inference.

---

### 9. `partial` — Mx1 cited as an inhibitor of virus *entry*

> **Introduction, p.1346:** "the myxovirus resistance 1 (Mx1) gene product is the inhibitor of virus entry²⁵"

**Ref 25:** Pillai, P. S. et al., *Science* **352**, 463–466 (2016). Identity: **matched**. The quotable span — *"mice expressing a functional Mx gene encoding a major interferon-induced effector against IAV in humans"* — supports Mx1 as an interferon-induced antiviral effector, but the paper is a study of caspase-dependent pathology and secondary bacterial burden. It makes no claim about a stage of the viral life cycle, and certainly not entry.

---

### 10. `partial` — the ISG sentence tracks ref 23's wording but cites ref 24, with a polarity flip

> **Introduction, p.1346:** "some ISGs can enhance innate pathogen-sensing capabilities or positively regulate IFN signalling²⁴"

Compare ref **23** (Schneider, W. M. et al., *Annu. Rev. Immunol.* **32**, 513–545, 2014), which is in the reference list but is *not* the reference attached here:

> "we describe ways in which ISGs both enhance innate pathogen-sensing capabilities and **negatively** regulate signaling through the JAK-STAT pathway"

The first clause is near-verbatim. The second is reversed. The reference actually attached, ref 24 (Schoggins et al. 2011), is an ISG overexpression screen; it supports functional diversity among ISGs (*"Broadly acting effectors included IRF1, C6orf150 …, HPSE, RIG-I …, MDA5 … and IFITM3"*) but says nothing about regulation of IFN signalling in either direction.

---

### 11. `partial` — ref 14 is an SF2 review carried in an SF1 bundle

> **Introduction, p.1346:** "helicase SF1 is rarely characterized in sensing pathogenic nucleic acids, although these proteins share a conserved core composed of two tandem RecA domains with ATPase activity and RNA binding ability¹²⁻¹⁴"

Refs 12 and 13 support a shared catalytic core — ref 13: *"SF1 and SF2 helicases share a catalytic core with high structural similarity."* Ref 14 (Linder & Jankowsky, "From unwinding to clamping — the DEAD box RNA helicase family") is a review of the **DEAD-box family, which is SF2**; nothing in it speaks to SF1 or to RecA-domain architecture. The specific phrase "two tandem RecA domains" is not stated in any of the three abstracts.

---

### 12. `partial` — ref 33 grounds the dataset, not the discovery

> **Introduction, p.1346:** "we analysed previously published … IVT-SAPAS data of VSV-infected monocyte-derived macrophages (MDMs) and identified ZNFX1 (a member of helicase SF1) as an ISG and mitochondrial-localised dsRNA sensor³³"

Ref 33 (Jia, X. et al., *Nat. Commun.* **8**, 14605, 2017) is the correct provenance for the dataset — *"genome-wide poly(A) sites switch … in response to vesicular stomatitis virus (VSV) infection in macrophages"* — and contains no ZNFX1 content. Because the superscript sits at the end of the whole sentence, it reads as external support for the identification, which is this manuscript's own finding.

---

## Substantiated claims

Thirteen claims were grounded with a verbatim span from their own cited source, several of them near-verbatim:

| Claim | Ref(s) | Note |
|---|---|---|
| cGAS and RLRs as the two main cytosolic sensors | 1–6 | Three of six independently quoted |
| DExD/H box helicases supplement RLR/cGAS function | 7 | |
| DDX60 in RIG-I-dependent and -independent responses | 8 | |
| DDX1/DDX21/DHX36–TRIF dsRNA sensing in DCs | 9 | |
| NLRP6 binds viral RNA via DHX15, interacts with MAVS | 11 | Near-verbatim |
| MAVS and STING adaptors induce type I IFNs and ISGs | 15, 16, 23 | |
| IFITM prevents infection before bilayer traversal | 26 | Verbatim |
| Tetherin retains virions on infected cell surfaces | 28, 29 | Verbatim |
| PQBP1 binds HIV-1 DNA, interacts with cGAS | 30 | Near-verbatim |
| RNF128 is an E3 ligase for K63 ubiquitination of TBK1 | 31 | Verbatim |
| OASL mediates RIG-I activation by mimicking polyubiquitin | 32 | Verbatim |
| RLRs as the principal viral RNA sensors | 3–6, 41 | |
| ZNFX1 required for epigenetic inheritance in *C. elegans* | 50, 51 | |

---

## Scope and limits

- **Abstract-level grounding.** Most of the cited literature is paywalled. Spans were taken from Europe PMC `core` abstracts. An abstract is a fair test for the kind of claim at issue here — a citation attached to a headline finding — but it cannot rule out that a `partial` claim is supported somewhere in a full text. Where that is the live possibility, the claim notes say so. The four `not_substantiated` claims are not of that kind: in each case the cited paper is about a different subject entirely.
- **Out of scope.** Claims resting on the manuscript's own experiments are `calculation`-type support and are not graded by this skill. For those, see the [`manuscript-consistency-audit`](../manuscript-consistency-audit/findings-report.md) output in the sibling folder.
- **Refs 17–22** were treated as congruent members of a ten-reference background bundle and were not separately quoted; refs 39, 40 and the methods citations carry no in-scope claim.
- **Not checked:** whether the cited works are the *best* available support, whether any citation is self-serving, and whether the reference list is complete. Those are review questions, not grounding questions.
