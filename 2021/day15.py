#! /usr/bin/env python3

import numpy as np
import tcod

np.set_printoptions(linewidth=100000)

with open('day15in') as f:
    data = np.genfromtxt(f, delimiter=1, dtype=int)


def increment(array):
    adder = np.ones([array.shape[0], array.shape[1]], dtype=int)
    new_array = np.add(array, adder)
    new_array[new_array == 10] = 1
    return new_array


next_array = increment(data)
for _ in range(4):
    data = np.hstack((data, next_array))
    next_array = increment(next_array)
next_array = increment(data)
for _ in range(4):
    data = np.vstack((data, next_array))
    next_array = increment(next_array)

graph = tcod.path.SimpleGraph(cost=data, cardinal=1, diagonal=0)

pf = tcod.path.Pathfinder(graph)
pf.add_root((0, 0))
pf.resolve()
print(pf.distance)
