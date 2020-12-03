from math import prod

with open('input.txt') as f:
    data = list(f.read().strip().split('\n'))

steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

trees = []
for step in steps:
    r_step, c_step = step
    tree = 0
    col = 0
    for row in range(r_step, len(data), r_step):
        col += c_step
        if col > len(data[row]) - 1:
            col = col - len(data[row])

        if data[row][col] == '#':
            tree += 1

    trees.append(tree)
print(f'Part 1: {trees[1]}\nPart 2: {trees} --> {prod(trees)}')

