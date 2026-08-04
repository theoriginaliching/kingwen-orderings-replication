# Errata and corrections

Corrections to *Statistical Structure of the Historical Orderings of the I Ching
Hexagrams: Pair Rule, Family Gradient, and the Limits of Demonstrability*
(Zenodo, concept DOI 10.5281/zenodo.21609653, which always resolves to the newest
version; the version this record accompanies is version 3, DOI 10.5281/zenodo.21776041).

This is a living document. It is updated when a defect is found, not when a defect is
fixed.

**Deposit status.** Version 3 is **PUBLISHED**, deposited on 2026-08-03, version DOI
`10.5281/zenodo.21776041`, archive `kingwen-orderings-replication-main.zip`, 244557 bytes, sha256
`0069259effc1290d4fc2c598ea8bf88dc0e1c1b76fa2523d0521f2c016c48aa5`,
tagged `zenodo-v3` on commit `d6afae20bbefba56728251f34f8e3870c43e2cbd`. It was
verified after publication by downloading the archive from the record itself, hashing it
to that value, extracting it into an empty directory and running the suite there: 270
checks, 0 failures. **Nothing below is waiting for a deposit.**

**Where it stands, 2026-08-03, after the third deposit.** Twenty-five entries: four
defects in the paper (E-1 to E-4), four in the deposited package (P-1 to P-4), three
clarifications for the next version (C-1 to C-3), and fourteen things examined and found
sound (X-1 to X-14). **All eight defects are now APPLIED**: every one of them is corrected in the
object deposited as version 3, and each says where. They keep describing the defect as
versions 1 and 2 print it, because that is what a reader holding those versions has in
front of them. **No figure of the paper changes in any entry**, and that is measured and not
asserted: every figure reproduces in every tree of the package: 192 of 192 in the first
deposit, 202 of 202 in the second, 246 of 246 on the `main` this branch merged, and 270 of
270 in the third deposit, verified after publication by downloading it from the record.
None of the entries themselves was rewritten. The defects in the paper are defects of description whose
consequences all hold, and one missing assertion; the defects in the package are
statements it makes about itself.

**What a corrected version does with these entries.** It corrects the text and it keeps
the record. Both halves are needed and neither replaces the other: without correcting the
text, a new version goes on saying what is known to be false; without the record, a reader
cannot find out what the version they hold actually said. So the entries below are **not**
rewritten when a correction is made. Each goes on describing the defect as it stands in the
deposits, where it exists and cannot be taken out, and a separate line names where it was
corrected. A reader holding any version can therefore tell which of the two they are
looking at.

**One rule was inverted to make these corrections, and it is recorded rather than
smoothed over.** The standing rule of this project is that a change to the text is born in
the laboratory repository, where `paper.tex` is canonical, and is mirrored into this
package; never the other way round. The two corrections above were born here, in the
package, because they came out of the errata work and the errata work lives here. The
result is that for a time the mirror ran backwards.

The state can be made consistent again by applying the same change to the canonical copy,
and it must be, before this branch reaches `main`. But leaving it consistent without saying
that the direction was reversed once would hide the one thing a later reader would want to
know: that the two files diverged, and in which direction. **What would have prevented it
is not vigilance but sequence.** Step (c) of the plan for version 3 said the changes start
in the laboratory and are mirrored here, and then the work was done in the order the errata
made convenient rather than in the order the plan prescribed. The plan itself did not say
where to begin, only where the canonical copy lives, so it has been corrected to name the
laboratory as the first move of that step. A rule that is not attached to a step is a rule
that gets read after the fact.

**What holds an entry up.** No entry here depends on the follow up paper being correct.
Each states the evidence available in this package, or in printed sources anyone can
consult, and can be checked from those alone. Where an entry names that work, it is
recording **where the discrepancy was found**, which is not the same as what establishes
it: found by, not established by. If the follow up paper vanished tomorrow, every entry
below would stand exactly as it is.

## What this file is

A public record of every defect found in the deposited paper, with the evidence for
each, from the moment it is found. An entry appears here before any corrected version
is deposited, so that a reader who has the paper can find the correction without
waiting for a new deposit.

## What this file is not

It is not a changelog of the deposited versions. It does not assert that the list is
complete. It asserts only that every defect known to the author at the date of the last
entry appears below.

## Policy on deposits

Corrections are recorded here as they are found and deposited in a single batch, not one
at a time. The reason is mechanical rather than editorial: each new deposit carries a new
version DOI, the current version DOI is cited by name in several places, and each round
of updating those places is an occasion to introduce exactly the drift that is being
corrected.

The consequence is declared rather than hidden: between the date an entry appears here
and the date of the next deposit, the deposited paper contains the defect and this file
is the only public record of it.

## Status vocabulary

- **OPEN**: found, evidence recorded, not yet deposited.
- **APPLIED**: corrected in a deposited version. The entry names that version.
- **EXAMINED, NOT AN ERRATUM**: something was checked and found to be correct. These
  entries stay. A record that lists only what it found is a record that has dropped
  what it looked for.
- **NOTED, FOR THE NEXT VERSION**: nothing printed is false, and something could be said
  more precisely. It is not a correction and creates no obligation to deposit; it is a
  note to whoever edits the sentence next.

## Categories

An entry's identifier says which kind of thing it is, because the kinds are not judged
by the same standard. The prefixes are separate series and none continues another.

- **E-**: a defect in the text of the deposited paper. This is what the file was opened
  for.
- **P-**: a defect in the deposited replication package: its README, its landing page,
  its suite, anything shipped in the archive that is not the paper. The paper can be
  correct while the package that carries it is not.
- **C-**: a clarification for the next version. Nothing printed is false.
- **X-**: examined and found not to be an erratum.

The six required fields below govern **E-** and **P-** entries, which are the entries
that assert a defect. **C-** and **X-** entries carry four: what was examined, the
measurement, the date, and the status.

## Required fields

Every entry carries all six. An entry missing one is incomplete and says so. The six are
a floor and not a ceiling: an entry may carry further labelled fields, such as a cross
reference to another record, or an exhibited witness inside its evidence.

The six govern a defect entry. An entry under *Examined and not an erratum* records
something that was checked and found sound; it carries what was checked, the measurement,
the date and the verdict, and has no "what it should say" because nothing should say
anything else.

1. **Printed text**, verbatim, with a pointer to section, page or table.
2. **What it should say.**
3. **Evidence** that the printed text is wrong, with its own pointer.
4. **Date found.**
5. **Figures affected**, with the measurement that establishes the answer. An
   unmeasured "none" is not an answer.
6. **Status.**

## How the quoted text is transcribed

One rule, governing every verbatim in this file, so that it is stated once rather than
argued in each entry.

**Artefacts of composition are normalised, and named beside the quotation that carries
them. Characters of the text are preserved.**

Named beside, not named only here. A policy section is where a reader looks after they
have been surprised, and by then the damage is done: a substitution that appears only in
the policy is a silent substitution at the place it matters, which is the shape of defect
this file catches in others. Every entry that quotes an altered span says which characters
were altered, in that entry, next to that quotation. Measured on this file: four
quotations carry an altered character, and each carries its own note.

The line between the two is not a matter of taste. A compositor decides where a line
breaks, whether `fi` is drawn as one glyph or two, and whether a word is split with a
hyphen at a margin; none of that is in the text, and all of it changes if the page size
changes. The author decides that the possessive of `sequence` carries an apostrophe;
that is in the text, and it survives any re-typesetting. So:

- **Normalised**, and named: line breaks, ligature codepoints, hyphens introduced by a
  break across a line or a page, and the symbol glyphs the compositor draws for operators
  the source writes as plain text or as a macro: U+2212 for a hyphen-minus, U+00D7 for
  `\times`, U+2248 for `\approx`. These are written here as `-`, `x` and `~`, and the
  entry that quotes them says so. The operator is the text; the glyph is the drawing of
  it, and a reader searching a PDF viewer for a quotation is better served by the form
  they can type.
- **Preserved**, exactly: every other character, including U+2019 where the artifact
  composes a typographic apostrophe, and every digit, bracket and mark of punctuation
  the author put there.

There is a practical test behind the rule, and it is the reason the rule is not the
other way round. A reader should be able to take a quotation from this file, search for
it in the deposited PDF, and find it. A quotation carrying U+FB01 in `verification`
fails that test: the string is not findable, because a reader types `fi` and the file
holds one glyph. A quotation carrying U+2019 passes it, because the reader's copy has
U+2019 too.

**Where the quotations still differ from the LaTeX source.** They are taken from the
deposited PDF, because an erratum corrects what the reader has in front of them, and what
the reader has is the compiled artifact. Measured against the deposited `paper.tex`, two
differences remain after the normalisation above, and both are the typesetter's work:

1. **Macros that render as text.** The source writes the reference to Table 2 as
   `Table~\ref{tab:chan}` and the laboratory address as `\url{https://...}`; the PDF
   renders the first as `Table 2` and the second as the bare address. The quotations here
   carry the rendered forms.
2. **Apostrophes.** The source writes an ASCII apostrophe, `sequence's` and `block's`;
   the PDF composes U+2019. The quotations here carry U+2019, because that is the
   character in the artifact and it is a character of the text, not of the composition.

Everything else agrees with the source character for character. The spans quoted in C-1
agree with it exactly once the ligatures are decomposed and the `\url{}` wrapper is
unwrapped, which is what the rule above requires and what C-1 does.

---

# Verification against the printed sources

The two constructed sequences of the paper have been compared, position by position,
against the printed record they claim to reproduce. This is the part of the work that
rests on nothing in this project.

| sequence | source | comparison | result |
|---|---|---|---|
| Jing Fang | Nielsen (2003), Table 2, p. 3, entry BA GONG GUA | 64 of 64 positions | no discrepancy |
| Mawangdui | Shaughnessy (1996), pp. 28-29, printed figures | 11 of 11 | no discrepancy |
| Mawangdui | Shaughnessy (1996), p. 17, the stated rule, reimplemented separately | 64 of 64 positions | no discrepancy |

**What the package did and did not do until now**, measured in all four trees rather than
recalled: `MAWANGDUI` and `JING_FANG` occur fifteen times in `verify_paper.py` and not one
of those occurrences is a comparison against a source; the names `Shaughnessy` and
`Nielsen` occur zero times in it; and the only literal sequence table anywhere in the
package is `KING_WEN`, sixty-four values. The other two sequences are generated from the
construction rules, so there was no list of either to compare against anything. Both were
therefore verified against the rules as implemented, and not against the printed record,
which is the gap these comparisons close.

**A consequence worth having.** Jing Fang agrees in all sixty-four positions, and
`KW_NUMBER` is a bijection, so the comparison also validates `KING_WEN` itself, the single
external datum this package embeds, against Nielsen. The one number nobody could derive is
now the one number checked against a third party.

**What is independent here, and what is not.** Shaughnessy and Nielsen are printed, third
party and unconnected to this project, and they are the independent element. The audit of
this repository that turned up several of the entries below is **not** independent: it was
run by a separate session of the same process, with the same author, and it appears in
those entries as provenance and nothing more. Claiming otherwise in the very document
where errors are corrected would be the worst possible place to overstate.

The comparisons above were carried out in the course of the follow up work, with the books
in hand. This file records them, with their page pointers, so that a reader can repeat
them; the package does not perform them, and this round does not add a checker that would.

---

# Open entries

`None.` Every defect found so far is corrected in a deposited version and filed under
**Applied** below, each naming the version that applied it. This part is not deleted when
it empties: a record whose open section disappears when it is empty cannot be told apart
from a record that never had one.

---


# Clarifications for the next version

Nothing in this section is false. Each entry records a sentence that is exact as printed
and could be less easy to misread, so that whoever edits it next is not editing blind.

## C-1. "A public repository" does not say which repository

**What was examined.** The number the paper gives for its verification suite, and whether
it describes the replication package the reader downloads with the paper. Page 3 of the
deposited PDF, the paragraph headed `Reproducibility.`, whose first sentence is broken
across the page boundary inside the word `accompanying`:

> Every numerical claim in this paper is asserted by an automated suite of 63
> verification sections in a public repository (exit status zero is a publication gate for
> the accompanying interactive laboratory).

and page 12, third block, in Section 8:

> As a secondary resource, the same material is explored in an extended interactive
> laboratory of 45 experiments at https://experiments.theoriginaliching.com (in Spanish;
> an English version is in progress), whose assertion suite comprises 63 sections executed
> as a publication gate (exit status zero required); computed statistics are frozen as
> assertions once verified, so that no figure can drift silently.

*Physical layer, named as the transcription rule requires.* Three glyphs in these two
spans are the ligature U+FB01, which the typesetter composes for the pair `fi`: one on
page 3, in `verification`, and two on page 12, in `verified` and in `figure`. They are
written above as `fi`, decomposed. The first span is also cut by the page break inside
`accompanying`, printed as `accompany-` at the foot of page 3 and `ing` at the head of
page 4; the hyphen is the break, not the word, and is not reproduced. Line breaks of the
printed column are not reproduced either. No character of the text is altered.

One consequence worth recording, because it costs nothing and settles a question a reader
might otherwise have to ask: with the ligatures decomposed, these two spans agree
character for character with the deposited `paper.tex` as well as with the PDF, once the
source's `\url{...}` wrapper around the laboratory address is unwrapped. Measured, both
spans, against the `paper.tex` of the version 2 archive. Neither sentence contains a
cross reference or an apostrophe, so the other two divergences named in the transcription
rule do not arise here.

The version 1 deposit prints 61 in both places and is otherwise identical.

