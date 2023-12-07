#! /usr/bin/env python3

from parse import parse
import operator
from dataclasses import dataclass

with open('day11in') as f:
    data = f.read().split('\n\n')

@dataclass
class Monkey:
    monkey: int
    items: list
    op: any
    scale: int
    divisor: int
    truedest: int
    falsedest: int
    inspections: int = 0
    def inspect(self):
        try:
            item = self.items.pop(0)
        except IndexError:
            return
        self.inspections += 1
        if self.scale == 'old':
            item = self.op(item, item)
        else:
            self.scale = int(self.scale)
            item = self.op(item, self.scale)
        # item //= 3 # include for part 1
        item %= 9699690 # part 2
        return (self.truedest, item) if item % self.divisor == 0 else (self.falsedest, item)
    def take(self, item):
        self.items.append(item)

monkeys = []

def splitter(string):
    return list(map(int, string.split(', ')))

def operation(op):
    return {'+': operator.add, '*': operator.mul}[op]

for monkey in data:
    monkey = parse('Monkey {monkey:d}:\n  Starting items: {items:splitter}\n  Operation: new = old {op:operation} {scale}\n  Test: divisible by {divisor:d}\n    If true: throw to monkey {truedest:d}\n    If false: throw to monkey {falsedest:d}'
                    , monkey, dict(splitter=splitter, operation=operation))
    monkeys.append(Monkey(**monkey.named))

for _round in range(10000): # 20 for part 1
    for monkey in monkeys:
        while True:
            result = monkey.inspect()
            if not result:
                break
            monkeys[result[0]].take(result[1])

# part 1 & 2
print(sorted(list(map(lambda x: x.inspections, monkeys)))[-2:])