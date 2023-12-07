#! /usr/bin/env python3

import numpy as np

with open('day12in') as f:
    data = list(map(list, f.read().splitlines()))

heights = np.asarray(data, dtype=str)

# part 1
# start = np.array(np.where(heights == 'S')).flatten()
# end = np.array(np.where(heights == 'E')).flatten()

# part 2
start = np.array(np.where(heights == 'E')).flatten()

#print(start, end)
heightmap = np.vectorize(ord)(heights)

heightmap[tuple(start)] = 123
#heightmap[tuple(end)] = 123

queue = []

def get_legal_neighbors(s, heightmap, current_distance):
    edges = heightmap.shape
    neighbors = []
    directions = (np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1]))
    for direction in directions:
        neighbor = np.add(s, direction)
        if neighbor[0] < 0 or neighbor[0] > edges[0]-1 or neighbor[1] < 0 or neighbor[1] > edges[1]-1:
            continue
        #if heightmap[tuple(neighbor)] > heightmap[tuple(s)] + 1:
        # part 2
        if heightmap[tuple(neighbor)] < heightmap[tuple(s)] - 1:
            continue
        neighbors.append((neighbor, current_distance + 1))
    return neighbors

def bfs(visited, heightmap, current):
    current_distance = 0
    visited[tuple(current[0])] = current_distance
    queue.append(current)
    while queue:
        s = queue.pop(0)
        current_distance = s[1]
        # if heightmap[tuple(s[0])] == 123:
        # part 2
        if heightmap[tuple(s[0])] == 97:
            break
        for neighbor, neighbor_distance in get_legal_neighbors(s[0], heightmap, current_distance):
            neighbor = tuple(neighbor)
            if neighbor not in visited.keys():
                visited[tuple(neighbor)] = neighbor_distance
                queue.append((neighbor, neighbor_distance))
    return visited

# part 1
# print(bfs({}, heightmap, (start, 0))[tuple(end)])

# part 2
print(max(bfs({}, heightmap, (start, 0)).values())-1)