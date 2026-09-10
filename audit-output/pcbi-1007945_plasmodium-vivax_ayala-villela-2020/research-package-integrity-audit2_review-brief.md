# Review Brief: Malaria Drug-Resistance Modelling Paper

This brief summarizes an integrity audit of the paper "Early transmission of sensitive strain slows
down emergence of drug resistance in Plasmodium vivax" (Ayala & Villela, 2020, *PLOS Computational
Biology*) and its supplementary reproducibility code. It is written for researchers, reviewers,
editors, and authors, and does not require reading code or audit implementation details. A separate,
more technical document (the comprehensive technical audit) contains the full evidence and
methodology behind every statement here.

## B1. Review at a Glance

| Area | Assessment | What this means |
| --- | --- | --- |
| Package completeness | LIMITATION | Two supporting materials referenced by the paper (a rendered output document, and the code behind one figure) were not supplied, so parts of the paper could not be checked. |
| Checked manuscript-to-code parameter values | CONCERN | Two numeric input values differ between the paper's own parameter table and the supplied code. |
| Independently recalculated results | POSITIVE | The core mathematical formula behind one figure was recalculated from scratch, in a separate implementation, and its behavior matches how the paper describes it. |
| Full source-code execution | LIMITATION | The authors' original R code could not be run in this review because the required software was not available; this is a limitation of the review environment, not a finding about the code. |
| Misconduct inference | NEUTRAL | This audit checks whether reported numbers and code correspond. It does not assess, and does not find, any intent to mislead. |

**In brief:**
- The paper and its supplementary code were compared value-by-value for every fixed model input listed in the paper's main parameter table.
- Two of those input values do not match between the table and the code.
- The mathematical effect of both mismatches was independently recalculated: it is small (under 2%) and does not change the shape or ordering of the affected curves in the ranges checked.
- One figure in the paper (a parameter-sensitivity analysis) has no supporting code or data available to review at all.
- No part of this review concludes that any result is fabricated, invalid, or unreliable — only that two specific values could not be reconciled, and some material could not be checked because it was not supplied.

## B2. Issues Requiring Attention

| Priority | Assessment | Issue | Where to look | What the evidence shows | Why it matters | Recommended reviewer action |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | CONCERN | [F-01] Different human-population value used for a model parameter | Table 1 (parameter list); the code behind Figure 3 | The paper's Table 1 states the human population value as 625, but the supplied code uses 624 for this same parameter in both disease models. | Recalculating the affected formula with each value shows the difference changes the result by at most 0.08%, a very small amount that does not affect which curve is higher or lower in the figure. | Ask the authors to confirm which value (624 or 625) was actually used to produce the published figure, and to correct whichever source is wrong. |
| 2 | CONCERN | [F-02] Different latent-infection probability value for the P. vivax model | Table 1 (parameter list); the P. vivax code behind Figure 3 | The paper's Table 1 states this probability as 0.21, but the supplied P. vivax code uses 0.29. | Recalculating with each value shows this is the larger of the two discrepancies, shifting the affected P. vivax curves by up to about 1.9%, still a small amount that does not change their overall shape or ordering in the ranges checked. | Ask the authors to confirm which value (0.21 or 0.29) generated the published P. vivax curves, and to correct whichever source is wrong. |

