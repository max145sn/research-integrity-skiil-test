# Experiment Audit Report — "Meaning in Life" Dataset

**Date**: 2026-04-10
**Auditor**: External reviewer backend, fresh zero-context cross-model reviewer
(`gpt-5.3-codex`, high reasoning effort, sandboxed read-only, no prior
conversation context), substituting for `mcp__codex__codex` per the
`experiment-audit` skill's reviewer-independence requirement (that MCP tool is
unavailable in this environment; see "Reviewer Backend Note" below).
**Project**: `documents/Meaning in Life/` (byte-identical to `code/Code.R`,
`results/Data.csv`, `paper/Manuscript.pdf` at the repo root — verified via
`git diff --no-index`, no differences found)

## Overall Verdict: FAIL

## Integrity Status: fail

The FAIL is driven by **Check C (Result File Existence)**: a large share of
the manuscript's numeric claims (all of Study 2) reference a raw data file
that does not exist anywhere in this repository, so those claims cannot be
verified from the evidence provided. Study 4's claims, which *are*
independently verifiable, matched the underlying data. This is the same
missing-Study-2-data condition flagged in the earlier `paper-claim-audit` run
(`PAPER_CLAIM_AUDIT.md`), now assessed here specifically as an experiment
**integrity** issue (unverifiable ground truth / phantom results risk) rather
than a claim-accuracy issue.

## Checks

### A. Ground Truth Provenance: WARN
- **Evidence**: `Code.R:8-11` (hardcoded `setwd()` + `read.csv("Study2rawdataexp.csv")` / `read.csv("Study4rawdataexp.csv")`), `Code.R:263-275` (condition derived from survey column `RO-BR-FL_9`), `Code.R:288-305` (MIL outcome constructed from `MLQ_1..6` items with reverse-coding and attention-check exclusion applied before analysis).
- **Details**: For Study 4, the outcome (MIL) and condition grouping are both loaded directly from real participant survey responses in `Data.csv` — not model-generated or circularly derived. Attention-check-based exclusion is explicit in code and consistently disclosed in the manuscript. However, **Study 2's ground truth cannot be verified at all**: the raw file `Study2rawdataexp.csv` that `Code.R` expects does not exist anywhere in this repository (confirmed via `git log --all` and repo-wide glob in the earlier claim audit, and re-confirmed by the independent reviewer here). This is a provenance gap, not confirmed fabrication — but it means Study 2's reported ground truth is unverifiable and should not be treated as confirmed.

