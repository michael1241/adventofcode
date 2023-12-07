#! /usr/bin/env python3

from parse import parse

with open('day15in') as f:
    data = f.read().splitlines()

squares = []

for row in data:
    squares.append(parse('Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}', row).named)

def square_size(s):
    s['size'] = abs(s['sx'] - s['bx']) + abs(s['sy'] - s['by'])
    return s

squares = list(map(square_size, squares))

beacons = {(s['bx'], s['by']) for s in squares}

y = 2000000

occupied = set()

for x in range(-2000000,6000000):
    position = (x, y)
    if position in occupied or position in beacons:
        continue
    for s in squares:
        dist = abs(s['sx'] - x) + abs(s['sy'] - y)
        if dist <= s['size']:
            occupied.add(position)
            break
    if x % 1000 == 0:
        print(x)

print(len(occupied))

#print(min(list(map(lambda x: min(x.values()), squares)))) #-290982
#print(max(list(map(lambda x: max(x.values()), squares)))) #4102300