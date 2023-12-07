#! /usr/bin/env python3

import numpy as np

with open('day09in') as f:
    data = f.read().splitlines()

head = np.array([0, 0])
route = [np.array([0, 0])]

def path(start, direction, magnitude):
    return [start + (n * direction) for n in range(1, magnitude+1)]

# generate all coordinates visited by the head
for line in data:
    match line.split(' '):
        case ['U', magnitude]: route.extend(path(route[-1], np.array([0, 1]), int(magnitude)))
        case ['D', magnitude]: route.extend(path(route[-1], np.array([0, -1]), int(magnitude)))
        case ['L', magnitude]: route.extend(path(route[-1], np.array([-1, 0]), int(magnitude)))
        case ['R', magnitude]: route.extend(path(route[-1], np.array([1, 0]), int(magnitude)))

def knot_router(prior_route):
    knot = np.array([0, 0])
    knot_route = [np.array([0, 0])]

    for position in prior_route:
        diff = position - knot
        dist = np.linalg.norm(diff)
        # still within 1 unit of previous
        if dist < 2.0:
            continue
        # orthogonal movement
        if dist == 2.0:
            knot += diff // 2
            knot_route.append(knot.copy())
        # diagonal movement
        if dist > 2.0:
            # determine the quadrant of direction and move that way
            angle = np.degrees(np.arctan2(*diff))
            if 0 <= angle < 90: knot += np.array([1, 1])
            if 90 <= angle < 180: knot += np.array([1, -1])
            if -180 <= angle < -90: knot += np.array([-1, -1])
            if -90 <= angle < 0: knot += np.array([-1, 1])
            knot_route.append(knot.copy())
    return knot_route

# part 1
print(np.unique(knot_router(route), axis=0).size // 2)

# part 2
prior_route = route
for n in range(9):
    prior_route = knot_router(prior_route)

print(np.unique(prior_route, axis=0).size // 2)
