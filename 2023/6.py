#! /usr/bin/env python3

from functools import reduce
import operator

test = {'time': [7, 15, 30], 'distance': [9, 40, 200]}
data = {'time': [53, 89, 76, 98], 'distance': [313, 1090, 1214, 1201]}

def dist(press_time, total_time):
    return press_time * (total_time - press_time)

results = []
for time, distance in zip(*data.values()):
    results.append(len(list(filter(lambda d: d > distance, map(lambda x: dist(x, time), range(time+1))))))

print(reduce(operator.mul, results))

# part 2
# time = 53897698
# distance = 313109012141201

# y = -x^2 + total_time --- intercept with --- y = total_distance
# solve in wolfram alpha
# x = 6623214 or 47274484 so 40651271 ways