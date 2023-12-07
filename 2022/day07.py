#! /usr/bin/env python3

import re
from collections import defaultdict

with open('day07in') as f:
    data = f.read().splitlines()

items = defaultdict(int)
contents = defaultdict(set)

location = ['/']

for line in data[1:]:
    match line.split():
        case ['$', 'cd', _dir]: 
            if _dir == '..':
                location.pop()
            else:
                location.append(f'{_dir}/')
        case ['$', 'ls']: continue
        case ['dir', _dir]:
            contents[''.join(location)+f'{_dir}/'].add(''.join(location))
        case [size, f]: items[''.join(location)] += int(size)

for subdir, _dir in sorted(contents.items(), key=lambda x: x[0].count('/'), reverse=True):
    items[_dir.pop()] += items[subdir]

# part 1
print(sum([x for x in items.values() if x <= 100000]))

# part 2
print(sorted(list(filter(lambda x: x[1] >= 30000000 - (70000000 - items['/']), items.items())), key=lambda x: x[1])[0])

