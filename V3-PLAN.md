# Plan for version 3

**This is a plan as of 2026-08-03, and a copy of it is sealed inside the deposited
archive. Its status is not read here. It is read in `ERRATA.md` and in the commit
history.**

That warning is not decoration. This file is part of the package, so it goes into the
archive, and the archive is built before the deposit exists: steps (f) and (g), reserving
the version DOI and tagging the deposited commit, happen *after* the zip is sealed. A
sealed copy therefore says that the deposit has not been made, and it will go on saying so
for as long as the archive exists, because nothing inside a frozen artifact can be
corrected later. The alternative was to mark every step done before sealing, which would
have been worse: it would have declared as finished two steps that had not yet happened.
Of the two available honesties, this file takes the dated one.

**Where each step actually stands is recorded outside this file**, in the entries and in
the git log, which are the things that can still be written to after a deposit is sealed.

Originally written 2026-08-03 on branch `errata`, when nothing here had been executed. The
plan exists so that the first irreversible step can be looked at before it happens rather
than explained afterwards.

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

**Rehearsed on 2026-08-03, in a throwaway worktree, and then destroyed.** The answers
below are measured and not predicted. The trial used a worktree rather than a branch
switch, so the real checkout was never touched:

    git worktree add <scratch>/merge-trial -b merge-trial errata
    cd <scratch>/merge-trial && git merge origin/main
    ... resolve, run, measure ...
    git worktree remove --force <scratch>/merge-trial && git branch -D merge-trial

**What the rehearsal measured.**

| question | answer |
|---|---|
| conflicts | three files, exactly the three predicted: `verify_paper.py`, `README.md`, `index.html` |
| checks after the merge | **256**, which is 212 plus 246 minus the 202 they share |
| `section_errata` | present, called, and emitting all nine of its checks |
| the P-2 repair | alive, by its effect: the run prints `reproduced: 0.342   paper: 0.35` |
| the E-3 repair | alive, by its effect: `reproduced: 3.8   paper: 4.0`, and still able to fail, since moving the declared value to 6.0 fails it alone on the merged tree |
| documented mutation (c) | **238 passed, 18 failed, 256 total**, re-measured and not computed |
| `ok=` overrides | 24 on the merged tree, unchanged from this branch: the remote added checks, none of them with an override |
| banned dash characters | zero in the merged tree |

**What the rehearsal found that this plan did not anticipate**, and it is the most useful
thing it produced.

1. **The remote has already mechanised P-1.** Its two commits add `section_surfaces()` and
   `check_published_counts()`, and the second asserts that every check count published in
   `README.md` and `index.html` is the number the script actually runs. That is precisely
   the defect P-1 records, turned into a gate. **The consequence for the merge is
   excellent: immediately after it, the suite fails until the surfaces are swept.** The
   merge cannot be left half done and green. The two failures the trial saw were exactly
   that, `reproduced: [212, 246]   paper: [256]`, and they disappeared when the surfaces
   were set to the measured figure.
2. **"Keep both sides" is the right resolution everywhere except the count lines.** For
   `verify_paper.py` it is right and the order that falls out is the required one, with
   `section_errata()` before `section_surfaces()` and `check_published_counts()` last,
   because that one counts the assertions it is about to add. For the README's map table
   it is right: the branch's row and the remote's three rows are all true. For the count
   lines it is wrong and produced a README declaring two different totals at once, which
   the remote's own check then reported. Resolve those to a single line and set it to the
   measured number.
3. **P-1 itself needs a line after the merge**: the class it records is enforced on the
   merged tree, and the entry should say so, still describing the deposits, in the same
   shape as the repair lines of P-2 and E-3.
4. **The README's account of a non-zero exit becomes incomplete.** It now explains two
   meanings, a claim of the paper failing and a directory that does not match the file
   table. After the merge there is a third: a published count that no longer matches the
   suite. That sentence must gain its third case.
5. **E-1's branch column of line pointers shifts** to 1050 and 1092 on the merged tree.
   The deposit columns are untouched, which is why they were written as the ones that
   sustain the entry.

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
- `ERRATA.md`, the section on the count moving, which gains the new move;
- and the mutation triple is **iterated to a fixed point**, not measured once: it is itself
  a published count, so the run that measures it reads it. Write the measured value, measure
  again against the tree that contains it, repeat until two runs agree, and report how many
  iterations it took.

**What can go wrong.** A figure that quotes the count and is not on this list. The list was
built by measurement in an earlier round, but a merge brings a file this branch has never
swept: `verify_paper.py` from the remote may itself contain a self-referential figure. Grep
the merged tree for the old counts, 211, 212 and 246, before declaring the sweep done.

