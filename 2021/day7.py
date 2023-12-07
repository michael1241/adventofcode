#! /usr/bin/env python3

from statistics import median, mean
from math import ceil, floor

crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open('./day7in') as f:
    crabs = [int(x) for x in f.read().split(',')]

med = median(crabs)  # used for part 1
avg = mean(crabs)


def triangle(n):
    return int(n * (n + 1) / 2)


avgs = (floor(avg), ceil(avg))


def checkFuel(avg):
    fuel = 0
    for crab in crabs:
        fuel += triangle(abs(crab - avg))
    return fuel


print(min((checkFuel(avg) for avg in avgs)))
