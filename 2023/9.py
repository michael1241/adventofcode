#! /usr/bin/env python3

from itertools import pairwise

with open('9test') as f:
    data = list(map(lambda x: list(map(int, x.split(' '))), f.read().splitlines()))

def finder(seq, prev=None):
    def popup(seq, last):
        return seq + [seq[-1]+last]
    gaps = [b-a for a, b in pairwise(seq)]
    last = gaps[-1]
    if last == 0:
        return popup(gaps, last)
    return popup(finder(gaps, seq), last)


print(finder(data[0]))
print('------------')
print(finder(data[1]))
print('------------')
print(finder(data[2]))
