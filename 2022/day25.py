#! /usr/bin/env python3

import math

with open('day25intest') as f:
    data = f.read().splitlines()

def parse_number(num):
    total = 0
    for n, char in enumerate(num[::-1]):
        val = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[char]
        total += val * (5**n)
    return total

print(sum(map(parse_number, data)))