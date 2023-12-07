#! /usr/bin/env python3

import re

with open('5data') as f:
    data = f.read().split("\n\n")

def almanac2test(dest, source, size):
    def f(inp):
        if inp >= source and inp < source + size:
            return inp + (dest - source)
    return f

seeds = list(map(int, data[0].split(': ')[1].split(' ')))
almanac = {n: list(map(lambda x: list(map(int, x.split(' '))), re.split(r':\n|[\n]', _map)[1:])) for n, _map in enumerate(data[1:])}
tests = {n: list(map(lambda x: almanac2test(*list(map(int, x.split(' ')))), re.split(r':\n|[\n]', _map)[1:])) for n, _map in enumerate(data[1:])}

results = []

for seed in seeds:
    for step in tests.values():
        for test in step:
            result = test(seed)
            if result is not None:
                seed = result
                break
    results.append(seed)

print(min(results))