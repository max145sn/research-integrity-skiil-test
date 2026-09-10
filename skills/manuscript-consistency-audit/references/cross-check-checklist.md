# Cross-check sweep

Work through these categories. Each one is a class of error that recurs across
manuscripts, with the shape of the check that catches it.

## Contents

1. [Headline metrics across documents](#1-headline-metrics-across-documents)
2. [Series and list ordering](#2-series-and-list-ordering)
3. [Prose against source data](#3-prose-against-source-data)
4. [Derived quantities](#4-derived-quantities)
5. [Paired quantities and transpositions](#5-paired-quantities-and-transpositions)
6. [Tables against their own source data](#6-tables-against-their-own-source-data)
7. [Legends against text against data](#7-legends-against-text-against-data)
8. [Source-data workbook hygiene](#8-source-data-workbook-hygiene)
9. [Summary statistics computed inside the workbook](#9-summary-statistics-computed-inside-the-workbook)
10. [Units and conversion conventions](#10-units-and-conversion-conventions)
11. [Cross-references](#11-cross-references)
12. [Panel lettering](#12-panel-lettering)
13. [Methods coherence](#13-methods-coherence)
14. [Component and instrument specifications](#14-component-and-instrument-specifications)
15. [The rebuttal as a source](#15-the-rebuttal-as-a-source)
16. [Replicate counts and derived replicates](#16-replicate-counts-and-derived-replicates)

---

## 1. Headline metrics across documents

The paper's two or three signature numbers appear in the abstract, the
introduction's closing paragraph, the results, the discussion, at least one SI
note, and a comparison table. Collect all instances of each and diff them.

Watch for a single digit changing — `9.71` becoming `9.77` in one location. These
survive proofreading because both look plausible and neither is obviously wrong
in isolation.

Also confirm each instance carries the same **conditions**: same voltage, same
frequency, same device, same units. A metric quoted at one condition in the
abstract and a different condition in the results is not necessarily an error,
but the conditions must be stated in both places.

## 2. Series and list ordering

Sentences of the form "at A, B, C and D, X increased from p, q, r, s to w, x, y, z"
are unusually error-prone: the reader must hold three parallel lists in
register, and so must whoever wrote it.

Check each list against the same values wherever else they appear (a table, the
source data). A reversed list produces values that are individually correct and
collectively wrong.

A second check that needs no external source: does the series behave
monotonically in the direction the paper's own argument requires? A series
claiming performance improves as conditions worsen contradicts the thesis and is
usually a reversal.

## 3. Prose against source data

For every measurement quoted in prose that has a source-data sheet, confirm the
sheet reproduces it. Use the plateau statistic for settled traces and the mean
for steady ones.

The strongest version of this finding: **two of three quoted values match the
sheets exactly and the third does not.** The exact matches confirm you have
identified the right sheets and the right statistic, so the mismatch is the
paper's, not yours. Say this explicitly in the query — it is what makes the
finding undeniable.

## 4. Derived quantities

Re-derive every computed number from the paper's own stated inputs:

- efficiencies (output ÷ input)
- percentage improvements and ratios
- densities (value ÷ area — and check the implied area is consistent across
  every density in the paper)
- means and standard deviations of tabulated repeats
- weighted averages

When a set of derived values shares one input, recompute all of them. If most
reproduce and one does not, the shared input validates your method.

For weighted averages, check *which* weights were used. A result that fails to
reproduce with the stated weights but reproduces exactly with a different figure
from earlier in the same passage tells you precisely what went wrong — report the
diagnosis, not just the mismatch.

## 5. Paired quantities and transpositions

Where a sentence reports two percentages, ratios or improvements side by side,
compute both. Transposition — each value attached to the other quantity — is
common and invisible without arithmetic, because both numbers are correct.

## 6. Tables against their own source data

Comparison tables (literature benchmarks, per-reference bar charts) usually have
a matching source-data sheet. Compare row by row.

Look for duplicated value pairs within the source data: two references carrying
identical values to four decimal places usually means a copy-paste that
overwrote real data. Report the disagreement with the table as the finding, and
note the duplication as an observation — diagnosing the cause is the author's job.

Also check the table's own claim about this work against the values it lists
(e.g. a "power density exceeds 10 W/m²" summary against a table whose entries do
not).

## 7. Legends against text against data

For each figure, three sources should agree on the operating conditions: the
legend, the text that discusses it, and the source data. Any two disagreeing is a
finding; report all three values so the author can see which is the outlier.

Legends are the weakest of the three — they are written last and edited least.

## 8. Source-data workbook hygiene

Journals publish these files. Check:

- **Duplicated condition headers** — the same label on treatment and control,
  making the figure unverifiable from its own data.
- **Headers contradicting contents** — a column labelled for one variable holding
  values belonging to another.
- **Sheet names** matching the figures they claim to support.
- **Missing sheets** for figures that present quantitative data.
- **Values pasted into the wrong column type** — a voltage trace sitting in a
  column headed for current, recognisable because its magnitude and range belong
  to the other quantity.

## 9. Summary statistics computed inside the workbook

Where a sheet holds replicate measurements alongside a mean and a standard
deviation, **recompute the mean and SD from the replicates**. These columns are
spreadsheet formulas, and a formula whose range is off by one column silently
folds an unrelated value into every row.

This is high-yield for two reasons. The error is invisible in the plotted figure,
which just shows a slightly wrong bar with slightly wrong whiskers. And the wrong
value usually propagates into the SI prose, where it becomes a claim the paper
makes about its own device.

The diagnostic is precise: if the stated mean does not match the mean of the
replicates, try including the adjacent column — the label column, an index, a
condition value. When that reproduces the stated figure exactly, you have both
the error and its cause, which makes the query trivially actionable.

Do the same for any tabulated mean in the SI: check it against the values it
claims to summarise.

## 10. Units and conversion conventions

Where the paper converts between units, check that one convention is used
throughout. Mixed conventions produce numbers that are each defensible in
isolation and mutually inconsistent.

Recurring cases:

- **Molar gas volume** — 22.4 L/mol (STP, 273.15 K) versus 24.79 L/mol (SATP,
  298.15 K). A yield-to-moles conversion and a Faradaic-efficiency calculation
  in the same note using different volumes is a real inconsistency.
- **Peak vs. peak-to-peak vs. RMS** for amplitudes and charge densities.
- **Areas** — check that every density in the paper implies the same effective
  area, and that the area matches what the Methods describe.
- **Per-cycle vs. per-second** rates.

Recompute the conversion both ways. If one reported quantity reproduces under one
convention and another reproduces only under a different one, name both — the
author needs to know which figures move when they standardise.

## 11. Cross-references

For every "(Figure X)", "(Table SY)", "(Note SZ)": read the target's caption and
confirm it contains what the sentence claims.

Highest-yield cases:

- A sentence citing a figure for a **number the figure does not contain** — for
  example citing a characteristic curve as the source of a power value.
- Adjacent-figure errors: citing 5F where 5G was meant, S34 where S35 was meant.
  Check whether the same fact is cited correctly elsewhere; if so, that confirms
  the intended target and makes the query easy to answer.
- Off-by-one figure numbers in the SI, where the main text cites correctly and an
  SI note does not (or vice versa).

## 12. Panel lettering

Read each multi-panel legend as a sequence. Check for repeated letters, gaps, and
letters cited in the text that the legend never defines. A legend running
(A)–(H) then repeating (D) and (E) means every text citation above (H) points at
nothing.

## 13. Methods coherence

Check that the described method can actually produce the reported measurement:

- Does the named detector or instrument respond to the named analyte?
- Does the quoted instrument model match the named configuration?
- Are stated sample volumes, durations and rates mutually consistent?
- Do stated component ratings meet the stated operating conditions?

Incidental details are often the tell. A carrier gas, a temperature, a
concentration chosen for one technique but reported alongside another suggests
the *label* is wrong rather than the experiment — which is the more useful and
more answerable query.

## 14. Component and instrument specifications

Where the paper names specific parts and lists their capabilities, check the
reported operating points against those capabilities. A stated output range wider
than the listed part can deliver means either the part list or the range is
wrong, or an undisclosed additional stage was used.

This class of finding often reveals something substantive about the
architecture — worth raising carefully, because the answer may change how the
work is described rather than just fixing a number.

## 15. The rebuttal as a source

The response to reviewers states what the authors changed. Check that promised
changes are present, and that numbers quoted in the rebuttal match the revised
manuscript. Divergence here usually means a revision was applied in one place and
not another.

---

## 16. Replicate counts and derived replicates

A legend saying "n = 3 independent experiments" is a checkable claim about the
workbook. `scripts/scan_workbook.py` runs both halves of this, but the check needs no
script — see step 5 of `SKILL.md` for the four lines that do it.

**Count the group.** Blocks of two under a legend claiming three are a finding on
their own. Scan for short runs rather than eyeballing — they hide well when the
neighbouring groups are the right length.

**Read the formulas, not just the values.** `data_only=True` returns cached
results and discards every formula, so a derived cell is indistinguishable from a
measurement. Load the book twice and classify what turns up:

- *Expected* — means, SDs, ratios, percentages, normalisation of a raw column.
- *Reportable* — a formula in a cell the figure plots as an individual replicate.

The high-signal shape is a replicate defined as a constant minus the others
(`=3-C70-D70`, `=2-D5`). It pins the group sum to the constant and the mean to
exactly 1, and it leaves n-1 free values — so a "triplicate" carries two
measurements and its error bar summarises two numbers. Note how widely the shape
is used: seven cells among a hundred otherwise-static control groups is a
different fact from a sheet-wide convention, and the difference is worth stating.

Do not read intent off a formula, and do not lean on the group summing to a round
number — mean-normalisation makes every normalised triplet sum to 3 by
construction, so sums alone prove nothing. The formula is the evidence. The
finding is that the effective n is below the stated n and the raw values are
absent; the ask is for the raw measurements.

**Then screen the blocks** for identical values repeated within a group, SDs of
zero next to non-zero neighbours, columns correlating at r = 1.000, and series
stepping by exact integers while parallel series do not. Each is a pointer, not a
finding — see "Screens that cannot carry a finding on their own" in `SKILL.md`.
If a pointer does not resolve into something demonstrable it belongs in "checked
but not raised", if anywhere.
