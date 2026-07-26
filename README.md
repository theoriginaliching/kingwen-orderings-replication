# Replication package

**Statistical Structure of the Historical Orderings of the I Ching Hexagrams**
*Pair Rule, Family Gradient, and the Limits of Demonstrability*

This repository is the replication package for the paper. It contains the manuscript
source, the compiled PDF, and a single self-contained script that reproduces **every
numerical claim** made in the paper from first principles.

| File | What it is |
|---|---|
| `verify_paper.py` | Self-contained verification of every figure in the paper (standard library only) |
| `paper.tex` | Manuscript source (LaTeX) |
| `paper.pdf` | Compiled manuscript |
| `index.html` | Landing page for the package |
| `LICENSE` | MIT license, covering the code |
| `LICENSE-text` | CC BY 4.0, covering the paper text and figures |

## Running the verification

```bash
python3 verify_paper.py            # all checks, one line each
python3 verify_paper.py --quiet    # summary and failures only
```

Requirements: Python 3.8 or later. **No third-party packages**, no network access, no data
files. Runtime is under thirty seconds; the Monte Carlo sections dominate, and the ladder of
six conditional nulls in Appendix A is the largest of them.

The script prints `PASS` or `FAIL` for each check, showing the reproduced value beside the
value printed in the paper, and exits `0` if and only if all checks pass:

```
==================================================================
  176 checks passed, 0 failed, 176 total
==================================================================
  REPLICATION COMPLETE: every figure in the paper reproduces.
```

The only external datum is the received King Wen sequence, embedded as a literal table.
Every other ordering (Mawangdui, Jing Fang, binary, Gray) is generated algorithmically from
the construction rules documented in Section 2 of the paper, so the package verifies the
constructions as well as the statistics.

## Section-to-verification map

Every claim in the paper maps to a named check in `verify_paper.py`.

| Paper | Claim | Verified in |
|---|---|---|
| 2 | Reversal and complementation are involutions and commute (the Klein group of the pair rule) | `section_0` |
| 2 | Each of the five orderings is a permutation of `0..63`; the 32 pairs partition positions `1..64` | `section_0` |
| 2 | `8` hexagrams are reversal-invariant, occupying `4` pairs matched by complementation | `section_0` |
| 3 | Random expectation `n(n-1)/4 = 1008`, sd `86.3`, maximum `2016` | `section_3` |
| 8 | Olsvanger's coincidence: sum of `0..63` = `C(64,2)` = `2016`, both halving to `1008` | `section_3` |
| 3.1 | Inversions vs binary: King Wen `1013`, Mawangdui `1008`, Jing Fang `1008` | `section_3` |
| 3.1 | Kendall tau `-0.005`, `0.000`, `0.000`; all within `0.06` sd | `section_3` |
| 3 | Adjacent Hamming cost: Gray `63`, Jing Fang `93`, binary `120`, Mawangdui `141`, King Wen `211` | `section_3` |
| 4.1 | Pairwise inversions `759`, `909`, `872` with `z = -2.89`, `-1.15`, `-1.58` | `section_4` |
| 4.1 | Monte Carlo `p = 0.0034` (20,000 samples, fixed seed), Bonferroni `0.0102 < 0.05` | `section_4` |
| 4.2 | Pairs adjacent in Mawangdui `0/32`, sharing an octet `0/32` | `section_4` |
| 4.2 | Mean positional separation `24.4` against `(n+1)/3 = 21.7` | `section_4` |
| 4.3 | Within octets `95/224` (expectation `112`), between octets `664/1792` (expectation `896`) | `section_4` |
| 4.3 | Octet means `18.0, 26.6, 31.9, 43.0` (monotone male line), `20.0`, `39.8, 38.5, 42.2` | `section_4` |
| 4.3 | Spearman `0.619`, exact permutation `p = 0.0575` over the `8!` octet orders | `section_4` |
| 4.3 | Conditional nulls: within-octet mean `776` (sd `11`, `z = -1.51`), octet-order mean `991` (sd `131`) | `section_4` |
| 5.1 | King Wen statistics `3.349`, `-0.247`, `7` balanced groups | `section_5` |
| 5.1 | Free-shuffle percentiles `97.9`, `99.2`; pair-preserving `29.0` to `29.4`, `6.4`, `89.6` | `section_5` |
| 5.1 | Within/between-pair asymmetry invariant under the pair null (sd `0`) | `section_5` |
| 5.1 | Balanced-group expectation `2.6` (free) against `4.4` (pair-preserving) | `section_5` |
| 5.2 | Within-pair mean `3.75 = 120/32`, between-pair `2.94`; total matching cost `120` | `section_5` |
| 5.3 | Complement-only matching costs `192` against the King Wen `120` | `section_5` |
| 5.4 | `28/28` ties on "more yang first"; battery `14/28`, `16/28`, `12/28`, `7/15`, `7/15` with exact p-values | `section_5` |
| 5.4 | Nuclear criterion `8/24` decidable (4 ties), `p = 0.076`; different basins `16/28` | `section_5` |
| 5.5 | Mirror components: extremes `10/16` (`p = 0.227`), middles `9/16` (`p = 0.402`), centers `12/16` (`p = 0.038`) | `section_5` |
| 5.5 | Centers and smaller-nuclear agree `16/16` on co-decidable pairs | `section_5` |
| 5.4 | Pair index `i` addresses positions `2i` and `2i+1`, the invariant the smoothing criteria rest on | `section_5` |
| 5.6 | Battery of nine criteria, Bonferroni `0.038 x 9 = 0.35`; sample fixed at `28` pairs | `section_5` |
| 5.6 | Power floor: `22` of 28 agreements, or `14` of 16, would be needed to survive the correction | `section_5` |
| 6.1 | Walsh energy by interaction order, dominant DFT harmonic and Haar width for all five orderings | `section_6` |
| 6 | Jing Fang anti-linear: `0.0` percent first order, `74.5` percent fourth order | `section_6` |
| 6 | King Wen number signal: `77.4` percent in even orders against `47.6` percent uniform | `section_6` |
| 7 | Cycle type of the King Wen permutation `[52, 10, 2]` | `section_7` |
| 4.1, 5.1 | Seed robustness: kinship `p < 0.01` and pair-null percentiles within `3` points, with seeds `7` and `99` | `section_seeds` |
| A | Table A1: the 17 varying percentiles of the six-rung ladder (20,000 samples, seed `20260722`) | `section_appendix_a` |
| A | Table A1: the constant cells do not vary under their null | `section_appendix_a` |
| A | Rung P3: the four palindrome anchors `[0, 13, 14, 30]`; detection by value would catch `8` | `section_appendix_a` |
| A | Invariance: `7` yang-balanced blocks in every control sample of rungs P4 and P5 | `section_appendix_a` |
| A | Multiplicity of the ladder: `17` non-constant entries, correction `0.035 x 17 = 0.6` | `section_appendix_a` |
| all | The frozen figures appear verbatim in `paper.tex`; no em dashes | `section_paper` |

