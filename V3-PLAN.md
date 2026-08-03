# Plan for version 3

Written 2026-08-03 on branch `errata`. **Nothing here has been executed.** The plan exists
so that the first irreversible step can be looked at before it happens rather than
explained afterwards.

The steps are in order. Each carries what it needs before it can start, what it produces,
what can go wrong, and how the result is checked. Where a step has a cheap way to be
rehearsed without consequence, that is written down too, because the whole point of a plan
for an irreversible act is to find the reversible version of it first.

## State this plan starts from

| object | value |
|---|---|
| branch `errata` | descends from `73d9a77cdc59ea1410ae815cbb484dc68eb752d1`, 212 checks |
| local `main` | `73d9a77cdc59ea1410ae815cbb484dc68eb752d1`, 30 commits |
| `origin/main` | `95437d30f805be447cccabb30ea54ff983741f52`, 32 commits, 246 checks |
| deposits | v1 `10.5281/zenodo.21609654` (192 checks), v2 `10.5281/zenodo.21628654` (202) |
| tags | `zenodo-v1` on `88d3d5e7`, `zenodo-v2` on `61486e35` |

The branch and `origin/main` have diverged: two commits on the remote, `d6669487` and
`95437d30`, both of 2026-07-28, which rewrote parts of the suite and added 187 lines.
They are not in this branch, and this branch's work is not in them.

---

## (a) Merge `origin/main` into `errata`

**Merge, and not rebase.** This is not a preference. Rebasing rewrites every commit hash
on the branch, and this file, `ERRATA.md`, names commits and line numbers by hash: the
repair commits `10786bd` and `d25149a`, the derivation commit `90d4455`, the count table's
five rows, the tags on `88d3d5e7` and `61486e35`. A rebase would make every one of those
pointers false in the same instant, silently, and the entries would then describe objects
that no longer exist. A merge leaves them all valid.

**Needs.** A clean working tree; the fetch already done; a note of the current count, 212,
and of the remote's, 246, so the merged figure can be compared against both.

**What it produces.** A merge commit on `errata` containing both histories, and a suite
whose size is not the sum of the two figures and cannot be predicted from them: the two
sides both edit `verify_paper.py`, and 212 plus 246 is not the answer to anything.

**What can go wrong.**

1. **Conflicts in `verify_paper.py`.** Both sides changed it. The remote's `d6669487`
   rewrote how frozen figures and surfaces are checked, by location rather than by
   presence; this branch added `section_errata` and two repairs. A careless resolution can
   drop `section_errata` entirely, or drop the P-2 repair, and the suite would still pass,
   because what was dropped is a check and not a failure. **This is the dangerous failure
   mode of the whole plan: a silent subtraction that no test reports.**
2. **Conflicts in `README.md` and `index.html`**, guaranteed: both sides edited the lines
   that print the check count, and both sides edited the surrounding prose.
3. **The inventory check may fail after the merge**, if the remote added a file the file
   table does not list. Measured: the remote's two commits touch only `README.md`,
   `index.html` and `verify_paper.py`, so no new file is expected, but the check will say
   so either way and its message names the file.
4. **`ERRATA.md` measurements go stale.** E-1's line pointers name ranges in
   `verify_paper.py` "at the head of this branch" as a courtesy; after the merge the file
   shifts and that column is wrong until re-measured. The deposit columns are unaffected,
   which is the reason they were written as the ones that sustain the entry.

**Rehearse it first, at no cost.** Do the merge on a throwaway branch, measure the count
and read the resolved file, then throw it away and do it for real with the answer already
known:

    git switch -c merge-trial errata
    git merge origin/main
    ... resolve, run the suite, note the count ...
    git switch errata && git branch -D merge-trial

**How the result is checked.** The suite runs; the count is recorded as measured, never
computed; `git log --oneline errata` shows both histories; and, specifically against
failure mode 1, the merged `verify_paper.py` is grepped for `section_errata`, for the nine
check labels it emits, and for the two repairs, `round(0.038 * 9, 3)` with `0.35`, and the
`free-shuffle percentile, lag-1 autocorrelation` check. A check that vanished in a merge
does not announce itself.

## (b) Re-measure everything, and sweep the surfaces in the same act

**Needs.** Step (a) merged and the suite passing.

**What it produces.** A new count, and every self-referential figure in the package moved
to it in the same commit.

**The lesson this comes from.** Entry P-1 exists because the suite grew and the surfaces
that quote its size were corrected a day later, with a deposit in between. The correction
and the count must move together or the package ships a statement about itself that is
false.

**The list to sweep**, each to the value the run prints and not to an arithmetic guess:

- `README.md`, the sample output of a clean run;
- `README.md`, the expected result of the documented mutation (c), **re-measured by
  running it**, not adjusted: it was 193/18/211, then 194/18/212, and the eighteenth
  failure is the inventory check naming `mutant.py`, which is the recipe noticing its own
  scaffolding;
- `index.html`, the summary line and the package description;
- `ERRATA.md`, the count table, which gains a row for the merged head;
- `ERRATA.md`, the header summary;
- `ERRATA.md`, E-1's line pointers, re-measured for the branch column only;
- `ERRATA.md`, the section on the count moving, which gains the new move.

**What can go wrong.** A figure that quotes the count and is not on this list. The list was
built by measurement in an earlier round, but a merge brings a file this branch has never
swept: `verify_paper.py` from the remote may itself contain a self-referential figure. Grep
the merged tree for the old counts, 211, 212 and 246, before declaring the sweep done.

## (c) The changes to the paper for v3

