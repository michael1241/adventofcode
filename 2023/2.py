#! /usr/bin/env python3

from collections import defaultdict
from functools import reduce

with open('2data') as f:
    lines = f.read().splitlines()

def parseColors(reveal):
    totals = defaultdict(int)
    colors = list(map(lambda x: x.split(' '), reveal.split(',')))
    for color in colors:
        totals[color[2]] = int(color[1])
    return totals

def parseReveals(game):
    reveals = [parseColors(reveal) for reveal in game.split(';')]
    max_reveals = {k: max(d[k] for d in reveals) for k in rules_dict.keys()}
    return max_reveals

def parseGame(line):
    ident, game = line.split(':')
    ident = ident.split(' ')[-1]
    max_reveals = parseReveals(game)
    return ident, max_reveals

def checkRestriction(rules_dict, line):
    ident, game = line
    for color, value in rules_dict.items():
        if game.get(color) and game[color] > value:
            return 0
    return int(ident)

def powerCalculate(line):
    return reduce((lambda x, y: x * y), line[1].values())

rules_dict = {'red': 12, 'green': 13, 'blue': 14}

# part 1
print(sum([checkRestriction(rules_dict, parseGame(line)) for line in lines]))

# part 2
print(sum([powerCalculate(parseGame(line)) for line in lines]))

