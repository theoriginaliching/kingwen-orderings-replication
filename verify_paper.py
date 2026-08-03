#!/usr/bin/env python3
"""
Replication package for:

    Statistical Structure of the Historical Orderings of the I Ching Hexagrams
    Pair Rule, Family Gradient, and the Limits of Demonstrability

This script is SELF-CONTAINED: it depends only on the Python standard library and
reproduces, from first principles, every numerical claim made in the paper. Each check
prints PASS or FAIL with the reproduced value next to the value printed in the paper.
The script exits 0 if and only if every check passes.

    python3 verify_paper.py            # run all checks
    python3 verify_paper.py --quiet    # only the summary and any failures

Runtime: under thirty seconds (the Monte Carlo sections dominate).

Conventions (Section 2 of the paper). Lines are numbered 1 (bottom) to 6 (top);
yang = 1, yin = 0. A hexagram is the 6-bit integer whose most significant bit is line 1,
so Kun = 0 and Qian = 63. The only external datum is the King Wen sequence itself,
embedded below as the received order; every other ordering is generated algorithmically
from the documented construction rules.
"""

import itertools
import math
import cmath
import random
import re
import sys
from math import comb, sqrt

# ---------------------------------------------------------------------------
# Data and engine
# ---------------------------------------------------------------------------

N = 64

# The received King Wen sequence: position (0-indexed) to hexagram value.
# King Wen number k occupies position k - 1.
KING_WEN = [
    63, 0, 34, 17, 58, 23, 16, 2, 59, 55, 56, 7, 47, 61, 8, 4,
    38, 25, 48, 3, 37, 41, 1, 32, 39, 57, 33, 30, 18, 45, 14, 28,
    15, 60, 5, 40, 43, 53, 10, 20, 49, 35, 62, 31, 6, 24, 22, 26,
    46, 29, 36, 9, 11, 52, 44, 13, 27, 54, 19, 50, 51, 12, 42, 21,
]

# Trigram bit patterns, read bottom to top (yang = 1).
TRI = {
    "Qian": "111", "Dui": "110", "Li": "101", "Zhen": "100",
    "Xun": "011", "Kan": "010", "Gen": "001", "Kun": "000",
}


def line_bit(k):
    """Bit mask of line k (1 = bottom = most significant)."""
    return 1 << (6 - k)


def hexagram(lower, upper):
    """Value of the hexagram with the given lower and upper trigrams."""
    return int(TRI[lower] + TRI[upper], 2)


def popcount(x):
    return bin(x).count("1")


def hamming(a, b):
    return popcount(a ^ b)


def rotate(v):
    """180-degree rotation (fan): reverse the order of the six lines."""
    return int(format(v, "06b")[::-1], 2)


def complement(v):
    """Complement (dui): flip every line."""
    return ~v & 63


def nuclear(v):
    """Nuclear hexagram (hu gua): lines 2-3-4 below, 3-4-5 above."""
    b = format(v, "06b")
    return int(b[1:4] + b[2:5], 2)


# --- The Monte Carlo protocol (Section 2 of the paper) ---------------------
# Every random draw in this file comes from one of these seeds. They are named so that
# a reader can see at a glance which protocol a number belongs to, and so that no seed
# can be changed in one place and not in another.

SEED_PAIR_NULL = 424242       # permutation nulls of Sections 4 and 5
SEED_PERCENTILES = 20260722   # percentile protocols of Section 5
SEED_LADDER = 20260722        # the ladder of conditional nulls, Appendix A
SEED_LADDER_CONTROL = 454545  # the independent re-derivation, used for control samples
ROBUSTNESS_SEEDS = (7, 99)    # not protocol seeds: only to show the draw does not matter


# --- The five orderings (Section 2) ---------------------------------------

BINARY = list(range(N))
GRAY = [n ^ (n >> 1) for n in range(N)]

# Mawangdui: eight octets by upper trigram in the family order, each octet headed by the
# doubled hexagram, then the remaining lower trigrams in a fixed order.
MWD_UPPER = ["Qian", "Gen", "Kan", "Zhen", "Kun", "Dui", "Li", "Xun"]
MWD_LOWER = ["Qian", "Kun", "Gen", "Dui", "Kan", "Li", "Zhen", "Xun"]


def build_mawangdui():
    out = []
    for upper in MWD_UPPER:
        out.append(hexagram(upper, upper))
        for lower in MWD_LOWER:
            if lower != upper:
                out.append(hexagram(lower, upper))
    return out


# Jing Fang: the Eight Palaces in bagong order; within a palace, the pure hexagram, five
# generations flipping lines 1..5 cumulatively, the wandering soul (re-flip line 4) and
# the returning soul (restore the lower trigram).
JF_HEADS = ["Qian", "Zhen", "Kan", "Gen", "Kun", "Xun", "Li", "Dui"]
LOWER_MASK = line_bit(1) | line_bit(2) | line_bit(3)


def build_palace(head):
    pure = hexagram(head, head)
    seq, cur = [pure], pure
    for k in range(1, 6):
        cur ^= line_bit(k)
        seq.append(cur)
    wandering = seq[5] ^ line_bit(4)
    seq.append(wandering)
    returning = (wandering & ~LOWER_MASK & 63) | (pure & LOWER_MASK)
    seq.append(returning)
    return seq


def build_jing_fang():
    return [v for head in JF_HEADS for v in build_palace(head)]


MAWANGDUI = build_mawangdui()
JING_FANG = build_jing_fang()

ORDERINGS = {
    "Binary": BINARY,
    "Gray": GRAY,
    "Mawangdui": MAWANGDUI,
    "King Wen": KING_WEN,
    "Jing Fang": JING_FANG,
}

# King Wen number of each hexagram value.
KW_NUMBER = {v: i + 1 for i, v in enumerate(KING_WEN)}


# --- Statistics -----------------------------------------------------------

def inversions(seq):
    """Inversion count of a sequence of distinct integers (Fenwick tree)."""
    tree = [0] * (N + 1)
    total = 0
    for x in reversed(seq):
        i = x
        while i > 0:
            total += tree[i]
            i -= i & -i
        i = x + 1
        while i <= N:
            tree[i] += 1
            i += i & -i
    return total


def inversions_between(x, y):
    """Kendall inversion count between two orderings of the same 64 objects."""
    pos = {v: i for i, v in enumerate(y)}
    return inversions([pos[v] for v in x])


def hamming_cost(seq):
    """Total adjacent Hamming cost of an ordering."""
    return sum(hamming(seq[i], seq[i + 1]) for i in range(len(seq) - 1))


EXPECTED_INV = N * (N - 1) / 4                      # 1008
SD_INV = sqrt(N * (N - 1) * (2 * N + 5) / 72)       # 86.3
MAX_INV = N * (N - 1) // 2                          # 2016


def kendall_tau(inv):
    return 1 - 4 * inv / (N * (N - 1))


def binomial_one_tailed(k, m):
    """Exact binomial p-value, one-tailed toward the observed direction."""
    if m == 0:
        return 1.0
    tail = range(k, m + 1) if 2 * k >= m else range(0, k + 1)
    return sum(comb(m, j) for j in tail) / 2 ** m


def binomial_two_sided(k, m):
    """Exact binomial p-value, two-sided by doubling the observed tail."""
    return min(1.0, 2 * binomial_one_tailed(k, m))


# --- Reporting ------------------------------------------------------------

RESULTS = []
QUIET = "--quiet" in sys.argv


def check(section, claim, reproduced, paper, ok=None, fmt=str):
    """Record one check: reproduced value against the value printed in the paper."""
    if ok is None:
        ok = reproduced == paper
    RESULTS.append(ok)
    if not QUIET or not ok:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {section:<5} {claim}")
        print(f"         reproduced: {fmt(reproduced)}   paper: {fmt(paper)}")
    return ok


def read_text(path):
    """File contents, or None when the file is not next to this script."""
    import os
    if not os.path.exists(path):
        return None
    return open(path, encoding="utf-8").read()


def close(a, b, tol):
    return abs(a - b) <= tol


def head(title):
    if not QUIET:
        print()
        print(title)
        print("-" * len(title))


# ---------------------------------------------------------------------------
# Section 0: structural invariants
# ---------------------------------------------------------------------------

def section_0():
    """Invariants that hold before any statistic is computed. If one of these fails, every
    figure below is meaningless: the encoding or an ordering has been corrupted."""
    head("Section 0: structural invariants of the encoding and the orderings")

    # Reversal (fan) is the 180-degree rotation of the figure; on this encoding it is the
    # reversal of the six lines, so rotation and reversal are the same map and are checked
    # once. With complementation they generate the Klein group of the pair rule: the third
    # non-identity element is their composition, and it is an involution too.
    check("0", "reversal is an involution on all 64 hexagrams",
          all(rotate(rotate(v)) == v for v in range(N)), True)
    check("0", "complementation is an involution on all 64 hexagrams",
          all(complement(complement(v)) == v for v in range(N)), True)
    check("0", "reversal and complementation commute; their composition is an involution",
          all(rotate(complement(v)) == complement(rotate(v))
              and rotate(complement(rotate(complement(v)))) == v for v in range(N)), True)

    orderings = [("King Wen", KING_WEN), ("Mawangdui", MAWANGDUI), ("Jing Fang", JING_FANG),
                 ("binary", BINARY), ("Gray", GRAY)]
    for name, seq in orderings:
        check("0", f"the {name} ordering is a permutation of 0 to 63 (no repeats, none missing)",
              (len(seq), sorted(seq) == list(range(N))), (N, True))

    # Eight hexagrams are invariant under reversal; in the received sequence they occupy
    # four pairs, which are therefore matched by complementation instead.
    palindromes = [v for v in range(N) if rotate(v) == v]
    check("0", "hexagrams invariant under reversal", len(palindromes), 8)
    check("0", "King Wen pairs made of two palindromes", sum(
        1 for i in range(32) if KING_WEN[2 * i] in palindromes and KING_WEN[2 * i + 1] in palindromes), 4)

    positions = sorted(pos for i in range(32) for pos in (2 * i + 1, 2 * i + 2))
    check("0", "the 32 pairs partition positions 1 to 64",
          (len(positions), len(set(positions)), positions == list(range(1, N + 1))),
          (N, N, True))
    check("0", "every pair is matched by reversal or by complementation",
          all(rotate(KING_WEN[2 * i]) == KING_WEN[2 * i + 1]
              or complement(KING_WEN[2 * i]) == KING_WEN[2 * i + 1] for i in range(32)), True)


