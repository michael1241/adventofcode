#! /usr/bin/env python3

from itertools import cycle
import parse
from math import lcm

with open('8data') as f:
    instr, _, *nodes = f.read().splitlines()

instr = cycle(instr)
lookup = {'L': 0, 'R': 1}

nodes = list(map(lambda x: parse.parse('{} = ({}, {})', x), nodes))
nodes = {a: (b, c) for a, b, c in nodes}

def period(node, nodes, instr, lookup, ended):
    count = 0
    while True:
        direction = lookup[next(instr)]
        node = nodes[node][direction]
        count += 1
        if ended(node):
            return count
# part 1
# print(period('AAA', nodes, instr, lookup, lambda x: x == 'ZZZ'))

# part 2
travel_nodes = [_ for _ in nodes.keys() if _.endswith('A')]
periods = []

for node in travel_nodes:
    periods.append(period(node, nodes, instr, lookup, lambda x: x.endswith('Z')))

print(lcm(*periods))