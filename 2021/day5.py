#! /usr/bin/env python3

import numpy as np
from itertools import cycle, starmap

np.set_printoptions(threshold=np.inf)

with open('./day5in') as f:
    lines = f.read().splitlines()


def parse(l):
    a, b = [tuple(map(int, s.split(','))) for s in l.split(' -> ')]
    return a, b


def lineGen(a, b):
    xmod = 1 if b[0] >= a[0] else -1
    xs = range(a[0], b[0] + xmod, xmod)
    ymod = 1 if b[1] >= a[1] else -1
    ys = range(a[1], b[1] + ymod, ymod)
    cyc = xs if len(xs) < len(ys) else ys
    if cyc is xs:
        return zip(cycle(xs), ys)
    return zip(xs, cycle(ys))


def filt(c):
    return c[0][0] == c[1][0] or c[0][1] == c[1][1]


coords = list(map(parse, lines))

# for ignoring non orthogonals in part one
#coords = list(filter(filt, coords))

draw_lines = starmap(lineGen, coords)

field = np.zeros([1000, 1000], dtype=int)

for l in draw_lines:
    for c in l:
        field[c] += 1

print(field[np.where(field >= 2)].size)
