#! /usr/bin/env python3

from more_itertools import pairwise, windowed

with open('./day1in') as f:
    lines = map(int, f.read().split("\n")[:-1])


def one(lines):
    return sum((map(lambda l: l[0] < l[1], pairwise(lines))))


def two(lines):
    return one(map(sum, windowed(lines, 3)))


print(two(lines))
