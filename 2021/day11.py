#! /usr/bin/env python3

from itertools import product, starmap, islice

with open('./day11in') as f:
    data = [list(map(int, list(x))) for x in f.read().splitlines()]


class Oct():
    def __init__(self, energy):
        self.energy = energy
        self.charged = False
        self.has_flashed = False

    def __repr__(self):
        return str(self.energy)

    def setNeighbors(self, d, y, x):
        xi = (0, -1, 1) if 0 < x < len(d) - 1 else ((0, -1) if x > 0 else (0, 1))
        yi = (0, -1, 1) if 0 < y < len(d[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
        self.neighbors = list(islice(starmap((lambda a, b: d[x + a][y + b]), product(xi, yi)), 1, None))

    def increase(self):
        if self.energy >= 9:
            self.energy = 0
            if not self.has_flashed:
                self.charged = True
        else:
            self.energy += 1

    def discharge(self):
        if not self.has_flashed:
            for n in self.neighbors:
                n.increase()
            self.charged = False
            self.has_flashed = True

    def reset_flash(self):
        if self.has_flashed:
            self.has_flashed = False
            self.energy = 0


# create objects
for yn, y in enumerate(data):
    for xn, x in enumerate(y):
        data[yn][xn] = Oct(x)

# set neighbor references
for yn, y in enumerate(data):
    for xn, x in enumerate(y):
        x.setNeighbors(data, xn, yn)

# flatten
flat_data = [o for sub in data for o in sub]


def checkAll(d):
    cleared = 0
    flashes = 0
    to_check = len(d)
    while cleared < to_check:
        cleared = 0
        for o in d:
            if o.charged and not o.has_flashed:
                o.discharge()
                flashes += 1
            else:
                cleared += 1
    return flashes


def step(d):
    flashes = 0
    for o in d:
        o.increase()
    flashes += checkAll(d)
    for o in d:
        o.reset_flash()
    return flashes


def one(fd):
    total_flashes = 0
    for _ in range(100):
        total_flashes += step(fd)
    return total_flashes


# print(one(flat_data))

def two(fd):
    steps = 0
    while True:
        step(fd)
        steps += 1
        if all(o.energy == 0 for o in fd):
            return steps


print(two(flat_data))
