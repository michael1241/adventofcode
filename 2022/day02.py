#! /usr/bin/env python3

import itertools

with open('day02in') as f:
	data = list(map(lambda x: tuple(x.split()), f.read().splitlines()))

testdata = list(map(lambda x: tuple(x.split()), ['A Y', 'B X', 'C Z']))

#print(list(itertools.product('ABC', 'XYZ')))
def score(game):
	result = {
		('A', 'X'): 3,
		('A', 'Y'): 6,
		('A', 'Z'): 0,
		('B', 'X'): 0,
		('B', 'Y'): 3,
		('B', 'Z'): 6,
		('C', 'X'): 6,
		('C', 'Y'): 0,
		('C', 'Z'): 3
		}
	pick_value = {'X': 1, 'Y': 2, 'Z': 3}
	return result[game] + pick_value[game[1]]

# part 1
print(sum(list(map(score, data))))

to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
to_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

def to_play(game):
	match game[1]:
		case 'X':
			return (game[0], to_lose[game[0]])
		case 'Y':
			return (game[0], to_draw[game[0]])
		case 'Z':
			return (game[0], to_win[game[0]])

# part 2
print(sum(list(map(score, map(to_play, data)))))