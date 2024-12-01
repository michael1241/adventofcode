#! /usr/bin/env python3

import numpy as np

with open('10test') as f:
    text = f.read().splitlines()

data = np.array([np.array([*row], dtype=str) for row in text])

print(data)
prev = np.where(data == 'S')

