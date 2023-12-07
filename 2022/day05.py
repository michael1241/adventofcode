#! /usr/bin/env python3

import parse
import pandas as pd

with open('day05in') as f:
    moves = f.read()[325:].splitlines()

stacks = pd.read_fwf('day05in', widths=[4,4,4,4,4,4,4,4,4], header=None)[:9]

def stack_read(stack, stack_num):
    output = []
    for val in stack:
        if type(val) == float:
            continue
        output.insert(0, val[1])
    return {stack_num: output}

all_stacks = {}

for column in stacks.columns:
    vals = stacks[column].to_list()
    all_stacks = all_stacks | stack_read(vals[:-1], vals[-1])

moves = [parse.parse('move {} from {} to {}', move) for move in moves]

def make_move(_from, to, all_stacks):
    crate = all_stacks[_from].pop()
    all_stacks[to].append(crate)
    return all_stacks

def do_instructions(move, all_stacks):
    num, _from, to = move
    for n in range(int(num)):
        all_stacks = make_move(_from, to, all_stacks)
    return all_stacks

def move_multiple(move, all_stacks):
    num, _from, to = move
    crates = []
    for n in range(int(num)):
        crates.append(all_stacks[_from].pop())
    for crate in crates[::-1]:
        all_stacks[to].append(crate)
    return all_stacks

# part 1
#for move in moves:
#    all_stacks = do_instructions(move, all_stacks)
#print("".join([x.pop() for x in all_stacks.values()]))

# part 2
for move in moves:
    all_stacks = move_multiple(move, all_stacks)
print("".join([x.pop() for x in all_stacks.values()]))