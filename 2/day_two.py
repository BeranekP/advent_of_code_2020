with open('input.txt') as f:
    data = list(f.read().strip().split('\n'))

PART = 2
valid = 0

def parse_passwords(line):
    rule, password = pasword_rule.split(': ')
    count, letter = rule.split()
    min_c, max_c = map(int, count.split('-'))
    return password, letter, min_c, max_c

# Part 1
if PART == 1:
    for pasword_rule in data:
        password, letter, min_c, max_c = parse_passwords(pasword_rule)
        if password.count(letter) in range(min_c, max_c + 1):
            valid += 1

    print('Valid (part 1): ', valid)


# Part 2
if PART == 2:
    def search_string(string, letter, start=0, pos=[]):
        idx = string.find(letter, start)
        if idx >= 0:
            pos.append(idx)
        if idx < 0:
            return pos
        else:
            return search_string(string, letter, idx + 1, pos)



    for pasword_rule in data:
        password, letter, idx1, idx2 = parse_passwords(pasword_rule)
        idx1, idx2 = idx1 - 1, idx2 - 1
        pos = search_string(password, letter, pos=[])
        if pos:
            if (idx1 in pos and not idx2 in pos) or (not idx1 in pos and idx2 in pos):
                valid += 1

    print('Valid (part 2): ', valid)