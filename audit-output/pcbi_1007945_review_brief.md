# Research Package Integrity Audit — Issue-Focused Review Brief (Output B)

**Package:** Ayala MJC, Villela DAM (2020), PLOS Computational Biology 16(6):e1007945.
**Companion document:** `pcbi_1007945_integrity_audit.md` (comprehensive technical audit, Output A).
**Skill:** `research-package-integrity-audit2` (commit `c8e4d87`, tool-verified via SHA256 match).

## B1. Review Snapshot

- Package components reviewed: manuscript PDF + S1 supplementary R code (`pcbi.1007945.s001.Rmd`).
- Source execution status: `EXECUTION_NOT_ATTEMPTED` (no R runtime in this environment; no lockfile/container found to attempt an install).
- Independent recomputation status: `PARTIALLY_RECOMPUTED` — R0 formula independently re-implemented in Python and evaluated; Fig 4's ODE simulation and Fig 5's sensitivity analysis were not.
- Demonstrated issues: 2 (F-01, F-02), both parameter-table-vs-code mismatches.
- Issues with impact not yet determined: 0 — both findings' impact was quantified via independent recomputation.
- Central blocked checks: 3 (Fig 5 code/data missing; S2 rendered document missing; no execution of Fig 3/Fig 4 code).
- Package status: partially complete, minor demonstrated parameter discrepancies, no misconduct inferred.

## B2. Issues Requiring Attention

```text
[F-01] Nh = 624 in code vs. 625 in manuscript Table 1
Where: Table 1 ("m — Mosquitoes per human, Nm/Nh = 2435/625"); S1 Rmd, parf/parv vectors (2nd element)
What differs: code uses Nh=624 (matches Fig 4's initial conditions Sh=623+Is=1); Table 1 states 625
Why it matters: quantified — max 0.080% relative effect on R0 curves (both species); not qualitatively material
Evidence: DIRECTLY_INSPECTED, CROSS_DOCUMENT_MATCH, RECOMPUTED
Reviewer action: confirm which Nh value generated the published Fig 3 curves
```

```text
[F-02] phit = 0.29 in code (P. vivax) vs. 0.21 in manuscript Table 1
Where: Table 1 ("phit — probability of remaining with latent parasites = 0.21"); S1 Rmd, parv vector (12th element)
What differs: code uses 0.29 for all P. vivax R0 panels; Table 1 states 0.21 (single point value, no alternate table row)
Why it matters: quantified — max 1.85% (R0s) / 1.74% (R0r) relative effect, the dominant contributor to a combined ~1.9% shift; curve shape and sensitive-vs-resistant ordering unaffected in tested range
Evidence: DIRECTLY_INSPECTED, CROSS_DOCUMENT_MATCH, RECOMPUTED
Reviewer action: confirm which phit value generated the published P. vivax R0 panels (Fig 3, 1b-4b)
```

## B3. Paper Navigation Guide

- **Tables:** Table 1 — both F-01 (Nh) and F-02 (phit) originate here.
- **Figures:** Fig 3 — both findings affect the R0 curves plotted in this figure; Fig 5 — central blocked check (no supporting code/data supplied).
- **Supplementary information:** S1 File (`pcbi.1007945.s001.Rmd`) — contains the code where F-01/F-02 were located; S2 File — referenced but not supplied (blocked cross-check).
- No issues or central blocked checks were found in the Abstract, Methods narrative text, or Results narrative text — those sections were not independently claim-verified in this pass (see Output A, Section 6) and are therefore neither cleared nor flagged.

## B4. Blocked Central Checks

- **Fig 5 (parameter sensitivity, LHS analysis):** missing artifact — no code or result data supplied for this figure, though it is described in the Methods (R packages `lhs`, `sensitivity`). Affected: Fig 5 and any narrative claims about which parameters most influence resistance-emergence timing. Needed to resolve: author-supplied LHS code/data.
- **S2 File (rendered document):** missing artifact — the manuscript's own cross-check artifact for S1's output. Affected: ability to verify Fig 3/Fig 4 published images against a known-good render without re-executing R. Needed to resolve: author-supplied S2 File.
- **Fig 3 / Fig 4 execution:** no R runtime available in this audit environment. Affected: full-figure regeneration and pixel-level correspondence checks for both figures (the R0 *formula* underlying Fig 3 was independently recomputed in Python; the plotting code and Fig 4's ODE simulation were not). Needed to resolve: an R environment with `deSolve` and `latex2exp` installed.

## B5. Compact Author Questions

- Table 1 reports Nh = 625, but the supplied code uses Nh = 624 for all R0 calculations (both species) — which value generated the published Fig 3?
- Table 1 reports phit = 0.21, but the supplied code uses phit = 0.29 for the P. vivax R0 calculations — which value generated the published P. vivax panels of Fig 3?
- Could the S2 File (rendered document from S1) be supplied to allow direct cross-checking of the published figures?
- Could the Fig 5 sensitivity-analysis code and/or result data be supplied?

## B6. Scope Note

> This brief lists demonstrated issues and central blocked checks from the completed audit. It does not imply misconduct, and absence from this brief does not mean every other claim was independently reproduced. See the comprehensive technical audit (`pcbi_1007945_integrity_audit.md`) for full coverage and limitations.
