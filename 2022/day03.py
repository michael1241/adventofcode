#! /usr/bin/env python3

from itertools import islice

with open('day03in') as f:
    data = f.read().splitlines()

def dif(s):
    a, b = s[:len(s)//2], s[len(s)//2:]
    return "".join(set(a) & set(b))

def convert(l):
    return ord(l) - (38 if l.isupper() else 96)

# part 1
print(sum(map(convert,map(dif, data))))

def batched(iterable, n):
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

def dif3(a, b, c):
    return "".join(set(a) & set(b) & set(c))

# part 2
print(sum([convert(dif3(a, b, c)) for a, b, c in batched(data, 3)]))