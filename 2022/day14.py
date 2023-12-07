#! /usr/bin/env python3

import numpy as np
import itertools
np.set_printoptions(threshold=np.inf)
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

with open('day14in') as f:
    data = list(map(lambda x: list(map(lambda y: tuple(map(int, y.split(','))), x.split(' -> '))), f.read().splitlines()))

# minx, maxx, miny, maxy = 1000, 0, 1000, 0
# for line in data:
#     for x, y in line:
#         if x < minx: minx = x
#         if x > maxx: maxx = x
#         if y < miny: miny = y
#         if y > maxy: maxy = y
# print(minx, maxx, miny, maxy)
# 464 556 13 167

system = np.chararray([200,800], unicode=True) # wasteful size but still tiny
system[:] = '.'

# part 2
data.append([(0, 169), (799, 169)])

for line in data:
    current = None
    for x, y in line:
        if current is None:
            current = np.array([y, x])
            continue
        diff = np.array([y, x]) - current
        scale = max(abs(diff))
        unit = (diff / scale).astype(int)
        system[tuple(current)] = '#'
        for _ in range(scale):
            current += unit
            system[tuple(current)] = '#'
        current = np.array([y, x])

grain = np.array([0, 500])
count = 0
while True:
    count += 1
    while True:
        # part 1
        # if grain[0] > 198:
        #     break
        # part 2
        if system[tuple(grain)] == '+':
            break
        if system[tuple(grain + np.array([1, 0]))] == '.':
            grain += np.array([1, 0])
            continue
        if system[tuple(grain + np.array([1, -1]))] == '.':
            grain += np.array([1, -1])
            continue
        if system[tuple(grain + np.array([1, 1]))] == '.':
            grain += np.array([1, 1])
            continue
        else:
            system[tuple(grain)] = '+'
            break
    # part 1
    # if grain[0] > 198:
    #     break
    # part 2
    grain = np.array([0, 500])
    if system[tuple(grain)] == '+':
        break

np.savetxt('day14out', system[0:170,300:700], delimiter='', fmt='%s')
print(np.where(system == '+')[0].size)