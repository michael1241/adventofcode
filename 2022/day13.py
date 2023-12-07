#! /usr/bin/env python3

import functools

with open('day13in') as f:
    # part 1
    # data = list(map(lambda x: list(map(eval, x.split('\n'))), f.read().split('\n\n')))
    data = list(map(eval, filter(lambda x: x != '', f.read().splitlines())))

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left > right:
            return -1
        return 0
    if type(left) == int:
        return compare([left], right)
    if type(right) == int:
        return compare(left, [right])
    for subleft, subright in zip(left, right):
        if result := compare(subleft, subright):
            return result
    return compare(len(left), len(right))

# part 1
# output = []
# for n, (left, right) in enumerate(data):
#     output.append((n+1, compare(left, right)))
# print(sum([a for a, b in output if b == 1]))

# part 2
data.append([[2]])
data.append([[6]])

sorted_data = sorted(data, key=functools.cmp_to_key(compare), reverse=True)

print((sorted_data.index([[2]])+1) * (sorted_data.index([[6]])+1))