**Needs.** `paper.tex` here is a byte-for-byte mirror; the canonical copy lives in the
laboratory repository, whose own suite asserts that identity and asserts that the section
count printed in the manuscript equals the number of sections it executes. **Every text
change starts there and is mirrored here, never the other way round.**

**What goes in.**

1. The page pointers for the source verification: Shaughnessy (1996) p. 17 for the rule and
   pp. 28-29 for the printed figures; Nielsen (2003) p. 3, Table 2, entry BA GONG GUA.
2. What the errata corrects in the manuscript: E-1, the description of P4, which is a false
   sentence whose printed theorem two paragraphs below already says the right thing; E-2,
   the ladder described as one of increasing structure; and, if it is taken, C-2, the
   approximation that rounds 0.342 to 0.35.
3. E-3 needs no manuscript change: it was repaired by asserting the figure, not by editing
   the sentence.

**What can go wrong.** Editing `paper.tex` in this repository breaks the mirror and the
laboratory's gate fails, which is the gate working. The order is: laboratory first, gate
green there, then mirror here. Also, any change to the printed section count must be made
with the laboratory's suite in the same act, since it asserts the printed number against
itself.

**How the result is checked.** The laboratory gate passes; `paper.tex` here is
byte-identical to the canonical one; this package's suite passes; the recompiled
`paper.pdf` carries the same document metadata checks it carries now.

## (d) Build the archive, extract it into a clean directory, and run the suite there

**Needs.** Steps (a) to (c) done, everything committed.

**Why this step exists.** Because it did not exist when the current archives were built,
and P-1 is the consequence: the version 2 archive shipped a suite of 202 checks with four
surfaces declaring 192, and a single run inside the extracted archive would have caught it
in twenty seconds. This is the precondition this lane wrote for itself.

**What it produces.** An archive that has been run, not one that has been assembled.

**The procedure.** Build the zip; extract it into an empty directory; run
`python3 verify_paper.py` there; require exit status 0 and record the literal tail of the
output; then hash the archive and every file in it, and keep those hashes for step (f).

**What can go wrong.**

1. The archive carries files the file table does not list, or lists files it does not
   carry. The inventory check inside the extracted copy is exactly the check for this and
   it names the offender.
2. The archive is built from the wrong commit. Record the commit in the same act as the
   hashes.
3. The suite passes in the working copy and fails in the extracted one, which is the
   interesting case and the reason for the step: a working copy has files an archive does
   not.

## (e) Deposit as a new version of the same Zenodo record

**Needs.** Step (d) green, with the run recorded.

**What it produces.** Version 3 of the record: a new version DOI, the same concept DOI,
`10.5281/zenodo.21609653`.

**What can go wrong, and the one trap that is already known.** The manuscript prints its
own archive DOI, and at v2 that was the version DOI of v1, because the PDF was compiled
before the new version existed. Entry X-3 records that this was declared in the version
notes rather than hidden, which is the honest handling of an unavoidable ordering. Zenodo
can reserve a DOI before publication, and reserving it first and compiling the manuscript
with the reserved DOI removes the trap instead of documenting it. **Decide which of the two
before depositing, not after.**

Second risk: the version notes are part of the deposit and are where a reader learns what
changed. They should say, in the plain form v2 used, what moved and what did not: that the
paper's text changed in the places the errata names, that the replication package gained
the errata log and the checks that watch it, and which DOI the PDF prints.

Third risk, procedural: this plan does not authorise the deposit. Depositing is outward
facing and irreversible in the sense that matters, a public record with a DOI, and it
happens only on an explicit instruction that says so.

## (f) Tag `zenodo-v3` on the exact commit

**Needs.** The deposit published and its files downloadable.

**The method, which is settled and should not be improvised.** Identify the commit by hash
of the deposited artifacts, never by date. Download the deposited files, hash them, and
compare against the trees of every commit: the commit whose tree matches the deposited
archive file for file, byte for byte, is the one to tag. That is how `zenodo-v1` and
`zenodo-v2` were placed, and in the v1 case the PDF hash alone left four candidates while
the whole-tree comparison left exactly one.

The tag is annotated and carries the evidence: the DOI, the file sizes and sha256 of every
deposited file, the candidate set the PDF hash allows, the whole-tree match that fixes the
commit, and the URLs and UTC instants of the downloads, since a figure taken from the
network is a harvested figure and carries its provenance.

**What can go wrong.** The archive Zenodo serves is not byte-identical to the one built in
step (d), for instance because it was rebuilt from a branch that moved. Then the tag cannot
be placed with certainty, and the rule is the one already applied twice: **if it cannot be
identified with certainty, do not tag.** A wrong tag is worse than none, because it looks
authoritative afterwards.

## (g) The `IsReviewedBy` relation to the second paper

**Needs.** The second paper having an identifier to point at.

**What can go wrong, and it is a wording risk rather than a technical one.** `IsReviewedBy`
says, to every machine that reads the metadata, that this work was reviewed by that one.
The second paper is by the same author and comes out of the same process. This lane has
already written, in the section on the printed sources, that the audit of this repository
is not independent and that what is independent here is Shaughnessy and Nielsen. Declaring
a review relation to a work by the same author, in the record of a paper whose errata log
insists on that distinction, would undo the distinction in the one place where readers of
the record will see it.

The safer relations say the true thing without the implication: `IsSupplementedBy`, or
`IsReferencedBy`, or `IsCitedBy` once the second paper cites this one. If `IsReviewedBy` is
still wanted, the version notes should state plainly who performed the review, so that the
relation cannot be read as third party. **This one is a decision and not a step, and it
should be taken deliberately.**

---

## What this plan does not authorise

Merging to `main`. Touching Zenodo. Building a checker of the printed sources. Any of the
seven steps above, until each is asked for by name.