## (c) The changes to the paper for v3

**Needs.** `paper.tex` here mirrors the canonical copy in the laboratory repository, whose
own suite asserts that identity and asserts that the section count printed in the manuscript
equals the number of sections it executes. **Every text change starts there and is mirrored
here, never the other way round.**

**The first move of this step is therefore in the laboratory, not here.** Edit
`paper/paper.tex` in `iching-experiments`, run its gate, and only then copy the result into
this package. This sentence was missing when the step was first written, which said where
the canonical copy lives but not where to begin, and on 2026-08-03 the work was done in
the order the errata made convenient: the corrections were written here first and the
mirror ran backwards until the canonical copy caught up. Recorded in `ERRATA.md`.

**The rule for comparing a mirror.** *Two copies of the same file are compared by
normalised content or by git blob, never by raw bytes on disk, and the report says which of
the two was used.* The reason is measured, not theoretical: this checkout stores
`paper.tex` with LF and the laboratory checkout stores it with CRLF, so the same text
hashes differently on disk, one byte per line, 53552 against 53955 before the change and
54419 against 54822 after it. An earlier check in this lane compared raw working-tree bytes
and read "identical", then later read "different" for a change of line endings alone, while
the text was the same both times. Neither reading was informative.

Measured after the repair of 2026-08-03, and stated in the required form: **by blob**, both
sides are `526ea9881d29295498265fd2e90e587e1594abf8`; **by normalised content**, both are
`2c22fc181a9957514365f2c14214f02d07e7601f479ea8e3b09558b76068b1f0`; **by raw disk bytes**
they differ, 54419 here against 54822 there, which is the 403 line endings and nothing else.

The laboratory's own mirror gate compares **raw disk bytes**, measured by reading it:
`verificar_replicacion` in `scripts/experimentos.py` opens both files with `'rb'` and
compares. It is sound where it stands, because both of its operands live inside the same
checkout and therefore share one line-ending convention, but the comparison it makes is of
the checkout rather than of the content, and it would give a false verdict the day those
two files were ever checked out under different settings. That is a defect of that
repository to fix in that repository, and it was left alone here.

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

## (d) Merge `errata` into `main`

**This step was missing from the first draft of this plan, and its absence was a defect.**
The plan merged `origin/main` into `errata` and then deposited from `errata`, and never
said when `errata` returns to `main`. Left that way, a reader arriving at GitHub sees the
default branch without the errata while Zenodo serves a version 3 that contains it: two
truths, decided by which door you came through. The whole point of the log is that there
is one record of what is known.

**The prohibition is lifted, and the lifting is declared rather than assumed.** Every round
of this work carried the instruction not to merge into `main`. That rule had a reason: while
the errata was being written, `main` was the frozen thing the entries described, and a merge
would have moved the object under the description. **That reason has now expired.** The
entries name the deposits, by DOI and by commit hash and by file hash, and the deposits are
frozen whatever `main` does. The rule protected the description while it was being written;
the description is written; the rule is retired here, in the open, so that it is not
quietly ignored later.

**Needs.** Steps (a) to (c) done: `origin/main` merged into `errata`, the surfaces swept,
the count re-measured, the paper's v3 changes mirrored, and the suite green.

**What it produces.** A `main` that contains everything: the remote's checks, this
branch's errata log, its two repairs, `section_errata`, and the plan. From here on there
is one line of history and the branch has done its job.

**Order matters and it is why this step sits here.** It goes **before** the archive is
built, so that the archive is built from `main` and the tag `zenodo-v3` lands on `main`.
An archive built from a side branch would deposit a tree that the default branch does not
show, which is the same two-truths problem one layer down.

**What can go wrong.** Little, if (a) to (c) really are done: the merge is a fast forward
or close to it, since `errata` already contains `origin/main`. The risk is doing it before
the sweep, which would put a `main` on public view whose surfaces contradict its own suite,
and the remote's `check_published_counts` would fail on the default branch. Run the suite
on `main` after the merge, before pushing, and confirm the same count.

**Done on 2026-08-03, and one thing about the rehearsal is worth stating plainly.** The
throwaway worktree was created from the *local* `main`, which was still
`73d9a77cdc59ea1410ae815cbb484dc68eb752d1`, so the "202 checks before" it measured is the
old base and the merge it rehearsed is not the operation that was then applied: the applied
operation was a fast forward from `95437d30f805be447cccabb30ea54ff983741f52` to
`a3d8dea53693173145cc14213d4ed3634681c543`. Nothing is invalidated by that, and the reason
is worth keeping: **a fast forward resolves nothing and therefore cannot drop a check.** It
moves a pointer to a commit that already exists and has already been measured. The
rehearsal was insurance against a resolution that never had to happen. What needed
correcting was the report, which read as though the rehearsal had validated the applied
operation.