# ---------------------------------------------------------------------------
# Section 3: distance to the binary ordering
# ---------------------------------------------------------------------------

def section_3():
    head("Section 3: distance to the binary ordering, an exact-randomness tie")

    check("3", "random expectation of inversions is n(n-1)/4", EXPECTED_INV, 1008.0)
    check("3", "standard deviation sqrt(n(n-1)(2n+5)/72)", round(SD_INV, 1), 86.3)
    check("3", "maximum inversion count", MAX_INV, 2016)

    # The coincidence behind Olsvanger's sum symmetries, noted in Related work: the sum of
    # the 64 hexagram values and the number of hexagram pairs are the same number, and both
    # halve to 1008. Nothing connects the two facts beyond the arithmetic of 64.
    check("3", "sum of the values 0 to 63 equals the number of pairs C(64,2)",
          (sum(range(N)), comb(N, 2)), (2016, 2016))
    check("3", "both halve to 1008, the random expectation of the inversion count",
          (MAX_INV // 2, int(EXPECTED_INV)), (1008, 1008))

    inv_kw = inversions_between(KING_WEN, BINARY)
    inv_mwd = inversions_between(MAWANGDUI, BINARY)
    inv_jf = inversions_between(JING_FANG, BINARY)
    check("3.1", "King Wen inversions vs binary", inv_kw, 1013)
    check("3.1", "Mawangdui inversions vs binary", inv_mwd, 1008)
    check("3.1", "Jing Fang inversions vs binary", inv_jf, 1008)

    check("3.1", "King Wen Kendall tau", round(kendall_tau(inv_kw), 3), -0.005)
    check("3.1", "Mawangdui Kendall tau exactly zero", kendall_tau(inv_mwd), 0.0)
    check("3.1", "Jing Fang Kendall tau exactly zero", kendall_tau(inv_jf), 0.0)
    worst = max(abs(i - EXPECTED_INV) / SD_INV for i in (inv_kw, inv_mwd, inv_jf))
    check("3.1", "all three within 0.06 sd of the expectation", worst < 0.06, True)

    costs = {name: hamming_cost(seq) for name, seq in ORDERINGS.items()}
    check("3", "adjacent Hamming cost, Gray (theoretical minimum)", costs["Gray"], 63)
    check("3", "adjacent Hamming cost, Jing Fang", costs["Jing Fang"], 93)
    check("3", "adjacent Hamming cost, binary", costs["Binary"], 120)
    check("3", "adjacent Hamming cost, Mawangdui", costs["Mawangdui"], 141)
    check("3", "adjacent Hamming cost, King Wen (the roughest walk)", costs["King Wen"], 211)


# ---------------------------------------------------------------------------
# Section 4: the kinship and its mechanism
# ---------------------------------------------------------------------------

def section_4():
    head("Section 4: the kinship of the two oldest orderings, and its mechanism")

    kw_mwd = inversions_between(KING_WEN, MAWANGDUI)
    kw_jf = inversions_between(KING_WEN, JING_FANG)
    mwd_jf = inversions_between(MAWANGDUI, JING_FANG)
    check("4.1", "King Wen to Mawangdui inversions", kw_mwd, 759)
    check("4.1", "King Wen to Jing Fang inversions", kw_jf, 909)
    check("4.1", "Mawangdui to Jing Fang inversions", mwd_jf, 872)

    z = lambda inv: (inv - EXPECTED_INV) / SD_INV
    check("4.1", "King Wen to Mawangdui z-score", round(z(kw_mwd), 2), -2.89)
    check("4.1", "King Wen to Jing Fang z-score", round(z(kw_jf), 2), -1.15)
    check("4.1", "Mawangdui to Jing Fang z-score", round(z(mwd_jf), 2), -1.58)

    # Monte Carlo null of uniform relative order: 20,000 samples, fixed seed.
    rng = random.Random(SEED_PAIR_NULL)
    samples = 20000
    counts = []
    for _ in range(samples):
        perm = list(range(N))
        rng.shuffle(perm)
        counts.append(inversions(perm))
    p_mc = sum(1 for c in counts if abs(c - EXPECTED_INV) >= abs(kw_mwd - EXPECTED_INV)) / samples
    check("4.1", "Monte Carlo p for King Wen to Mawangdui (20,000 samples)",
          round(p_mc, 4), 0.0034, ok=close(p_mc, 0.0034, 0.002), fmt=lambda x: f"{x:.4f}")
    check("4.1", "Bonferroni-corrected p over 3 comparisons stays below 0.05",
          round(p_mc * 3, 4), 0.0102, ok=p_mc * 3 < 0.05, fmt=lambda x: f"{x:.4f}")
    # Robustness: the most demanding family is all ten pairs among the five orderings.
    check("4.1", "Bonferroni over all 10 pairwise comparisons stays below 0.05",
          round(0.0034 * 10, 3), 0.034, ok=0.0034 * 10 < 0.05, fmt=lambda x: f"{x:.3f}")
    mc_mean = sum(counts) / samples
    mc_sd = sqrt(sum((c - mc_mean) ** 2 for c in counts) / samples)
    check("4.1", "Monte Carlo confirms the closed-form expectation and sd",
          (round(mc_mean), round(mc_sd)), (1008, 86),
          ok=close(mc_mean, EXPECTED_INV, 3) and close(mc_sd, SD_INV, 2))

    # 4.2 Excluding the pair mechanism.
    pairs = [(KING_WEN[2 * i], KING_WEN[2 * i + 1]) for i in range(32)]
    pos_mwd = {v: i for i, v in enumerate(MAWANGDUI)}
    adjacent = sum(1 for a, b in pairs if abs(pos_mwd[a] - pos_mwd[b]) == 1)
    same_octet = sum(1 for a, b in pairs if pos_mwd[a] // 8 == pos_mwd[b] // 8)
    separation = sum(abs(pos_mwd[a] - pos_mwd[b]) for a, b in pairs) / 32
    check("4.2", "King Wen pairs adjacent in Mawangdui", adjacent, 0)
    check("4.2", "King Wen pairs sharing a Mawangdui octet", same_octet, 0)
    check("4.2", "mean positional separation of pair partners", round(separation, 1), 24.4)
    check("4.2", "random expectation (n+1)/3", round((N + 1) / 3, 1), 21.7)

    # 4.3 The family gradient.
    pos_kw = {v: i for i, v in enumerate(KING_WEN)}
    octet_of = lambda v: pos_mwd[v] // 8
    within_disc = within_total = between_disc = between_total = 0
    for a in range(N):
        for b in range(a + 1, N):
            discordant = (pos_kw[a] - pos_kw[b]) * (pos_mwd[a] - pos_mwd[b]) < 0
            if octet_of(a) == octet_of(b):
                within_total += 1
                within_disc += discordant
            else:
                between_total += 1
                between_disc += discordant
    check("4.3", "hexagram pairs within a common octet", within_total, 224)
    check("4.3", "discordant pairs within octets", within_disc, 95)
    check("4.3", "expectation within octets", within_total // 2, 112)
    check("4.3", "hexagram pairs spanning two octets", between_total, 1792)
    check("4.3", "discordant pairs between octets", between_disc, 664)
    check("4.3", "expectation between octets", between_total // 2, 896)
    check("4.3", "total deficit of inversions (roughly 249)",
          (within_total // 2 - within_disc) + (between_total // 2 - between_disc), 249)

    means = [sum(KW_NUMBER[v] for v in MAWANGDUI[8 * b:8 * b + 8]) / 8 for b in range(8)]
    labels = ["Qian", "Gen", "Kan", "Zhen", "Kun", "Dui", "Li", "Xun"]
    printed = [18.0, 26.6, 31.9, 43.0, 20.0, 39.8, 38.5, 42.2]
    for name, got, want in zip(labels, means, printed):
        check("4.3", f"mean King Wen position of the {name} octet", round(got, 1), want)
    male = means[:4]
    check("4.3", "the male line is monotone in the family order", male == sorted(male), True)
    check("4.3", "probability of a specific monotone arrangement of four means",
          round(1 / 24, 3), 0.042)

    def spearman(xs, ys):
        def rank(values):
            order = sorted(range(len(values)), key=lambda i: values[i])
            out = [0] * len(values)
            for place, i in enumerate(order):
                out[i] = place + 1
            return out
        rx, ry = rank(xs), rank(ys)
        n = len(xs)
        d2 = sum((rx[i] - ry[i]) ** 2 for i in range(n))
        return 1 - 6 * d2 / (n * (n * n - 1))

    index = list(range(1, 9))
    rho = spearman(index, means)
    check("4.3", "Spearman correlation of octet index with mean King Wen position",
          round(rho, 3), 0.619)
    exact = sum(1 for perm in itertools.permutations(range(8))
                if spearman(index, [means[p] for p in perm]) >= rho - 1e-12)
    check("4.3", "exact permutation p over the 8! octet orders",
          round(exact / math.factorial(8), 4), 0.0575)

    octets = [MAWANGDUI[8 * b:8 * b + 8] for b in range(8)]

    rng = random.Random(SEED_PAIR_NULL)
    within_null = []
    for _ in range(samples):
        shuffled = []
        for octet in octets:
            block = octet[:]
            rng.shuffle(block)
            shuffled += block
        within_null.append(inversions_between(KING_WEN, shuffled))
    mean_w = sum(within_null) / samples
    sd_w = sqrt(sum((x - mean_w) ** 2 for x in within_null) / samples)
    check("4.3", "null shuffling within octets: mean inversions",
          round(mean_w), 776, ok=close(mean_w, 776, 3))
    check("4.3", "null shuffling within octets: sd", round(sd_w), 11, ok=close(sd_w, 11, 2))
    check("4.3", "the observed 759 sits at z = -1.51 of that null",
          round((kw_mwd - mean_w) / sd_w, 2), -1.51,
          ok=close((kw_mwd - mean_w) / sd_w, -1.51, 0.06))

    rng = random.Random(SEED_PAIR_NULL)
    order_null = []
    for _ in range(samples):
        perm = list(range(8))
        rng.shuffle(perm)
        order_null.append(inversions_between(KING_WEN, [v for b in perm for v in octets[b]]))
    mean_o = sum(order_null) / samples
    sd_o = sqrt(sum((x - mean_o) ** 2 for x in order_null) / samples)
    check("4.3", "null shuffling the octet order: mean inversions",
          round(mean_o), 991, ok=close(mean_o, 991, 5))
    check("4.3", "null shuffling the octet order: sd", round(sd_o), 131, ok=close(sd_o, 131, 15))


# ---------------------------------------------------------------------------
# Section 5: the pair structure
# ---------------------------------------------------------------------------

def rotation_pairs():
    """The 28 non-palindromic (rotation) pairs and the 4 palindromic ones."""
    pairs = [(KING_WEN[2 * i], KING_WEN[2 * i + 1], i) for i in range(32)]
    rot = [(a, b, i) for a, b, i in pairs if rotate(a) == b]
    pal = [(a, b, i) for a, b, i in pairs if rotate(a) != b]
    return pairs, rot, pal


def section_5():
    head("Section 5: the pair structure, conditional re-analysis and the limits")

    pairs, rot, pal = rotation_pairs()
    check("5", "rotation pairs in the King Wen sequence", len(rot), 28)
    check("5", "palindromic pairs (joined by complement)", len(pal), 4)
    check("5", "palindromic pairs sit at Hamming distance 6",
          all(hamming(a, b) == 6 for a, b, _ in pal), True)

    # --- 5.1 Chan's signatures ---
    def mean_transition(seq):
        return sum(hamming(seq[i], seq[i + 1]) for i in range(63)) / 63

    def autocorrelation(seq):
        d = [hamming(seq[i], seq[i + 1]) for i in range(63)]
        m = sum(d) / len(d)
        num = sum((d[i] - m) * (d[i + 1] - m) for i in range(len(d) - 1))
        den = sum((x - m) ** 2 for x in d)
        return num / den

    def balanced_groups(seq):
        return sum(1 for g in range(16) if sum(popcount(seq[4 * g + j]) for j in range(4)) == 12)

    def within_pair_mean(seq):
        return sum(hamming(seq[2 * k], seq[2 * k + 1]) for k in range(32)) / 32

    stats = {
        "mean transition distance": mean_transition,
        "lag-1 autocorrelation": autocorrelation,
        "yang-balanced groups of four": balanced_groups,
        "within-pair mean distance": within_pair_mean,
    }
    observed = {name: fn(KING_WEN) for name, fn in stats.items()}
    check("5.1", "mean transition distance of the King Wen sequence",
          round(observed["mean transition distance"], 3), 3.349)
    check("5.1", "lag-1 autocorrelation of transition distances",
          round(observed["lag-1 autocorrelation"], 3), -0.247)
    check("5.1", "yang-balanced groups of four", observed["yang-balanced groups of four"], 7)

    samples = 20000
    kw_pairs = [(KING_WEN[2 * i], KING_WEN[2 * i + 1]) for i in range(32)]

    def free_sample(rng):
        seq = list(range(N))
        rng.shuffle(seq)
        return seq

    def pair_sample(rng):
        blocks = kw_pairs[:]
        rng.shuffle(blocks)
        seq = []
        for a, b in blocks:
            if rng.random() < 0.5:
                a, b = b, a
            seq += [a, b]
        return seq

    def percentiles(sampler, seed=SEED_PERCENTILES):
        rng = random.Random(seed)
        draws = {name: [] for name in stats}
        for _ in range(samples):
            seq = sampler(rng)
            for name, fn in stats.items():
                draws[name].append(fn(seq))
        return {name: 100 * sum(1 for x in draws[name] if x < observed[name] - 1e-9) / samples
                for name in stats}, draws

    free_pct, _ = percentiles(free_sample)
    check("5.1", "free-shuffle percentile, mean transition distance",
          round(free_pct["mean transition distance"], 1), 97.9,
          ok=close(free_pct["mean transition distance"], 97.9, 0.6))
    check("5.1", "free-shuffle percentile, yang-balanced groups",
          round(free_pct["yang-balanced groups of four"], 1), 99.2,
          ok=close(free_pct["yang-balanced groups of four"], 99.2, 0.8))
    # The third free-shuffle percentile of Table 2. It was computed here and never
    # asserted, which made the abstract's "every numerical claim is asserted" false
    # by exactly one figure; entries E-3 and P-3 of ERRATA.md record that state.
    # The band is the width its two neighbours use, and it has to be a band: the
    # figure comes from the other implementation and its draw, not from this one.
    check("5.1", "free-shuffle percentile, lag-1 autocorrelation",
          round(free_pct["lag-1 autocorrelation"], 1), 4.0,
          ok=close(free_pct["lag-1 autocorrelation"], 4.0, 0.6))

    pair_pct, pair_draws = percentiles(pair_sample)
    # The paper documents both implementations: 29.0 and 29.4 (P(<) on a tied statistic).
    check("5.1", "pair-preserving percentile, mean transition distance (29.0 to 29.4)",
          round(pair_pct["mean transition distance"], 1), 29.4,
          ok=29.0 - 0.6 <= pair_pct["mean transition distance"] <= 29.4 + 0.6)
    check("5.1", "pair-preserving percentile, lag-1 autocorrelation (marginal)",
          round(pair_pct["lag-1 autocorrelation"], 1), 6.4,
          ok=close(pair_pct["lag-1 autocorrelation"], 6.3, 0.8))
    check("5.1", "pair-preserving percentile, yang-balanced groups",
          round(pair_pct["yang-balanced groups of four"], 1), 89.6,
          ok=close(pair_pct["yang-balanced groups of four"], 89.7, 0.8))
    spread = max(pair_draws["within-pair mean distance"]) - min(pair_draws["within-pair mean distance"])
    check("5.1", "within/between-pair asymmetry is invariant under the pair null (sd 0)",
          spread, 0.0)

    # Expectation of balanced groups under both nulls (2.6 free, 4.4 pair-preserving).
    rng = random.Random(SEED_PERCENTILES)
    free_groups = [balanced_groups(free_sample(rng)) for _ in range(samples)]
    rng = random.Random(SEED_PERCENTILES)
    pair_groups = [balanced_groups(pair_sample(rng)) for _ in range(samples)]
    check("5.1", "expected balanced groups under the free null",
          round(sum(free_groups) / samples, 1), 2.6,
          ok=close(sum(free_groups) / samples, 2.6, 0.15))
    check("5.1", "expected balanced groups under the pair-preserving null",
          round(sum(pair_groups) / samples, 1), 4.4,
          ok=close(sum(pair_groups) / samples, 4.4, 0.15))

    # --- 5.2 The correction ---
    total_within = sum(hamming(a, b) for a, b in kw_pairs)
    between = sum(hamming(KING_WEN[2 * k + 1], KING_WEN[2 * k + 2]) for k in range(31)) / 31
    check("5.2", "total Hamming cost of the King Wen matching", total_within, 120)
    check("5.2", "mean within-pair Hamming distance (not 3.56)", total_within / 32, 3.75)
    check("5.2", "mean between-pair distance, agreeing with Chan", round(between, 2), 2.94)
    check("5.2", "pair partners are internally more distant", total_within / 32 > between, True)

    # --- 5.3 The matching cost floor ---
    complement_cost = sum(hamming(v, complement(v)) for v in range(N)) // 2
    check("5.3", "cost of the complement-only matching", complement_cost, 192)
    check("5.3", "the King Wen matching costs 120 against that 192", total_within, 120)

    # --- 5.4 The battery ---
    yang = lambda v, k: (v & line_bit(k)) != 0
    ties_yang = sum(1 for a, b, _ in rot if popcount(a) == popcount(b))
    check("5.4", "'more yang first' is undecidable on every rotation pair", ties_yang, 28)

    greater_value = sum(1 for a, b, _ in rot if a > b)
    bottom_yang = sum(1 for a, b, _ in rot if yang(a, 1))
    top_yang = sum(1 for a, b, _ in rot if yang(a, 6))
    check("5.4", "greater binary value first", (greater_value, 28), (14, 28))
    check("5.4", "p-value for greater binary value first",
          round(binomial_one_tailed(greater_value, 28), 3), 0.575)
    check("5.4", "bottom line yang first", (bottom_yang, 28), (16, 28))
    check("5.4", "p-value for bottom line yang first",
          round(binomial_one_tailed(bottom_yang, 28), 3), 0.286)
    check("5.4", "top line yang first", (top_yang, 28), (12, 28))
    check("5.4", "p-value for top line yang first",
          round(binomial_one_tailed(top_yang, 28), 3), 0.286)

    # The smoothing criteria read the neighbors of a pair, so they need positions, while
    # rotation_pairs() hands out pair indices. The bridge is the layout of the sequence
    # itself: pair i occupies positions 2i and 2i+1, so KING_WEN[2i] is its first member and
    # KING_WEN[2i+1] its second. That coupling used to be implicit in the arithmetic below;
    # it is now checked, because if it ever broke every neighbor read would silently address
    # the wrong hexagram and the criteria would still return plausible-looking counts.
    check("5.4", "pair index i addresses positions 2i and 2i+1 of the sequence",
          all(KING_WEN[2 * i] == a and KING_WEN[2 * i + 1] == b for a, b, i in pairs), True)

    def smoothing(outgoing):
        wins = ties = 0
        for a, b, i in rot:
            pos = 2 * i
            assert KING_WEN[pos] == a and KING_WEN[pos + 1] == b, \
                f"pair {i} is not at positions {pos} and {pos + 1}"
            if not outgoing:
                if pos == 0:
                    continue
                external = KING_WEN[pos - 1]
                d_kw, d_alt = hamming(external, a), hamming(external, b)
            else:
                if pos + 2 > 63:
                    continue
                external = KING_WEN[pos + 2]
                d_kw, d_alt = hamming(b, external), hamming(a, external)
            if d_kw == d_alt:
                ties += 1
            elif d_kw < d_alt:
                wins += 1
        return wins, ties

    win_in, tie_in = smoothing(False)
    win_out, tie_out = smoothing(True)
    check("5.4", "orientation smooths the incoming transition", (win_in, 28 - tie_in), (7, 15))
    check("5.4", "ties on the incoming transition", tie_in, 13)
    check("5.4", "p-value for incoming smoothing",
          round(binomial_one_tailed(win_in, 28 - tie_in), 3), 0.500)
    check("5.4", "orientation smooths the outgoing transition", (win_out, 27 - tie_out), (7, 15))
    check("5.4", "ties on the outgoing transition", tie_out, 12)
    check("5.4", "p-value for outgoing smoothing",
          round(binomial_one_tailed(win_out, 27 - tie_out), 3), 0.500)

    greater_nuclear = smaller_nuclear = nuclear_ties = 0
    for a, b, _ in rot:
        na, nb = nuclear(a), nuclear(b)
        if na == nb:
            nuclear_ties += 1
        elif na > nb:
            greater_nuclear += 1
        else:
            smaller_nuclear += 1
    decidable = greater_nuclear + smaller_nuclear
    check("5.4", "greater nuclear value first", (greater_nuclear, decidable), (8, 24))
    check("5.4", "toward smaller-nuclear-first", (smaller_nuclear, decidable), (16, 24))
    check("5.4", "ties on the nuclear criterion", nuclear_ties, 4)
    check("5.4", "p-value for the nuclear criterion",
          round(binomial_one_tailed(greater_nuclear, decidable), 3), 0.076)

    basins = sum(1 for a, b, _ in rot if nuclear(nuclear(a)) != nuclear(nuclear(b)))
    check("5.4", "pairs whose members fall in different nuclear basins", (basins, 28), (16, 28))

    # --- 5.5 The signal of the centers ---
    def correct(v, i, j):
        return yang(v, i) == (i % 2 == 1) and yang(v, j) == (j % 2 == 1)

    def component(i, j):
        wins, decidable, winner = 0, 0, {}
        for idx, (a, b, _) in enumerate(rot):
            if yang(a, i) == yang(a, j):
                continue
            decidable += 1
            if correct(a, i, j):
                wins += 1
                winner[idx] = 1
            else:
                winner[idx] = -1
        return wins, decidable, winner

    for (i, j), name, want, want_p in [((1, 6), "extremes", (10, 16), 0.227),
                                       ((3, 4), "middles", (9, 16), 0.402),
                                       ((2, 5), "centers", (12, 16), 0.038)]:
        wins, decidable, _ = component(i, j)
        check("5.5", f"correct-first on the {name} ({i},{j})", (wins, decidable), want)
        check("5.5", f"p-value on the {name}",
              round(binomial_one_tailed(wins, decidable), 3), want_p)

    wins_c, dec_c, center_winner = component(2, 5)
    check("5.5", "two-sided p on the centers",
          round(binomial_two_sided(wins_c, dec_c), 3), 0.077)
    agree = total = 0
    for idx, (a, b, _) in enumerate(rot):
        if idx not in center_winner:
            continue
        na, nb = nuclear(a), nuclear(b)
        if na == nb:
            continue
        total += 1
        if center_winner[idx] == (1 if na < nb else -1):
            agree += 1
    check("5.5", "centers and smaller-nuclear agree on every co-decidable pair",
          (agree, total), (16, 16))
    check("5.5", "on decidable center pairs, line 5 and line 2 always differ",
          all(yang(a, 5) != yang(a, 2) for a, b, _ in rot if yang(a, 2) != yang(a, 5)), True)

    # --- 5.6 The dual reading ---
    # The battery is exactly nine criteria: five structural, one nuclear, three mirror
    # components. A tenth candidate, more-yang-first, is excluded by theorem (28/28 ties)
    # and therefore is not part of the correction.
    bateria = ["greater binary value first", "bottom line yang first", "top line yang first",
               "smooths the incoming transition", "smooths the outgoing transition",
               "greater nuclear value first", "correct-first on (1,6)",
               "correct-first on (3,4)", "correct-first on (2,5)"]
    check("5.6", "the battery comprises nine tested criteria", len(bateria), 9)
    check("5.6", "more-yang-first is excluded by theorem, undecidable on all 28 pairs",
          sum(1 for a, b, _ in rot if popcount(a) == popcount(b)), 28)
    # The power floor: how strong a criterion would have to be to survive the correction
    # at all. These are the two thresholds quoted in Section 5.6.
    def battery_threshold(m):
        """Fewest agreements over m decidable pairs whose exact one-tailed p survives the
        nine-test Bonferroni correction."""
        return next(k for k in range(m // 2, m + 1)
                    if binomial_one_tailed(k, m) * 9 < 0.05)

    check("5.6", "agreements needed over all 28 pairs to survive the battery correction",
          battery_threshold(28), 22)
    check("5.6", "agreements needed over 16 decidable pairs to survive it",
          battery_threshold(16), 14)
    # The paper prints "0.038 x 9 ~ 0.35" and the exact product is 0.342. The
    # column on the right quotes what the paper prints; the column on the left
    # shows the exact product, not its two-place rounding, so that the reader can
    # see the approximation the paper is making instead of two numbers that look
    # like they should be equal. Entry P-2 of ERRATA.md records the previous state,
    # in which this line declared 0.34, a value the paper does not print anywhere.
    check("5.6", "Bonferroni over the nine criteria (0.038 x 9, printed as approximately 0.35)",
          round(0.038 * 9, 3), 0.35, ok=close(0.038 * 9, 0.35, 0.02))
    check("5.6", "the sample is fixed forever at 28 rotation pairs", len(rot), 28)


# ---------------------------------------------------------------------------
# Section 6: spectral portraits
# ---------------------------------------------------------------------------

def walsh_energy(signal):
    """Percent of non-DC Walsh energy by interaction order 1..6."""
    energy = [0.0] * 7
    for w in range(N):
        coeff = sum(signal[p] * (-1 if popcount(w & p) & 1 else 1) for p in range(N))
        energy[popcount(w)] += coeff * coeff
    non_dc = sum(energy) - energy[0]
    return [100 * energy[k] / non_dc for k in range(1, 7)]


def dft_dominant(signal):
    best, best_k = -1.0, 1
    for k in range(1, 33):
        mag = abs(sum(signal[p] * cmath.exp(-2j * math.pi * k * p / N) for p in range(N)))
        if mag > best:
            best, best_k = mag, k
    return best_k


def haar_rows():
    rows = []
    for p in range(6):
        width = N >> p
        half = width >> 1
        for q in range(1 << p):
            row = [0] * N
            start = q * width
            for i in range(half):
                row[start + i] = 1
            for i in range(half, width):
                row[start + i] = -1
            rows.append((width, row))
    return rows


HAAR = haar_rows()


def haar_dominant(signal):
    """Width of the single Haar wavelet of largest normalized energy."""
    best, best_width = -1.0, N
    for width, row in HAAR:
        coeff = sum(row[p] * signal[p] for p in range(N))
        energy = coeff * coeff / width
        if energy > best:
            best, best_width = energy, width
    return best_width


def section_6():
    head("Section 6: spectral portraits of the five orderings")

    printed = {
        "Binary": ([100, 0, 0, 0, 0, 0], 1, 64),
        "Gray": ([75, 25, 0, 0, 0, 0], 1, 64),
        "Mawangdui": ([20.9, 34.4, 14.1, 22.3, 7.3, 1.2], 24, 4),
        "King Wen": ([21.5, 16.8, 28.4, 25.7, 5.1, 2.5], 16, 4),
        "Jing Fang": ([0.0, 15.3, 5.3, 74.5, 3.8, 1.2], 7, 32),
    }
    for name, seq in ORDERINGS.items():
        signal = [v - 31.5 for v in seq]              # the common signal, centered
        want_walsh, want_k, want_haar = printed[name]
        got = [round(x, 1) for x in walsh_energy(signal)]
        check("6.1", f"Walsh energy by order, {name}", got, want_walsh,
              ok=all(close(g, w, 0.1) for g, w in zip(got, want_walsh)))
        check("6.1", f"dominant DFT harmonic, {name}", dft_dominant(signal), want_k)
        check("6.1", f"dominant Haar width, {name}", haar_dominant(signal), want_haar)

    jf = walsh_energy([v - 31.5 for v in JING_FANG])
    check("6", "Jing Fang is anti-linear: no first-order component", round(jf[0], 1), 0.0)
    check("6", "Jing Fang concentrates 74.5 percent in fourth-order interactions",
          round(jf[3], 1), 74.5)

    # The single-order convention, stated in Section 6 for contrast.
    kw_numbers = [KW_NUMBER[v] for v in BINARY]
    energy = [0.0] * 7
    for w in range(N):
        coeff = sum(kw_numbers[v] * (-1 if popcount(w & v) & 1 else 1) for v in range(N))
        energy[popcount(w)] += coeff * coeff
    non_dc = sum(energy) - energy[0]
    even = 100 * (energy[2] + energy[4]) / non_dc
    counts = [0] * 7
    for w in range(N):
        counts[popcount(w)] += 1
    uniform = 100 * (counts[2] + counts[4]) / (sum(counts) - counts[0])
    check("6", "King Wen number signal: even interaction orders carry 77.4 percent",
          round(even, 1), 77.4)
    check("6", "uniform expectation for orders {2,4} is 47.6 percent", round(uniform, 1), 47.6)


# ---------------------------------------------------------------------------
# Section 7: the cycle type noted in related work
# ---------------------------------------------------------------------------

def section_7():
    head("Section 7: the cycle type of the King Wen permutation")

    seen = [False] * N
    cycles = []
    for start in range(N):
        if seen[start]:
            continue
        length, cur = 0, start
        while not seen[cur]:
            seen[cur] = True
            cur = KING_WEN[cur]
            length += 1
        cycles.append(length)
    check("7", "cycle type of the King Wen permutation relative to binary order",
          sorted(cycles, reverse=True), [52, 10, 2])


# ---------------------------------------------------------------------------
# Seed robustness
# ---------------------------------------------------------------------------

# The frozen pair-null percentiles of Section 5.1, as reported. Repeating the protocol
# with other seeds must land near them, not on them: a different draw is a different
# sample, so these are bands and not point values.
PAIR_NULL_BAND = {
    "mean transition distance": 29.4,
    "lag-1 autocorrelation": 6.2,
    "yang-balanced groups of four": 89.8,
}
BAND_WIDTH = 3.0


def section_seeds():
    """The published figures use the protocol seeds of Section 2. This section repeats the
    two Monte Carlo protocols with unrelated seeds and asserts that the conclusions hold:
    the kinship stays significant and the pair-null percentiles stay in their band. The
    conclusions of the paper therefore do not depend on the draw."""
    head("Seed robustness: the conclusions do not depend on the draw")

    samples = 20000
    kw_mwd = inversions_between(KING_WEN, MAWANGDUI)
    kw_pairs = [(KING_WEN[2 * i], KING_WEN[2 * i + 1]) for i in range(32)]

    def mean_transition(seq):
        return sum(hamming(seq[i], seq[i + 1]) for i in range(63)) / 63

    def alternation(seq):
        d = [hamming(seq[i], seq[i + 1]) for i in range(63)]
        m = sum(d) / len(d)
        return (sum((d[i] - m) * (d[i + 1] - m) for i in range(len(d) - 1))
                / sum((x - m) ** 2 for x in d))

    def balanced_groups(seq):
        return sum(1 for g in range(16) if sum(popcount(seq[4 * g + j]) for j in range(4)) == 12)

    stats = {
        "mean transition distance": mean_transition,
        "lag-1 autocorrelation": alternation,
        "yang-balanced groups of four": balanced_groups,
    }
    observed = {name: fn(KING_WEN) for name, fn in stats.items()}

    def pair_sample(rng):
        blocks = kw_pairs[:]
        rng.shuffle(blocks)
        seq = []
        for a, b in blocks:
            if rng.random() < 0.5:
                a, b = b, a
            seq += [a, b]
        return seq

    for seed in ROBUSTNESS_SEEDS:
        rng = random.Random(seed)
        counts = []
        for _ in range(samples):
            perm = list(range(N))
            rng.shuffle(perm)
            counts.append(inversions(perm))
        p_mc = sum(1 for c in counts
                   if abs(c - EXPECTED_INV) >= abs(kw_mwd - EXPECTED_INV)) / samples
        check("seeds", f"kinship p stays below 0.01 with seed {seed}",
              round(p_mc, 4), "< 0.01", ok=p_mc < 0.01, fmt=str)

        rng = random.Random(seed)
        draws = {name: [] for name in stats}
        for _ in range(samples):
            seq = pair_sample(rng)
            for name, fn in stats.items():
                draws[name].append(fn(seq))
        for name in stats:
            pct = 100 * sum(1 for x in draws[name] if x < observed[name] - 1e-9) / samples
            check("seeds", f"pair-null percentile of {name} within {BAND_WIDTH:.0f} points "
                           f"of {PAIR_NULL_BAND[name]} with seed {seed}",
                  round(pct, 1), PAIR_NULL_BAND[name],
                  ok=close(pct, PAIR_NULL_BAND[name], BAND_WIDTH))


# ---------------------------------------------------------------------------
# Appendix A: robustness under a hierarchy of conditional nulls
# ---------------------------------------------------------------------------

# Table A1, frozen. None marks a cell where the statistic does not vary under that
# null: its percentile is arithmetic, not evidence, and is checked as invariance.
LADDER = {
    "P0": {"transition": 97.5, "alternation": 3.8,  "balanced": 99.2, "within": 99.9},
    "P1": {"transition": 29.4, "alternation": 6.2,  "balanced": 89.8, "within": None},
    "P2": {"transition": 31.9, "alternation": 6.5,  "balanced": 87.7, "within": None},
    "P3": {"transition": 33.2, "alternation": 10.8, "balanced": 90.4, "within": None},
    "P4": {"transition": 29.9, "alternation": 3.3,  "balanced": None, "within": None},
    "P5": {"transition": 17.6, "alternation": 3.5,  "balanced": None, "within": None},
}

LADDER_SAMPLES = 20000


def section_appendix_a():
    head("Appendix A: the ladder of conditional nulls (Table A1)")

    kw_pairs = [(KING_WEN[2 * i], KING_WEN[2 * i + 1]) for i in range(32)]

    def mean_transition(seq):
        return sum(hamming(seq[i], seq[i + 1]) for i in range(63)) / 63

    def alternation(seq):
        d = [hamming(seq[i], seq[i + 1]) for i in range(63)]
        m = sum(d) / len(d)
        num = sum((d[i] - m) * (d[i + 1] - m) for i in range(len(d) - 1))
        return num / sum((x - m) ** 2 for x in d)

    def balanced_groups(seq):
        return sum(1 for g in range(16) if sum(popcount(seq[4 * g + j]) for j in range(4)) == 12)

    def within_pair_mean(seq):
        return sum(hamming(seq[2 * k], seq[2 * k + 1]) for k in range(32)) / 32

    stats = {
        "transition": mean_transition,
        "alternation": alternation,
        "balanced": balanced_groups,
        "within": within_pair_mean,
    }
    observed = {name: fn(KING_WEN) for name, fn in stats.items()}

    # The anchors of rung P3 are the pairs whose two members are palindromic (invariant
    # under rotation) and are therefore matched by complementation. Detecting complement
    # pairs by value would catch eight, because in four rotation pairs reversal and
    # complementation coincide; nailing eight pairs moves the P3 row.
    anchors = [i for i, (a, b) in enumerate(kw_pairs) if rotate(a) == a and rotate(b) == b]
    check("A", "rung P3: the four palindrome pairs, fixed in position and orientation",
          anchors, [0, 13, 14, 30])
    check("A", "detecting complement pairs by value (a XOR b = 63) would catch eight",
          sum(1 for a, b in kw_pairs if a ^ b == 63), 8)

    def assemble(prs, flips):
        seq = []
        for (a, b), flip in zip(prs, flips):
            seq += [b, a] if flip else [a, b]
        return seq

    def sample(rung, rng):
        """One draw from the null of the given rung. The order in which the generator is
        consumed is part of the definition: it is what makes the table reproducible."""
        if rung == "P0":
            seq = list(range(N))
            rng.shuffle(seq)
            return seq
        if rung == "P1":
            prs = kw_pairs[:]
            rng.shuffle(prs)
            return assemble(prs, [rng.random() < 0.5 for _ in prs])
        if rung == "P2":
            upper, lower = kw_pairs[:15], kw_pairs[15:]
            rng.shuffle(upper)
            rng.shuffle(lower)
            prs = upper + lower
            return assemble(prs, [rng.random() < 0.5 for _ in prs])
        if rung == "P3":
            free = [p for i, p in enumerate(kw_pairs) if i not in anchors]
            rng.shuffle(free)
            prs, flips, it = [], [], iter(free)
            for i in range(32):
                if i in anchors:
                    prs.append(kw_pairs[i])
                    flips.append(False)
                else:
                    prs.append(next(it))
                    flips.append(rng.random() < 0.5)
            return assemble(prs, flips)
        if rung == "P4":
            blocks = [kw_pairs[2 * b:2 * b + 2] for b in range(16)]
            rng.shuffle(blocks)
            prs = []
            for block in blocks:
                block = block[:]
                if rng.random() < 0.5:
                    block.reverse()
                prs += block
            return assemble(prs, [rng.random() < 0.5 for _ in prs])
        if rung == "P5":
            return assemble(kw_pairs, [rng.random() < 0.5 for _ in kw_pairs])
        raise ValueError(rung)

    varying = []
    for rung, row in LADDER.items():
        rng = random.Random(SEED_LADDER)
        draws = {name: [] for name in stats}
        for _ in range(LADDER_SAMPLES):
            seq = sample(rung, rng)
            for name, fn in stats.items():
                draws[name].append(fn(seq))
        for name in stats:
            values = draws[name]
            constant = max(values) - min(values) < 1e-9
            pct = 100 * sum(1 for x in values if x < observed[name] - 1e-9) / LADDER_SAMPLES
            if row[name] is None:
                if not constant:
                    varying.append(f"{rung}/{name}")
                continue
            # Tolerance 0.051 rather than 0.05: Python rounds half to even, so a raw
            # 31.95 prints as 31.9 in the paper and must still match its own source.
            check("A", f"Table A1 percentile, {rung} / {name}",
                  round(pct, 1), row[name], ok=close(pct, row[name], 0.051))
    check("A", "the constant cells of Table A1 do not vary under their null", varying, [])

    # The multiplicity of the ladder: the residue at rung P5 is one cell among the
    # non-constant entries of the table, and the appendix reports both readings.
    cells = sum(1 for row in LADDER.values() for value in row.values() if value is not None)
    check("A", "non-constant entries of Table A1", cells, 17)
    check("A", "correction of the residue over the table (0.035 x 17 = 0.6)",
          round(0.035 * cells, 3), 0.6, ok=close(0.035 * cells, 0.6, 0.006))

    # The micro-theorem: preserving the block partition preserves each block's yang sum,
    # so the yang-balanced signature is a constant from rung P4 upward.
    blocks = [sum(popcount(KING_WEN[4 * g + j]) for j in range(4)) for g in range(16)]
    check("A", "blocks of four with yang sum 12 in the received sequence",
          sum(1 for b in blocks if b == 12), 7)
    for rung in ("P4", "P5"):
        rng = random.Random(SEED_LADDER_CONTROL)
        values = sorted({balanced_groups(sample(rung, rng)) for _ in range(200)})
        check("A", f"rung {rung}: yang-balanced groups equal 7 in every control sample",
              values, [7])


# ---------------------------------------------------------------------------
# Front matter: the paper names itself the same way everywhere
# ---------------------------------------------------------------------------

def section_front_matter():
    """The title, the subtitle and the author live in paper.tex and are repeated by hand on
    every surface that presents the paper. This section reads the canonical forms out of the
    manuscript and asserts that the package repeats them exactly, so a retyped title cannot
    drift from the one the PDF carries."""
    head("Front matter: title, subtitle and citation, against paper.tex")

    import os
    import re
    here = os.path.dirname(os.path.abspath(__file__))
    tex = read_text(os.path.join(here, "paper.tex"))
    if tex is None:
        check("front", "paper.tex is present next to this script", False, True)
        return

    # The canonical strings live once in paper.tex, as three macros, and everything else
    # (the title page, the PDF document metadata, this verifier) reads them from there.
    macros = dict(re.findall(r"\\newcommand\{\\(paper(?:title|subtitle|author))\}\{(.+?)\}\n", tex))
    for nombre in ("papertitle", "papersubtitle", "paperauthor"):
        if nombre not in macros:
            check("front", f"paper.tex defines the canonical macro {nombre}", False, True)
            return
    title = " ".join(macros["papertitle"].split())
    subtitle = " ".join(macros["papersubtitle"].split())
    author = " ".join(macros["paperauthor"].split())

    # The title page and the author line must be BUILT from those macros, never retyped:
    # that is what keeps the cover and the PDF metadata from drifting apart.
    check("front", "the title page is built from the canonical macros",
          "\\title{\\papertitle\\\\[0.35em]" in tex, True)
    check("front", "the author line is built from the canonical macro",
          "\\author{\\paperauthor\\thanks{" in tex, True)
    check("front", "canonical title, read from paper.tex",
          title, "Statistical Structure of the Historical Orderings of the I Ching Hexagrams")
    check("front", "canonical subtitle, read from paper.tex",
          subtitle, "Pair Rule, Family Gradient, and the Limits of Demonstrability")
    check("front", "canonical author, read from paper.tex",
          author, "Alexis García Hurtado")

    for name in ("README.md", "index.html"):
        surface = read_text(os.path.join(here, name))
        if surface is None:
            check("front", f"{name} is present next to this script", False, True)
            continue
        check("front", f"{name} carries the canonical title", title in surface, True)
        check("front", f"{name} carries the canonical subtitle", subtitle in surface, True)

    # The BibTeX entry is what a reader copies into their own bibliography, so its title
    # field has to match the manuscript character for character, subtitle included.
    for name in ("README.md", "index.html"):
        surface = read_text(os.path.join(here, name))
        if surface is None:
            continue
        found = re.search(r"title\s*=\s*\{(.+?)\},\n", surface)
        check("front", f"BibTeX title in {name} matches paper.tex character for character",
              found.group(1) if found else None, f"{title}: {subtitle}")

    # The social card is the form a shared link shows, and it is typed by hand like the rest.
    page = read_text(os.path.join(here, "index.html"))
    if page is not None:
        card = re.search(r'<meta property="og:title" content="([^"]+)">', page)
        check("front", "og:title on the landing carries title and subtitle",
              card.group(1) if card else None, f"{title}: {subtitle}")

    # Zenodo issues two identifiers, and they are checked apart because they mean
    # different things.
    #
    #   - the VERSION DOI names one deposit: the one this manuscript was archived with.
    #     The PDF is a frozen artefact, so it is correct that it keeps printing its own
    #     version even after later ones appear.
    #   - the CONCEPT DOI names no version: it always resolves to the latest. It is the
    #     one the living surfaces carry (this landing, the READMEs, the BibTeX entry a
    #     reader copies into their bibliography), so that following it lands on the newest.
    #
    # They are not required to agree: they differ on purpose. What is checked is the
    # string, in each surface; nothing in this file touches the network.
    doi_version = "10.5281/zenodo.21609654"
    doi_concept = "10.5281/zenodo.21609653"
    check("front", "paper.tex carries the version DOI it was archived with",
          doi_version in tex, True)
    for name in ("README.md", "index.html"):
        surface = read_text(os.path.join(here, name))
        if surface is None:
            continue
        check("front", f"{name} carries the concept DOI (all versions)",
              doi_concept in surface, True)
        check("front", f"{name} no longer announces a pending DOI",
              "DOI pending" not in surface, True)
        field = re.search(r"doi\s*=\s*\{(.+?)\}", surface)
        check("front", f"BibTeX doi field in {name} is the concept DOI",
              field.group(1) if field else None, doi_concept)


# ---------------------------------------------------------------------------
# PDF document metadata
# ---------------------------------------------------------------------------

def _pdf_string(raw):
    """One PDF string value, in either of the two forms a producer may use: a literal
    between parentheses, or hexadecimal between angle brackets. A leading BOM (FE FF)
    means the bytes are UTF-16BE, which is how an accented name survives; without it the
    bytes are PDFDocEncoding, which agrees with Latin-1 over the range we use."""
    import re
    if raw.startswith(b"<"):
        hexa = re.sub(rb"[^0-9A-Fa-f]", b"", raw[1:-1])
        if len(hexa) % 2:
            hexa += b"0"
        data = bytes.fromhex(hexa.decode("ascii"))
    else:
        body, out, i = raw[1:-1], bytearray(), 0
        while i < len(body):
            c = body[i]
            if c == 0x5C and i + 1 < len(body):
                nxt = body[i + 1]
                if 0x30 <= nxt <= 0x37:                      # octal escape
                    j, digits = i + 1, b""
                    while j < len(body) and len(digits) < 3 and 0x30 <= body[j] <= 0x37:
                        digits += body[j:j + 1]
                        j += 1
                    out.append(int(digits, 8))
                    i = j
                    continue
                out.append({0x6E: 10, 0x72: 13, 0x74: 9}.get(nxt, nxt))
                i += 2
                continue
            out.append(c)
            i += 1
        data = bytes(out)
    if data[:2] == b"\xfe\xff":
        return data[2:].decode("utf-16-be")
    return data.decode("latin-1")


def _pdf_info(data):
    """The document information dictionary of a PDF, as a plain dict of strings.

    Nothing but the standard library: the dictionary may sit in the file as it is, or
    inside a compressed object stream, which is where a modern producer puts it. Both are
    covered by looking for it in the raw bytes and in every inflatable stream. The Info
    dictionary is the one carrying /Author; the outline entries carry /Title alone."""
    import re
    import zlib
    entry = re.compile(rb"/(\w+)\s*(<[0-9A-Fa-f\s]*>|\((?:[^()\\]|\\.)*\))")
    blobs = [data]
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        try:
            blobs.append(zlib.decompress(data[start:end]))
        except Exception:
            pass
    for blob in blobs:
        i = blob.find(b"/Author")
        if i < 0:
            continue
        opening = blob.rfind(b"<<", 0, i)
        closing = blob.find(b">>", i)
        if opening < 0 or closing < 0:
            continue
        return {k.decode("ascii"): _pdf_string(v)
                for k, v in entry.findall(blob[opening:closing + 2])}
    return {}


def section_pdf_metadata():
    """The PDF a reader downloads carries its own title and author in the document
    information dictionary: that is what a repository, a reference manager and a browser
    tab read, and it is invisible in the text, so nothing else would catch it drifting.
    Here the compiled PDF is opened and its /Title and /Author are asserted against the
    canonical strings of paper.tex, the same ones the title page is built from."""
    head("PDF document metadata, against the canonical strings of paper.tex")

    import os
    import re
    here = os.path.dirname(os.path.abspath(__file__))
    tex = read_text(os.path.join(here, "paper.tex"))
    if tex is None:
        check("pdf", "paper.tex is present next to this script", False, True)
        return
    macros = dict(re.findall(r"\\newcommand\{\\(paper(?:title|subtitle|author))\}\{(.+?)\}\n", tex))
    if len(macros) != 3:
        check("pdf", "paper.tex defines the three canonical macros", sorted(macros), 3)
        return
    expected_title = f"{macros['papertitle']}: {macros['papersubtitle']}"
    expected_author = macros["paperauthor"]

    # The metadata must be BUILT from the macros too: retyping them here would be exactly
    # the drift this section exists to prevent.
    check("pdf", "pdftitle is built from the canonical macros",
          "pdftitle={\\papertitle: \\papersubtitle}" in tex, True)
    check("pdf", "pdfauthor is built from the canonical macro",
          "pdfauthor={\\paperauthor}" in tex, True)

    path = os.path.join(here, "paper.pdf")
    if not os.path.exists(path):
        check("pdf", "paper.pdf is present next to this script", False, True)
        return
    info = _pdf_info(open(path, "rb").read())
    check("pdf", "the PDF carries a document information dictionary", bool(info), True)
    check("pdf", "/Title exists in the PDF", "Title" in info, True)
    check("pdf", "/Author exists in the PDF", "Author" in info, True)
    check("pdf", "/Title of the PDF matches paper.tex", info.get("Title"), expected_title)
    check("pdf", "/Author of the PDF matches paper.tex", info.get("Author"), expected_author)


# ---------------------------------------------------------------------------
# Paper source identity
# ---------------------------------------------------------------------------

#: Every frozen figure of the paper, with the exact places it occupies in
#: paper.tex: a tuple of (line number, how many times on that line).
#:
#: WHY POSITIONS AND NOT PRESENCE. This section used to ask only whether each
#: frozen string appeared somewhere in the manuscript. A defect injection study
#: measured what that costs, and the result was a clean cut: of the frozen
#: figures that occur exactly once in paper.tex, every single edit was caught;
#: of those that occur more than once, not one was, because editing one copy
#: left the others satisfying the check. Sixteen of these twenty-nine occur more
#: than once, so more than half the manuscript's key numbers could be altered
#: without this script noticing.
#:
#: WHY LINE NUMBERS ARE SAFE HERE, AND ONLY HERE. paper.tex is an archived
#: artefact: it is what the version DOI points at, and it must not change. Its
#: line numbering is therefore as frozen as its content, and pinning positions
#: is stricter than counting occurrences because it also catches a figure that
#: MOVED. The living surfaces -- README.md and index.html -- are not pinned this
#: way; they are checked by structure in section_surfaces(), because pinning a
#: document that is meant to be edited would break on the first paragraph added.
FROZEN_FIGURES = (
    ("1013", ((51, 1), (64, 1), (89, 1), (91, 1), (106, 1))),
    ("1008", ((51, 3), (64, 3), (82, 1), (89, 3), (105, 1), (107, 1), (133, 1), (294, 3))),
    ("759", ((51, 1), (66, 1), (119, 1), (129, 1), (133, 1))),
    ("-2.89", ((51, 1), (66, 1), (119, 1))),
    ("0.0034", ((51, 1), (119, 2))),
    ("3.75", ((68, 2), (162, 1), (173, 2))),
    ("120", ((68, 1), (93, 1), (103, 1), (173, 3), (177, 1))),
    ("12/16", ((51, 1), (70, 1), (201, 1), (211, 1), (230, 1))),
    ("0.038", ((51, 1), (70, 1), (193, 1), (201, 1), (211, 2), (230, 1))),
    ("74.5", ((72, 1), (257, 1), (278, 1), (284, 1), (288, 1))),
    ("95/224", ((129, 1),)),
    ("664/1792", ((129, 1),)),
    ("776", ((133, 2),)),
    ("18.0", ((131, 1),)),
    ("26.6", ((131, 1),)),
    ("31.9", ((131, 1), (393, 1))),
    ("43.0", ((131, 1),)),
    ("0.619", ((131, 1),)),
    ("0.0575", ((131, 1),)),
    ("192", ((177, 1),)),
    ("2016", ((89, 1), (294, 2))),
    ("86.3", ((82, 1), (89, 1))),
    ("17.6", ((396, 1),)),
    ("3.5", ((68, 1), (173, 2), (396, 1), (401, 2))),
    ("33.2", ((394, 1),)),
    ("29.9", ((395, 1),)),
    ("87.7", ((393, 1),)),
    ("90.4", ((394, 1),)),
    ("constant = 7", ((395, 1), (396, 1))),
)


def _positions(text, needle):
    """Where a string sits: ((line number, occurrences on that line), ...)."""
    return tuple((number, line.count(needle))
                 for number, line in enumerate(text.splitlines(), 1)
                 if needle in line)


def section_paper():
    head("Paper source: every frozen figure is where the paper puts it")

    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper.tex")
    if not os.path.exists(path):
        check("tex", "paper.tex is present next to this script", False, True)
        return
    tex = open(path, encoding="utf-8").read()
    for value, expected in FROZEN_FIGURES:
        check("tex", f"paper.tex carries {value} at exactly the declared positions",
              _positions(tex, value), expected)
    check("tex", "paper.tex contains no em dash", tex.count(chr(0x2014)), 0)


# ---------------------------------------------------------------------------
# The errata log keeps its own declared shape
# ---------------------------------------------------------------------------
#
# Nine checks, one per property. Each walks the whole log inside itself and
# reports the entries or files that broke the property, so a failure names the
# culprit instead of announcing that something somewhere is wrong. The
# contribution to the suite is fixed at nine: it does not grow when an entry is
# added, because a log that costs a check per entry teaches its author to write
# fewer entries.
#
# The content scans read entry bodies and not the whole file. That is not an
# optimisation. ERRATA.md describes the tokens these checks look for, so a flat
# scan would read the description of a check as an instance of the thing it
# forbids, and would fail against its own specification.

ERRATA_SECTION = {
    "E": "Open entries",
    "P": "Open entries",
    "C": "Clarifications for the next version",
    "X": "Examined and not an erratum",
}
ERRATA_STATUS = {
    "E": {"OPEN", "APPLIED"},
    "P": {"OPEN", "APPLIED"},
    "C": {"NOTED, FOR THE NEXT VERSION"},
    "X": {"EXAMINED, NOT AN ERRATUM"},
}
ERRATA_DEFECT_FIELDS = ("Printed text.", "What it should say.", "Evidence.",
                        "Date found.", "Figures affected.", "Status.")
ERRATA_RECORD_FIELDS = ("What was examined.", "Measurement.", "Date examined.",
                        "Status.")
ERRATA_MARKERS = ("PENDING POINTER", "PENDING TRANSCRIPTION")


def errata_entries(text):
    """Every entry of the log: identifier, category, the part it sits under, body."""
    import re
    lines = text.split("\n")
    entries, part = [], None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            part = line[2:].strip()
        m = re.match(r"## ([EPCX])-(\d+)\.", line)
        if m:
            j = i + 1
            while j < len(lines) and not re.match(r"^#{1,2} ", lines[j]):
                j += 1
            entries.append({"id": f"{m.group(1)}-{m.group(2)}", "cat": m.group(1),
                            "part": part, "body": "\n".join(lines[i:j])})
    return entries


def errata_field(body, label):
    """The text of one labelled field, up to the next label."""
    import re
    mark = f"**{label}**"
    if mark not in body:
        return None
    rest = body[body.index(mark) + len(mark):]
    nxt = re.search(r"\*\*[A-Z][^*]*\.\*\*", rest)
    return rest[:nxt.start()] if nxt else rest


def package_files(here):
    """Every file of the package, by the declared rule.

    The rule is an exclusion and not an inclusion, deliberately: an exclusion
    rule that meets something new lets it through and the inventory check then
    fails loudly, while an inclusion rule would quietly ignore it. At a gate one
    picks the rule that shouts. Excluded: entries whose name begins with a dot,
    and Python bytecode caches. Everything else belongs to the package, and the
    walk descends into subdirectories, because errata-evidence/ is one.
    """
    import os
    out = []
    for root, dirs, names in os.walk(here):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for name in names:
            if name.startswith(".") or name.endswith(".pyc"):
                continue
            rel = os.path.relpath(os.path.join(root, name), here).replace("\\", "/")
            out.append(rel)
    return sorted(out)


def readme_inventory(readme):
    """The names the README file table declares, as written in its first column."""
    import re
    listed = []
    for line in readme.split("\n"):
        m = re.match(r"\|\s*`([^`]+)`\s*\|", line)
        if m:
            listed.append(m.group(1))
    return listed


def section_errata():
    head("The errata log, against the shape it declares for itself")

    import os
    import re
    here = os.path.dirname(os.path.abspath(__file__))
    log = read_text(os.path.join(here, "ERRATA.md"))
    readme = read_text(os.path.join(here, "README.md"))
    if log is None or readme is None:
        # Nine failures rather than nine checks that quietly do not happen: the
        # contribution to the count is fixed whether the files are there or not.
        for claim in ("the log is present next to this script",
                      "defect entries carry the six required fields",
                      "record entries carry their four fields",
                      "entry identifiers use a declared prefix and are unique",
                      "every status is one its category admits",
                      "no entry leaves a pending marker standing",
                      "every printed-text field quotes or is marked pending",
                      "every sha256 is written unabbreviated",
                      "the README file table is a complete inventory"):
            check("errata", claim, False, True)
        return

    entries = errata_entries(log)

    bad = [f"{e['id']} lacks {f}" for e in entries if e["cat"] in "EP"
           for f in ERRATA_DEFECT_FIELDS if f"**{f}**" not in e["body"]]
    check("errata", "defect entries carry the six required fields", bad, [])

    bad = [f"{e['id']} lacks {f}" for e in entries if e["cat"] in "CX"
           for f in ERRATA_RECORD_FIELDS if f"**{f}**" not in e["body"]]
    check("errata", "record entries carry their four fields", bad, [])

    seen, bad = {}, []
    for e in entries:
        if e["id"] in seen:
            bad.append(f"{e['id']} appears twice")
        seen[e["id"]] = True
        want = "Applied" if "**Status.** APPLIED" in e["body"] else ERRATA_SECTION[e["cat"]]
        if e["part"] != want:
            bad.append(f"{e['id']} sits under {e['part']!r}, not {want!r}")
    check("errata", "every entry is filed once, under its category's part", bad, [])

    bad = []
    for e in entries:
        field = errata_field(e["body"], "Status.") or ""
        # The status is what stands before the first full stop; an entry may go on
        # to say what it is waiting for, and P-1 does.
        status = field.strip().split(".")[0].strip()
        if status not in ERRATA_STATUS[e["cat"]]:
            bad.append(f"{e['id']} carries status {status!r}")
    check("errata", "every status is one its category admits", bad, [])

    ids = [e["id"] for e in entries]
    bad = [i for i in ids if not re.fullmatch(r"[EPCX]-\d+", i)]
    check("errata", f"the {len(ids)} entry identifiers use a declared prefix", bad, [])

    bad = [f"{e['id']} still carries {m}" for e in entries for m in ERRATA_MARKERS
           if m in e["body"] and "incomplete" not in e["body"]]
    check("errata", "no entry leaves a pending marker standing", bad, [])

    bad = []
    for e in entries:
        if e["cat"] not in "EP":
            continue
        field = errata_field(e["body"], "Printed text.")
        # A blockquote or a fenced block both count as quotation. The second is
        # what an entry about the package uses, because what it quotes is code,
        # and a rule that only knew about blockquotes would push those entries
        # into the wrong form to satisfy it.
        quoted = field is not None and (any(l.lstrip().startswith(">")
                                            for l in field.split("\n"))
                                        or "```" in field)
        marked = field is not None and any(m in field for m in ERRATA_MARKERS)
        if not (quoted or marked):
            bad.append(f"{e['id']} has no quoted printed text and no pending mark")
    check("errata", "every printed-text field quotes or is marked pending", bad, [])

    bad = []
    for e in entries:
        for token in re.findall(r"`([^`]+)`", e["body"]):
            if re.fullmatch(r"[0-9a-f]{6,}(?:\.\.\.|…)[0-9a-f]{3,}", token):
                bad.append(f"{e['id']} abbreviates {token}")
        for m in re.finditer(r"sha256\s*\n?\s*`([^`]+)`", e["body"]):
            if not re.fullmatch(r"[0-9a-f]{64}", m.group(1)):
                bad.append(f"{e['id']} writes a sha256 of {len(m.group(1))} characters")
    check("errata", "every sha256 is written unabbreviated", bad, [])

    present = package_files(here)
    listed = readme_inventory(readme)
    dirs = [n.rstrip("/") for n in listed if n.endswith("/")]
    files = [n for n in listed if not n.endswith("/")]
    unlisted = [f"present and unlisted: {p}" for p in present
                if p not in files and not any(p.startswith(d + "/") for d in dirs)]
    absent = ([f"listed and absent: {n}" for n in files
               if not os.path.isfile(os.path.join(here, n))]
              + [f"listed and absent: {d}/" for d in dirs
                 if not os.path.isdir(os.path.join(here, d))])
    check("errata", f"the README file table lists all {len(present)} files, and no others",
          unlisted + absent, [])
# Living surfaces: front matter read from the places it lives in
# ---------------------------------------------------------------------------
#
# The same study that found the frozen figures were checked by presence found
# the same hole here. Of the front matter drifts it injected one surface at a
# time, eleven escaped: the title altered in the README heading, in the HTML
# <title>, in the og:title meta tag and in the display heading; the subtitle
# altered on both surfaces; the author altered in the landing byline; and every
# DOI edit on both. They escaped because nothing read those places. The front
# matter section compared the canonical macros of paper.tex and the BibTeX title
# line, and took the rest of both documents on trust.
#
# These surfaces are checked by STRUCTURE, not by position. README.md and
# index.html are meant to be edited, so pinning their line numbers the way
# paper.tex is pinned would break on the first paragraph added. What is pinned
# is which heading, which meta tag, which field each string lives in.

#: (surface, what to call it, pattern with one group, regex flags, which string).
SURFACE_LOCATIONS = (
    ("README.md", "the bold title line", r"^\*\*(.+?)\*\*$", re.M, "title"),
    ("README.md", "the italic subtitle line", r"^\*([^*].*?)\*$", re.M, "subtitle"),
    ("README.md", "the BibTeX author field", r"author\s*=\s*\{(.+?)\}", 0, "bibtex_author"),
    ("index.html", "the <title> element", r"<title>(.*?)</title>", re.S, "title"),
    ("index.html", "the og:title meta tag", r'og:title"\s+content="(.*?)"', 0, "title_subtitle"),
    ("index.html", "the display heading", r'<h1>\s*(.*?)\s*<span class="sub">', re.S, "title"),
    ("index.html", "the display subtitle", r'<span class="sub">(.*?)</span>', re.S, "subtitle"),
    ("index.html", "the byline", r"^\s*(.+?) &middot; Independent Researcher", re.M, "author"),
    ("index.html", "the BibTeX author field", r"author\s*=\s*\{(.+?)\}", 0, "bibtex_author"),
)

#: How many times each identifier must occur on each surface. A count of zero is
#: as much a claim as any other: the landing must NOT carry the version DOI,
#: because following it would land a reader on a superseded deposit.
IDENTIFIER_COUNTS = (
    ("paper.tex", "10.5281/zenodo.21609654", 1, "the version DOI it was archived with"),
    ("README.md", "10.5281/zenodo.21609653", 4, "the concept DOI"),
    ("README.md", "10.5281/zenodo.21609654", 1, "the version DOI, named once in the claim map"),
    ("index.html", "10.5281/zenodo.21609653", 3, "the concept DOI"),
    ("index.html", "10.5281/zenodo.21609654", 0, "no version DOI at all"),
)


def section_surfaces():
    head("Living surfaces: the front matter is right where it lives")

    import os
    here = os.path.dirname(os.path.abspath(__file__))
    tex = read_text(os.path.join(here, "paper.tex"))
    if tex is None:
        check("surface", "paper.tex is present next to this script", False, True)
        return
    macros = dict(re.findall(r"\\newcommand\{\\(paper(?:title|subtitle|author))\}\{(.+?)\}\n", tex))
    title = " ".join(macros.get("papertitle", "").split())
    subtitle = " ".join(macros.get("papersubtitle", "").split())
    author = " ".join(macros.get("paperauthor", "").split())
    family = author.split(" ", 1)[-1]
    expected = {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "title_subtitle": f"{title}: {subtitle}",
        # BibTeX names go family-first; the canonical string is the same name.
        "bibtex_author": f"{family}, {author.split(' ', 1)[0]}",
    }

    for surface, where, pattern, flags, key in SURFACE_LOCATIONS:
        text = read_text(os.path.join(here, surface))
        if text is None:
            check("surface", f"{surface} is present next to this script", False, True)
            continue
        found = re.search(pattern, text, flags)
        check("surface", f"{where} of {surface} carries the canonical {key}",
              " ".join(found.group(1).split()) if found else None, expected[key])

    for surface, identifier, count, describe in IDENTIFIER_COUNTS:
        text = read_text(os.path.join(here, surface))
        if text is None:
            check("surface", f"{surface} is present next to this script", False, True)
            continue
        check("surface", f"{surface} carries {describe}, exactly {count} time(s)",
              text.count(identifier), count)


#: Where each surface publishes how many checks this script runs. The count went
#: stale once before, from 192 to 202, and nothing here noticed; a published
#: number with no assertion behind it is exactly what this package exists to
#: refuse.
PUBLISHED_COUNT_PATTERNS = (
    r"\d+ checks passed, \d+ failed, (\d+) total",
    r"\((\d+) checks, standard library only\)",
)


def check_published_counts(total):
    head("Published counts: every surface agrees on how many checks there are")

    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for surface in ("README.md", "index.html"):
        text = read_text(os.path.join(here, surface))
        if text is None:
            check("count", f"{surface} is present next to this script", False, True)
            continue
        published = sorted({int(m) for pattern in PUBLISHED_COUNT_PATTERNS
                            for m in re.findall(pattern, text)})
        check("count", f"every check count published in {surface} is the real one",
              published, [total])


# ---------------------------------------------------------------------------

def main():
    print("Replication of: Statistical Structure of the Historical Orderings")
    print("                of the I Ching Hexagrams")
    print()
    print("Self-contained verification. Every figure printed in the paper is recomputed")
    print("here from the embedded King Wen sequence and the documented construction rules.")

    section_0()
    section_3()
    section_4()
    section_5()
    section_6()
    section_7()
    section_seeds()
    section_appendix_a()
    section_front_matter()
    section_pdf_metadata()
    section_paper()
    section_errata()
    section_surfaces()

    # The published count has to come last, because it counts itself: the two
    # assertions it is about to add are part of the number it checks.
    check_published_counts(len(RESULTS) + 2)

    passed = sum(1 for r in RESULTS if r)
    failed = len(RESULTS) - passed
    print()
    print("=" * 66)
    print(f"  {passed} checks passed, {failed} failed, {len(RESULTS)} total")
    print("=" * 66)
    if failed:
        print("  REPLICATION FAILED: the paper and this code disagree.")
        return 1
    print("  REPLICATION COMPLETE: every figure in the paper reproduces.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