## Breaking the package

A verification package is worth what it catches. The three mutations below were run once
against this exact file; each is the kind of slip a careless transcription could introduce,
and each is caught. They write a throwaway copy, so nothing in the repository changes:

```bash
# (a) one flipped bit: hexagram 63 becomes 62 in position 1
sed 's/^    63, 0, 34,/    62, 0, 34,/' verify_paper.py > mutant.py && python3 mutant.py; rm mutant.py

# (b) a duplicated hexagram: 63 appears twice and 0 disappears
sed 's/^    63, 0, 34,/    63, 63, 34,/' verify_paper.py > mutant.py && python3 mutant.py; rm mutant.py

# (c) a Mawangdui family out of order: Gen and Kan swapped
sed 's/"Qian", "Gen", "Kan"/"Qian", "Kan", "Gen"/' verify_paper.py > mutant.py && python3 mutant.py; rm mutant.py
```

| Mutation | First check to fail | What happens |
|---|---|---|
| (a) one flipped bit | `0`, the King Wen ordering is a permutation of 0 to 63 | 12 of the first 43 checks fail, then the run aborts with `KeyError: 63` in Section 4 |
| (b) duplicated hexagram | `0`, the King Wen ordering is a permutation of 0 to 63 | 12 of the first 43 checks fail, then the run aborts with `KeyError: 0` |
| (c) Mawangdui family swapped | `3.1`, Mawangdui inversions vs binary | the run completes and reports `159 checks passed, 17 failed, 176 total` |

Exit status is `1` in all three cases. Note the shape of (a) and (b): a corrupted King Wen
table is no longer a permutation of the 64 values, Section 0 says so before any statistic is
computed, and the run then aborts rather than printing numbers derived from impossible data.
Mutation (c) is the subtler one, since a reordered Mawangdui family is still a valid
permutation; it is caught by the inversion counts, and its 17 failures are exactly the claims
that depend on the Mawangdui construction.

## Compiling the manuscript

```bash
tectonic paper.tex        # or: pdflatex paper.tex
```

`paper.pdf` in this repository is the compiled output of `paper.tex` and is included as a
distribution artifact. The two are kept in sync; `paper.tex` here is byte-for-byte identical
to the manuscript source in the laboratory repository, which asserts that identity as part of
its own verification suite.

## Related resources

- **Extended interactive laboratory**: https://experiments.theoriginaliching.com, and its
  repository at https://github.com/theoriginaliching/iching-experiments. It explores the same
  material in 45 experiments, each backed by its own assertions in a 61-section verification
  suite that runs as a publication gate. Its web interface is in Spanish; an English version is
  in progress. This package and the paper are in English.
- **Archived version**: DOI pending.

## Licenses

- **Code** (`verify_paper.py`, `index.html`, configuration): MIT, see `LICENSE`.
- **Paper text and figures** (`paper.tex`, `paper.pdf`): CC BY 4.0, see `LICENSE-text`.

## Citation

```bibtex
@misc{kingwen-orderings,
  title  = {Statistical Structure of the Historical Orderings of the I Ching Hexagrams:
            Pair Rule, Family Gradient, and the Limits of Demonstrability},
  author = {García Hurtado, Alexis},
  year   = {2026},
  note   = {Replication package. DOI pending}
}
```
