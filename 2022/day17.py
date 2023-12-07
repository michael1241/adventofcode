#! /usr/bin/env python3

from itertools import cycle
import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

with open('day17in') as f:
    pattern = cycle(f.read())
test_pattern = cycle('>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>')

col_height = 5000
chamber = np.chararray([col_height,9], unicode=True)
chamber[:] = '.'
chamber[:,0] = '#' # left wall
chamber[:,8] = '#' # right wall
chamber[col_height-1 ,:] = '#'

def make_shape():
    h = yield
    for shape in cycle([
        lambda h: np.array([[h,3],[h,4],[h,5],[h,6]]).T,
        lambda h: np.array([[h,4],[h-1,3],[h-1,4],[h-1,5],[h-2,4]]).T,
        lambda h: np.array([[h,3],[h,4],[h,5],[h-1,5],[h-2,5]]).T,
        lambda h: np.array([[h,3],[h-1,3],[h-2,3],[h-3,3]]).T,
        lambda h: np.array([[h,3],[h-1,3],[h,4],[h-1,4]]).T
        ]):
        h = yield shape(h)

def is_collision(s, chamber, direction):
    s_local = s.copy()
    match direction:
        case 'l':
            s_local[1,:] += np.array([-1])
        case 'r':
            s_local[1,:] += np.array([1])
        case 'd':
            s_local[0,:] += np.array([1])
    return '#' in chamber[[*s_local]]

gen = make_shape()
next(gen)
s = None

shapes_count = 0

for push in pattern:
    if s is None:
        h = np.where(chamber[:,1:8] == '#')[0].min() - 4 # find bottom + 3
        s = gen.send(h) # generate next shape at correct height
        shapes_count += 1
    match push:
        case '<':
            if not is_collision(s, chamber, 'l'):
                s[1,:] += np.array([-1]) # move one left
        case '>':
            if not is_collision(s, chamber, 'r'):
                s[1,:] += np.array([1]) # move one right
    if not is_collision(s, chamber, 'd'):
        s[0,:] += np.array([1]) # move one down
        continue
    chamber[[*s]] = '#'
    np.savetxt('day17out', chamber, delimiter='', fmt='%s')
    s = None
    if shapes_count == 2022:
        break

np.savetxt('day17out', chamber, delimiter='', fmt='%s')

print(col_height - (np.where(chamber[:,1:8] == '#')[0].min() + 1))