**Measurement.** The figure is exact, at both deposits, and it is the laboratory's. The
laboratory suite executed 61 sections at the commit current when the version 1 record was
created and 63 at the commit current when the version 2 record was created; it executes 63
today. The identity is enforced rather than observed: the laboratory's own suite reads the
number printed in the manuscript and asserts that it equals the count of sections it
executes, failing its publication gate otherwise. Nothing here is wrong, and nothing needs
correcting in any deposited version.

**What could be said more precisely.** The phrase "a public repository" does not name
which repository, and the reader is holding another one that answers to the same
description: this replication package is a public repository too, and it also runs an
automated suite as a gate. Its suite is a different object of a different size, measured
in both deposits: ten section functions and 192 checks in version 1, eleven and 202 in
version 2. Neither deposit contains 61 or 63 of anything. A reader who takes "a public
repository" to mean the package in their hands will look for 63 of something and find no
such number, with nothing in the sentence to tell them they are looking in the wrong
place. Naming the repository, once, would close that.

**Date examined.** 2026-07-31.

**Status.** NOTED, FOR THE NEXT VERSION.

---

## C-2. An approximation that rounds the wrong way

**What was examined.** The sentence on page 9 of the deposited PDF, in the paragraph on
the battery of nine criteria:

> With nine tests, 0.038 x 9 ~0.35.

*What was altered, named here.* The multiplication sign is U+00D7 in the artifact and
the approximation sign is U+2248; both are the compositor's rendering of the source's
`\times` and `\approx`, and are written above as `x` and `~`. The missing space after
the `~` is not a slip and is not mine: the text layer of the artifact reads `~0.35` with
no space, because the gap LaTeX sets around a relation is drawn and not encoded. An
earlier version of this entry inserted one, and a reader searching the artifact for the
quotation would have failed to find it, by exactly the failure the transcription rule
exists to prevent. No digit is altered.

**Measurement.** The exact product is 0.34199999999999997. Its rounding to two decimal
places is 0.34, not 0.35, and the package's own suite computes exactly that:
`round(0.038 * 9, 2)` returns 0.34, and the corresponding check declares 0.34 as the
paper's value, which is the separate defect recorded in P-2. Nothing in the paper is
false: the sentence is an approximation, its point is that a Bonferroni-corrected value of
this size is nowhere near 0.05, and 0.342 is nowhere near 0.05. Under its intended reading
the claim holds.

What lifts it out of "examined and sound" is not the arithmetic but the disagreement:
0.35 is not the two-place rounding of 0.342, and the manuscript and its own verification
script print different digits for the same quantity. A reader who computes the product
gets a third rendering. One of the three should give way, and the cheapest is the printed
one.

**Corrected in the manuscript for version 3.** The sentence now prints the exact product:

> With nine tests, 0.038 x 9 = 0.342.

**This entry stays a clarification and is not reclassified.** Under its intended reading
the printed sentence was not false: it was an approximation, and its point was that a
corrected value of that size is nowhere near 0.05, which is true of 0.342. What made it
worth a note was never falsity but disagreement, the manuscript and its own verification
script printing different digits for one quantity, and printing the exact value removes the
disagreement at its source rather than papering over it. The good consequence is
mechanical: with an exact figure printed, the check that guards it stops being a tolerance
and becomes an equality. Measured after the change: the suite carries **23** `ok=`
overrides where it carried 24, and the one that went is this one.

**Swept for siblings before closing, because one case and a class need different repairs.**
Every printed approximation in the manuscript was checked against the value it
approximates. There are three. The standard deviation of the inversion count prints 86.3
against an exact 86.30179604156567, which is its correct rounding to one place. The
probability of a monotone arrangement prints 0.042 against an exact 0.041666..., which is
its correct rounding to three. The battery correction printed 0.35 against an exact 0.342,
which is the rounding of nothing: not to two places, where it is 0.34, and not to three,
where it is 0.342. **One of three, so a case and not a class**, and the repair is the case.

**Date examined.** 2026-08-03.

**Status.** NOTED, FOR THE NEXT VERSION. The clarification is applied in the manuscript of
version 3, deposited 2026-08-03, and the entry stays here describing what versions 1 and 2
print.

---

## C-3. Three floats the prose never points at, one of them Table 1

**What was examined.** Whether every table and figure of the paper is reached from the
text. Measured on the final `paper.tex`: 15 labels and 35 references, and **three labels
that nothing references**.

| label | line | what it is |
|---|---|---|
| `tab:orders` | 98 | **Table 1**, the five orderings against the binary order: the table of the paper's first result |
| `tab:fingerprints` | 248 | Table 5, the spectral fingerprints of the five orderings |
| `fig:fingerprints` | 285 | the figure of the same spectral portraits |

**Measurement.** They are not reached another way either. The literal strings `Table 1`,
`Table 5` and `Figure 1` appear nowhere in the prose, and no deictic phrase stands in for
them: no `the table below`, no `the figure above`, none of that family anywhere in the
manuscript. The floats are placed by LaTeX where it finds room, and nothing in the sentences
sends a reader to them. **A reader of Section 3 is never told that the table of results is a
table, or where it is.**

**Where a pointer would go, proposed and not written.** For `tab:orders`, the sentence of
Section 3 that states the three inversion counts, which is the sentence the table tabulates;
for `tab:fingerprints` and `fig:fingerprints`, the paragraph of Section 6 that describes the
Walsh energies, which is what both display. **This is new prose in the manuscript and it is
the author's to write**, so nothing was changed: this entry records the gap and the
proposal, and the manuscript is untouched.

**Written in the manuscript for version 3.** The author decided the three pointers and
they are in the text, each with `\ref` rather than a literal number, each the shortest
sentence that carries a reader to the float, and none of them asserting anything the paper
did not already assert:

| float | where it went | the sentence, verbatim |
|---|---|---|
| `tab:orders` | end of Result 3.1, the sentence that states the three inversion counts | `Table~\ref{tab:orders} collects these counts.` |
| `tab:fingerprints` | end of Result 6.1, the sentence that describes the three columns | `These are the columns of Table~\ref{tab:fingerprints}.` |
| `fig:fingerprints` | the same place | `Figure~\ref{fig:fingerprints} plots the Walsh energies.` |

Measured after the change: 15 labels, 38 references, **zero orphans**, zero unresolved
references. The three names were then removed from `ORPHAN_FLOATS_DECLARED` in
`verify_paper.py`, so the check that bounded the gap now permits none at all.

**Date examined.** 2026-08-03.

**Status.** NOTED, FOR THE NEXT VERSION. The three pointers are written in the manuscript of
version 3, deposited 2026-08-03, and the entry stays here describing what versions 1 and 2
print.

---

# Examined and not an erratum

Everything below was measured on 2026-07-31 inside the two deposited archives themselves,
extracted from their zip files, not in a working copy.

## X-1. The file table of the package README does not claim to be an inventory

**What was examined.** Whether the table of files in `README.md` is a complete list of
what the deposit ships.

**Measurement.** The table declares six files, identically in both deposits:
`verify_paper.py`, `paper.tex`, `paper.pdf`, `index.html`, `LICENSE`, `LICENSE-text`. The
version 1 archive carries nine files and the version 2 archive eleven. Undeclared in
both: `README.md`, `logo-128.webp`, `vercel.json`; undeclared in version 2 additionally:
`robots.txt`, `sitemap.xml`.

**Why this is not an erratum.** Nothing declares completeness. The lines that introduce
the table read, character for character in both deposits:

> This repository is the replication package for the paper. It contains the manuscript
> source, the compiled PDF, and a single self-contained script that reproduces **every
> numerical claim** made in the paper from first principles.

and the table's own header is `| File | What it is |`. A description of what a package
contains is not a manifest of everything in it, and a header naming a column "File" does
not promise to enumerate all of them. A claim that was never made cannot be false.

**Observation kept with it.** The repository does two jobs and the README described one.
It is the replication package, and it is also the source of the deployed landing site;
the undeclared files were, with one exception, the second job's: `vercel.json`,
`robots.txt`, `sitemap.xml` and `logo-128.webp` serve the site, and `README.md` is the
file doing the describing. The shortfall was not drift in the table. It was a second
office the table was never written for. This holds for the version 1 archive too, which
is short by three: it was not clean here and later spoiled.

**What was changed, and why it is not a correction of this entry.** The table in the
package README has since been rewritten, on branch `errata`, as a complete inventory:
every file, grouped under three declared roles, replication path, deployed site, record
and evidence. The reason is not that files were missing. It is that a selection without a
written criterion cannot be checked by anyone, so no reader could tell an omission from a
choice, and neither could the author. With the roles declared, the list can be compared
against the archive by a stranger, and a file that fits no role is a question rather than
a detail nobody notices. The earlier table was not false and this is not an erratum
against it; the new one is merely checkable, which the old one was not.

**It was unwatched, and now it is watched.** When this entry was first written the
inventory was checkable and unchecked: nothing in `verify_paper.py` enumerated the
directory, so nothing would have noticed a file added to the archive and left out of the
table, or a row naming a file that is gone. That is no longer true. `section_errata`
checks it in both directions and names the file that broke it, and the property was proved
by mutation rather than assumed: a file added to a throwaway copy of the package is
reported by name. The earlier state is left written here rather than edited away, because
an inventory believed to be verified and in fact unverified is the more dangerous of the
two, and the record should show which one it was and when it changed.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-2. The section-to-verification map holds what it declares

**What was examined.** The map in `README.md`, introduced by:

> Every claim in the paper maps to a named check in `verify_paper.py`.

**Measurement.** Taken in the two deposited archives, which are what this entry is about.
Ten section functions are named by the map there. In the version 1 deposit ten section
functions exist, and every one is referenced. In the version 2 deposit eleven
exist, the same ten are referenced, and no row anywhere points at a target that does not
exist. The declaration therefore holds in both: every claim of the paper that the map
lists resolves to a section that is really there.

**The distinction, which is the point of the entry.** What lapsed in version 2 is a
different property: the map being, incidentally, a complete inventory of the suite's
sections. In version 1 it was one, by the coincidence of ten rows and ten sections.
Nobody ever declared it. The section without a row, `section_pdf_metadata`, asserts
properties of the compiled artifact, the document information dictionary of the PDF
against the canonical strings of `paper.tex`, which are not claims of the paper and so
fall outside what the map declares itself to cover.

**On this branch the map has moved on.** It now carries a row for `section_errata`, added
with the check itself, so eleven of the twelve section functions at the head of this
branch are named and `section_pdf_metadata` is still the one that is not. That changes
nothing above: the deposits are what they are, and this entry measures them.

**Cost, measured rather than characterised.** A reader who used the map as an index of
the suite would miss 7 of 202 checks in the version 2 deposit. That is the whole of the
exposure, and it is recorded because the difference between a map that was audited and a
map nobody looked at is exactly what this section exists to preserve.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-3. The single DOI constant in the version 2 archive states nothing false

**What was examined.** How the deposited suite names the archive identifier. In the
version 2 archive, `verify_paper.py` line 1160 reads:

> `doi = "10.5281/zenodo.21609654"`

one constant serving three assertions, with no separation between a version identifier
and a concept identifier.

**Measurement.** The claim the package actually makes about that string is that the
archive DOI appears in the manuscript, in both READMEs and in the BibTeX. Measured in
that tree, it does: `paper.tex`, `README.md`, `index.html` and `verify_paper.py` all
carry `10.5281/zenodo.21609654` and no other Zenodo identifier. The statement is true of
the tree that makes it.

**It is declared, and here is the declaration.** The record itself says so. The version 2
deposit carries version notes, held as an additional description of the record rather
than in its notes field, which read in part:

> Version 2 (2026-07-27): this version adds the preprint PDF as a separate file, so that
> the full text can be read directly from this record, and updates the replication
> package with a rebuilt PDF that now carries document metadata (title, author, subject
> and keywords). The text of the paper is unchanged between versions: no result, figure,
> table or reference has been modified.
>
> Note: the DOI printed inside the PDF (10.5281/zenodo.21609654) is the DOI of version 1
> of this record; the concept DOI 10.5281/zenodo.21609653 always resolves to the latest
> version.

Harvested from `https://zenodo.org/api/records/21628654`, requested with
`Accept: application/vnd.inveniordm.v1+json`, at 2026-08-01T00:17:09Z. The pointer is
given with the media type because it matters: the same URL requested in the legacy
representation, at 2026-07-31T21:10:59Z, returns a record with no notes field and no
additional descriptions, and an earlier pass of this audit concluded from it that no
version notes existed. They did. The conclusion was wrong because the question was put to
a representation that cannot carry the answer.

So the reader is not left to discover the discrepancy: the deposit states, in its own
record, which DOI the PDF prints and why, and which DOI resolves to the latest version.

**Why this is not an erratum.** The identifier printed is the version DOI of the first
deposit, carried by a package deposited as the second, and declared as such. That is a
state prior to a policy, not a false assertion: the split, in which the manuscript keeps
its version DOI while the living surfaces carry the concept DOI, arrives in commit
`9b4720999e63c5a0ba944ad261b5d6e2aac47031`, whose committer timestamp is
2026-07-27T16:52:01Z. The version 2 record was created at 2026-07-27T16:16:56Z. The
policy is 35 minutes younger than the deposit it would have changed. A deposit cannot be
faulted for not implementing a distinction that did not yet exist.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-4. What the measurement confirmed and did not correct

**What was examined.** Everything swept in the two deposited archives that came out
sound. Kept because a record that lists only what it caught cannot be told apart from a
record that looked for little.

**Measurement.** Six results, each taken inside the archives themselves.

1. **The version 1 deposit is consistent in everything measurable.** Its four declared
   check counts (`README.md` lines 35 and 115, `index.html` lines 179 and 197) all read
   192 and the tree measures 192; runtime 18.4 s against a declared "under thirty
   seconds"; exit status 0 clean and 1 under each mutation, as declared; standard library
   only, as declared, with no network module imported; the seeds and sample count of
   Appendix A, 20000 samples and seed 20260722, matching the constants
   `LADDER_SAMPLES` and `SEED_LADDER`; the robustness seeds `(7, 99)` matching
   `ROBUSTNESS_SEEDS`.
