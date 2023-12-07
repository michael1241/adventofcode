#! /usr/bin/env python3

import regex as re

with open('1data') as f:
    lines = f.read().splitlines()

# part 1
digits = [re.findall(r'\d', line) for line in lines]
print(sum(map(lambda x: int(x[0] + x[-1]), digits)))

# part 2
def findReplace(line):
    lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    found = list(re.finditer(r'one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9', line, overlapped=True))
    def swap(digit):
        return lookup[digit] if len(digit) > 1 else digit
    return int(swap(found[0][0]) + swap(found[-1][0]))

print(sum(list(map(findReplace, lines))))