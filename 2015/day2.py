#! /usr/bin/env python3

with open('day2in') as f:
	s = f.read().splitlines()

def total(a, b, c):
	a, b, c = map(int, [a, b, c])
	h, l, w = a*b, b*c, a*c
	paper = 2*h + 2*l + 2*w + min(h,l,w)
	sides = {h: (a, b), l: (b, c), w: (a, c)}
	bow = sum(sides[min(h,l,w)])*2 + (a*b*c)
	return bow #paper

print(sum([total(*p.split('x')) for p in s]))
	