2. **The map has no dangling target in either deposit.** Ten referenced, ten resolved in
   version 1; ten referenced, ten resolved in version 2. No row points at a section that
   does not exist, in either archive.
3. **The laboratory figure printed in the paper is exact at both deposit instants.** The
   suite of the laboratory repository executed 61 sections at the commit current when the
   version 1 record was created and 63 at the commit current when the version 2 record was
   created; the paper printed 61 and 63 respectively. It is 63 today. The identity is not
   a coincidence being reported after the fact: the laboratory's own suite asserts that
   the number printed in the paper equals the number of sections it executes, and fails
   the publication gate otherwise.
4. **The breaking demonstration reproduces exactly in version 1.** Running the three
   mutations documented in its README against its own tree: mutation (a) fails 12 of the
   first 43 checks and aborts with `KeyError: 63`; mutation (b) fails 12 of the first 43
   and aborts with `KeyError: 0`; mutation (c) completes and reports `175 checks passed,
   17 failed, 192 total`; exit status 1 in all three. Every figure in that table is the
   figure the package produces.
5. **The version notes of the second deposit agree with the measurement**, which is worth
   stating because a declaration that nobody checks is a declaration that has not been
   tested. They say the text of the paper is unchanged between versions and that no
   result, figure, table or reference has been modified. Measured on the text layers of
   the two deposited PDFs: Appendix A is identical, 2901 bytes with the same sha256; and
   across all fifteen pages exactly two characters differ, both of them the same one, the
   `1` of `61` becoming the `3` of `63` on page 3 and on page 12. That is the laboratory's
   section count and nothing else. No result, no figure, no table, no reference.
6. **None of the ten checks added in the second deposit asserts a figure of the paper.**
   Named, from the run: three in the front matter section, that the title page and the
   author line are built from the canonical macros and that the canonical author is read
   from `paper.tex`; and seven in the new PDF metadata section, that `pdftitle` and
   `pdfauthor` are built from the canonical macros, that the PDF carries a document
   information dictionary, that `/Title` and `/Author` exist in it, and that each matches
   `paper.tex`. Every one is about how the document names itself. Not one is about the
   King Wen sequence.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-5. The returning soul is built by a different operation than the one the source states

**What was examined.** The construction of the Jing Fang sequence in `verify_paper.py`,
function `build_palace`, the line that produces the eighth member of each palace, at line
136 of the version 2 deposit:

```python
    returning = (wandering & ~LOWER_MASK & 63) | (pure & LOWER_MASK)
```

The source rule for the returning soul is that the whole lower trigram of the wandering
soul is inverted, which in this representation is `wandering ^ LOWER_MASK`. The code does
something else: it restores the lower trigram of the pure hexagram. Two different
operations, and the question is whether they agree here.

**Measurement.** They agree, in all eight palaces, computed and not argued:

| palace head | pure | wandering | code | source rule | equal |
|---|---|---|---|---|---|
| Qian | 63 | 5 | 61 | 61 | yes |
| Zhen | 36 | 30 | 38 | 38 | yes |
| Kan | 18 | 40 | 16 | 16 | yes |
| Gen | 9 | 51 | 11 | 11 | yes |
| Kun | 0 | 58 | 2 | 2 | yes |
| Xun | 27 | 33 | 25 | 25 | yes |
| Li | 45 | 23 | 47 | 47 | yes |
| Dui | 54 | 12 | 52 | 52 | yes |

Built either way, the 64 positions of the sequence are identical, and both equal the
`JING_FANG` the package ships. The reason is measured too, in the same run: on arrival at
the wandering soul, lines 1, 2 and 3 have already been flipped, so the lower trigram of
the wandering soul is the exact complement of the pure hexagram's lower trigram, in all
eight palaces. Restoring it and inverting it are then the same operation.

**Why this is a note and not a defect.** Nothing printed is wrong and nothing computed is
wrong. What is recorded is a coincidence with a condition attached: the agreement holds
because of the order in which this calendar of generations flips its lines. Change that
calendar, and the two operations part company silently, with no check to notice, since
the suite asserts the sequence and not the rule that generates it. The note exists so that
whoever changes it knows what they are standing on.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-6. The figure that looked orphaned, and the set that was too small

**What was examined.** The number 246, which circulated in the records of the project and
which this file recorded as belonging to no tree of the package. That statement was made
over three trees: the two deposits and the head of this branch.

**Measurement.** The live `main` of this repository, commit
`95437d30f805be447cccabb30ea54ff983741f52`, prints exactly that. Extracted on 2026-08-03
into a clean directory and run there:

```
  246 checks passed, 0 failed, 246 total
```

with exit status 0. The figure had a home the whole time. The tree that produces it was
absent from the set that was examined, because this lane's clone of the repository was two
commits behind the remote and nobody had measured that: local `main` at
`73d9a77cdc59ea1410ae815cbb484dc68eb752d1` with 30 commits, `origin/main` at
`95437d30f805be447cccabb30ea54ff983741f52` with 32, behind by two and ahead by none. The
two commits, both of 2026-07-28, are
`d6669487b51ac141ab779891ab85db2503e08974` and
`95437d30f805be447cccabb30ea54ff983741f52`, and together they add 187 lines to the suite.

**The lesson, which is why this entry is kept.** A statement that something does not
exist is only ever a statement about the set that was looked at, and the set has to be
written down beside the claim. The sentence in this file was scoped honestly, it said "at
any of the three points measured here", and it was still misleading, because a reader
takes "measured here" to mean "measured". The scope was correct and invisible. Every
count in this file now names its trees in a table, and the live `main` is the fourth
column. The same correction was applied to the line pointers of E-1, which name the trees
they index and name the one they do not.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-7. The same lesson arriving twice, from two places that did not know about each other

**What was examined.** Whether the defect recorded in P-1, a package declaring a check
count its own suite does not have, was still only a written rule in this file or had become
something a machine enforces.

**Measurement.** It had become a machine, and not here. The repository's `main` gained
`section_surfaces` and `check_published_counts` in commits
`d6669487b51ac141ab779891ab85db2503e08974` and
`95437d30f805be447cccabb30ea54ff983741f52`, both of 2026-07-28. The second asserts that
every count published on a surface equals the total the suite runs. Measured on the merged
tree of 2026-08-03: with the surfaces still saying 212 and the suite running 256, the run
fails with two checks named `count`, each reporting `reproduced: [212]   paper: [256]`;
with the surfaces swept, 256 of 256 pass. This lane, over the same days and without
knowing of that work, wrote P-1, which records the same defect in the deposited archive,
with the timeline that produced it.

**Why it is kept, and it is the reason rather than the coincidence that matters.** A
written rule and a mechanism are not two ways of saying the same thing. This file already
carried the rule: the count must move together with the surfaces that quote it, in one act.
The rule was written because the rule had been broken, and it was broken again during this
very merge, when the surfaces sat at 212 while the suite ran 256. The difference is what
happened next. A rule that is violated produces a defect that somebody may notice later; a
mechanism that is violated produces a failing run before the commit is made. **A written
rule gets broken and a mechanism does not**, and the merge of this branch could not be left
half done and green precisely because the other side had turned the rule into a gate.

Two independent responses to one defect, arriving from two directions in the same week: a
record of it here, a gate against it there. Neither is redundant. The record explains what
went wrong in an archive that cannot be changed; the gate stops it happening again in one
that can.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.


---

## X-8. Every correction this log claims to have applied, checked where it points

**What was examined.** Two decisions of this phase were agreed in a message and never
reached the file: the exact product of C-2 and the citation of E-4. Both were caught by a
person reading, not by a mechanism, which is a poor way to find things. So rather than
assert that there are no others, the question was measured: does every correction this log
declares applied actually exist in the place it names?

**Measurement.** Three sweeps, on the tree at the head of `errata`.

*The content decisions of this phase, against the final `paper.tex`, seventeen of them:*
the two Shaughnessy pointers, the Nielsen pointer, the source-verification sentence and its
count of 64 of 64, the independence caution, `0.038 x 9 = 0.342`, the concept DOI, the
version DOI, the corrected ladder wording, the corrected P4 wording, the bibliography entry
for the companion preprint, its citation in Related work, its citation in Appendix A, the
`\clearpage`, and the two negatives, that the superseded version DOI is gone and that no
trace of the old 0.35 remains. **Seventeen present, none absent.**

*The declarations of applied correction in this file, sixteen of them:* every
`Repaired on this branch` and every `Corrected in the manuscript for version 3`, each
checked where it points, including the two that name a commit by hash, which were verified
against that commit rather than against the current file. **Sixteen verified, none
failing.**

*The prose of the log itself.* This one found something. **A run of four paragraphs was
duplicated inside C-2**, the correction note repeated verbatim with its two following
paragraphs. It came from a script that failed halfway, was fixed and re-run, and applied an
edit whose anchor still matched. Removed. The same sweep also found the README's opening
quoted twice, in P-3 and in X-1, which is two entries quoting one source and not a defect.

**What this does and does not settle.** It settles that nothing else agreed in this phase
is missing from the manuscript, and that no entry claims a repair that is not there. It
does not settle that nothing was ever agreed and forgotten before this phase, because a
decision that left no trace anywhere leaves nothing to measure. The permanent check added
alongside, `section_bibliography`, closes one narrow case of that shape and says in its own
docstring that it would not have caught E-4: an apparatus that checks what is written
cannot check what was decided and never written.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.


---


## X-9. What the checkers found, what they now watch, and what none of them can see

**What was examined.** An external audit of the manuscript raised three findings and asked
for three sweeps. All were measured on the final tree; the results are here so that the
figures are not only in a commit message.

**Measurement.**

*Floats.* 15 labels, 35 references, 3 orphans, 0 references without a label. The orphans are
the subject of C-3 above. Now watched: `section_floats` fails on a label nothing references
and on a reference that resolves to nothing, with the three known orphans **declared by name
in the code** so that the gap is bounded and a fourth cannot hide behind it. Proved able to
fail both ways: a new unreferenced label is reported as `['tab:brandnew']`, a reference to a
missing label as `['tab:ghost']`.

*The non-breaking space.* 36 prose references carry the tie and 9 do not. Six of the nine
are not references at all but paragraph headings, `Result 3.1.`, `Conclusion 4.2.` and their
kind, where a tie would be meaningless. **Three are real**: `Result 4.1` at line 121,
`Section 4.3` at line 318, and `Appendix A` at line 294, which is in the sentence added to
Related work this same day. A line break can separate any of the three from its number. Not
repaired: it is a change to the manuscript and it waits for the author.

*Figures printed more than once.* 64 distinct values appear at least twice once years,
small integers and structural constants are set aside. The largest groups are 1008 with
sixteen appearances, 0.038 with seven, and 1013, 759, 12/16, 3.75, 120 and 74.5 with five
each. **Every group was read, and no group names one quantity with two different values.**
The repetitions are the abstract restating the body, the body restating a table, and a
figure appearing as both a count and a component of a ratio, which is what a paper does. It
is not made a gate: a check on repeated values would have to know which appearances mean the
same quantity, and that distinction is editorial, not mechanical. The measurement is
recorded so that the next reader does not have to redo it.

*Countable claims about the paper's own contents.* Eleven were enumerated and counted.
**Ten already have an assertion behind them**, including the seventeen non-constant cells of
Table A1, which is asserted as `non-constant entries of Table A1` and not merely believed.
**One does not: the four signatures of Table 2**, which the paper names repeatedly and no
check counts.

*Pointers into other people's works.* Seven, all naming the work they point into: two into
Shaughnessy (1996), one into Nielsen (2003), four into Hacker (1993). **None is ambiguous**,
and none could be confused with a pointer into this paper's own sections, which are written
`Section~` with a tie and a `ref`.

**The limit of the whole apparatus, which is the part worth keeping.** The suite now runs
269 checks across the figures, the surfaces, the compiled PDF's text and layout, the
bibliography, the floats and this log's own shape. **Not one of them can see a decision that
was taken and never written.** That is not a gap to be closed by another check: a decision
that left no trace leaves nothing to compare against. It failed twice in this project, with
the exact product of C-2 and the citation of E-4, and both times what caught it was a person
holding the list of what had been agreed against the file. **The only instrument for that
class is the list itself, compared by hand**, which is the sweep recorded in X-8. Every
checker here watches what is written; the list is what watches what was decided.

**What changed after this entry was written.** Three of the five measurements above
describe a state that no longer exists, and saying so here is cheaper than leaving a reader
to discover it. The three orphan floats now have pointers, written as C-3 records. The three
real missing ties are written: `Result~4.1`, `Appendix~A` and `Section~4.3`. The four
signatures of Table 2 are asserted: `CHAN_SIGNATURES` names them once and is read twice,
as the keys of the statistics the suite computes and as the row count Table 2 must print,
so the paper's four and the suite's four are one constant read in two places. Proved able to
fail: a fifth row printed in Table 2 reports `reproduced: 5   paper: 4`, and the fourth row
removed reports `reproduced: 3   paper: 4`. **The two measurements that stand unchanged are
the repeated figures, which named no quantity twice, and the pointers into other people's
works, none of them ambiguous.** What does not change at all is the closing paragraph: the
apparatus still cannot see a decision that was taken and never written.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-10. What each sweep actually looked at, and a report of mine that had to be corrected

**What was examined.** Whether the sentence "zero long dashes" is true of the set of files
a reader would take it to cover. It was not, in reports of mine written earlier in this
phase, and the correction is the entry.

