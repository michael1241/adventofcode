#! /usr/bin/env python3

with open('day01in') as f:
	data = f.read()

data = [list(map(int, x.split('\n'))) for x in data.split('\n\n')]

# part 1
print(max([sum(elf) for elf in data]))

# part 2
print(sum(sorted([sum(elf) for elf in data])[-3:]))
