with open('input.txt') as f:
    passport_raw = list(f.read().strip().split('\n\n'))

#print(passport_raw)
required = set(['pid', 'ecl', 'eyr', 'hcl', 'byr', 'iyr', 'hgt', 'cid'])
optional = ['cid']

part_1 = {'invalid': 0, 'valid': 0}
part_2 = {'invalid': 0, 'valid': 0}

def missing_props(props):
    return set(props).symmetric_difference(required) != set(optional) and set(props).symmetric_difference(required)

def validate_props(props):

    if int(props['byr']) not in range(1920, 2003):
        return False
    
    if int(props['iyr']) not in range(2010, 2021):
        return False
    
    if int(props['eyr']) not in range(2020, 2031):
        return False
    
    if props['hgt'].endswith('in') or props['hgt'].endswith('cm'):
        val, unit = int(props['hgt'][:-2]), props['hgt'][-2:]
        if unit == 'cm' and val not in range(150, 194):
            return False
        if unit == 'in' and val not in range(59, 77):
            return False
    
    if not (props['hgt'].endswith('in') or props['hgt'].endswith('cm')):
        return False
    
    if props['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if props['hcl'].startswith('#') and len(props['hcl']) == 7:
        try: 
            int(props['hcl'][1:], 16)
        except ValueError:
            return False
    
    if not props['hcl'].startswith('#') or len(props['hcl']) != 7:
        return False
    
    if len(props['pid']) != 9 or not props['pid'].isdigit():
        return False
    
    return True
    

for passport in passport_raw:
    passport = passport.replace('\n', ' ').split(' ')
    props = {}
    for info in passport:  
        prop, value = info.split(':')
        props[prop] = value
    
    k = props.keys()
    
    if missing_props(k):
        part_1['invalid'] += 1
    else:
        if validate_props(props):
            part_2['valid'] += 1
        else:
            part_2['invalid'] += 1
        part_1['valid'] += 1

print('Part 1: ', part_1)
print('Part 2: ', part_2)