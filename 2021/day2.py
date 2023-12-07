#! /usr/bin/env python3

import numpy as np

with open('./day2in') as f:
    lines = f.read().split("\n")[:-1]


def splitter(inst):
    a, b = inst.split(' ')
    return (a, int(b))


instructions = map(splitter, lines)


def one(instructions):

    moves = {'up': np.array([0, -1]), 'down': np.array([0, 1]), 'forward': np.array([1, 0])}

    location = np.array([0, 0])

    for direction, magnitude in instructions:
        movement = moves[direction] * magnitude
        location += movement
    return location.prod()


def two(instructions):

    moves = {'up': -1, 'down': 1}

    location = np.array([0, 0])
    aim = 0

    for direction, magnitude in instructions:
        if direction in moves:
            aim += moves[direction] * magnitude
        else:
            location += np.array([magnitude, magnitude * aim])
    return location.prod()


print(two(instructions))
