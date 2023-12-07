#! /usr/bin/env python3

import numpy as np

with open('day18in') as f:
    rocks = list(map(np.array, list(map(lambda x: list(map(int, x.split(','))), f.read().splitlines()))))

total = len(rocks) * 6 # max sides exposed

while rocks:
    rock = rocks.pop()
    for compare_rock in rocks:
        if np.absolute(rock - compare_rock).sum() == 1:
            total -= 2

print(total)