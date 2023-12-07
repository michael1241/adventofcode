#! /usr/bin/env python3

import numpy as np
from scipy import ndimage

np.set_printoptions(threshold=np.inf)

with open('./day9in') as f:
    data = np.genfromtxt(f, delimiter=1)


def neighbors(x, y, wid, hi):
    return filter(lambda coord: coord != (x, y), ((max(x - 1, 0), y), (min(x + 1, wid - 1), y), (x, max(y - 1, 0)), (x, min(y + 1, hi - 1))))


def one(d):
    mins = []
    points = np.nditer(d, flags=['multi_index'])
    for point in points:
        x, y = points.multi_index
        m = np.array([d[loc] for loc in neighbors(x, y, *d.shape)]).min()
        if m <= point:
            continue
        mins.append(point + 1)
    return sum(mins)


# print(one(data))

def two(d):
    label, num_label = ndimage.label(data < 9)
    size = np.bincount(label.ravel())
    return np.array(sorted(size[1:])[-3:]).prod()


# print(two(data))
