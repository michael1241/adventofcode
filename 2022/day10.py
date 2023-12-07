#! /usr/bin/env python3

with open('day10in') as f:
    data = f.read().splitlines()

current = 1
values = [1]

for line in data:
    match line.split(' '):
        case ['noop']:
            values.append(current)
        case ['addx', x]:
            x = int(x)
            values.extend([current, current+x])
            current += x

history = list(zip(range(1, len(values)+1), values))

# part 1
print(sum([cycle*value for cycle, value in history[19:220:40]]))

# part 2
for n in range(40):
    print(['#' if abs(value - n) < 2 else '.' for cycle, value in history[n:240:40]][::-1])