**Then step (d) required one more thing, which the plan had not foreseen.** The laboratory
carries its own snapshot of this package under `replication/`, and it was stale by the
whole errata. Re-synchronised mechanically from `a3d8dea` on the same day: five files
entering, four changing, none leaving, five unchanged. **The direction matters and the two
directions live in the same repository.** For `paper.tex` the laboratory is canonical and
the package is the mirror, which is why the inversion recorded in `ERRATA.md` was an
inversion. For `replication/` the package is canonical and the laboratory holds the mirror,
so package to laboratory is the correct direction and not a second inversion. Confusing the
two would be easy and would be wrong.

## (e) Build the archive from `main`, extract it into a clean directory, and run the suite there

**Needs.** Steps (a) to (d) done, everything committed and `main` carrying it.

**Decided, and it closes a question rather than answering it once.** *The archive is always
built from this package, on `main`, and never from the laboratory's `replication/`
snapshot.* The package is canonical for that directory and a copy cannot be the origin of a
deposit. The rule matters because the snapshot drifts: it is refreshed by hand, so any
commit here leaves it stale until someone re-synchronises it, and if the archive could come
from either side then "which of the two" would have to be decided correctly every single
time. With the rule, the drift cannot reach the archive at all.

**Why this step exists.** Because it did not exist when the current archives were built,
and P-1 is the consequence: the version 2 archive shipped a suite of 202 checks with four
surfaces declaring 192, and a single run inside the extracted archive would have caught it
in twenty seconds. This is the precondition this lane wrote for itself.

**What it produces.** An archive that has been run, not one that has been assembled.

**The procedure.** Build the zip; extract it into an empty directory; run
`python3 verify_paper.py` there; require exit status 0 and record the literal tail of the
output; then hash the archive and every file in it, and keep those hashes for step (f).

**Build it with the line endings turned off, and this was measured the hard way.** A first
archive built on 2026-08-03 with a plain `git archive` on this machine came out with CRLF
in all twelve text files, because the command applies the checkout's conversion. By content
it was exactly the tree it claimed to be; by raw bytes every text file differed from the
blob. That would have broken the one method this project uses to place a deposit tag: for
`zenodo-v1` and `zenodo-v2` the commit was identified by hashing every file of the
deposited archive against every commit tree, and a CRLF archive matches no tree at all. The
deposited archives of v1 and v2 are LF, because GitHub generates them from the blobs
without conversion. So the archive must be built the same way:

    git -c core.autocrlf=false -c core.eol=lf archive --format=zip         --prefix=kingwen-orderings-replication-main/ -o <name>.zip main

Rebuilt that way it is byte for byte the tree of its commit, which is the property step (g)
depends on. **Verify that property before depositing, not after**: hash every file in the
archive against the commit tree and require an exact match.

**One figure cannot live in the archive: the archive's own hash.** Recording it inside the
package would change the package, which would change the archive, which would change the
hash. It belongs in the annotated tag of step (g), which is written after the archive
exists and lives outside the tree it describes. Same shape as the mutation triple, with no
fixed point available.

**What can go wrong.**

1. The archive carries files the file table does not list, or lists files it does not
   carry. The inventory check inside the extracted copy is exactly the check for this and
   it names the offender.
2. The archive is built from the wrong commit. Record the commit in the same act as the
   hashes.
3. The suite passes in the working copy and fails in the extracted one, which is the
   interesting case and the reason for the step: a working copy has files an archive does
   not.

## (f) Reserve the version DOI, then deposit as a new version of the same record

**Needs.** Step (d) green, with the run recorded.

**What it produces.** Version 3 of the record: a new version DOI, the same concept DOI,
`10.5281/zenodo.21609653`.

**The DOI the manuscript prints: print both, and the trap disappears.** At v2 the
manuscript printed the version DOI of v1, because a PDF is compiled before the version it
will become exists. Entry X-3 records that this was declared in the version notes rather
than hidden, which is the honest handling of an unavoidable ordering, but it is still a
sentence that has to be revisited at every deposit.

The manuscript should print **both** identifiers, which removes the ordering problem
instead of documenting it:

- the **concept DOI**, `10.5281/zenodo.21609653`, which always resolves to the latest
  version and is known in advance, so it depends on nothing that does not yet exist.
  Measured rather than assumed, from the record's own metadata: requested at
  `https://zenodo.org/api/records/21628654` on 2026-08-03T10:42:46Z, the field
  `conceptdoi` reads `10.5281/zenodo.21609653` and `conceptrecid` reads `21609653`;
