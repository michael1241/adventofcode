#! /usr/bin/env python3

import numpy as np

with open('day08in') as f:
    data = list(map(list, f.read().splitlines()))

forest = np.asarray(data, dtype=int)
visible = np.zeros_like(forest)

def is_visible(array):
    visibility = np.zeros_like(array)
    tallest = -1
    for n, tree in enumerate(array):
        if tree > tallest:
            tallest = tree
            visibility[n] += 1
    return visibility

for n, row in enumerate(forest):
    from_left = is_visible(row)
    from_right = is_visible(row[::-1])[::-1]
    visible[n] += (from_left+from_right)

visible = visible.T
forest = forest.T

for n, row in enumerate(forest):
    from_left = is_visible(row)
    from_right = is_visible(row[::-1])[::-1]
    visible[n] += (from_left+from_right)

# part 1
print(np.count_nonzero(visible))

# part 2

def explore(x, y, forest):
    score = 1
    for direction in ((1, 0), (0, 1), (0, -1), (-1, 0)):
        count = 0
        dx, dy = x, y
        tallest = forest[x, y]
        while True:
            dx += direction[0]
            dy += direction[1]
            if dx < 0 or dy < 0  or dx > 98 or dy > 98:
                break
            if forest[dx, dy] >= tallest:
                count += 1
                break
            count += 1
        if count != 0:
            score *= count
    return score


it = np.nditer(forest, flags=['multi_index'])
top = 0
for cell in it:
    result = explore(*it.multi_index, forest)
    if result > top:
        top = result
print(top)
