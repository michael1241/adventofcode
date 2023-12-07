#! /usr/bin/env python3

import operator

with open('day21in') as f:
    data = f.read().splitlines()

def parser(monkey):
    name, instr = monkey.split(': ')
    try:
        return name, int(instr)
    except ValueError:
        m1, op, m2 = instr.split(' ')
        op = {'+': operator.add, '*': operator.mul, '/': operator.truediv, '-': operator.sub}[op]
        return name, (m1, op, m2)

monkeys = {}
for monkey in data:
    name, instr = parser(monkey)
    monkeys[name] = instr

print(monkeys)

def solve(monkey, monkeys):
    instr = monkeys[monkey]
    if type(instr) == int:
        return instr
    return instr[1](solve(instr[0], monkeys), solve(instr[2], monkeys))

print(solve('root', monkeys))