### B. Score Normalization: WARN
- **Evidence**: `Code.R:329, 332-338` (Cohen's d from raw sample means/SDs, no self-referential normalization), `Code.R:423-431, 447-460, 494-499` (regression coefficients, Bayes factor computation via `BayesFactor` package), manuscript §4.2.2 / §4.4.2 (Bayesian results).
- **Details**: No evidence of metrics being normalized against the model's own output (no fraudulent self-referential denominators found). However, the independent reviewer flagged a **Bayes factor notation inconsistency**: the manuscript reports values labeled `BF01 = 0.033`, `BF01 = 0.185`, `BF01 = 0.181` and interprets each as "evidence in favour of the null model." Under standard convention, `BF01` (null-over-alternative) values **below 1 indicate evidence *against* the null**, not for it — a value of 0.181 in `BF01` notation would normally mean the alternative model is ~5.5× more likely than the null. Our independent Study 4 recomputation (from the earlier claim audit) obtained `BF10 = 0.181` for the unadjusted test, which *is* correctly interpreted as favoring the null (since BF10 < 1 favors H0). This strongly suggests the manuscript's Bayesian results are internally consistent in *value* but are **mislabeled as BF01 when they are actually BF10** throughout §4.2.2/§4.4.2. We assess this as a likely notation/reporting error rather than fabrication (the underlying numeric computation and interpretation direction are consistent with genuine BF10 values), but it is a real defect that should be corrected, since as written the manuscript's own stated definition of BF01 contradicts its own numbers.

### C. Result File Existence: FAIL
- **Evidence**: Study 4 claims — manuscript §4.4 (Table 2/3 means, SDs, N=294/291, t(289)=-0.845, p=.399, adjusted regression) cross-checked against `Data.csv` via independent Python recomputation (`audit-output/recompute_study4.py`, corroborated independently by the fresh reviewer's own recomputation). Study 2 claims — manuscript §4.2 references analyses over `Study2rawdataexp.csv`, which does not exist in this repository (`Code.R:8-9, 53-101`; confirmed absent via repo-wide search).
- **Details**: All Study 4 numeric claims we can check (sample sizes, group means/SDs, unadjusted t-test/Cohen's d, adjusted regression coefficients, the (mislabeled) Bayes factors) matched the values recomputable directly from `Data.csv`. **Every Study 2 numeric claim (~15 statistics, per the earlier claim audit) is unverifiable** because its underlying raw data file is absent from the repository — this is exactly the "claimed results reference nonexistent files" fraud pattern this check is designed to catch. We cannot conclude fabrication (the file may simply not have been included when this repo was assembled), but from the evidence available in this repository, these claims are not currently backed by any accessible primary data.

### D. Dead Code Detection: WARN
- **Evidence**: `Code.R:28-32, 97` (unused item-level variables `st2$mil1..mil5` and `unstb2` computed but not fed into any downstream model), `Code.R:355-412` (exploratory Box-Cox transform / interaction / quadratic-term probing), manuscript "Unregistered exploratory analyses" section.
- **Details**: A few intermediate variables are computed in the Study 2 block but never referenced again (likely leftover/vestigial code, not concealment, since Study 2's core results are already unverifiable for other reasons). The larger exploratory analysis branch (outlier exclusion, Box-Cox transform, added interaction/quadratic terms) is clearly and consistently labeled as exploratory/unregistered in both code comments and the manuscript text, and its results are not substituted for the preregistered confirmatory numbers — this is a pass on the "phantom/undisclosed exploratory substitution" pattern specifically, even though the unused variables above are worth cleaning up.

### E. Scope Assessment: WARN
- **Evidence**: manuscript framing as a "direct replication" of Studies 2 and 4 of Heintzelman et al. (2013), plus an "Unregistered exploratory" meta-analysis pooling this replication's Study 4 effect with the original paper's Study 2 and Study 4 effects using hardcoded summary statistics from the original publication (`Code.R:494-562`).
- **Details**: Verifiable primary data in this repository supports only Study 4 (N=291 after exclusions). The manuscript's "direct replication" framing spans both Study 2 and Study 4, and its pooled meta-analytic conclusion draws on Study 2 results that cannot be checked here, plus external hardcoded statistics from the original 2013 study that are disclosed as coming from that source but are not independently re-derivable from anything in this repository. This is not necessarily inflated language (the manuscript does disclose its meta-analysis inputs), but the claimed scope exceeds what can be independently verified from the files provided, so it is flagged WARN rather than PASS.

### F. Evaluation Type: real_gt
- **Evidence**: `Code.R:269-275, 288-305` — outcome and condition are both drawn directly from human participant survey responses in the raw CSV.
- **Details**: This is a real human-subjects dataset (real_gt), not a synthetic/model-generated proxy, self-supervised setup, or simulation. This classification applies confidently to the verifiable Study 4 portion; Study 2's evaluation type cannot be confirmed since its raw data is absent, though the code and manuscript describe an analogous real-participant design.

## Action Items
- Locate and add `Study2rawdataexp.csv` to the repository (or otherwise make it available) so Study 2's ~15 numeric claims can be independently verified; until then, treat all Study 2 results as unverified in any downstream use of this manuscript.
- Correct the Bayes factor labeling in §4.2.2/§4.4.2: the reported values (0.033, 0.185, 0.181) appear to be BF10 (evidence ratio for alternative-over-null) mislabeled as BF01 (null-over-alternative); as written, the manuscript's own stated interpretation ("BF01 < 1 supports the null") is internally inconsistent with the standard definition of BF01.
- Remove or document the purpose of unused Study 2 intermediate variables (`st2$mil1..mil5`, `unstb2`) in `Code.R` — currently dead code with no effect on reported results, but worth cleaning up for auditability.
- If this manuscript's meta-analysis or "direct replication" claims are used elsewhere, qualify them to note that only Study 4 is independently verifiable from the materials in this repository.

## Claim Impact
- Study 4 sample sizes, means/SDs, t-test, Cohen's d, adjusted regression (Table 2/3, §4.4.1): **supported** — independently recomputed and matched.
- Study 4 Bayes factors (§4.4.2): **needs qualifier** — numerically reproducible but the BF01/BF10 labeling appears backwards; interpretation direction should be re-verified against the raw `BayesFactor` package output.
- Study 2 sample sizes, means/SDs, ANOVA, regression, Bayes factors (§4.2): **unsupported** — no raw data file exists in this repository to verify any of these claims.
- Pooled meta-analytic effect combining this study with the original 2013 paper: **needs qualifier** — depends on the unverifiable Study 2 result plus externally-sourced (not independently re-derivable) original-study statistics.
- Overall "direct replication of Studies 2 and 4" framing: **needs qualifier** — accurate for Study 4 only, given current repository contents.

## Reviewer Backend Note

The skill specifies `mcp__codex__codex` (model `gpt-6-astra`, reasoning
effort `ultra`) as the default reviewer backend, with `mcp__manual_review__review`
as a fallback if that MCP tool is unavailable. Neither MCP tool is available
in this environment. Consistent with the substitution already validated with
the user across the three prior `paper-claim-audit` runs, the executor
(Claude, this session) collected file paths only and dispatched a **separate,
stateless `task`-tool agent** (`agent_type: general-purpose`, `model:
gpt-5.3-codex`, high reasoning effort, sandboxed to a single self-contained
prompt with no reference to this conversation) to perform the actual A–F
integrity judgment. This preserves the skill's core "reviewer independence"
principle (different model family, zero prior context, executor does not
participate in the integrity judgment) even though the exact MCP tool named
in the skill is unavailable here.
