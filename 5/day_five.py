with open('input.txt') as f:
    boarding_passes = list(f.read().strip().split('\n'))

ID = 0
IDs = []
for boarding_pass in boarding_passes:
    rows = list(range(0, 128))
    columns = list(range(0, 8))
    for letter in boarding_pass:
        if letter == 'F':
            rows = rows[:len(rows) // 2]
        if letter == 'B':
            rows = rows[len(rows) // 2:]
        if letter == 'R':
            columns = columns[len(columns) // 2:]
        if letter == 'L':
            columns = columns[:len(columns) // 2]
    
    IDs.append(rows[0] * 8 + columns[0])
    if IDs[-1] > ID:
        ID = IDs[-1]

print('Part 1: ', ID)

IDs = sorted(IDs)
for i, num in enumerate(IDs):
    if i < len(IDs):
        if IDs[i+1] != num + 1:
            print('Part 2: ',num + 1)
            break