Both items above are demonstrated discrepancies between two documents the authors themselves supplied (the paper's own table and its own code), not results of executing the code or comparing against external data.

## B3. What Checked Out Well

| Assessment | Check completed | Result | Scope limitation |
| --- | --- | --- | --- |
| POSITIVE | Every one of the paper's 19 listed model-input parameters was compared, for both disease models, against the corresponding value in the supplied code (38 comparisons total). | 32 of the 38 values matched exactly or fell within the range the paper allows; 4 did not apply to a given model; only 2 did not match (see B2). | This check covers only the fixed numeric inputs stated in Table 1/Table 2 — it does not cover the paper's narrative conclusions, its simulation results, or its fifth figure. |
| POSITIVE | The mathematical formula for the reproduction-number curves shown in Figure 3 was independently rebuilt from the paper's methods, in a separate program, and evaluated across the full range of drug-coverage values the paper considers. | The independently rebuilt formula behaves the same way the paper describes it, and let both concerns above be quantified rather than left as unmeasured discrepancies. | This covers only the underlying formula, not the plotting code that produces the actual figure image, and not the separate simulation code behind Figure 4. |

## B4. What Could Not Be Verified

| Assessment | Item | Why it could not be verified | Effect on the review | What would resolve it |
| --- | --- | --- | --- | --- |
| LIMITATION | Figure 5 (parameter-sensitivity analysis) | The paper describes this analysis and the software packages used to produce it, but no supporting code or result data for it was supplied for review. | This figure, and any conclusions drawn specifically from it, remain unverified by this audit. | The authors could supply the sensitivity-analysis code and its output data. |
| LIMITATION | Whether the published Figures 3 and 4 exactly match a run of the supplied code | The paper mentions a second supplementary document that was generated by running the code, which would let the published figures be checked directly, but that document was not supplied. The code itself also could not be executed in this review because the required software (the R programming language and its packages) was not available. | The figures could not be regenerated or directly confirmed against a known-good rendering in this review. | The authors could supply the rendered output document, or the review could be repeated in an environment with the required software installed. |
| NOT ASSESSED | Independent recalculation of Figure 4's simulation results | This was judged feasible with additional effort but was not completed within this review. | No conclusion, positive or negative, can be drawn about Figure 4 from this audit. | A follow-up review could rebuild this simulation independently, as was done for Figure 3's formula. |
| NOT ASSESSED | Systematic verification of the paper's narrative and comparative claims (for example, statements about which factors most affect drug resistance) | This review focused on the paper's numeric parameter table; a full list of every checkable statement in the paper's results and discussion was not built. | No conclusion, positive or negative, can be drawn about these statements from this audit. | A follow-up review could build a complete list of checkable claims and verify each one individually. |

None of the rows above indicate that anything in the paper is incorrect — they indicate that certain material was not available or not yet reviewed.

## B5. Paper Navigation Guide

| Paper location | What to check | Related item |
| --- | --- | --- |
| Table 1 (model parameters) | Compare the human-population value and the latent-infection probability against the code | F-01, F-02 |
| Figure 3 (reproduction-number curves) | Confirm which parameter values generated the published curves | F-01, F-02 |
| Figure 5 (parameter-sensitivity analysis) | Note that supporting code/data for this figure was not available for review | See B4 |
| Supplementary Information ("S2 File") | Note that this rendered document, which could confirm the other figures, was not available for review | See B4 |

## B6. Author Questions

| # | Location | Question for the authors | Why this question is needed |
| ---: | --- | --- | --- |
| 1 | Table 1 and Figure 3 | Table 1 states the human-population parameter as 625, but the supplied code uses 624 for both disease models. Which value was used to produce the published figure? | The paper and its own code disagree on this value. |
| 2 | Table 1 and Figure 3 | Table 1 states the latent-infection-probability parameter (for P. vivax) as 0.21, but the supplied code uses 0.29. Which value was used to produce the published figure? | The paper and its own code disagree on this value. |
| 3 | Supplementary Information | Could the rendered output document referenced as "S2 File" be made available, so the published figures can be checked directly against a known output of the code? | This document is mentioned but was not available for this review. |
| 4 | Figure 5 | Could the code and data behind the parameter-sensitivity analysis shown in Figure 5 be made available? | Neither was included with the material provided for this review. |

## B7. Bottom Line

**What is good:** Nearly all of the paper's listed model-input values (32 of 38 checked) match the supplied code exactly, and the core mathematical formula behind the main figure was independently rebuilt and confirmed to behave as described.

**What needs attention:** Two specific input values — a human-population count and a latent-infection probability — differ between the paper's own table and its own code. Both differences were measured and found to shift the affected results by less than 2%, without changing their overall pattern.

**What remains unknown:** One figure's supporting analysis was not available for review at all, and the published figures could not be directly regenerated or cross-checked against a known-good version because the required software and a reference document were both unavailable.

**What this does not mean:** This review does not conclude, and is not designed to determine, whether anyone acted improperly. It also does not confirm that every claim in the paper is correct — only the items listed above were checked.

## B8. Scope Note

This brief lists demonstrated issues, completed positive checks, and central verification limitations.
A concern indicates an evidence-backed discrepancy, while a limitation indicates that verification
could not be completed. Neither label implies misconduct. Absence from this brief does not mean every
other claim was independently reproduced. See the comprehensive technical audit
(`pcbi_1007945_integrity_audit.md`) for the full evidence, coverage, and limitations.
