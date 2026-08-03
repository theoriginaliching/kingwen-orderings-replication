# Errata and corrections

Corrections to *Statistical Structure of the Historical Orderings of the I Ching
Hexagrams: Pair Rule, Family Gradient, and the Limits of Demonstrability*
(Zenodo, version DOI 10.5281/zenodo.21609654; concept DOI 10.5281/zenodo.21609653).

This is a living document. It is updated when a defect is found, not when a defect is
fixed.

**Where it stands, 2026-08-03.** Fourteen entries: three defects in the paper (E-1, E-2,
E-3), three in the deposited package (P-1, P-2, P-3), two clarifications for the next
version (C-1, C-2), and six things examined and found sound (X-1 to X-6). **No figure of
the paper changes in any entry**, and that is measured and not asserted: every figure
reproduces in every tree of the package: 192 of 192 in the first deposit, 202 of 202 in
the second, 246 of 246 on the live `main`, and 212 of 212 at the head of this branch,
with no failures anywhere. Two entries, P-2 and the pair E-3 and P-3, have been repaired
on this branch and remain open in the deposits, which is where they exist; each names the
commit that repairs it. The defects in the paper are defects of description whose
consequences all hold, and one missing assertion; the defects in the package are
statements it makes about itself.

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

   **A fourth tree exists and these ranges do not index it.** The live `main` of the
   repository, commit `95437d30f805be447cccabb30ea54ff983741f52`, carries a
   `verify_paper.py` of 69341 bytes, sha256
   `72abade176ab5f8826afa4dece160ab46b2641fa2fde8dbeff2d7e6b4d7a3faf`, in which the file
   has shifted: the line quoted above as 1035 is 1036 there, and the micro theorem comment
   quoted below as 1077 is 1078. The ranges are deliberately **not** re-derived for that
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

**Status.** OPEN.

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

**Status.** OPEN.

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

**Status.** OPEN. Corrected in the repository on 2026-07-28 in commit
`73d9a77cdc59ea1410ae815cbb484dc68eb752d1`; still present in the deposited archive
10.5281/zenodo.21628654, which is what a reader downloads today; closes with the next
deposit, which will carry the corrected surfaces and be named here as the version that
applied it.

**Note for a reader who has the package.** Run it. The program prints its own count, and
the count it prints is the true one.

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
under a column headed `paper:`. A clean run therefore shows

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
every `check()` call in four trees: 154 calls in the version 2 deposit, 161 in the live
`main`, 164 at the head of this branch, of which **23 carry an `ok=` override in every
tree**. Three of the 23 declare a value different from the one their tolerance tests:

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

**Status.** OPEN. Present in both deposits and in the live `main`, which is what a
reader downloads.

**Repaired on this branch**, in commit `10786bdd2e8ff40fb0271dbfa6fd50b259ef0b44`, which
changes the declared value to 0.35 and leaves the tolerance alone. The entry above
describes the deposits and is not rewritten to match the repair: a reader of a future
version who finds this entry and then reads the shipped code must be able to tell which
of the two they are looking at. Nothing in a deposit is altered by that commit, and the
correction reaches a reader only when a version carrying it is deposited.

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

**Status.** OPEN. In the deposits and in the live `main`, which are the objects this
entry is about.

**Repaired on this branch**, in commit `d25149ac4dc1105918f7fadb3ae067314f184cbd`, which
asserts the figure: the free-shuffle percentile of the lag-1 statistic, band 0.6, the
width its two neighbours use, because the printed 4.0 comes from the other implementation
and this one measures 3.8. The assertion was shown able to fail before it was believed:
moving the declared value to 6.0 fails it alone, and negating the statistic it rests on
fails it along with its two relatives. The entry above describes the deposits, where the
figure is still unasserted, and is deliberately not rewritten to match the branch.

**Cross reference.** The same defect on the package's surface is P-3, which follows. One
defect, two surfaces, one figure, one repair.

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

**Status.** OPEN. In the deposits and in the live `main`.

**Repaired on this branch** by the same commit as E-3,
`d25149ac4dc1105918f7fadb3ae067314f184cbd`. One assertion makes both sentences true.

**Cross reference.** E-3. The two entries are the same defect on two surfaces and are
kept apart only because the categories of this file are by surface: the paper's text is
E, the package is P. They are repaired by one assertion.


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

**Date examined.** 2026-08-03.

**Status.** NOTED, FOR THE NEXT VERSION.

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

Entries appear here when something is checked and found correct. They are kept for
the same reason the entries above are kept: a list that records only its hits does not
let a later reader tell what was looked at from what was never looked at.

---

# Applied

`None yet.` The first deposit carrying corrections will list the entries it applies and
the version DOI it creates.

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
value and no count. The count is declared in surfaces that a reader reads, and
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
| head of branch `errata`, after the two repairs | `d25149ac4dc1105918f7fadb3ae067314f184cbd` | 212 |

The first two are frozen and their figures are unchanged. The third and the fifth are this
branch, before and after the repairs of P-2 and E-3, which added one assertion and moved
the count by one. **The fourth is the tree this lane did not have.** Five rows is not a
problem to be tidied away: it is what the table is for, since each row is a different
object and a reader has to be able to tell which one a figure belongs to. An earlier version of this paragraph said
that the figure 246 circulated in the records of the project and belonged to no tree
measured here, which was true of the three trees then examined and false as an impression:
246 is what the live `main` prints, measured on 2026-08-03 by extracting `95437d30` into a
clean directory and running the suite there, `246 checks passed, 0 failed, 246 total`,
exit status 0. The figure was never orphaned. The set that was looked at was too small,
and it was too small because nobody had written it down. See X-6.
