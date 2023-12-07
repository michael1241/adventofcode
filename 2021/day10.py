#! /usr/bin/env python3

with open('./day10in') as f:
    lines = f.read().splitlines()

"""
lines = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]
"""


def checker(row, mode="add"):
    """Takes a row and returns score of first error or 0."""
    types = {
        '(': ('round', 1),
        ')': ('round', -1),
        '[': ('square', 1),
        ']': ('square', -1),
        '{': ('brace', 1),
        '}': ('brace', -1),
        '<': ('angle', 1),
        '>': ('angle', -1)
    }
    stack = [(None, None)]
    errorvals = {'round': 3, 'square': 57, 'brace': 1197, 'angle': 25137}
    for c in row:
        typ, val = types[c]
        styp, sval = stack[-1]
        if typ == styp and val + sval == 0:
            stack.pop()
            continue
        if val == -1:
            return errorvals[typ]
        stack.append((typ, val))
    if mode == "add":
        return 0
    if mode == "stack":
        return stack

#print(sum(map(checker, lines)))


uncorrupted = filter(lambda x: checker(x) == 0, lines)

uncorrupted_stacks = [checker(row, "stack") for row in uncorrupted]


def completer(stack):

    vals = {'round': 1, 'square': 2, 'brace': 3, 'angle': 4}
    total = 0
    for bracket, _ in stack[::-1]:
        if not bracket:
            return total
        total *= 5
        total += vals[bracket]


print(sorted(list(map(completer, uncorrupted_stacks)))[len(uncorrupted_stacks) // 2])
