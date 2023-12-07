#! /usr/bin/env python3

import string
import operator

with open('day5in') as f:
	s = f.read().splitlines()

doubles = {c+c for c in string.ascii_lowercase}
forbidden = {'ab', 'cd', 'pq', 'xy'}
vowels = {'a', 'e', 'i', 'o', 'u'}

def check(s):
	pairs = set(map(operator.add, s[:-1] ,s[1:]))
	return pairs.intersection(doubles) and not pairs.intersection(forbidden) and len([_ for _ in s if _ in vowels]) >= 3

#print(len(list(filter(check, s))))

