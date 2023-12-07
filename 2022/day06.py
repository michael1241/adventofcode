#! /usr/bin/env python3

from collections import deque

with open('day06in') as f:
    data = f.read()

# part 1
#offset = 4
#history = deque(data[:offset], offset)

# part 2
offset = 14
history = deque(data[:offset], offset)

for n, char in enumerate(data[offset:]):
    history.append(char)
    if len(history) == len(set(history)):
        print(n+offset+1)
        break

