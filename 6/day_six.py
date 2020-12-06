with open('input.txt') as f:
    groups = list(f.read().strip().split('\n\n'))

groups = [group.split('\n') for group in groups]


print('Part 1: ', sum((len(set(''.join(group))) for group in groups)))


# Part 2
setified = []
for group in groups:
    g = []
    if len(group) > 1:
        for item in group:
            g.append(set(item))
    else:
        g.append(set(group))
    setified.append(g)

total = 0
for group in setified:
    common = set.intersection(*group)
    if common:
        if len(common) == 1:
            total += len(*common)
        else:
            total += len(common)

print('Part 2: ', total)