**Measurement.** The subject set of each sweep, declared, because a count is meaningless
without the set it counted over.

| sweep | subjects | result |
|---|---|---|
| dashes, package | the 12 tracked text files of this repository, decoded as UTF-8 | 0 of U+2012, U+2013, U+2014, U+2015, U+2212 |
| dashes, deposited archive | every file inside the zip | 0 |
| dashes, laboratory | the 273 tracked text files of `iching-experiments` | 0 em dashes; **113 U+2013 and 97 U+2212 in 45 files** |
| floats | `paper.tex`, all `\label`, `\ref` and `\pageref` | 15 labels, 38 references, 0 orphans |
| bibliography | `paper.tex`, the body against `thebibliography` | 16 entries, 0 unnamed, 15 citations, 0 unresolved |
| frozen figures | the 29 pinned figures, old text against new | 0 changed their count, 0 moved |

**The laboratory's 210 stay, and this is the reason.** They are not this package's files and
not this project's prose: none falls in `paper/`, `replication/` or `scripts/`. That
repository's own style arbiter permits the en dash in references and APA ranges and forbids
only the em dash, of which there are none; and its U+2212 are typographic minus signs in
numbers the web renders, which its own comparison code normalises back to a hyphen before
reading them. A blanket replacement across 45 files of an application would change what is
rendered and could break its internationalisation checks, for a rule that repository never
adopted. The count is recorded here so that it is a decision and not an oversight.

**The report that had to be corrected.** Earlier rounds of this phase reported "zero long
dashes in both repositories". The package figure was right. The laboratory figure was
measured over the files this work touched, and reported as though it covered the repository.
**The same shape as the count that was published while stale**, which is the defect recorded
in P-1: a true statement about a narrow set, published where a reader reads it as a wide
one. It was found by widening the sweep to every tracked file and comparing the result
against what had been said, and the correction was issued in the same report that found it.
What it costs to prevent is one line: the subjects, written next to the count.

**And one more, found while writing this entry.** The status line of C-2 printed the same
sentence twice, consecutively and verbatim. It is the identical mechanism as the duplicated
block that X-8 found, an edit whose anchor still matched when a script was re-run, and it
survived the sweep that found the first one because that sweep compares whole paragraphs and
this repetition sits inside one. Removed. The sweep is not widened to sentences: the entry
records where its resolution ends, which is the honest repair when the alternative is a
check that would report every deliberate repetition in a log that quotes itself.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-11. A deposit checklist carrying hashes from a round that had already been superseded

**What was examined.** The author stopped a deposit because both files failed their hashes:
the archive and the compiled PDF each measured something other than what the checklist said,
and the checklist also said the PDF had not been recompiled while the PDF plainly had
changed. Two files wrong and a contradiction in the same document is the shape of a
corrupted package, so the deposit was halted, which was the correct call on the evidence
available.

**Measurement.** Nothing was corrupted. The expected values were real, and they were old.

| what the checklist expected | what it actually was |
|---|---|
| archive `13166d5f460d950f4e64e74863cd363d6e58b2c9f92372947d0a213ce5e2a4df` | the archive of commit `279b58c6`, rebuilt from that commit and matching to the bit |
| `paper.pdf` `55dedd04feccd7a335e0557f85232f5a306ed98b9f3c6d29169d771148e963a0` | the PDF committed at `279b58c6` and unchanged at `b3f97672` |

Two commits followed that state, both of them work that had been asked for and reported:
`b3f97672`, the manuscript audit, which changed no `.tex` and therefore recompiled no PDF,
which is why the PDF hash still held there; and `6dc361a0`, the three decisions, which
changed the manuscript and recompiled the PDF exactly once, which is where both hashes moved.
The archive on disk is byte for byte the tree of `6dc361a0` across all 14 files, and the
`paper.pdf` inside it is identical to the loose one. **Every number the author measured was
right, and so was every number in each report at the time it was written. What was wrong was
using the numbers from one round as the checklist for another.**

**What made the diagnosis possible, and it is worth keeping.** The archive is built with
`core.autocrlf=false` and `core.eol=lf` precisely so that it is a function of the commit and
nothing else. That is what turned an unexplained hash into an answered question: rebuilding
the archive from each candidate commit reproduced the expected value exactly, which
identifies the round a file came from instead of guessing at it. A checklist that cannot be
re-derived from a commit cannot be audited, only believed.

**The lesson, which is the reason this entry exists.** This is the stale-status defect of
P-1 turned on the deposit procedure itself: a set of true figures, published where a reader
takes them to describe the current state. Every earlier instance was about a document
carrying a number that had moved underneath it; this one was about a handover carrying
hashes that had moved underneath it. **A deposit block is built from the final state,
measured at the moment of handover, and never copied forward from the last report read.**
The rule now has a mechanical shape: measure the artefacts, then name the commit they came
from by rebuilding the archive from it, and only then write the block. It costs one command
and it is the difference between a halted deposit and a deposited wrong file.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-12. The landing page printed a count from a tree it did not name

**What was examined.** The public landing page, `paper.theoriginaliching.com`, against the
deposit it links to. A post sending sceptical readers to that URL was about to be written,
which is the moment a surface stops being internal.

**Measurement.** The landing printed **272 checks** in two places, its verification block
and its resources row, and the deposited version 3 runs **270**. Both figures were true of
something. Neither said of what. Measured: the live page is byte for byte `index.html` at
commit `00dfec64`, so it was current, not stale; the two extra checks entered in that same
commit and are the two identifier counts that the published version DOI made checkable.
**A reader who followed the link, downloaded the archive and ran it would have got 270 and
concluded the page was wrong about its own package.**

*And the abstract was not the deposited abstract.* Item (4) read `(12/16, p = 0.038
uncorrected)` where the deposit prints `(12/16, uncorrected one-tailed p = 0.038;
two-sided 0.077)`. The paraphrase drops the sidedness and the two-sided figure from the
single number a sceptic checks first, and 0.077 is the one that does not clear 0.05. The
landing is the face of the paper and may not paraphrase it. Restored word for word.

**The rule, now mechanical.** Every figure printed on a public surface names the tree it
came from, and there are exactly two: the **live repository**, whose count is measured
against the run in progress, and the **deposit**, whose count is a constant pinned to the
archive and never derived from the live one. `check_published_counts` reads them
separately, so a live number sitting where a deposit number belongs fails rather than
passing quietly. The landing now shows the deposited run of 270 labelled as version 3 with
its version DOI, and the live count on its own line labelled as the live repository.

**And the PDF is pinned by hash.** `section_landing` asserts that the `paper.pdf` the
landing serves hashes to `80b1648d2ce040c4cd33a84e4e1027b03c55a648c41798ce5a71ba2966a7b3d3`,
the bytes deposited as version 3, rather than to the file next to it. **It will fail the
moment the manuscript is recompiled, and stay failing until a new deposit exists**, which
is the intended behaviour and not an inconvenience: a page carrying a citable DOI must
serve the bytes that DOI resolves to. The repair when it fails is to deposit, not to edit
the constant. All three checks proved able to fail: a paraphrased abstract and a dropped
sentence each report the differing text, and one flipped byte in the PDF reports
`4b60659c...` against the deposited hash.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-13. Where the source of the paper lives, decided rather than inherited

**What was examined.** Which repository is the canonical home of the manuscript. The
question had never been decided in writing, and the three mirror problems recorded earlier
in this log all grew from the answer being ambiguous: the same content lived in two
repositories with no mechanical link, so every property that ought to follow from being one
thing had to be re-established by somebody remembering.

**Measurement.** The old working rule was that changes are born in the laboratory,
`iching-experiments`, and travel to this package. **During version 3 that rule was inverted
in fact**: every manuscript change of this phase was made here, compiled here, deposited
from here and tagged here, and the laboratory's copy was updated afterwards to match. The
laboratory's copies were a snapshot refreshed by hand, going stale on every commit here,
with nothing to notice.

**The decision.** The canonical home of the paper source is **this repository**, which is
the one that is deposited, tagged and archived. The reason is not preference: this is the
only copy that has a DOI, a tag naming the exact commit, and an archive whose bytes are
fixed. A canonical copy has to be the one a stranger can cite.

**What follows in the laboratory**, applied in the same round: its `paper/` stops being a
source and keeps only a pointer to this repository and to the tag `zenodo-v3`; its
`replication/` stops being a copy and keeps only the provenance manifest, so its gate
checks the manifest against the named commit instead of comparing bytes it no longer holds;
and every page that linked a local copy links this repository, the landing or Zenodo
instead. **The drift is not made legible, it is removed**: with one copy there is nothing
left to fall out of step.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

## X-14. The commits of this phase carry an author address that is not the account's

**What was examined.** A deployment was blocked with `the commit email
research@theoriginaliching.com could not be matched to a GitHub account`. The question is
what to do about the commits already pushed, which is a question about hashes and not
about mail.

**Measurement.** Both repositories carried a **local** git identity,
`The Original I Ching Research <research@theoriginaliching.com>`, overriding the account
identity in the global configuration, `alexcat84 <alexcat84@users.noreply.github.com>`. It
signs 69 commits here and 108 in the laboratory. Two commits of this repository, `d666948`
and `95437d3` of 2026-07-28, carry the account address, which is what a
`users.noreply.github.com` address is: bound to that account by construction. The local
override is removed in both repositories, so both now inherit the account identity, and
every commit from here on is attributable.

**The history is NOT rewritten, and this is the reason.** Changing an author address
rewrites every commit that carries it, and a commit hash is a function of its metadata as
well as its tree. The rewrite would leave every tree byte for byte identical and change
every identifier that names one. What names them: the tag `zenodo-v3` and its message; the
commit `d6afae20` recorded in this file, in the README, in `V3-PLAN.md` and in the
laboratory's manifest; and the deposited archive itself, whose whole method of
identification is that rebuilding it from the named commit reproduces its sha256 to the
bit. **The archive would still rebuild**, since the tree does not move, but the commit it
is attributed to would no longer exist, and X-11 exists precisely because that
identification was worth having. Rewriting to fix an address would trade a working method
of proof for a cosmetic uniformity of authorship.

So the repair is forward and not backward: the identity is corrected, the next commit
carries it, and the deployment that was blocked runs on that commit. **The addresses on
the historical commits stay wrong and stay recorded here**, which is the same choice this
log makes everywhere else: the deposits keep their defects and the record names them.

**Date examined.** 2026-08-03.

**Status.** EXAMINED, NOT AN ERRATUM.

---

Entries appear here when something is checked and found correct. They are kept for
the same reason the entries above are kept: a list that records only its hits does not
let a later reader tell what was looked at from what was never looked at.

---

# Applied

Eight entries, all applied in **version 3**, deposited 2026-08-03, version DOI
`10.5281/zenodo.21776041`, archive sha256
`0069259effc1290d4fc2c598ea8bf88dc0e1c1b76fa2523d0521f2c016c48aa5`.

Four defects of the paper (E-1, E-2, E-3, E-4) and four of the package (P-1, P-2, P-3,
P-4). **They are not rewritten here.** Each goes on describing the defect exactly as
versions 1 and 2 print it, because that is what a reader holding one of those versions
has in front of them, and each carries a line naming where it was corrected. The
placeholder this section used to hold said that the first deposit carrying corrections
would list the entries it applies and the version DOI it creates. This is that list.

---

## E-1. The description of the fourth rung of Appendix A

**Printed text.** Appendix A, page 14, first paragraph, fifth item of the list of
rungs:

> (P4) pairs permuted within and across the sixteen blocks of four consecutive
> positions, preserving the block partition

The item continues `; and (P5) ...` in the printed list; the span above is the
description of P4 in full. Line breaks of the printed column are not reproduced; no
other character is altered.

Transcribed character for character from the **version 2 deposit**
(10.5281/zenodo.21628654), file `garcia-hurtado-2026-king-wen-orderings-preprint.pdf`,
15 pages, 119326 bytes, sha256
`01c83c3d6d01878050a702b91901b55760218e4c6adcac4d57a9461a64904cfd`. The same sentence,
character for character, stands in the PDF carried inside the version 1 deposit
(10.5281/zenodo.21609654), 118955 bytes, sha256
`77ec0f6953657638ec04157b87de987cb737c8dd5bdef1eb6db2876ba18bb53f`: the two deposits
differ in the document metadata of the PDF, not in this text. The deposit is named
because the reader may hold either one, not because the wording differs.

**What it should say.** The blocks of four consecutive positions are permuted among
themselves, and a pair never leaves its block. Block membership is preserved by the
sampler; what is randomised is the arrangement of the blocks.

**Evidence.** Three internal witnesses, two of which agree against the third.