- the **version DOI**, reserved at Zenodo before depositing, so that the paper can say
  which exact version each figure was checked against.

With both printed, no future version forces that sentence to be touched again: the concept
DOI keeps pointing at the newest deposit, and the version DOI keeps pointing at the one
the numbers were measured on.

Second risk: the version notes are part of the deposit and are where a reader learns what
changed. They should say, in the plain form v2 used, what moved and what did not: that the
paper's text changed in the places the errata names, that the replication package gained
the errata log and the checks that watch it, and which DOI the PDF prints.

Third risk, procedural: this plan does not authorise the deposit. Depositing is outward
facing and irreversible in the sense that matters, a public record with a DOI, and it
happens only on an explicit instruction that says so.

## (g) Tag `zenodo-v3` on the exact commit of `main`

**Needs.** The deposit published and its files downloadable. The tag goes on the commit
of `main`, which after step (d) is the commit the archive was built from.

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

## (h) The relation to the second paper: `IsCitedBy`

**Decided.** The relation is **`IsCitedBy`**, the exact reciprocal of the `Cites` the
second paper already declares. Both records then state one fact, from their two ends, and
claim nothing else.

**`IsReviewedBy` is discarded, and the reason is worth keeping.** It was proposed to
declare the asymmetry between the two works. But "review" connotes independent review;
the author of both is the same; and `ERRATA.md` insists, in the section that opens the
document, that what is independent here is Shaughnessy and Nielsen and that the audit of
this repository is not. A metadata field saying otherwise would contradict the document in
the one place a reader looks before opening anything.

**Where the substantive relation lives.** Not in a metadata field. It lives in `ERRATA.md`,
where each entry states its own evidence, names the follow up work as where a discrepancy
was found rather than as what establishes it, and where the reader can check the claim
instead of taking the record's word for it. A relation type is a label with no evidence
attached, and labels are exactly what this file exists to distrust.

**Needs.** The second paper having a registered identifier to point at.

**What can still go wrong.** Declaring `IsCitedBy` before the second paper is published
points at nothing; the relation waits until that identifier exists.

---

## The order of what is left, step by step, so that nothing is compiled twice

Written on 2026-08-03, when `paper.pdf` was measured and found to be the **uncorrected**
text: it is still the file deposited as version 2, and it carries the old description of
P4, the old wording of the ladder, and the superseded version DOI. The manuscript beside it
is the corrected one. Nothing in the package could see that until `section_pdf_text` was
added, because the suite reads `paper.tex` and the laboratory only checks that the PDF is
committed, is a PDF and is not empty.

The compile happens **once**, and it happens after the DOI, because the DOI is printed in
the text. In order:

1. **The author reserves the version DOI at Zenodo**, through New version and Reserve DOI,
   publishing nothing. This is manual and outside this repository.
2. **That DOI replaces the named gap** `PENDING VERSION DOI` in `paper.tex` here, and the
   same change is mirrored into the laboratory's canonical copy, laboratory first if the
   rule of step (c) is followed.
3. **`paper.pdf` is compiled once**, from the final `paper.tex`.
4. **`section_pdf_text` is run**, and must pass: it is the assertion that the compiled
   artifact is the manuscript beside it. If the compile went stale or partial, this is what
   says so.
5. **The archive is built from `main`, with the line-ending flags**, verified byte for byte
   against the tree of its commit, extracted into a clean directory, and the suite is run
   there.
6. **The author deposits**, manually.
7. **The tag `zenodo-v3` is placed on the exact commit**, annotated, with the sha256 of the
   archive in the annotation, which is where it can live.
8. **`IsCitedBy` is declared** in the record's metadata.

Two things move between now and then, and both are expected. The check count will change
when the marks of `section_pdf_text` start passing and again if anything else is added, so
the published counts are swept in the same act each time. And the archive of this round,
`e52ff4bfcb6fd63d54da4f56c32516f397e8c93a1255b10dea575a68b4959239`, built from
`cf800dc6`, **is superseded**: it was built to prove the extract-and-run precondition works,
and the archive that is deposited is built from the final commit, after step 3.

## The order, in one line

Merge `origin/main` into `errata`; sweep and re-measure; make the paper's v3 changes;
merge `errata` into `main`; build the archive from `main`; extract it into a clean
directory and run the suite there; reserve the version DOI; deposit; tag `zenodo-v3` on
`main`; declare `IsCitedBy`.

## What this plan does not authorise

Touching Zenodo. Building a checker of the printed sources. Any step above, until it is
asked for by name. Merging into `main` is now a step of this plan rather than a
prohibition, but it is still a step, and it happens when it is asked for and not before.
