#! /usr/bin/env python3

from more_itertools import pairwise, interleave_longest
from collections import Counter, defaultdict

with open('day14in') as f:
    data = f.read().splitlines()

polymer, rules = data[0], data[2:]
rules = {a: b for a, b in [rule.split(' -> ') for rule in rules]}


def one(p, r, n):
    for _ in range(n):
        newitems = [r[a + b] for a, b in pairwise(p)]
        p = list(interleave_longest(p, newitems))

    res = Counter(p).values()
    return max(res) - min(res)


def two(p, r, n):
    first = p[0]
    last = p[-1]
    counts = Counter(["".join(i) for i in pairwise(p)])
    newcounts = defaultdict(int)
    for _ in range(n):
        for pair, count in counts.items():
            newcounts[pair[0] + r[pair]] += count
            newcounts[r[pair] + pair[1]] += count
        counts = newcounts.copy()
        newcounts = defaultdict(int)
    doubletotals = defaultdict(int)
    for pair, count in counts.items():
        doubletotals[pair[0]] += count
        doubletotals[pair[1]] += count
    totals = {k: v // 2 for k, v in doubletotals.items()}
    totals[first] += 1
    totals[last] += 1
    return totals


# print(one(polymer, rules, 10))
output = two(polymer, rules, 40).values()

print(max(output) - min(output))
