#! /usr/bin/env python3

import re
from collections import defaultdict

with open('day07in') as f:
    data = f.read()

dir_re = re.compile(r'dir (\w+)')
sizes_re = re.compile(r'\d+')
files_re = re.compile(r'(\d+) (\w+\.\w+)')

dirs = defaultdict(int)

splitted = data.split('cd ')
for s in splitted[::-1]:
    print(s)
    dir_name = s.split()[0]
    if dir_name in dirs:
        continue
    print(dir_name)
    dirs[dir_name] += sum(map(int, re.findall(sizes_re, s)))
    print(dirs[dir_name])
    print(dirs)
    sub_dirs = re.findall(dir_re, s)
    print(sub_dirs)
    if sub_dirs:
        for sub_dir in sub_dirs:
            dirs[dir_name] += dirs[sub_dir]
    #files = re.findall(files_re, s)
    #if files:
    #    for file in files:
    #        dirs[file[1]] += int(file[0])

    print('\n\n')

print(sum([d for d in dirs.values() if d <= 100000]))
