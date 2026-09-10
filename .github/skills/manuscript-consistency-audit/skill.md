---
name: manuscript-consistency-audit
description: "Audit a manuscript package (main text, supplementary information, source data workbook, rebuttal) for internal inconsistencies — headline metrics that disagree between abstract, results, discussion, SI notes, tables and source data; arithmetic that does not reproduce; figure/table/note cross-references pointing at the wrong object; mislabelled panels and source-data columns. Produces an evidence-backed findings report for the editor plus ready-to-send author queries that point at the location without handing over the diagnosis. Use whenever someone supplies manuscript files and asks to compare them, cross-check reported values, verify numbers against the data, hunt for discrepancies or misreferences, or draft author queries — including \"is anything inconsistent here\", \"do the numbers add up\", \"check the SI against the main text\", or any pre-acceptance or post-review data check. Covers whether the paper contradicts itself, not journal house style."
---

# Manuscript consistency audit

You are checking whether a paper contradicts **itself**. Not whether the science
is right, not whether it meets house style, not whether the claims are novel —
only whether the numbers, cross-references and labels in the supplied files agree
with each other.

This matters most at the stage where it is usually requested: a manuscript that
has cleared peer review and is close to acceptance. At that point the editor is
the last reader who will systematically compare the abstract against Table S5
against the source data. Nobody downstream will.

## Search wide, report narrow

These are two different decisions and conflating them is the main way this audit
goes wrong.

**Searching** should be exhaustive and curious. Open every sheet. Recompute every
derived number, including the ones inside the spreadsheet. Follow anomalies
wherever they lead, including into places the sweep list does not name. The sweep
below is a floor, not a ceiling — the best findings are often one step past where
you expected to stop, and a manuscript's most damaging error is frequently in a
passage nobody thought to verify because it looked like boilerplate.

**Reporting** is where the bar below applies. Suppress a candidate because you
could not demonstrate it — never because you did not look.

If you find yourself deciding not to check something on the grounds that it
probably will not turn anything up, that is the wrong instinct. Check it, then
decide whether what you found clears the bar.

## The certainty bar

**Report only what you can demonstrate from the supplied files.** Every query you
raise costs the author a round-trip and spends the editor's credibility. On a
paper that is otherwise ready, a query that turns out to be your own
misunderstanding is worse than a small thing missed — it delays a finished paper
and teaches the author to discount the whole list.

So the test for every candidate finding is:

> Does the contradiction fall out of two supplied documents, or out of
> arithmetic, with no interpretation needed?

If you have to argue for it, drop it. Specifically, **do not report**:

- **Rounding-level gaps.** Two routes to the same quantity differing by ~1% are
  rounding of intermediate values, not errors.
- **Framing and emphasis.** The abstract leading with a different data point than
  the results section is an editorial choice. "Nearly an order of magnitude" for
  a 7× improvement is rhetoric, not an inconsistency.
- **Methodology opinions.** Whether a normalisation is the fairest one, whether a
  comparison is apples-to-apples — these are review comments, not consistency
  findings.
- **Anything with an innocent explanation you cannot rule out.** See the traps
  below.

Being right about ten things beats being right about eight and wrong about two.
Say so plainly when you cut something you had considered — the user needs to know
the bar was applied, and may want to overrule you.

### Screens that cannot carry a finding on their own

Distributional screens — Benford, terminal-digit uniformity, variance homogeneity,
inter-column correlation — are search tools, not findings. Each returns a
probability under an assumed null, and for a small block of normalised replicates
that null is rarely one you can defend. A query saying the digits look wrong is
unanswerable, and it spends credibility you do not get back.

Run them to decide **where to look**. Report only what they lead you to, in the
terms the rest of this file uses: a formula in a replicate cell, an exact
duplicate block, an SD that does not match its own replicates, a series stepping
by whole numbers while its neighbours do not. Those are demonstrable. The screen
that found them is not the finding and does not belong in the query.

Benford in particular is the wrong instrument for most source data. It needs
values spanning several orders of magnitude; viability ratios clustered between
0.2 and 1.5 fail it by construction, and reporting that failure would be an error
of your own.

### Traps that look like findings

Before flagging, ask what would make this *not* an error. Recurring cases:

