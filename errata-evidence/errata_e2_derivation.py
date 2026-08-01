"""Entry E-2 of ERRATA.md: the containment order of the six conditional nulls P0..P5 of
Appendix A, computed from the DEFINITIONS AS PRINTED in the deposited PDF
(garcia-hurtado-2026-king-wen-orderings-preprint.pdf, sha256 01c83c3d...4cfd, p. 14).

This is a reproduction with a known target, not an independent derivation: the result
(eleven strict containments, four incomparable pairs, zero equalities) was already
written in ERRATA.md before this file was run.  What makes it evidence rather than
decoration is that it can fail, and it did: the first generating set written for P4 was
too small to generate the group, this procedure returned P4 as contained in P2, and the
exhaustive enumeration below refuted it.

Nothing is imported from verify_paper.py: the predicates are written from the printed
prose, not read off the sampler.  This file is support for the entry; the evidence the
entry rests on is the eight witnesses exhibited in ERRATA.md itself, which a reader can
check by hand against the printed definitions.

Encoding.  In King Wen numbering the received sequence is literally 1,2,...,64, so a
member of any rung is a permutation s of 1..64.  Received pairs are (1,2),(3,4),...,
(63,64); pair index k (0-based) occupies slots 2k, 2k+1.

Every rung P1..P5 factors as  O_R x F_R  :  O_R a set of pair orders (a subgroup of
S_32) and F_R a set of orientation vectors (all of {0,1}^32, except P3 which forces
0 at the four anchors).  For non-empty product sets,
    O_A x F_A  subset  O_B x F_B   iff   O_A subset O_B  and  F_A subset F_B,
so the decision is exact: subgroup containment is decided on generators, and the flip
part on the forced-zero coordinate sets.

READING_P4: the printed P4 clause is self-contradictory; that is erratum E-1.  The
reading used here is the one the printed micro theorem of the same appendix forces
(block sums preserved => a pair never leaves its block).  Under the alternative literal
reading, P4 would coincide with P1 and the order would contain an equality; reported.
"""

from itertools import permutations

N, NPAIRS = 64, 32
ANCHORS = [0, 13, 14, 30]      # pairs (1,2) (27,28) (29,30) (61,62), printed in P3
CANON = 15                     # "15 and 17 pairs", printed in P2
BLK = 2                        # a block of four consecutive positions = 2 pairs
RECEIVED = list(range(1, N + 1))


# --------------------------------------------------------------- predicates ----
def pair_of(h):
    return (h - 1) // 2


def in_P0(s):
    return sorted(s) == RECEIVED


def in_P1(s):
    return in_P0(s) and all(pair_of(s[2 * k]) == pair_of(s[2 * k + 1])
                            for k in range(NPAIRS))


def occupancy(s):
    return [pair_of(s[2 * k]) for k in range(NPAIRS)]


def flipped(s):
    return [s[2 * k] > s[2 * k + 1] for k in range(NPAIRS)]


def in_P2(s):
    return in_P1(s) and set(occupancy(s)[:CANON]) == set(range(CANON))


def in_P3(s):
    if not in_P1(s):
        return False
    occ, fl = occupancy(s), flipped(s)
    return all(occ[a] == a and not fl[a] for a in ANCHORS)


