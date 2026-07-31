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

Every entry carries all six. An entry missing one is incomplete and says so.

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
   `PENDING POINTER: file and function in the replication package.`
2. The micro theorem printed in the same appendix states that quartets preserve the
   yang sum and that seven blocks sum to twelve. Under the literal reading of the
   printed description, a pair could leave its block, block sums would not be preserved,
   the count of blocks summing to twelve would not be invariant, and the reported
   constant value at P4 and P5 would not follow. Under that reading the printed theorem
   is false. `PENDING POINTER: theorem location in Appendix A.`
3. The theorem and the code agree with each other. The dissenting witness is the prose.

**Date found.** 2026-07-31, during the formal verification carried out for the
follow up paper on the generalised null ladder.

**Figures affected.** None.
Measurement: the seven constant cells of the frozen table were re-derived from the
inheritance property and all seven hold, with none refuted. Full re-execution of
`verify_paper.py` against the deposited version: `PENDING`.

**Status.** OPEN.

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
in both directions. `PENDING POINTER: verification record and commit.`

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
