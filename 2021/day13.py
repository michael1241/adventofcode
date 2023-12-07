#! /usr/bin/env python3

import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=100000)

with open('day13in') as f:
    dots = [(int(x), int(y)) for x, y in (c.split(',') for c in f.read().splitlines())]

xmax = max(dots)[0] + 1
ymax = max(dots, key=lambda item: item[1])[1] + 1

paper = np.zeros((ymax, xmax), dtype=int)


for x, y in dots:
    paper[(y, x)] = '1'


def fold(pap, ax, val):
    ax = 0 if ax == 'y' else 1
    pap = np.delete(pap, val, axis=ax)
    a, b = np.split(pap, 2, axis=ax)
    b = np.flip(b, axis=ax)
    result = np.clip(np.add(a, b), 0, 1)
    return result


folds = (('x', 655), ('y', 447), ('x', 327), ('y', 223), ('x', 163), ('y', 111), ('x', 81), ('y', 55), ('x', 40), ('y', 27), ('y', 13), ('y', 6))
#test_folds = (('y', 7), ('x', 5))

for a, v in folds:
    paper = fold(paper, a, v)

print(paper)

# part 1
# print(paper.sum())