1. The replication code permutes the list of blocks. A pair never changes block.
   `verify_paper.py`, function `sample()` nested inside `section_appendix_a()`, branch
   `if rung == "P4":`, lines 1034-1043. The line that shows block membership is
   preserved is line 1035:

   ```python
   blocks = [kw_pairs[2 * b:2 * b + 2] for b in range(16)]   # line 1035
   rng.shuffle(blocks)                                       # line 1036
   ```

   Each block is built once, as two received consecutive pairs, and it is the *list of
   blocks* that is shuffled. The only freedom inside a block is `block.reverse()`
   (line 1041), which exchanges the two pairs of the same block. No pair is ever moved
   between blocks.

   *Which file those line numbers index.* A line range is worthless without the file it
   counts. The range above indexes `verify_paper.py` **as deposited in version 2**
   (10.5281/zenodo.21628654), 58910 bytes, sha256
   `9f835bd1f7e4af5b09de103b48f8fd2b875737553446f47a564a2c0e9f0042a7`, tagged
   `zenodo-v2` in this repository. That is the copy that sustains this entry, because it
   is the copy the reader of the deposit holds. Two courtesies, measured rather than
   assumed: the same lines carry the same code in `verify_paper.py` as deposited in
   version 1 (52980 bytes, tag `zenodo-v1`, sha256
   `bb857fffca9276ce2b1c3f13a4798a03978fea843b2385f84a2581176347ade8`) and at the head of
   this branch (60916 bytes, sha256
   `8a7085c5cd4d372843038c6a0a342626a1362f362c2b9f2db41997186ef1b957`). Those three files
   differ in size and in hash; they do not differ in that region, which is why one range
   serves all three.

   **Other trees exist and these ranges do not index them.** The live `main` of the
   repository, commit `95437d30f805be447cccabb30ea54ff983741f52`, carries a
   `verify_paper.py` of 69341 bytes, sha256
   `72abade176ab5f8826afa4dece160ab46b2641fa2fde8dbeff2d7e6b4d7a3faf`, in which the file
   has shifted: the line quoted above as 1035 is 1036 there, and the micro theorem comment
   quoted below as 1077 is 1078. Since the merge of 2026-08-03 the head of this branch has
   shifted too, and by more: the same two anchors are at **1050** and **1092** there. The
   deposit ranges are untouched by any of it. The ranges are deliberately **not** re-derived for that
   tree, because this entry is about what the deposits contain and the deposits are what
   the reader holds. They are excluded by name rather than by silence. A line range
   without its tree is the same defect as a count without its subject set, and this file
   has now made that mistake once, in the paragraph on the count, which is enough. Hashes are written unabbreviated here and everywhere in this file: a
   truncated hash cannot be checked, and a record whose identifiers cannot be checked is
   a record that asks to be believed.
