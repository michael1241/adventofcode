#! /usr/bin/env python3

from parse import parse

with open('day16in') as f:
    data = f.read().splitlines()

valves = []

def splitter(string):
    return string.split(', ')

for valve in data:
    valves.append(parse('Valve {valve} has flow rate={rate:d}; tunnel leads to valve {towards:splitter}', valve, dict(splitter=splitter)).named)

print(valves)