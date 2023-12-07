#! /usr/bin/env python3

import numpy as np

np.set_printoptions(threshold=np.inf)

numbers = [91, 17, 64, 45, 8, 13, 47, 19, 52, 68, 63, 76, 82, 44, 28, 56, 37, 2, 78, 48, 32, 58, 72, 53, 9, 85, 77, 89, 36, 22, 49, 86, 51, 99, 6, 92, 80, 87, 7, 25, 31, 66, 84, 4, 98, 67, 46, 61, 59, 79, 0, 3, 38, 27, 23, 95, 20, 35, 14, 30, 26, 33, 42, 93, 12, 57, 11, 54, 50, 75, 90, 41, 88, 96, 40, 81, 24, 94, 18, 39, 70, 34, 21, 55, 5, 29, 71, 83, 1, 60, 74, 69, 10, 62, 43, 73, 97, 65, 15, 16]


class Board():
    def __init__(self, squares):
        self.squares = squares
        self.mask = np.zeros((5, 5))
        self.complete = False

    def __repr__(self):
        return str(self.squares)

    def hit(self, num):
        hit = np.where(self.squares == num)
        self.mask[hit] = 1

    def win(self):
        if 5 in self.mask.sum(axis=0) or 5 in self.mask.sum(axis=1):
            return True
        return False

    def value(self):
        return np.ma.masked_array(self.squares, mask=self.mask).sum()


with open('./day4in') as f:
    data = np.genfromtxt(f)
    boards = [Board(data[i:i + 5]) for i in range(0, len(data), 5)]


def one(bs, nums):
    for num in nums:
        for board in bs:
            board.hit(num)
            if board.win():
                return board.value() * num


def two(bs, nums):
    wins = 0
    bnum = len(bs)
    for num in nums:
        for board in bs:
            if board.complete:
                continue
            board.hit(num)
            if board.win():
                board.complete = True
                wins += 1
            if wins == bnum:
                return board.value() * num


print(two(boards, numbers))
