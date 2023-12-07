#! /usr/bin/env python3

from collections import defaultdict

with open('day12in') as f:
    lines = [l.split('-') for l in f.read().splitlines()]

graph = defaultdict(set)
for line in lines:
    a, b = line
    graph[a].add(b)
    graph[b].add(a)


def canGoTo(vert, token, inPath):
    if vert == 'start':
        return False, token
    if vert.isupper():
        return True, token
    if not inPath:
        return True, token
    if token:
        return True, False
    return False, False


def findPaths(g, s, e, inputpath, inputtoken=True):
    localpath = inputpath + [s]
    if s == e:
        return localpath
    paths = []
    for vert in g[s]:
        inPath = vert in localpath
        canvisit, token = canGoTo(vert, inputtoken, inPath)
        if canvisit:
            new_paths = findPaths(g, vert, e, localpath, token)
            paths.extend(new_paths)
    return paths


result = (findPaths(graph, 'start', 'end', []))

print(sum([1 for v in result if v == 'start']))

size = len(result)
'''
idx_list = [idx + 1 for idx, val in
            enumerate(result) if val == 'end']
res = [result[i: j] for i, j in
       zip([0] + idx_list, idx_list + 
           ([size] if idx_list[-1] != size else []))]

for i in res:
    print(",".join(i))
'''
