# Errata and corrections

Corrections to *Statistical Structure of the Historical Orderings of the I Ching
Hexagrams: Pair Rule, Family Gradient, and the Limits of Demonstrability*
(Zenodo, version DOI 10.5281/zenodo.21609654; concept DOI 10.5281/zenodo.21609653).

This is a living document. It is updated when a defect is found, not when a defect is
fixed.

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

## Which layer the quoted text comes from

This note governs every verbatim in this file, so that it is stated once rather than
argued in each entry.

Quotations are taken from the **rendered layer of the deposited PDF**, not from the
LaTeX source that produced it. The reason is the purpose of the document: an erratum
corrects what the reader has in front of them, and what the reader has is the compiled
artifact. A reader who compares a quotation here against `paper.tex` will therefore find
differences that are not defects but the ordinary work of the typesetter. Two such
differences are present in the spans quoted below, both measured against the deposited
`paper.tex`:

1. **Cross references.** The source writes the reference to Table 2 as the macro
   `Table~\ref{tab:chan}`; the PDF renders it as `Table 2`. The quotation in E-2 carries
   the rendered form.
2. **Apostrophes.** The source writes an ASCII apostrophe, `sequence's` and `block's`;
   the PDF composes the typographic form, U+2019. The quotations here carry U+2019,
   because that is the character in the artifact.

Beyond these, the spans quoted in this file agree with the source character for
character. Where a printed span contains a ligature codepoint or a word broken by
hyphenation across a line, an entry quoting it says so; none of the spans quoted so far
contains either.

---

# Open entries

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
   `8a7085c5cd4d372843038c6a0a342626a1362f362c2b9f2db41997186ef1b957`). The three files
   differ in size and in hash; they do not differ in that region, which is why one range
   serves all three. Hashes are written unabbreviated here and everywhere in this file: a
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
| head of branch `errata` of this package | 202 | 0 | 202 |

No check fails and no figure moves. The two deposits differ in the size of the suite,
not in any reproduced figure: the suite grew between them.

**Status.** OPEN.

**Cross reference.** Recorded a second time, as `SELF D-2`, in the verification record
of the follow up paper on the generalised null ladder. One defect, two records, and
this is the pointer between them. That record is internal: its repository has no public
remote, so it cannot be cited here by URL, and nothing in this entry is transported from
it. The evidence above stands on the deposited artifact and on this package alone.

**Note for a reader who has only the paper.** The theorem, not the sentence, states what
the sampler does. A reader who follows the theorem is not misled.

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
`|P0|` = 64!, `|P1|` = 32!·2^32, `|P2|` = 15!·17!·2^32, `|P3|` = 28!·2^28,
`|P4|` = 16!·2^16·2^32, `|P5|` = 2^32, and ordering by those gives P0, P1, **P3, P2**,
P4, P5. `|P3|` is 41 times `|P2|`, so the two rungs print in the opposite order to their
size. This is consistent with their being incomparable and it is not a contradiction; it
is simply one defence the printed wording does not have.

**Evidence.** The fifteen pairwise containments between the six rungs were computed
from predicates derived from the printed definitions. Eleven strict containments, four
incomparable pairs, zero equalities. Each refutation is accompanied by an exhibited
witness, that is a concrete permutation lying in one rung and not in the other, checked
in both directions.

The derivation below is not transported from anywhere. An earlier record of the same
result exists in a repository with no public remote, which cannot be cited here, and
copying its prose would be copying a paraphrase; so the predicates were written again
from the printed definitions of P0 to P5 in the deposit, and the witnesses were
produced again.

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

**Status.** OPEN.

---

# Examined and not an erratum

Everything below was measured on 2026-07-31 inside the two deposited archives themselves,
extracted from their zip files, not in a working copy.

## X-1. The file table of the package README does not claim to be an inventory

**What was checked.** Whether the table of files in `README.md` is a complete list of
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

