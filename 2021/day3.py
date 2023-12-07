#! /usr/bin/env python3

import numpy as np

with open('./day3in') as f:
    lines = np.array(list(map(list, f.read().splitlines()))).astype(int)


def modeAndAnti(arr):
    inv = np.where((arr == 0) | (arr == 1), arr ^ 1, arr)
    anti = inv.mean(axis=0).round().astype(int)
    m = np.where((anti == 0) | (anti == 1), anti ^ 1, anti)
    return m, anti


def arrayToInt(arr):
    return int(''.join(arr.astype(str)), 2)


def one(l):
    gamma, epsilon = modeAndAnti(l)
    return gamma, epsilon
    # return arrayToInt(gamma) * arrayToInt(epsilon)


def filt(arr, pos, value):
    return arr[(arr[:, pos] == value)]


def two(l):
    oxy = l.copy()
    co2 = l.copy()

    oxy_gam, co2_gam = modeAndAnti(l)

    for pos in range(len(l[0])):
        if len(oxy) != 1:
            oxy = filt(oxy, pos, oxy_gam[pos])
            oxy_gam, _ = modeAndAnti(oxy)
        if len(co2) != 1:
            co2 = filt(co2, pos, co2_gam[pos])
            _, co2_gam = modeAndAnti(co2)

    return arrayToInt(oxy[0]) * arrayToInt(co2[0])


print(two(lines))
