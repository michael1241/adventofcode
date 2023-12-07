#! /usr/bin/env python3

import re

with open('day04in') as f:
    data = list(map(lambda x: list(map(int, re.split('[,-]', x))), f.read().splitlines()))

def contained(a, b, c, d):
    return (a >= c and b <= d) or (c >= a and d <= b)

def overlap(a, b, c, d):
    return (b >= c and a <= d) or (a >= d and b <= c)

# part 1
print(sum(list(map(lambda x: contained(*x), data))))

# part 2
print(sum(list(map(lambda x: overlap(*x), data))))