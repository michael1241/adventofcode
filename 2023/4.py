#! /usr/bin/env python3

import re
from collections import defaultdict

with open('4data') as f:
    data = f.read().splitlines()

def score(card, part):
    ident, wins, nums = re.split(r':|\|', card)
    wins = set(filter(None, wins.split(' ')))
    nums = set(filter(None, nums.split(' ')))
    matches = len(wins.intersection(nums))
    return round(2**(matches-1)) if part == 1 else matches

# part 1
print(sum(map(lambda card: score(card, part=1), data)))

# part 2

scores = {}
counts = defaultdict(int)

for n, card in enumerate(data):
    card_num = n + 1
    card_score = score(card, part=2)
    scores[card_num] = card_score
    counts[card_num] = 1

for n, score in scores.items():
    for m in range(n, n + score):
        counts[m+1] += 1*counts[n]

print(sum(counts.values()))