2. The micro theorem printed in the same appendix states that quartets preserve the
   yang sum and that seven blocks sum to twelve. Under the literal reading of the
   printed description, a pair could leave its block, block sums would not be preserved,
   the count of blocks summing to twelve would not be invariant, and the reported
   constant value at P4 and P5 would not follow. Under that reading the printed theorem
   is false. Location: Appendix A, page 14, second paragraph (the one opening "Three
   observations"), the second observation, which reads in the deposit:

   > Second, from P4 upward the yang-balanced groups of four cease to be a statistic
   > and become a constant: preserving the block partition preserves each block’s yang
   > sum (in the received sequence the sixteen sums include exactly seven equal to 12),
   > so this signature is a corollary of block membership

   Line breaks of the printed column are not reproduced; no other character is altered.

   Its counterpart in the replication package is `verify_paper.py`, lines 1077-1086,
   comment "The micro-theorem". That range indexes the same file as the range above:
   `verify_paper.py` as deposited in version 2, sha256
   `9f835bd1f7e4af5b09de103b48f8fd2b875737553446f47a564a2c0e9f0042a7`, tag `zenodo-v2`;
   it holds unchanged in the version 1 deposit and at the head of this branch. The
   printed location, page 14 of the deposited PDF, is the one that sustains the entry;
   the code range is corroboration.
3. The theorem and the code agree with each other. The dissenting witness is the prose.

**Date found.** 2026-07-31, during the formal verification carried out for the
follow up paper on the generalised null ladder.

**Figures affected.** None.
Measurement: the seven constant cells of the frozen table were re-derived from the
inheritance property and all seven hold, with none refuted. Full re-execution of
`verify_paper.py`, run on 2026-07-31 against the deposited trees themselves, extracted
from the zip files of the two deposits and not from a working copy:

| tree run | checks passed | failed | total |
|---|---|---|---|
| version 2 deposit, 10.5281/zenodo.21628654 | 202 | 0 | 202 |
| version 1 deposit, 10.5281/zenodo.21609654 | 192 | 0 | 192 |
| head of branch `errata`, before the repairs | 211 | 0 | 211 |
| head of branch `errata`, after the repairs | 212 | 0 | 212 |

No check fails and no figure moves. The two deposits differ in the size of the suite,
not in any reproduced figure: the suite grew between them.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
The two page pointers are printed in the manuscript of that deposit. The entry
goes on describing versions 1 and 2, where the pointers are absent.

**Cross reference, and what it is not.** The same defect is recorded a second time, as
`SELF D-2`, in the verification record of the follow up paper on the generalised null
ladder. That record is where the discrepancy was found. It is not what establishes it,
and this entry does not lean on it: the two witnesses above, the sampler and the printed
theorem, are both inside the published replication package, two paragraphs apart in the
same appendix and a few lines apart in the same script, and a reader holding the deposit
can check them without knowing that any follow up paper exists. Nothing here is
transported from that record, which in any case sits in a repository with no public remote
and could not be cited by URL. Found by that work; established by this package.

**Note for a reader who has only the paper.** The theorem, not the sentence, states what
the sampler does. A reader who follows the theorem is not misled.

**Corrected in the manuscript for version 3**, on branch `errata`, 2026-08-03. The clause
now reads:

> (P4) the sixteen blocks of four consecutive positions permuted among themselves, so
> that a pair never leaves its block, with the two pairs inside a block free to exchange
> and all orientations free

which says what the sampler does. The test that mattered was not that the new sentence
reads well but that it leaves the printed theorem two paragraphs below **true under its
literal reading**, which the old one did not: blocks permuted among themselves, with no
pair leaving its block, preserve the block partition, so each block's yang sum is
preserved, so the count of blocks summing to twelve is invariant and the statistic is a
constant from P4 upward, exactly as the theorem says. The mechanical counterpart of that
argument is already asserted and passes: `rung P4: yang-balanced groups equal 7 in every
control sample`. The entry above is unchanged and still describes the deposits.

---

---

## E-2. The ladder described as one of increasing structure

**Printed text.** Appendix A, page 14, opening paragraph, second sentence:

> We re-evaluate the four signatures of Table 2 under a ladder of six nulls of
> increasing structure, each conceding more of the sequence’s architecture and asking
> what remains

The apostrophe in `sequence’s` is U+2019 in the artifact and is reproduced as such
here. Line breaks of the printed column are not reproduced; no other character is
altered.

Transcribed character for character from the **version 2 deposit**
(10.5281/zenodo.21628654), sha256
`01c83c3d6d01878050a702b91901b55760218e4c6adcac4d57a9461a64904cfd`. The same sentence
stands character for character in the PDF inside the version 1 deposit
(10.5281/zenodo.21609654), sha256
`77ec0f6953657638ec04157b87de987cb737c8dd5bdef1eb6db2876ba18bb53f`.

**What it should say.** The six nulls are ordered by containment, and that order is
partial rather than total. A later rung concedes a different part of the architecture,
not a larger part of it.

**Characterisation.** A false general statement all of whose particular consequences
hold. It is false as a general statement: the family is not a chain, so there is no
sense in which each rung concedes more than the one before it. Measured on the printed
order itself, two of its five consecutive steps are not steps at all. `(P2, P3)` and
`(P3, P4)` are incomparable, each refuted in both directions by a witness exhibited
below; the other three, `(P0, P1)`, `(P1, P2)` and `(P4, P5)`, are strict containments.
Every particular consequence nonetheless holds, and none is withdrawn: the printed order
is a valid linear extension of the containment order, since all eleven strict
containments print the larger group before the smaller, so every statement of the form
"the statistic varies at this rung and is constant at the next" survives unchanged, and
no figure in Table A1 moves.

The printed sequence cannot be defended as an ordering by size either, and the
measurement is recorded rather than passed over: the six sets have exact cardinalities
`|P0|` = 64!, `|P1|` = 32! x 2^32, `|P2|` = 15! x 17! x 2^32, `|P3|` = 28! x 2^28,
`|P4|` = 16! x 2^16 x 2^32, `|P5|` = 2^32, and ordering by those gives P0, P1, **P3, P2**,
P4, P5. `|P3|` is 41 times `|P2|`, so the two rungs print in the opposite order to their
size. This is consistent with their being incomparable and it is not a contradiction; it
is simply one defence the printed wording does not have.

**Evidence.** The fifteen pairwise containments between the six rungs were computed
from predicates derived from the printed definitions. Eleven strict containments, four
incomparable pairs, zero equalities. Each refutation is accompanied by an exhibited
witness, that is a concrete permutation lying in one rung and not in the other, checked
in both directions.

The derivation below is not transported from anywhere, and it does not rest on the follow
up work in which the question arose. An earlier record of the same result exists in a
repository with no public remote, which cannot be cited here, and copying its prose would
be copying a paraphrase; so the predicates were written again from the printed definitions
of P0 to P5 in the deposit, and the witnesses were produced again. The fifteen containments
and their witnesses are computable from the definitions the paper itself prints, by anyone
holding the deposit, which is what establishes the entry. That work is where the question
came from, and that is all it is.

*What this is, named exactly.* It is not an independent derivation, and calling it one
would overstate it. The result was already written in this file before the computation
was run: eleven strict containments, four incomparable pairs, zero equalities, all three
figures printed in the skeleton of this entry. The work was done again from the printed
definitions, but with the answer in view, so the correct name is a reproduction with a
known target. It is worth less than a blind derivation, in which the numbers could not
be steered toward the expected ones. It is worth more than a transport, for one reason
that can be checked: a reproduction can fail, and this one did fail. The first
generating set written for P4 was too small to generate the group, the decision
procedure returned P4 as contained in P2, and the exhaustive enumeration refuted it. A
transcription cannot produce that error, because it never computes anything, and cannot
catch it either. That failure, and not the final agreement with the printed claim, is
what distinguishes a derivation actually run from a description of one.

*Notation.* In King Wen numbering the received sequence is literally 1, 2, ..., 64, so
a member of any rung is a permutation of the 64 hexagram numbers. It is written as its
32 slots, each slot holding one pair in its printed orientation. A witness is given as
the received order with one named change; every slot not named holds what it holds in
the received order, which fixes the permutation completely.

*Predicates, each from its printed definition.* (P0) any permutation of the 64.
(P1) every slot holds a received pair, in either orientation. (P2) P1, and the pairs
occupying the first fifteen slots are exactly the fifteen pairs of the first canon.
(P3) P1, and each of the four palindrome pairs (1,2), (27,28), (29,30), (61,62) sits in
its own slot in its received orientation. (P4) P1, and the two pairs of each received
block of four consecutive positions are still together in one block. (P5) P1, and the
pair order is the received one, orientations free.

The reading of P4 used here is the corrected one of E-1, which the printed micro
theorem forces. Under the literal reading of the printed sentence, in which a pair may
leave its block, P4 would coincide with P1: the order would then carry one equality and
ten strict containments, not eleven and zero, and the theorem of the same appendix
would be false. The defect of E-1 and the shape of this order are the same fact seen
twice.

*The four incomparable pairs, with witnesses checked in both directions.*

| pair | witness | in | not in |
|---|---|---|---|
| P2, P4 | received order with pairs (3,4) and (7,8) transposed: slots 1-4 read (1,2) (7,8) (5,6) (3,4) | P2 | P4 |
| P2, P4 | received order with pairs (29,30) and (31,32) transposed: slots 14-17 read (27,28) (31,32) (29,30) (33,34) | P4 | P2 |
| P2, P3 | received order with pairs (1,2) and (3,4) transposed: slots 1-4 read (3,4) (1,2) (5,6) (7,8) | P2 | P3 |
| P2, P3 | received order with pairs (3,4) and (31,32) transposed: slots 1-3 read (1,2) (31,32) (5,6) | P3 | P2 |
| P3, P4 | received order with pairs (3,4) and (7,8) transposed: slots 1-4 read (1,2) (7,8) (5,6) (3,4) | P3 | P4 |
| P3, P4 | received order with the first two blocks transposed: slots 1-5 read (5,6) (7,8) (1,2) (3,4) (9,10) | P4 | P3 |
| P3, P5 | received order with pairs (3,4) and (5,6) transposed: slots 1-4 read (1,2) (5,6) (3,4) (7,8) | P3 | P5 |
| P3, P5 | received order with pair (1,2) written 2, 1: slots 1-3 read (2,1) (3,4) (5,6) | P5 | P3 |

Each row was evaluated against both predicates, and each of the eight came out a member
of the first rung and not of the second. Two rows per pair are given rather than one,
because incomparability is two refutations and not one: neither rung contains the other.

The witness that separates P4 from P2 is the transversality made concrete. Pairs
(29,30) and (31,32) are the two halves of the eighth block; exchanging them keeps every
block intact, so the sequence is a member of P4, and it moves a pair of the second canon
into a slot of the first, so it is not a member of P2.

The witness that separates P5 from P3 turns on orientation alone: P3 fixes the four
palindrome pairs in position *and* orientation, while P5 randomises all 32 orientations,
so the received order with (1,2) written 2, 1 lies in P5 and outside P3.

*Method, and a check on the check.* Each rung factors as a set of pair orders times a
set of orientation vectors, so containment is decided exactly: on the order part by
subgroup generators, on the orientation part by which coordinates are forced. That
decision was cross-checked against a full enumeration of the same construction shrunk to
eight pairs, four blocks of two, canon split three and five, which keeps the one feature
that matters, a canon boundary falling strictly inside a block. The cross-check earned
its keep, in the way recorded above. The corrected computation and the exhaustive
enumeration then agree: eleven strict, four incomparable, zero equalities.

**Verification record.** `errata-evidence/errata_e2_derivation.py` on branch `errata`. It
carries the six predicates, the decision procedure, the eight witnesses and the
exhaustive enumeration on the shrunk model, and it runs on the standard library alone.
Until it was committed the code existed only outside the repository, and the slot pointed
at this entry; it now points at the file, which is what a pointer is for. It sits in a
directory of its own, and not beside `verify_paper.py`, for the reason given in the
package README: it is not replication code and must not be able to be mistaken for it. The
prose of the entry first arrived in commit
`90d4455b140ad9e69fe7ff19c58aa08562a434e6`, on 2026-07-31.

The evidentiary weight, however, does not rest on that file or on any commit. It rests on
the eight witnesses exhibited above, which a reader checks by hand against the printed
definitions, with no code and no clone. The commit lives on a branch that is not merged
and may never be; a reader who has only the deposited paper can still verify every row of
the table. Code that can disappear must not be the thing an erratum stands on.

The canon division and the block partition are transversal: fifteen and seventeen pairs
put the boundary between slots fourteen and fifteen, which lie inside the eighth block
of four positions. This is a property of the object and not of the formalisation.

**Date found.** 2026-07-31, same verification.

**Figures affected.** None.
Measurement: the printed order of the six rungs is a valid linear extension of the
partial order, since all eleven strict containments print the larger group before the
smaller. Every statement of the form "the statistic varies at this rung and is constant
at the next" therefore survives unchanged.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.

**Corrected in the manuscript for version 3**, on branch `errata`, 2026-08-03. The opening
sentence now reads:

> under a ladder of six nulls ordered by containment, an order that is partial rather than
> a chain: each rung concedes some part of the sequence's architecture, not uniformly more
> than the rung before it, and we ask what remains

The word `increasing` is gone, and it has not been replaced by a second general claim that
would not hold either. What the new sentence asserts is what was measured: the family is
ordered by containment, and that order is partial. It does not claim the rungs grow, which
is false, nor that they are ordered by size, which is also false, since ordering the six
by cardinality puts P3 before P2 while the paper prints P2 first. The name `ladder` is kept
because the printed order is a valid linear extension of the containment order, so every
later reference to rungs, to `from P4 upward` and to the top of the ladder remains true as
a reference to the printed sequence. The entry above is unchanged and still describes the
deposits.

---

---

## P-1. The deposited package declares a check count its own suite does not have

The first entry about the package rather than the paper. The distinction is measured and
not assumed: neither `paper.tex` nor the compiled PDF states the number of checks in this
package anywhere, so no figure printed in the paper is touched by what follows.

**Printed text.** Four places in the version 2 deposit (10.5281/zenodo.21628654). In
`README.md` line 35 and `index.html` line 197, inside a sample of the program's own
output:

> ```
>   192 checks passed, 0 failed, 192 total
> ```

In `index.html` line 179:

> paper source, compiled PDF, and a self-contained script that reproduces every figure
> (192 checks, standard library only)

In `README.md` line 115, in the table of what each documented mutation produces:

> the run completes and reports `175 checks passed, 17 failed, 192 total`

**What it should say.** 202 in the first three. In the fourth, `185 checks passed, 17
failed, 202 total`.

**Evidence.** The suite deposited in the same archive, run against its own tree,
extracted from the deposited zip and not from a working copy: **202 checks passed, 0
failed, 202 total**. The documented mutation (c) then run on that tree exactly as its own
README prescribes: **185 passed, 17 failed, 202 total**, exit status 1, first failing
check `3.1`, which is the check the table names. The failure count of 17 and the identity
of the first failing check are correct as printed; the two totals are not.

Where the ten went, measured per section: the front matter section grew from 16 checks to
19, and a new section asserting the document metadata of the PDF contributed 7. Sixteen
plus three plus seven is the whole of the difference; no other section moved, and no
figure of the paper is among them.

The timeline is the explanation, and every instant in it is measured rather than
inferred:

| instant (UTC) | event |
|---|---|
| 2026-07-27T15:40:26Z | commit `61486e35665f0fc42212205ca05b0ead7048e0f6`, the tree later deposited, already carrying the 202-check suite |
| 2026-07-27T16:16:56Z | the version 2 record is created on Zenodo, 36 minutes later, with the surfaces still saying 192 |
| 2026-07-27T16:52:01Z | commit `9b4720999e63c5a0ba944ad261b5d6e2aac47031` separates the version DOI from the concept DOI, 35 minutes after the deposit |
| 2026-07-28T04:36:47Z | commit `73d9a77cdc59ea1410ae815cbb484dc68eb752d1` corrects the count on the surfaces, 192 to 202, twelve hours after the deposit |

**The version 1 deposit is consistent, and this is measured, not assumed.** All four
strings read 192 there and its tree measures 192; its mutation table reproduces exactly,
`175 checks passed, 17 failed, 192 total`, the figure it prints. The package did not carry
this defect from the start and does not carry it chronically. The mismatch is born in the
version 2 deposit, in a window of twelve hours and thirty-six minutes between a suite that
had already grown and surfaces that had not yet been updated, and it is corrected the
following day. One deposit is affected, and it is the current one, which is why the entry
is open.

**Date found.** 2026-07-31, during a consistency sweep of the two deposited archives.

**Figures affected.** None in the paper, and this is measured rather than asserted: every
figure of the paper reproduces in both deposits, 192 of 192 in version 1 and 202 of 202 in
version 2, with no failures in either. What is wrong is the package's statement about its
own suite, not any statement about the King Wen sequence.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Corrected in the repository on 2026-07-28 in commit
`73d9a77cdc59ea1410ae815cbb484dc68eb752d1`, and that correction is in the deposited
archive of version 3, which is what a reader downloads today. It remains present in
10.5281/zenodo.21628654, which is version 2. This entry said it would close with the
next deposit and name the version that applied it; that version is named here.

**Note for a reader who has the package.** Run it. The program prints its own count, and
the count it prints is the true one.

**The class is now mechanised, and not by this lane.** While these entries were being
written, the repository's `main` gained a check of its own, `check_published_counts`, which
asserts that every check count published in `README.md` and in `index.html` is the number
the suite actually runs. It arrived in commits `d6669487b51ac141ab779891ab85db2503e08974`
and `95437d30f805be447cccabb30ea54ff983741f52` of 2026-07-28, without knowledge of this
log, and it makes the defect recorded above impossible to repeat unnoticed: the surfaces
and the suite can no longer disagree without the run failing. Since the merge of
2026-08-03 that check runs on this branch too, and it is what caught the surfaces during
the merge itself. The entry stays open, because the deposits still carry the defect and a
gate on `main` does not reach into a frozen archive. See X-7.

---

---

## P-2. The suite prints a value the paper does not print, in the column that claims to quote it

**Printed text.** As it stands in the deposits, which is where the defect exists and
where it cannot be taken out. `verify_paper.py` of both deposits, line 742, and of the
live `main`, line 743:

```python
    check("5.6", "Bonferroni over the nine criteria (0.038 x 9)",
          round(0.038 * 9, 2), 0.34, ok=close(0.038 * 9, 0.35, 0.02))
```

The fourth argument is the value the suite attributes to the paper, and the run prints it
under a column headed `paper:`. A clean run of either deposit, or of the live `main`,
therefore shows

```
  [PASS] 5.6   Bonferroni over the nine criteria (0.038 x 9)
         reproduced: 0.34   paper: 0.34
```

**What it should say.** `0.35`, which is what the manuscript prints, with the equality
left to do its work; or, if the tolerance is kept, centred on the same value the column
declares. The two must not name different numbers.

**Evidence.** The manuscript prints `0.35` and never prints `0.34`. Measured in the
deposited `paper.tex` of version 2, in its compiled PDF at page 9, and in the same files
of version 1 and of the live `main`: the string `0.34` does not occur in `paper.tex` in
any of the four trees, and the sentence at issue reads `With nine tests, 0.038 x 9 ~
0.35.` The exact product is 0.34199999999999997, whose rounding to two places is 0.34,
which is what `round(0.038 * 9, 2)` returns and what both columns of the output show. So
the reader of the output sees `0.34` twice and has no way to learn that the paper says
something else. The equality that would have caught it is overridden by
`ok=close(0.038 * 9, 0.35, 0.02)`, whose band is wide enough to swallow the difference
and which compares against a third value, the printed one, that the column never shows.

**It is a case and not a class, and the difference decides the repair.** Measured over
every `check()` call: 154 calls in the version 2 deposit, 161 in the live `main`, 164 at
the head of this branch when this entry was written and 177 now, of which **23 carry an
`ok=` override in the deposits and in the live `main`, 24 at the head of this branch once
the assertion of E-3 was added, and 23 again from version 3 on**, because the correction
recorded in C-2 made the manuscript print the exact product and turned this very check from
a band into an equality. The assertion added by the repair of E-3 keeps its band, and the
reason is discussed there. Three of the 23 declare a value different from the one their tolerance tests:

| check | column declares | tolerance tests | the paper prints |
|---|---|---|---|
| 5.6, Bonferroni over the nine criteria | 0.34 | 0.35 | 0.35 |
| 5.1, pair-null percentile, lag-1 autocorrelation | 6.4 | 6.3 | 6.4 |
| 5.1, pair-null percentile, yang-balanced groups | 89.6 | 89.7 | 89.6 |

Only the first declares a value the paper does not print. The other two declare the
printed value and merely centre a Monte Carlo band on the value actually measured, which
is ordinary practice and conceals nothing. One case. Had it been a class, the repair would
have been a rule, that no check may declare one value and test another, enforced
mechanically; for a single case the repair is to correct the case and to record that the
sweep was done, so that nobody has to wonder later whether it was.

**Date found.** 2026-08-03. The discrepancy was found in the course of an audit of this
repository run by a separate session of the same process. That is where it was found and
not what establishes it: everything above is internal to the published package, the line
of code and the sentence of the manuscript sit in the same archive, and a reader with the
deposit and nothing else can check every claim in this entry. It would stand if the audit
had never happened.

**Figures affected.** None. Measured: the suite passes in all four trees with the
override as it stands, and would still pass with the column corrected to 0.35, since
0.342 is within 0.02 of 0.35. No conclusion of the paper moves either way, because both
0.34 and 0.35 are far above the 0.05 the sentence is arguing about.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Present in versions 1 and 2, which is what a reader of those versions downloads.

**Repaired on this branch**, in commit `10786bdd2e8ff40fb0271dbfa6fd50b259ef0b44`, which
changes the declared value to 0.35 and leaves the tolerance alone. The same commit changed
the left column from the two-place rounding to the three-place one, so that the line reads
`reproduced: 0.342   paper: 0.35` instead of showing 0.34 beside 0.35 on a line marked
PASS. That was not asked for, so it was measured rather than assumed: the suite has no
single display precision to break. Across its 165 checks, `round` is called to one place
19 times, to two places 5 times, to three places 16 times and to four places 4 times, and
the precision follows the figure being shown. The nearest sibling does exactly what this
line now does: the Appendix A check of `0.035 x 17 = 0.6` displays the exact product to
three places against a printed figure rounded to one, with a tolerance carrying the
difference. So this is not a new convention, it is the existing one, and the measurement
is recorded here rather than left as a matter of taste. The entry above
describes the deposits and is not rewritten to match the repair: a reader of a future
version who finds this entry and then reads the shipped code must be able to tell which
of the two they are looking at. Nothing in a deposit is altered by that commit, and the
correction reaches a reader only when a version carrying it is deposited.

---

---

## E-3. The abstract says every numerical claim is asserted, and one is not

**Printed text.** Page 1 of the deposited PDF, the abstract, its last sentence:

> Every numerical claim in this paper is asserted by an automated test suite in a public
> repository.

Line breaks of the printed column are not reproduced; no other character is altered.

The figure at issue is in Table 2, page 7:

> lag-1 autocorrelation of distances -0.247 4.0 6.4 marginal, not significant

*What was altered in that row, named here rather than left to the policy.* Two glyphs and
one piece of layout. The compositor draws U+2212 in `-0.247` where the source writes an
ordinary hyphen-minus, and it is written above as the hyphen-minus. The word `significant`
carries the ligature U+FB01 for `fi` in the artifact and is written above as two letters.
And the row is a table row: in the PDF its cells stand on separate lines, `lag-1
autocorrelation of distances`, `-0.247`, `4.0`, `6.4`, `marginal, not`, `significant`, and
they are joined above with single spaces. Nothing else in it is altered.

The figure `4.0` is the free-shuffle percentile of the lag-1 statistic.

**What it should say.** Either the sentence admits its exception, or the suite asserts the
figure. The narrow correction is the second: one assertion for the free-shuffle percentile
of the lag-1 statistic, and the sentence becomes true as printed.

**Evidence.** Measured over four trees, with the subject set declared: `paper.tex` and
`verify_paper.py` of the same tree; a figure is a decimal or a fraction in the body of
`paper.tex` after LaTeX markup is stripped; covered means the decimal appears in
`verify_paper.py`, or, for a fraction `a/b`, that either `a/b` or the tuple `(a, b)` does.
The tuple form matters and a literal-only test is wrong: the suite asserts 7/15 as
`(7, 15)`.

Of 115 figures printed in each deposit and 112 in the live `main`, **eight have no
counterpart, the same eight in all three of those trees**: 98.2, 0.037, 0.251, 4.0,
0.000, 1.000, 1/24, 120/32. Three of the eight are Chan's figures rather than
this paper's, and one of those, 0.251, is quoted only to be compared with our own -0.247.
Four more are formatting variants of figures the suite does assert: 0.000 and 1.000 are
Kendall taus printed to three places and asserted as 0.0, 1/24 is printed beside the
0.042 that is asserted, and 120/32 is printed beside the 3.75 that is asserted. That
leaves exactly one figure of the paper's own that the suite does not assert in any form:
**4.0**.

**A reading that was corrected before this entry was written.** The self-referential count
of verification sections, 61 in the first deposit and 63 in the second, is not asserted by
this package's suite either: measured, the strings `verification sections`,
`assertion suite comprises` and `laboratory of` occur zero times in `verify_paper.py` in
all four trees. It was tempting to add it to this entry and it would have been wrong. The
sentence says `an automated test suite in a public repository`, indefinite twice over. It
does not say this suite or this repository, and the laboratory's suite does assert that
count and is public. The sentence survives the section count. What it does not survive is
4.0.

**Date found.** 2026-08-03. Found in the course of an audit of this repository run by a
separate session of the same process, and established here by the measurement above, which
reads only `paper.tex` and `verify_paper.py` of the four trees and can be repeated by
anyone holding either deposit. That audit reported thirteen unasserted figures; the
measurement made here gives eight by the method declared, and where the two disagree this
one governs. The count came out different, which is the ordinary reason to re-measure a
lead rather than adopt it.

**Figures affected.** None. The unasserted figure is not a wrong figure: 4.0 is not
contradicted by anything, it is simply not checked. Measured: every tree passes its full
suite, 192 in the first deposit, 202 in the second, 246 on the live `main` and 212 at the
head of this branch after the repair below, none failing anywhere.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Present in versions 1 and 2, which are the objects this entry describes.

**Repaired on this branch**, in commit `d25149ac4dc1105918f7fadb3ae067314f184cbd`, which
asserts the figure: the free-shuffle percentile of the lag-1 statistic, band 0.6, the
width its two neighbours use, because the printed 4.0 comes from the other implementation
and this one measures 3.8. The assertion was shown able to fail before it was believed:
moving the declared value to 6.0 fails it alone, and negating the statistic it rests on
fails it along with its two relatives.

*What that band can see and what it cannot, said plainly.* It catches a gross error: the
2.0 point move to 6.0 fails it, as does any change to the statistic underneath, which
shifts the percentile to the other end of the scale. It would not see a drift of 0.3
points, and it is not meant to: the printed 4.0 comes from a different implementation and
a different draw, and this one measures 3.8, so a band narrower than the gap between two
honest implementations of the same quantity would fail for the wrong reason. That is the
line between a band with a reason and a tolerance that hides something, and it is the same
line P-2 is about. The reason is written here so that a later reader can judge the band
instead of trusting it. It also makes the entry's new check the twenty-fourth `ok=`
override on this branch, which is recorded in the inventory in P-2. The entry above describes the deposits, where the
figure is still unasserted, and is deliberately not rewritten to match the branch.

**What the repair did to the sentence, which is the reason this entry is an E.** The last
line of the abstract reads:

> Every numerical claim in this paper is asserted by an automated test suite in a public
> repository.

That sentence was false, and this entry is what made it false. It is now **true, and not one
word of the manuscript was changed to make it so.** The repair happened entirely in the
code: two assertions were added, one for the free-shuffle percentile of the lag-1 statistic
and one for the degenerate row of Table 1. **This is the only entry in this log where the
repair restores a claim of the paper instead of correcting it**, and that is precisely why
it is an **E** and not only a **P**: the defect lived in a promise the manuscript makes, and
the place to keep the promise was the suite.

*The subject set, declared, and every exclusion named.* Measured over `paper.tex` and
`verify_paper.py` of the same tree: 112 printed figures, of which **eight had no counterpart
when this entry was opened and none has one now**. Two were repaired by assertion:

1. **4.0**, the free-shuffle percentile of the lag-1 statistic in Table 2, asserted in
   commit `d25149ac4dc1105918f7fadb3ae067314f184cbd`.
2. **1.000**, the Kendall tau of the binary ordering against itself in Table 1, asserted
   together with the 0 inversions of the same row.

Three are not claims of this paper, and the distinction is not a convenience. They are
**98.2**, **0.037** and **0.251**: the first two appear inside the report of what Chan
(2026) found, and the third is printed as "against Chan's -0.251". A figure quoted from
another author is a claim about what that paper reports, which this suite cannot verify
without that author's implementation; and this paper's own counterparts to all three, the
3.349, the 97.9 and the -0.247 it measured for itself, are asserted.

Three are formatting variants of quantities that are asserted, and they do not count
because the quantity is checked and only its printed precision differs from the literal in
the code: **0.000** is the three-place rendering of the Kendall taus asserted as `0.0`,
**1/24** is printed beside the 0.042 that is asserted, and **120/32** is printed beside the
3.75 that is asserted, with 120 asserted separately.

Eight without a counterpart at the start, **zero at the end**.

*Why the last one was invisible, which is the part worth keeping.* The tau of the binary
ordering against itself is 1 by definition, and the inversions are 0 by definition. Nothing
in the suite compares an ordering **with itself**: every check in it was built to compare
two different orderings, so the degenerate case sat outside the shape of the instrument.
Its triviality is what hid it, not its difficulty. Swept for others of the same form across
every table in the paper, Table 1, Table 2, the centers table, the battery, the spectral
fingerprints and Table A1: **those two cells are the only self-comparisons in the paper, and
there are no other definitional values left unasserted.** The spectral row for the binary
ordering looks similar and is not the same thing, since its Walsh energies are computed and
are asserted with the other four.

**Cross reference.** The same defect on the package's surface is P-3, which follows. One
defect, two surfaces, one figure, one repair.

---

---

## P-3. The README makes the same promise, in the definite

**Printed text.** As it stands in the deposits. `README.md` of both deposits and of the
live `main`, in the opening paragraph:

> This repository is the replication package for the paper. It contains the manuscript
> source, the compiled PDF, and a single self-contained script that reproduces **every
> numerical claim** made in the paper from first principles.

**What it should say.** The same repair as E-3 makes both sentences true: assert the free
shuffle percentile of the lag-1 statistic. Failing that, the promise needs the exception
written into it.

**Evidence.** The measurement is the one recorded in E-3 and is not repeated here. What
differs is the strength of the claim, and it differs against this surface: the abstract
says `an automated test suite in a public repository`, indefinite, and survives everything
except 4.0; the README says `a single self-contained script`, definite and named, and so
promises that this script asserts every numerical claim of the paper. There is no second
suite for it to be leaning on. The same single figure falsifies it, and falsifies it more
plainly.

**Date found.** 2026-08-03, with E-3, and established by the same internal measurement.
The provenance is the same audit, recorded as where it was found.

**Figures affected.** None, as in E-3.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Present in versions 1 and 2.

**Repaired on this branch** by the same commit as E-3,
`d25149ac4dc1105918f7fadb3ae067314f184cbd`. One assertion makes both sentences true.

**Cross reference.** E-3. The two entries are the same defect on two surfaces and are
kept apart only because the categories of this file are by surface: the paper's text is
E, the package is P. They are repaired by one assertion.


---

---

## E-4. The paper says where the corrections were found and never says where to find it

**Printed text.** What is wrong here is an absence, and an absence cannot be quoted, so
what is quoted is the place where the reference belongs and is not: the closing sentence of
Related work, page 11 of the version 2 deposit, which runs straight from the last
unrelated remark to the end of the section.

> The tradition's own account of the sequence, the Xugua commentary, is narrative and is
> not treated here as a structural hypothesis, because it provides no formalizable rule.

Line breaks of the printed column are not reproduced; no other character is altered. The
absence itself is measured rather than described: against the `paper.tex` of the version 2
deposit, zero occurrences of `uninformative`, of `21750029`, of `order-theoretic` and of
`stopping criterion`, and a bibliography of fifteen entries, none of them that preprint.

**What it should say.** The errata of this package states, in several entries, that the
discrepancies were found *in the course of* that work. A reader who reads that sentence
looks for the work in the references and finds nothing there. The bibliography needs the
entry, and the body needs to say what that work is, as related work and not as support.

**Evidence.** Internal and immediate: the log makes the claim and the manuscript does not
carry the reference that would let anyone follow it. It is a defect of the pair, not of
either alone, and it is the only entry here whose evidence is a relation between two
documents rather than a measurement inside one.

**Whose failure this was.** Not the manuscript's author acting carelessly and not the
suite's. The instruction to cite that work was given in a supplement to one round and was
not carried into the next, so it fell between two rounds of the same process and nothing
noticed, because nothing checks for a citation that ought to exist. Recorded that way
because the alternative, leaving it unattributed, would make the log less useful to the
person most likely to hit the same seam: a process that hands work forward in rounds loses
what is written only in the margin of a round.

**Date found.** 2026-08-03, before the version 3 deposit.

**Figures affected.** None. Measured: the suite reports 264 checks, 0 failed, before and
after the citation was added, and no figure of the paper is touched by a bibliography entry
and two sentences of related work.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Present in versions 1 and 2, which is where it exists.

**Corrected in the manuscript for version 3**: the bibliography gains the entry in its alphabetical place, between Chan and Hacker, with the
title and the author string taken from the Zenodo record of that work rather than from the
instruction, since it is a self-citation and has to match how the work is registered. The
body cites it twice, in Related work and in Appendix A, whose object that work is, and in
both places as related work: it is named as giving an order-theoretic reading of the ladder
and as reporting the verification of the two constructions against their printed sources,
and **it is not used to support any correction**. Every entry in this log still stands on
this package alone.

---

---

## P-4. A table of the appendix printed in the middle of the bibliography

**Printed text.** The caption is correct; where it is printed is not. It opens:

> Table A1: Chan's four signatures across the ladder of conditional nulls, in the column
> order of Table 2: mean transition distance, lag-1 autocorrelation of distances,
> yang-balanced groups of four, and within/between-pair asymmetry.

Line breaks of the printed column are not reproduced; no other character is altered. In the
version 2 deposit and in every compile up to this one, that caption and the table it heads
are printed **on a page of the references**. Measured on the PDF as it stood at commit
`68089cada56d93f16709a3aa1ac1a3d7b371a164`: the bibliography runs from the `References`
heading on page 13 to its last entry on page 14, and the Table A1 caption is on page 14.

**What it should say.** The table belongs with the appendix that discusses it, after the
bibliography ends.

**Evidence.** The source order is correct and that is the point: in `paper.tex` the
bibliography closes at line 369, `\appendix` opens at line 371, and the table is declared
at line 382. It is not a mistake of ordering but of float placement, `[t]` sending the
table to the top of a page LaTeX found convenient, and the page it found convenient was a
page of references. **Nothing in the package could see it**: the suite reads `paper.tex`,
where the order is right, and a reader of the source would never notice. Only the compiled
artifact shows it.

**Date found.** 2026-08-03.

**Figures affected.** None. A float in the wrong place moves no number: the suite reported
the same figures before and after the fix.

**Status.** APPLIED. Version 3, deposited 2026-08-03, DOI
`10.5281/zenodo.21776041`.
Present in versions 1 and 2, which is where it exists.

**Corrected in the manuscript for version 3** with a `\clearpage` before `\appendix`, and measured in the compiled PDF rather than in the
source: the bibliography now ends on page 14 and Table A1 prints on page 15, together with
the Appendix A heading. The paper gains one page, 15 to 16.

**And the gap it came through is now watched.** `section_pdf_layout` asserts that no table
caption falls on a page of the bibliography, reading the compiled PDF page by page with the
standard library. The page segmentation it relies on is an assumption about the producer,
so it was checked against an independent reader rather than trusted: sixteen text streams
against sixteen pages, and seven probes placing captions, headings and the author name on
exactly the same pages. The first of its two checks exists to fail if that assumption ever
stops holding.

---

---

# The check on this file, specified and now implemented

`verify_paper.py` enforces this file mechanically, in `section_errata`, since the commit
that carries this paragraph. The specification below is kept as written, in the present
tense it was written in, because a specification that is quietly rewritten to match its
implementation stops being able to disagree with it.

**Shape, decided before the code.** One check per property, not one per entry. Each check
iterates over the entries inside itself and reports a single verdict; when it fails, its
message names the entry that broke it. The consequence is the point of the choice: the
contribution to the suite is **fixed at nine checks** and does not grow when an entry is
added. A file that costs a check per entry teaches the author to write fewer entries,
which is the opposite of what this file is for.

The rules are separate by category, because the categories are not held to one standard:
the six required fields govern **E-** and **P-** entries only, and **C-** and **X-**
entries carry four. A single rule applied to all four categories would either fail on the
examined entries or be too weak to catch anything.

**The nine checks.**

1. every **E-** and **P-** entry carries the six required fields, by their printed labels;
2. every **C-** and **X-** entry carries its four;
3. every entry identifier uses a declared category prefix, and no identifier is used
   twice;
4. every status is drawn from the vocabulary, and is one its category admits: no **C-**
   entry may be OPEN, no **E-** or **P-** entry may be EXAMINED, NOT AN ERRATUM;
5. no entry leaves a `PENDING POINTER` or `PENDING TRANSCRIPTION` marker standing unless
   its own text says it is incomplete;
6. every `**Printed text.**` field either quotes the artifact or carries an explicit
   pending marker, never a silent blank;
7. every hash written as a sha256 is 64 hexadecimal characters, unabbreviated;
8. every entry appears exactly once in the section its category belongs to, so that an
   entry cannot be dropped, duplicated, or filed where nobody will look for it;
9. the file table in `README.md` is a complete inventory of the package, checked in both
   directions, nothing present and unlisted and nothing listed and absent.

Each of the nine walks the whole file once and names the offender: not "an entry is
missing a field" but "P-1 is missing Figures affected". A check that says only that
something is wrong sends the reader to do the work the check was written to do.

**And that property is itself proved, by mutation.** A message that names the offender is
a claim about the checker, and claims about checkers are exactly the ones that go untested
until they are needed. The proof is the same instrument the package already uses on
itself: break the file on purpose and read what comes out. Concretely, delete the
`**Figures affected.**` field from entry P-1 in a throwaway copy of `ERRATA.md`, run the
suite against that copy, and require two things of the result, not one: that check 1
fails, and that the failure message contains the string `P-1`. A checker that fails
without naming the entry passes the first requirement and fails the second, and the
mutation is what tells them apart. The same shape, on a copy that nothing in the
repository sees, as the three mutations documented in the package README. A check whose
failure mode has never been run is a check whose failure mode is unknown.

**Both mutations were run, and here is what came out.** Two properties are claimed, so two
mutations, each on a throwaway copy of the whole package:

```
  [FAIL] errata defect entries carry the six required fields
         reproduced: ['P-1 lacks Figures affected.']   paper: []
  210 checks passed, 1 failed, 211 total          exit status 1
```

```
  [FAIL] errata the README file table lists all 14 files, and no others
         reproduced: ['present and unlisted: stray-notes.txt']   paper: []
  210 checks passed, 1 failed, 211 total          exit status 1
```

The first deleted the `Figures affected` field from P-1; the second added a file the table
does not know about. Each fails, and each names what broke it, which is the second half of
the requirement and the half that would have gone untested.

**The question that was open, and how it was decided.** Should the checker verify that the
file table in `README.md` is a complete inventory, now that the table declares itself to
be one? It carried a cost the other eight did not: until this commit `verify_paper.py`
opened five files by name and never looked at its own directory, and this rule makes it
read the directory listing for the first time in its life. The decision was to include it,
and the reason is that an inventory nobody checks is a claim with no gate behind it, which
is the shape of defect this whole file exists to record. The relationship between the suite
and the package is now different, and it is different on purpose rather than by drift.

The enumeration needs a rule, and the rule is written in the package README as well as
here, because a criterion that lives only in code cannot be read by the person the list is
for. Not part of the package: entries whose name begins with a dot, and Python bytecode
caches. Everything else is, and the walk descends into subdirectories, because
`errata-evidence/` is one. It is an exclusion rule and not an inclusion rule deliberately:
an exclusion rule that meets something new lets it through, and the check then fails
loudly and names the file, while an inclusion rule would ignore it in silence. At a gate
one chooses the rule that shouts. Measured against both deposited archives, the rule is a
no-op there: it excludes nothing from either, nine files in the version 1 archive and
eleven in version 2, all of them part of the package by this criterion.

**Cost, measured.** Nine checks, taking the suite from 202 to 211, and from 211 to 212 when the repair of E-3 added one assertion of its own. The contribution is
fixed and does not grow when an entry is added to this file, which is the property the
shape was chosen for.

## The count moved, and what that invalidates

On 2026-07-31, on branch `errata`, the suite went from **202 checks to 211**: the nine of
`section_errata`, no others. On 2026-08-03 it went from **211 to 212**, one assertion, the
repair of E-3 and P-3 recorded in commit `d25149ac4dc1105918f7fadb3ae067314f184cbd`. The
repair of P-2, commit `10786bdd2e8ff40fb0271dbfa6fd50b259ef0b44`, changed a declared
value and no count. On 2026-08-03 it went from **212 to 256**, by merging the remote's
history into this branch: the remote had added a section of surface checks and a check on
the published counts, and the merged suite runs both sides. Two figures were measured that
day rather than one, and both are reported: **254 passed with 2 failed out of 256**
immediately after the merge, before the surfaces were swept, and **256 of 256** after. The
total does not change between them. What changes is whether the package agrees with itself,
and the two failures were the remote's own check saying it did not.

On the same day it went from **256 to 259**, by the manuscript changes for version 3. The
three are declarations about the manuscript rather than about the King Wen sequence: the
paper now carries the concept DOI and a named gap where its version DOI goes, and the suite
asserts both of those and the absence of the superseded version DOI. The surfaces were swept
in the same commit and the remote's check reported them until they were, twice, first at
256 against 259 and then on the mutation line alone.

From there to the deposit it moved four more times, each in the commit that caused it and
each with the surfaces swept in the same act: **259 to 267** with the bibliographic gate
and the second-order sweep, **267 to 269** with the orphan-float gate, **269 to 270** with
the assertion of the four signatures of Table 2, and **270 to 272** in this closing round,
which added the two identifier counts that the published version DOI made checkable.
**The deposited archive of version 3 carries 270**, and that number is now fixed forever,
because the archive it belongs to cannot change: it was downloaded back from the record
after publication and run, 270 of 270. The counts above this line describe a moving object
and the 270 describes a frozen one, which is the whole difference between a repository and
a deposit.

**Three mirror problems in two rounds, and the class is architectural.** Worth recording
together, because each was fixed locally and the pattern is not local. First the direction
was inverted: a text change was born in the package when the laboratory is canonical for
it. Second the comparison was wrong: two copies were compared by raw disk bytes, which
measured the checkouts and not the content, and produced an "identical" and a "different"
without the text changing once. Third the copy fell behind: the laboratory's snapshot of
this package is refreshed by hand, so every commit here leaves it stale, and nothing
notices.

Three different faults, one cause. **The same content lives in two repositories with no
mechanical link between them**, so every property that ought to follow from being one thing
has to be re-established by somebody remembering to do it. The fixes so far are all of the
same shape: declare the direction, compare by content, write a manifest and a gate. They
make the drift legible; they do not remove it, because none of them can.

The structural repair would be for the laboratory to *link* rather than copy, by submodule
or subtree or a build step that fetches the package at a pinned commit, so that the copy
cannot be edited independently and cannot silently age. **That decision is not taken here**,
and it belongs to the laboratory rather than to this log. What belongs here is the record
that three separate defects came out of one arrangement, which is the argument anyone
weighing that decision will want.

**A surface that reads a figure cannot go stale. A surface that copies one can.** This is
the general form of what P-1 records, and it is worth stating as a preference and not only
as a lesson.

The package publishes its check count in `README.md` and in `index.html`, which are copies:
they hold a number that was true when someone typed it, and the only thing standing between
them and P-1 happening again is `check_published_counts`, a gate that compares the copy
against the truth and fails when they part. The gate is necessary precisely because the
figure is copied.

The laboratory does the other thing. Its suite runs this package's `verify_paper.py` as a
subprocess, reads the count out of the output, and asserts what it actually cares about,
that nothing failed and that the passes equal the total. Measured on 2026-08-03: the count
moved from 202 to 259 in one act and **the laboratory needed no sweep at all**, because it
never held a copy to sweep. It printed the new figure by itself.

So: where a figure can be read at the moment it is needed, read it, and assert the property
that matters rather than the number. Where it has to be copied, because a human reads the
surface and no program runs there, copy it and put a gate behind it. The gate is the
second-best form and it is what this package uses on its two published surfaces; the
laboratory's consumption is the better one and is the model to prefer when the choice
exists.

**A self-referential figure is not measured once. It is iterated to a fixed point, and
the number of iterations is reported.** This is a rule and not an anecdote of one round.

A published figure is self-referential when the run that produces it also reads it. The
mutation triple in the package README is the case at hand: it records what the documented
mutation produces, and it is itself a published count, so `check_published_counts` reads
it, so a wrong value adds a failure to the very run whose failures the triple reports.
Measuring once gives a number that is only correct if it was already correct. The
procedure is to write the measured value, measure again against the tree that now contains
it, and repeat until two consecutive runs agree.

Done here: a first reading taken from a copy made before the README was corrected gave
`240 checks passed, 19 failed`, which was wrong and would have been published as measured.
The iteration then gave `241 checks passed, 18 failed, 259 total`, and a second run against
that tree reproduced it exactly. **Two iterations to reach the fixed point**, and the second
is not ceremony: it is the one that distinguishes a fixed point from a guess.

*Swept, for other figures of the same shape.* Measured across the package: the two
published-count patterns match twice in `README.md` and twice in `index.html`, all four
reading 259, and those are the figures the check reads. They are not self-referential in
the sense above, because publishing a wrong check count adds a failure without changing the
total, so one measurement settles them. The patterns also match eight times in `ERRATA.md`,
at 192, 211 and 246, and **those are deliberately not scanned**: they are quotations of what
other trees print, including P-1's quotation of a deposit's own output, and a check that
read them would fail on a sentence describing a result rather than on a result. `V3-PLAN.md`
matches none. So the mutation triple is the only figure in the package that has to be
iterated, and it is now marked as such where it is written. The count is declared in surfaces that a reader reads, and
this is exactly the shape of P-1, so it is declared here rather than left to be discovered.

Every live declaration of the count was swept in the same commit that moved it, and each
was set to the figure the run prints rather than to a figure worked out on paper:
`README.md`, the sample output of a clean run; `README.md`, the expected result of the
documented mutation (c); `index.html`, twice, in the summary line and in the description
of the package. The mutation triple was **re-measured and not recalculated**, which turned
out to matter: at the head of this branch mutation (c) reports `193 checks passed, 18
failed, 211 total`, one failure more than the seventeen Mawangdui claims. The eighteenth
is `section_errata` reporting `mutant.py`, the scratch file the documented recipe writes
into the package. The gate notices the apparatus of its own demonstration. Nothing was
wrong with either the recipe or the check, and no amount of arithmetic would have
predicted the eighteenth failure from the seventeen.

**What merging would do to the count, said in advance.** This branch descends from
`73d9a77cdc59ea1410ae815cbb484dc68eb752d1` and does not contain the two commits that
`main` gained on 2026-07-28, `d6669487b51ac141ab779891ab85db2503e08974` and
`95437d30f805be447cccabb30ea54ff983741f52`, which add 187 lines to the suite and take it
to 246 checks. If this branch is ever merged, the count will move again, to the sum of
what the two sides assert rather than to either figure alone, and the surfaces will have
to be swept in that same act exactly as they were here. It is expected, it is nobody's
defect, and it is written before the fact so that it cannot later be read as drift. The
branch is **not** rebased onto the newer `main`, and will not be: rebasing rewrites every
commit hash on it, and the line pointers and commit names already recorded in these
entries would all become false in the same instant.

**What the older figures still mean.** Every reference to 202 in this file that speaks of
a deposit, of `main`, or of the version 2 archive remains correct and is left standing:
those objects have not changed and will not change here. The deposited archives measure
192 and 202 as they always did. The figure 211 is true of this branch and of nothing else
yet, and it becomes the package's figure only if this branch is ever merged or deposited,
which is a decision that has not been taken.

**Design constraint, stated as the principle it is.** *A document that describes tokens
contains them, so every check over such a document must distinguish use from mention.*
This is not a quirk of the proposal above; it is a property of any file that talks about
its own vocabulary, and it is the standing constraint on every check that will ever be
written against this one. An implementation that scans the file flat will report defects
in the descriptions rather than in the entries, and will fail against its own
specification.

This file already contains two mentions that are not uses, and they are examples rather
than an inventory:

1. The tokens `PENDING POINTER` and `PENDING TRANSCRIPTION`, printed in items 2 and 3
   above as examples of what an entry must not carry unmarked. There is no unfilled gap
   in this file; a flat scan for those strings would say otherwise.
2. The character U+2019, printed in the E-2 entry in the sentence that names it as the
   apostrophe of the transcribed artifact. A flat scan of the prohibited or notable
   character classes counts that mention as an occurrence, and reports a property of the
   prose that the prose does not have.

The project has a precedent for this exact shape of error: a gate whose grep read the
string `fail 0` in a summary line as evidence of success. It was not reading a result; it
was reading a sentence about a result. A checker that cannot tell a mention of a token
from a use of it is not checking the thing it names, and its passes mean nothing.

**Why it is not added now.** Adding a check moves the number of checks, and that number
is cited by name outside this file: in `README.md`, in `index.html`, and in the records
of the project that quote them. Moving it in the same act that introduces the errata
file would make the two changes indistinguishable afterwards, and the first thing this
file exists to prevent is exactly that kind of drift. Entry P-1 above is that drift, in
its own package, caught between a suite that grew and surfaces that had not: the count
must move once, deliberately, with the surfaces moving in the same act.

**The number, measured rather than assumed, over four trees.** The subject set is written
out because a count without one is not a measurement:

| tree | commit | checks |
|---|---|---|
| deposit v1, 10.5281/zenodo.21609654 | `88d3d5e7295520b47c32aea2591d8f01a53d007f` | 192 |
| deposit v2, 10.5281/zenodo.21628654 | `61486e35665f0fc42212205ca05b0ead7048e0f6` | 202 |
| head of branch `errata`, before the repairs | `a6ed004b0bf5094265e2f29c00070287db351679` | 211 |
| live `main` on GitHub | `95437d30f805be447cccabb30ea54ff983741f52` | 246 |
| head of branch `errata`, from `d25149ac4dc1105918f7fadb3ae067314f184cbd` onward | 212 |
| head of branch `errata`, after merging `origin/main` into it | 256 |
| head of branch `errata`, after the manuscript changes for version 3 | 259 |

The first two are frozen and their figures are unchanged. The third and the fifth are this
branch, before and after the repairs of P-2 and E-3, which added one assertion and moved
the count by one. The fifth row names the commit the figure starts at and not the head of
the branch, deliberately: the head moves every time this file is edited, and a row that
named it would be stale before the commit that wrote it finished. Every commit from
`d25149ac4dc1105918f7fadb3ae067314f184cbd` onward measures 212, because none of them
touches the suite, up to the merge that brought the remote's history in. The sixth row is
that merge: 256 checks, which is 212 plus the remote's 246 minus the 202 the two histories
share. It is measured and not computed, and the figure was read from a run before it was
written anywhere. A count that names one commit while the head is another is the same
defect as a count without its subject set, in miniature. **The fourth is the tree this lane did not have.** Five rows is not a
problem to be tidied away: it is what the table is for, since each row is a different
object and a reader has to be able to tell which one a figure belongs to. An earlier version of this paragraph said
that the figure 246 circulated in the records of the project and belonged to no tree
measured here, which was true of the three trees then examined and false as an impression:
246 is what the live `main` prints, measured on 2026-08-03 by extracting `95437d30` into a
clean directory and running the suite there, `246 checks passed, 0 failed, 246 total`,
exit status 0. The figure was never orphaned. The set that was looked at was too small,
and it was too small because nobody had written it down. See X-6.