- **Monotonic quantities at different operating points.** "77.3% at 18 V" and
  "75.4% at 16 V" look contradictory but are consistent if the quantity rises
  with the variable. Check the direction before calling it a conflict.
- **Derived vs. measured values.** For pulsed or non-sinusoidal signals, average
  power is not V×I of the equivalent values. Small gaps between a reported power
  and voltage×current are expected. Large ones (>10%) are worth checking.
- **A figure showing one run, a table reporting a mean.** Normal practice. Only a
  problem if the figure is claimed to show the mean.
- **Comparison tables reporting best-of-each per row.** A row pairing a peak
  current from one condition with a peak power from another may be deliberate.
- **Simulation parameters differing from experimental ones.** A model may
  legitimately use different component values.
- **Independently acquired datasets covering the same point.** Two sweeps that
  cross at one condition may differ by several percent through re-setup alone.

---

## Workflow

### 1. Extract the package

Convert every PDF to markdown and inventory every source-data sheet before
reading anything. Line-numbered manuscripts keep their line numbers through the
conversion, and those are what you cite back to the author.

```bash
uv run --with pymupdf4llm python -c "
import pymupdf4llm, pathlib
for pdf in pathlib.Path('<input_dir>').glob('*.pdf'):
    out = pathlib.Path('<work_dir>')/(pdf.stem + '.md')
    out.write_text(pymupdf4llm.to_markdown(str(pdf), show_progress=False), encoding='utf-8')
    print(pdf.name, '->', out.name)
"
uv run --with openpyxl python -c "
import openpyxl
wb = openpyxl.load_workbook('<workbook.xlsx>', read_only=True)
print(len(wb.sheetnames), 'sheets'); [print(' ', s) for s in wb.sheetnames]
"
```

Read the whole main text and the whole SI. Do not sample. The findings that
matter are almost always a value in one document versus the same value in
another, and you cannot spot that by skimming.

### 2. Build a metric ledger

For every quantitative claim in the paper, record **every place it appears**:
abstract, introduction, results, discussion, figure legends, SI notes, tables,
and the source data. Headline metrics typically appear five or six times.

This sweep — not clever reading — is what finds the real problems. A number that
appears once cannot contradict anything. A number that appears six times has six
chances to have been transcribed wrong, and in practice one of them usually was.

Work through the sweep list under **What to sweep** below as you go.

### 3. Recompute everything derived

Re-derive each computed quantity from the paper's own stated inputs:
efficiencies, percentage improvements, ratios, densities (value ÷ area), means of
tabulated repeats, weighted averages. Check that the reported result reproduces.

When one value in a series fails to reproduce and the others succeed, that is a
strong finding: the shared denominator confirms your method, so the outlier is
the paper's error and not yours.

### 4. Let the source data arbitrate

When prose and a table disagree, the source-data workbook usually settles it.
Small sheets should be read in full; for large traces you want header rows plus
per-column statistics including a **plateau** figure (mean of the final third),
which is what matches a prose claim like "stabilised at 3.6 V".

```bash
uv run --with openpyxl python -c "
import openpyxl, statistics
wb = openpyxl.load_workbook('<workbook.xlsx>', read_only=True, data_only=True)
for name in ['<sheet>', '<sheet>']:
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True))
    print('='*60); print(name, ws.calculate_dimension())
    if len(rows) <= 40:
        [print(r[:12]) for r in rows if any(x is not None for x in r)]
    else:
        [print(r[:12]) for r in rows[:6]]
        for c in range(1, min(12, max(len(r) for r in rows))):
            v = [r[c] for r in rows if len(r) > c and isinstance(r[c], (int, float))]
            if len(v) > 5:
                print(f'  col{c}: n={len(v)} min={min(v):.4g} mean={statistics.mean(v):.4g} '
                      f'max={max(v):.4g} plateau={statistics.mean(v[2*len(v)//3:]):.4g}')
"
```

Three things to check in the workbook itself, since it is rarely proofread:

- **Column and block headers.** Duplicated condition labels ("w/ secondary
  circuit" on both the treatment and the control) make a figure unverifiable.
- **Columns whose contents contradict their headers.** A column headed for one
  variable holding values that clearly belong to another.
- **Mean and standard-deviation columns.** Recompute them from the replicates
  they summarise. These are spreadsheet formulas, and a range that is off by one
  column quietly folds a label or an index value into every row — an error that
  is invisible in the plotted figure but usually propagates into the SI text as a
  claim about the device. Category 9 below has the diagnostic.

### 5. Check that the replicates are replicates

"n = 3 independent experiments" is a claim about the workbook, and the workbook
can contradict it two ways.

**Short groups.** Count the values in each replicate block. Two values under a
legend claiming three is a finding on its own.

**Derived values.** `data_only=True` returns cached results and throws every
formula away, so a cell holding `=3-C70-D70` reads back as a measured `0.939` and
looks like data. Always load the workbook a second time with formulas visible:

```bash
uv run --with openpyxl python -c "
import openpyxl
wb = openpyxl.load_workbook('<workbook.xlsx>', data_only=False)  # formulas, as text
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith('='):
                print(f'{ws.title}!{c.coordinate} = {c.value}')
"
```

A formula in a mean, an SD or a normalisation is expected. A formula in a cell the
figure plots as an individual replicate is not — that value is fixed by its
neighbours. The shape to know is a replicate defined as a constant minus the
others: it pins the group mean to exactly 1, and it leaves a group of three with
two free values, so the plotted error bar summarises two numbers.

Do not lean on the group summing to a round number — mean-normalisation makes
every normalised triplet sum to 3 by construction, so sums alone prove nothing.
The formula is the evidence.

State it as arithmetic, not motive: **the effective n is below the stated n**, and
the raw measurements are not in the file. Ask for them. A real third measurement
answers that in one line; nothing else does.

### 6. Check cross-references against what they point at

For each figure, table and note citation, read the target's actual legend or
caption and confirm it contains what the sentence claims. Misreferences cluster
in late-added text and in sentences that cite a figure for a number the figure
does not contain.

Also verify panel-letter sequences in legends run without repeats or gaps, and
that every panel the text cites actually exists in the legend.

### 7. Verify before reporting

Take each candidate finding and try to break it. Re-derive the arithmetic.
Re-read the cited passage in full rather than from your notes. Confirm the two
quoted passages really do refer to the same quantity under the same conditions.

Findings that do not survive this pass get dropped — and if you already told the
user about one, say plainly that you are withdrawing it and why. This step exists
because a first pass reliably produces one or two confident-sounding items that
dissolve on re-derivation.

### 8. Write the two deliverables

See **Output format** below.

---

## What to sweep

Sixteen categories, each a class of error that recurs across manuscripts.

**1. Headline metrics across documents.** The paper's two or three signature
numbers appear in the abstract, the introduction's closing paragraph, the
results, the discussion, at least one SI note, and a comparison table. Collect
all instances and diff them. Watch for a single digit changing — `9.71` becoming
`9.77` in one location. Confirm each instance carries the same **conditions**:
same voltage, frequency, device, units.

**2. Series and list ordering.** "At A, B, C and D, X increased from p, q, r, s
to w, x, y, z" is unusually error-prone — three parallel lists held in register.
Check each list wherever else it appears. A reversed list produces values that
are individually correct and collectively wrong. Also ask whether the series
behaves monotonically in the direction the paper's own argument requires.

**3. Prose against source data.** For every measurement quoted in prose that has
a sheet, confirm the sheet reproduces it. The strongest version: **two of three
quoted values match exactly and the third does not.** The exact matches confirm
you have the right sheet and the right statistic.

**4. Derived quantities.** Re-derive efficiencies, percentage improvements,
ratios, densities (and check the implied area is consistent across every density
in the paper), means and SDs of tabulated repeats, weighted averages. When a set
shares one input, recompute all of them. For weighted averages, check *which*
weights were used.

**5. Paired quantities and transpositions.** Where a sentence reports two
percentages side by side, compute both. Transposition is common and invisible
without arithmetic, because both numbers are correct.

**6. Tables against their own source data.** Compare comparison tables row by
row. Look for duplicated value pairs — two references carrying identical values
to four decimal places usually means a copy-paste that overwrote real data. Also
check the table's own summary claim against the values it lists.

**7. Legends against text against data.** Legend, discussing text and source data
should agree on operating conditions. Any two disagreeing is a finding; report
all three so the author can see which is the outlier. Legends are the weakest of
the three — written last, edited least.

**8. Source-data workbook hygiene.** Duplicated condition headers; headers
contradicting contents; sheet names not matching the figures they support;
missing sheets for figures presenting quantitative data; empty placeholder
sheets for figures whose legend promises source data; values pasted into the
wrong column type, recognisable because their magnitude belongs to another
quantity.

**9. Summary statistics computed inside the workbook.** Where a sheet holds
replicates alongside a mean and SD, recompute them. High-yield: the error is
invisible in the plotted figure and usually propagates into the SI prose. The
diagnostic is precise — if the stated mean does not match, try including the
adjacent column (a label, an index, a condition value). Apply the same test to
any column that claims to be a ratio or percentage of two other columns in the
same sheet: recompute it row by row, and note whether the discrepancy is
constant across rows or varies.

**10. Units and conversion conventions.** Check one convention is used
throughout: molar gas volume (22.4 vs 24.79 L/mol); peak vs peak-to-peak vs RMS;
areas implied by every density; per-cycle vs per-second. Recompute both ways and
name both conventions if different quantities need different ones.

**11. Cross-references.** For every "(Figure X)", "(Table SY)", "(Note SZ)":
read the target's caption and confirm it contains what the sentence claims.
Highest-yield: a sentence citing a figure for a **number the figure does not
contain**; adjacent-figure errors (5F for 5G, S34 for S35); off-by-one SI
numbering where the main text cites correctly and an SI note does not.

**12. Panel lettering.** Read each multi-panel legend as a sequence. Repeated
letters, gaps, and letters cited in the text the legend never defines. A legend
running (A)–(H) then repeating (D) and (E) means every text citation above (H)
points at nothing.

**13. Methods coherence.** Can the described method produce the reported
measurement? Does the named detector respond to the named analyte? Does the
instrument model match the named configuration? Are volumes, durations and rates
mutually consistent? Incidental details are often the tell — a carrier gas or
temperature chosen for one technique but reported alongside another suggests the
*label* is wrong rather than the experiment.

**14. Component and instrument specifications.** Check reported operating points
against the listed capabilities of named parts. A stated range wider than the
part can deliver means either the part list or the range is wrong.

**15. The rebuttal as a source.** Check that promised changes are present and
that numbers quoted in the rebuttal match the revised manuscript. Divergence
usually means a revision was applied in one place and not another.

**16. Replicate counts and derived replicates.** Count the values in each
replicate block against the legend's stated n. Then read the formulas, not just
the values: a cell the figure plots as an individual replicate but computed from
its neighbours (`=3-C70-D70`) leaves the group n-1 free values and pins its mean,
so a "triplicate" carries two measurements. Note how widely the shape is used —
seven cells among a hundred otherwise-static control groups is a different fact
from a sheet-wide convention. Screen the blocks too, for identical values within
a group, SDs of zero beside non-zero neighbours, columns correlating at r = 1.000,
and series stepping by exact integers while parallel series do not — but those are
pointers, not findings.

---

## Output format

Two deliverables, in this order. They are written for different readers and the
asymmetry between them is deliberate: **the editor gets the whole derivation, the
author gets a pointer.**

### Part 1 — Findings report (for the editor)

The editor reads this to decide what to send. It must let them verify each item
without reopening the files, and it must make the reasoning visible so they can
disagree.

Order by strength: items where two supplied documents contradict each other, or
where arithmetic fails, come first. Group into short sections if there are more
than about eight findings.

Each finding follows this shape:

> **N. One-line statement of the problem — location**
>
> > "exact quoted text"
>
> What it conflicts with, quoted or tabulated. The arithmetic, shown.
>
> A sentence on how it was identified, when that is not obvious.
>
> The question to put to the author.

Worked example:

> **4. One efficiency doesn't follow from its own stated power — main text lines 337–340**
>
> > "the output powers rose from 18.76 mW, 14.71 mW, and 10.05 mW to 22.67 mW, 22.90 mW, and 20.15 mW... Consequently, the overall circuit efficiencies improved from 68.0%, 53.3%, and 38.5% to 82.1%, 83.0%, and 73.0%"
>
> Against the stated 27.59 mW input (line 331), five of the six reproduce: 68.0%, 53.3%, 82.1%, 83.0%, 73.0%. The sixth does not — **10.05/27.59 = 36.4%, not 38.5%**.

Note what makes that convincing: the five that reproduce establish the method, so
the reader does not have to trust the arithmetic on faith.

Use a small table when comparing more than two values of the same quantity:

| | 1.8 V | 3.6 V | 5.0 V |
|---|---|---|---|
| `Figure 3J` source data | 82.42% | 92.31% | 92.31% |
| Table S4 | 83.0% | 94.9% | 93.6% |

#### Closing section: checked but not raised

A short list of candidates that did not clear the bar, one line each with the
reason. Keep it brief — this is a confidence signal, not a second report.

If you raised something earlier in the conversation and are now withdrawing it,
say so explicitly and give the reason. Do not quietly drop it; the user may
already have acted on it.

### Part 2 — Author queries (ready to send)

These go into a letter or a Word document, often verbatim.

#### Locate, don't diagnose

This is the governing principle and the one most easily got wrong.

A query's job is to send the author back to a specific place to **re-examine
their own work**. It is not to hand them a correction to paste in. An author told
"8.61 should be 8.16" changes one cell and moves on. An author told "the
film-free insertion loss in Supplementary Table 2 may not be consistent with its
source data" goes back to the measurement, works out why it is wrong, and checks
whether the same slip affected anything else. The second is the check the journal
actually wants, and only the second will catch a systematic error whose full
extent you could not see.

So each query names **where** and **which quantities**, states that an
inconsistency *appears* to exist between named locations, and asks for a check.
It does not supply:

- your recomputed value, or any arithmetic
- which of the conflicting values you believe is correct
- the mechanism you diagnosed — transposition, wrong denominator, off-by-one
  formula range, mislabelled column

Include a specific value only when it is needed to identify *which* instance you
mean, not as evidence.

Compare, for the same finding:

> ✗ *Please double check the insertion loss of the film-free device in
> Supplementary Table 2. It gives 8.61 dB, but the source data for Supplementary
> Fig. 3 gives −8.16 dB at that frequency, so it appears 8.61 may be a
> transposition of 8.16.*

> ✓ *Please double-check the centre frequency and insertion loss values for the
> film-free device given in Supplementary Table 2 and in the Supplementary Note
> III text, against the source data for Supplementary Fig. 3.*

And:

> ✗ *The reported Ip-p/Iset values do not equal the sheet's own Ip-p divided by
> its own Iset; every row is high by the same factor of 1.044, which suggests the
> ratios were computed against a set current about 4.2% lower than the one
> tabulated.*

> ✓ *Please double-check the three columns of the source data sheet for Fig. 4b
> (Iset, Ip-p, and Ip-p/Iset) and confirm that they are mutually consistent for
> all five input powers, and that the ratio plotted in Fig. 4b was computed from
> the set-current values tabulated in the same sheet.*

The second version of each is shorter, which is a useful check in itself: if a
query is long, you are probably explaining rather than pointing.

#### When to give more

Withholding the diagnosis is not the same as being vague. Three cases warrant
more:

- **The search would otherwise be too wide.** Narrow it by saying what *does*
  reconcile, without saying what is wrong: "the entries for the device with the
  film appear reproducible from the source data; those for the device without the
  film may need re-checking." That halves their search without naming the error.
- **The query is not actionable without the reasoning.** "Please check the
  detector" is unanswerable; the author needs to see that an FID does not respond
  to H₂ and that the quoted model number is a GC-MSD configuration. Give the
  reasoning when the author cannot act without it, and cut it when they can.
- **Nothing is there to be worked out.** Typos, verbatim duplicated sentences,
  empty source-data sheets, missing datasets. State these plainly and directly —
  applying the principle here just wastes a round-trip.

#### Voice

Enquiring, not accusatory. The author may have an answer; the query asks for a
check, not a correction. Standard openings: "Can you please double-check...",
"Please check...", "Please confirm...", "It appears that there may be...".

Prefer "may not be consistent", "appears there might be an inconsistency",
"please confirm these are consistent" over "does not match" or "is incorrect".

Where a plausible innocent explanation exists, offer it as the thing to confirm
rather than as a hedge — "if the two sets of measurements were made on
differently prepared samples, could this please be stated explicitly" both tells
them what would resolve it and leaves the finding standing if it does not apply.

#### Formatting: one unbroken paragraph per bullet

These get pasted into Word. A hard line break inside a bullet becomes a broken
line in the document, and indented sub-items under a parent bullet break worst of
all.

- Each bullet is a single continuous paragraph. No internal line breaks, however
  long it runs.
- No nested or indented sub-items. If one query covers several instances,
  promote each to its own top-level bullet, with a lead-in bullet above them.
- Where a second query follows from the first, open it with "Related to the
  above," rather than nesting it.
- Consistent units and range punctuation throughout (pick hyphens or en dashes
  for line ranges and stay with it; render units the same way every time).
- Straight or curly quotes are fine, but be consistent.

#### Worked examples

Conflict across several locations:

> * Can you please double-check the carrier mobility and sheet carrier density values reported for the SiOₓ/InSb/In₀.₆Al₀.₄Sb heterostructure and ensure they are consistent across the package? The relevant places are main text lines 169-171, Fig. 2b and its source data, Supplementary Note I §§3 and 5, Supplementary Table 1, and the source data for Supplementary Fig. 1. It appears there may be an inconsistency between the values quoted for the adopted heterostructure and those obtained for the corresponding composition in the InSb sputtering power series. If the two sets of measurements were made on differently prepared samples, could this please be stated explicitly in Supplementary Note I?

Value quoted in the text with no corresponding measurement:

> * Please check main text lines 249-250, which state that the current accuracy reaches "a local minimum at Iset = 100 nA", against the set-current values actually measured in Fig. 4a and its source data, and confirm the value quoted in the text.

Single quantity, several statements of it:

> * Please double-check the InSb layer dimensions given for the thermal simulation in Supplementary Note V against the layer thicknesses stated in main text line 174, Supplementary Note I §4 and Supplementary Note II, and confirm the thickness used in the simulation.

Arithmetic, with the arithmetic withheld:

> * Please double-check the percentage given in Supplementary Note XIII §3, where a reverse current of approximately 40 pA is expressed as a fraction of the minimum output current of 1.22 nA.

Ambiguous definition:

> * Please clarify how the root-mean-square value of Iout quoted in Supplementary Note XV (approximately 1.8 μA, against approximately 1.5 μA unmodulated) was defined and computed, and confirm that it is consistent with the traces in the source data for Supplementary Fig. 20 and that it holds for all four modulation functions described in that section. If the value applies to only one waveform, or to a particular component of the signal, please state this in the text.

Grouped misreferences — lead-in bullet, then each instance as its own bullet:

> * Please check the following figure citations, which may not point at the intended targets:
> * Main text lines 203-204, "output power also increases (Figure 2J)" — please confirm the panel cited.
> * The Figure 5F legend, "equivalent currents… (Figure S34)" — please confirm the supplementary figure cited.

Methods query where the reasoning must travel with it:

> * Please confirm the detector used for the hydrogen GC measurement in the Methods (lines 510-511). The text states "GC-FID (Agilent 7890B-5977A)", but an FID does not respond to H₂, and the model number given corresponds to a GC-MSD configuration. The argon carrier gas would be consistent with a TCD measurement. Please revise the detector designation to match the instrument actually used.

Direct, because nothing is there to work out:

> * Please correct the following in the main text: line 277 reads "Table 1 summarizes t1he electrical characteristics"; line 372 reads "we developed an modified IDT architecture"; and the sentence beginning "The active region of the current source…" appears verbatim at both lines 488-490 and lines 514-516.

---

## After delivery

Expect follow-ups of three kinds, and handle each without re-litigating the
audit:

- **"Explain finding N"** — the user does not understand what to check. Walk
  through what the text says, why it is a problem, and how it was identified,
  then re-draft that single query.
- **"Reformat these"** — usually a Word paste problem. Re-emit as
  single-paragraph bullets, and mention any typos or inconsistencies you silently
  fixed on the way through so the user is not surprised by a changed word.
- **"Make these more/less direct"** — adjust Part 2 only; Part 1 keeps the full
  derivation regardless. If asked to be more direct, add back the recomputed
  value and the diagnosis. If asked to be less direct, strip to location and
  quantity, and say which bullets you deliberately left explicit and why.

## Scope note

If the user also wants journal-compliance checking (declarations, section order,
title length, data availability wording), that is a different job — say so and
point at the relevant formatting skill rather than mixing the two lists. A
consistency audit that drifts into house style buries the findings that matter.

