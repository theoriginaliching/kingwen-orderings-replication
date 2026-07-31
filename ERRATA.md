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

1. **Printed text**, verbatim, with a pointer to section, page or table.
2. **What it should say.**
3. **Evidence** that the printed text is wrong, with its own pointer.
4. **Date found.**
5. **Figures affected**, with the measurement that establishes the answer. An
   unmeasured "none" is not an answer.
6. **Status.**

---

# Open entries

## E-1. The description of the fourth rung of Appendix A

**Printed text.** Appendix A, page 14, first paragraph, fifth item of the list of
rungs:

> (P4) pairs permuted within and across the sixteen blocks of four consecutive
> positions, preserving the block partition

The item continues `; and (P5) ...` in the printed list; the span above is the
description of P4 in full.

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
   between blocks. These line numbers hold identically in the version 1 deposit, the
   version 2 deposit and the head of this branch; the file has not been renumbered in
   that region.
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

   Its counterpart in the replication package is `verify_paper.py`, lines 1077-1086,
   comment "The micro-theorem".
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

**Verification record.** This entry. Re-derived on 2026-07-31 on branch `errata` of this
package, commit `90d4455b140ad9e69fe7ff19c58aa08562a434e6`, which is the commit that
first carried the derivation and the eight witnesses. The record points at a public
object rather than at a private one. The hash arrives in the commit after the one it
names, which is the only order in which a commit can name itself.

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

`None recorded yet.`

Entries will appear here when something is checked and found correct. They are kept for
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

**Design constraint, and it is not incidental.** The text of this proposal contains
literal instances of the very tokens the check would search for: items 2 and 3 above
print `PENDING POINTER` and `PENDING TRANSCRIPTION` as examples of what must not appear
unmarked. Any implementation must therefore exclude this section, or more precisely
exclude example spans, from its own scan. An implementation that scans the whole file
will report a defect in the description of the check rather than in any entry, and will
fail against its own specification. The project has a precedent for this exact shape of
error: a gate whose grep read the string `fail 0` in a summary line as evidence of
success. A checker that cannot tell an example of a token from an occurrence of it is
not checking the thing it names.

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
