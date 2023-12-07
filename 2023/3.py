#! /usr/bin/env python3

import numpy as np
from scipy.ndimage import label
from scipy.signal import convolve2d
import re

with open('3data') as f:
    text = f.read().splitlines()

data = np.array([np.array([*row], dtype=str) for row in text])

# mask for digits
digit_regex = re.compile(r'\d')
digit_match = np.vectorize(lambda x: bool(digit_regex.match(x)))
digits_mask = digit_match(data)

# find contiguous areas
labels, numL = label(digits_mask)
label_indices = [(labels == i).nonzero() for i in range(1, numL+1)]

# mask for symbols
symbol_regex = re.compile(r'[^\d.]')
symbol_match = np.vectorize(lambda x: bool(symbol_regex.match(x)))
symbols_mask = symbol_match(data)
kernel = np.ones((3, 3)) # find adjacent
symbols_mask = convolve2d(symbols_mask, kernel, mode='same') > 0

results = []
for number in label_indices:
    if any(symbols_mask[number]):
        results.append(int(''.join((data[number]))))
print(sum(results))

# part 2

gear_results = []

gear_candidates = np.transpose(np.where(data == '*'))

for candidate in gear_candidates:
    gear = np.zeros_like(data, dtype=bool)
    gear[candidate[0], candidate[1]] = True
    gear_mask = convolve2d(gear, kernel, mode='same') > 0

    overlaps = np.unique(labels[gear_mask])[1:]

    if overlaps.size == 2:
        overlap_nums = [label_indices[item-1] for item in overlaps]
        nums = [int(''.join(data[x])) for x in overlap_nums]
        gear_results.append(nums[0] * nums[1])
print(sum(gear_results))