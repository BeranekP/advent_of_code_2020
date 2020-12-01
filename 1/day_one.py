from itertools import combinations
from math import prod


with open('input.txt') as f:
    data = list(map(int, f.read().split()))


def calc_combinations(data, length, target):
    for t in combinations(data, length):
        if sum(t) == target:
            print(t, '-->', prod(t))


for l in [2, 3]:
    calc_combinations(data, l, 2020)