**Observation kept with it.** The repository does two jobs and the README describes one.
It is the replication package, and it is also the source of the deployed landing site;
the undeclared files are, with one exception, the second job's: `vercel.json`,
`robots.txt`, `sitemap.xml` and `logo-128.webp` serve the site, and `README.md` is the
file doing the describing. The shortfall is not drift in the table. It is a second office
the table was never written for. This matters for the version 1 archive too, which is
short by three: it was not clean here and later spoiled.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-2. The section-to-verification map holds what it declares

**What was checked.** The map in `README.md`, introduced by:

> Every claim in the paper maps to a named check in `verify_paper.py`.

**Measurement.** Ten section functions are named by the map. In the version 1 deposit ten
section functions exist, and every one is referenced. In the version 2 deposit eleven
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

**Cost, measured rather than characterised.** A reader who used the map as an index of
the suite would miss 7 of 202 checks in the version 2 deposit. That is the whole of the
exposure, and it is recorded because the difference between a map that was audited and a
map nobody looked at is exactly what this section exists to preserve.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-3. The single DOI constant in the version 2 archive states nothing false

**What was checked.** How the deposited suite names the archive identifier. In the
version 2 archive, `verify_paper.py` line 1160 reads:

> `doi = "10.5281/zenodo.21609654"`

one constant serving three assertions, with no separation between a version identifier
and a concept identifier.

**Measurement.** The claim the package actually makes about that string is that the
archive DOI appears in the manuscript, in both READMEs and in the BibTeX. Measured in
that tree, it does: `paper.tex`, `README.md`, `index.html` and `verify_paper.py` all
carry `10.5281/zenodo.21609654` and no other Zenodo identifier. The statement is true of
the tree that makes it.

**Why this is not an erratum.** The identifier printed is the version DOI of the first
deposit, carried by a package deposited as the second. That is a state prior to a policy,
not a false assertion: the split, in which the manuscript keeps its version DOI while the
living surfaces carry the concept DOI, arrives in commit
`9b4720999e63c5a0ba944ad261b5d6e2aac47031`, whose committer timestamp is
2026-07-27T16:52:01Z. The version 2 record was created at 2026-07-27T16:16:56Z. The
policy is 35 minutes younger than the deposit it would have changed. A deposit cannot be
faulted for not implementing a distinction that did not yet exist.

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

## X-4. What the measurement confirmed and did not correct

Kept because a record that lists only what it caught cannot be told apart from a record
that looked for little.

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

**Date examined.** 2026-07-31. **Status.** EXAMINED, NOT AN ERRATUM.

---

Entries appear here when something is checked and found correct. They are kept for
the same reason the entries above are kept: a list that records only its hits does not
let a later reader tell what was looked at from what was never looked at.

---

# Applied

`None yet.` The first deposit carrying corrections will list the entries it applies and
the version DOI it creates.

---

# A check on this file, proposed and deliberately not added yet

`verify_paper.py` could enforce this file mechanically. The proposal is written down
here so that it is not re-invented, and the reason for holding it back is written down
next to it so that the delay is not mistaken for an oversight.

**Proposed check.** For every entry under `# Open entries`:

1. all six required fields are present, by their printed labels;
2. no pointer is empty, that is, no field of an entry still reads `PENDING POINTER`
   without the entry saying in its own text that it is incomplete;
3. no verbatim is empty without a mark, that is, a `**Printed text.**` field either
   quotes the artifact or carries an explicit `PENDING TRANSCRIPTION` marker, never a
   silent blank;
4. every `sha256` written in the file is 64 hexadecimal characters;
5. every entry carries a status drawn from the vocabulary above;
6. the count of entries in the file matches the count the check reports, so that an
   entry cannot be dropped silently.

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
file exists to prevent is exactly that kind of drift.

**The number, measured rather than assumed.** Run on 2026-07-31: 202 checks, 0 failed,
at the head of this branch, and 202 likewise on the deposited tree of version 2. The
deposited tree of version 1 gives 192, which is the figure the suite had at that
deposit. At least one other figure, 246, circulates in the records of the project; it
does not belong to this package at any of the three points measured here, and the
discrepancy is recorded rather than quietly reconciled, since a number that two records
give differently is itself a finding.
