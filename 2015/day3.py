#! /usr/bin/env python3
import operator
from collections import defaultdict

with open('day3in') as f:
	s = f.read()

visited = defaultdict(int)
positions = {'s': (0, 0), 'r': (0, 0)}

for n, d in enumerate(s):
	santa = 's' if n % 2 == 0 else 'r'
	match d:
		case '^':
			positions[santa] = tuple(map(operator.add, positions[santa], (0, 1)))
		case 'v':
			positions[santa] = tuple(map(operator.add, positions[santa], (0, -1)))
		case '<':
			positions[santa] = tuple(map(operator.add, positions[santa], (-1, 0)))
		case '>':
			positions[santa] = tuple(map(operator.add, positions[santa], (1, 0)))
	visited[positions[santa]] += 1

print(len(visited))