def in_P4(s):
    if not in_P1(s):
        return False
    occ = occupancy(s)
    return all(len({occ[BLK * b] // BLK, occ[BLK * b + 1] // BLK}) == 1
               for b in range(NPAIRS // BLK))


def in_P5(s):
    return in_P1(s) and occupancy(s) == list(range(NPAIRS))


PRED = {"P0": in_P0, "P1": in_P1, "P2": in_P2,
        "P3": in_P3, "P4": in_P4, "P5": in_P5}
NAMES = ["P0", "P1", "P2", "P3", "P4", "P5"]


# ------------------------------------------------ order-part / flip-part -------
def order_ok(rung, o):
    """Is pair order o (a permutation of 0..31, o[k] = pair sitting in slot k) in O_R."""
    if rung in ("P0", "P1"):
        return True
    if rung == "P2":
        return set(o[:CANON]) == set(range(CANON))
    if rung == "P3":
        return all(o[a] == a for a in ANCHORS)
    if rung == "P4":
        return all(len({o[BLK * b] // BLK, o[BLK * b + 1] // BLK}) == 1
                   for b in range(NPAIRS // BLK))
    if rung == "P5":
        return o == list(range(NPAIRS))
    raise ValueError(rung)


FORCED = {"P1": set(), "P2": set(), "P3": set(ANCHORS), "P4": set(), "P5": set()}


def gens(rung):
    """Generators of O_R, as pair orders."""
    idt = list(range(NPAIRS))

    def tr(i, j):
        o = idt[:]
        o[i], o[j] = o[j], o[i]
        return o

    def cyc(idxs):
        o = idt[:]
        for t, i in enumerate(idxs):
            o[i] = idxs[(t + 1) % len(idxs)]
        return o

    if rung in ("P0", "P1"):
        return [tr(0, 1), cyc(list(range(NPAIRS)))]
    if rung == "P2":
        return [tr(0, 1), cyc(list(range(CANON))),
                tr(CANON, CANON + 1), cyc(list(range(CANON, NPAIRS)))]
    if rung == "P3":
        free = [p for p in range(NPAIRS) if p not in ANCHORS]
        return [tr(free[0], free[1]), cyc(free)]
    if rung == "P4":
        # S_2 wr S_16: the top group must act transitively on the sixteen blocks,
        # so a block transposition alone is not enough - a block cycle is needed too.
        swap01 = idt[:]
        swap01[0], swap01[1], swap01[2], swap01[3] = 2, 3, 0, 1
        cycleblocks = idt[:]
        nb = NPAIRS // BLK
        for b in range(nb):
            src = ((b + 1) % nb)
            cycleblocks[BLK * b], cycleblocks[BLK * b + 1] = BLK * src, BLK * src + 1
        return [swap01, cycleblocks, tr(0, 1)]
    if rung == "P5":
        return [idt]
    raise ValueError(rung)


def contains(B, A):
    """Exact decision of O_A x F_A subset of O_B x F_B, for A,B in P1..P5."""
    if not all(order_ok(B, g) for g in gens(A)):
        return False
    return FORCED[B] <= FORCED[A]


# -------------------------------------------------------------- witnesses -----
def build(order=None, flips=None):
    order = list(range(NPAIRS)) if order is None else order
    flips = [False] * NPAIRS if flips is None else flips
    s = []
    for k, p in enumerate(order):
        a, b = 2 * p + 1, 2 * p + 2
        s += [b, a] if flips[k] else [a, b]
    return s


def swap_pairs(i, j):
    o = list(range(NPAIRS))
    o[i], o[j] = o[j], o[i]
    return build(o)


def swap_blocks(bi, bj):
    o = list(range(NPAIRS))
    for t in range(BLK):
        o[BLK * bi + t], o[BLK * bj + t] = o[BLK * bj + t], o[BLK * bi + t]
    return build(o)


def flip_pair(k):
    f = [False] * NPAIRS
    f[k] = True
    return build(None, f)


def slots(s, lo, hi):
    return " ".join(f"({s[2*k]},{s[2*k+1]})" for k in range(lo, hi))


# ------------------------------------------- exhaustive confirmation (8 pairs) -
def exhaustive_small():
    """Same construction shrunk to 8 pairs: 4 blocks of two pairs, canon split 3/5,
    anchors {0, 3}.  The split is odd, so the canon boundary falls strictly inside a
    block, exactly as 15 does in the full object.  All 8! orders are walked; the flip
    part is handled by its forced-zero set, which makes the enumeration exact."""
    np_, split, anch, blk = 8, 3, [0, 3], 2

    def ok(r, o):
        if r in ("P0", "P1"):
            return True
        if r == "P2":
            return set(o[:split]) == set(range(split))
        if r == "P3":
            return all(o[a] == a for a in anch)
        if r == "P4":
            return all(len({o[blk*b] // blk, o[blk*b+1] // blk}) == 1
                       for b in range(np_ // blk))
        if r == "P5":
            return list(o) == list(range(np_))

    forced = {"P0": set(), "P1": set(), "P2": set(),
              "P3": set(anch), "P4": set(), "P5": set()}
    sets = {r: set() for r in NAMES}
    for o in permutations(range(np_)):
        for r in NAMES:
            if ok(r, o):
                sets[r].add(o)
    rel = {}
    for i in range(len(NAMES)):
        for j in range(i + 1, len(NAMES)):
            A, B = NAMES[i], NAMES[j]
            # A subset B iff orders subset and forced_B subset forced_A
            ab = sets[A] <= sets[B] and forced[B] <= forced[A]
            ba = sets[B] <= sets[A] and forced[A] <= forced[B]
            if A == "P0" or B == "P0":
                # P0 is the free shuffle: strictly larger than every pair-preserving
                # rung, since it contains non-pair-preserving sequences.
                other = B if A == "P0" else A
                rel[(A, B)] = ("P0 > " + other) if other != "P0" else "EQUAL"
                continue
            rel[(A, B)] = ("EQUAL" if ab and ba else
                           f"{A} < {B}" if ab else
                           f"{B} < {A}" if ba else
                           f"{A} || {B}")
    return sets, rel


if __name__ == "__main__":
    print("=" * 74)
    print("FULL OBJECT (32 pairs, 64 hexagrams): the fifteen pairwise relations")
    print("=" * 74)
    strict = inc = eq = 0
    for i in range(len(NAMES)):
        for j in range(i + 1, len(NAMES)):
            A, B = NAMES[i], NAMES[j]
            if A == "P0":
                print(f"  {B} < P0    strict   (P0 contains non-pair-preserving orders)")
                strict += 1
                continue
            ab, ba = contains(B, A), contains(A, B)
            if ab and ba:
                print(f"  {A} = {B}   EQUAL")
                eq += 1
            elif ab:
                print(f"  {A} < {B}    strict")
                strict += 1
            elif ba:
                print(f"  {B} < {A}    strict")
                strict += 1
            else:
                print(f"  {A} || {B}   INCOMPARABLE")
                inc += 1
    print(f"  --> {strict} strict, {inc} incomparable, {eq} equalities")

    print()
    print("=" * 74)
    print("WITNESSES for the incomparable pairs, checked in both directions")
    print("=" * 74)
    W = [
        ("P2", "P4", "received order with pairs (3,4) and (7,8) transposed",
         swap_pairs(1, 3), (0, 4)),
        ("P4", "P2", "received order with pairs (29,30) and (31,32) transposed",
         swap_pairs(14, 15), (13, 17)),
        ("P2", "P3", "received order with pairs (1,2) and (3,4) transposed",
         swap_pairs(0, 1), (0, 4)),
        ("P3", "P2", "received order with pairs (3,4) and (31,32) transposed",
         swap_pairs(1, 15), (0, 3)),
        ("P3", "P4", "received order with pairs (3,4) and (7,8) transposed",
         swap_pairs(1, 3), (0, 4)),
        ("P4", "P3", "received order with the first two blocks transposed",
         swap_blocks(0, 1), (0, 5)),
        ("P3", "P5", "received order with pairs (3,4) and (5,6) transposed",
         swap_pairs(1, 2), (0, 4)),
        ("P5", "P3", "received order with pair (1,2) written 2,1",
         flip_pair(0), (0, 3)),
    ]
    for a, b, desc, s, span in W:
        va, vb = PRED[a](s), PRED[b](s)
        print(f"  in {a}, not in {b}: {desc}")
        print(f"     slots {span[0]+1}-{span[1]}: {slots(s, *span)} ...")
        print(f"     member of {a}: {va}   member of {b}: {vb}   "
              f"{'OK' if (va and not vb) else 'FAIL'}")

    print()
    print("=" * 74)
    print("EXHAUSTIVE CONFIRMATION on the shrunk model (8 pairs, all 8! orders)")
    print("=" * 74)
    sets, rel = exhaustive_small()
    print("  order-set sizes:", {r: len(sets[r]) for r in NAMES})
    for k, v in rel.items():
        print("   ", v)

    print()
    print("Alternative literal reading of the printed P4 clause "
          "(pairs may cross blocks):")
    print("  P4(literal) is exactly the pair-preserving null P1, so the order would "
          "contain\n  one equality (P4 = P1) and ten strict containments, not eleven.")
