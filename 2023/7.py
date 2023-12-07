#! /usr/bin/env python3

from collections import Counter

with open('7data') as f:
    data = [a.split(' ') for a in f.read().splitlines()]

part = 2

def strength(cards):
    counts = Counter(cards)
    c = sorted(counts.values(), reverse=True)
    jacks = counts['J'] if part == 2 else 0
    match c:
        case [5]: return 7
        case [4, 1]: return 6 + {0: 0, 1: 1, 4: 1}[jacks]
        case [3, 2]: return 5 + {0: 0, 2: 2, 3: 2}[jacks]
        case [3, 1, 1]: return 4 + {0: 0, 1: 2, 3: 2}[jacks]
        case [2, 2, 1]: return 3 + {0: 0, 1: 2, 2: 3}[jacks]
        case [2, 1, 1, 1]: return 2 + {0: 0, 1: 2, 2: 2}[jacks]
        case [1, 1, 1, 1, 1]: return 1 + {0: 0, 1: 1}[jacks]

def mapper(card):
    j_val = ';' if part == 1 else '0'
    mapping = {'T': ':', 'J': j_val, 'Q': '<', 'K': '=', 'A': '>'}
    card_map = mapping.get(card)
    return card_map if card_map else card

data = [(cards, strength(cards), "".join(list(map(mapper, cards))), int(bid)) for cards, bid in data]

ordered = sorted(data, key=lambda cards: (cards[1], cards[2]))
result = sum([a*b for a, b in zip([cards[3] for cards in ordered], range(1, len(ordered)+1))])

print(result)