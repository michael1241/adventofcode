#! /usr/bin/env python3

with open('day1in') as f:
	s = f.read()

# part 1 print(s.count('(') - s.count(')'))

# part 2
floor = 0
for n, c in enumerate(s):
	match c:
		case '(':
			floor += 1
		case ')':
			floor -= 1
	if floor < 0:
		print(n+1)
		break
