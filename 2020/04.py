with open('2020/input04.txt','rt') as f:
    passports = []
    p = {}
    for l in f.readlines():
        if l.strip() == '':
            passports.append(p)
            p = {}
        else:
            for pair in l.strip().split(' '):
                values = pair.split(':')
                p[values[0]] = values[1]

valid_p1 = []
valid_p2 = []
import re
mkeys = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
for p in passports:
    invalid1 = False
    for k in mkeys:
        if k not in p.keys():
            invalid1 = True
            break
    else:
        valid_p1.append(p)

    if invalid1 is True:
        continue

    invalid = False
    for k in mkeys:
        if k == 'byr': invalid = True if int(p[k]) < 1920 or int(p[k]) > 2002 else False
        elif k == 'iyr': invalid = True if int(p[k]) < 2010 or int(p[k]) > 2020 else False
        elif k == 'eyr': invalid = True if int(p[k]) < 2020 or int(p[k]) > 2030 else False
        elif k == 'hgt': 
            m = re.match('^(\d+)(cm|in)$',p[k])
            if m is None:
                invalid=True
            else:
                if m[2] == 'cm':
                    invalid = True if int(m[1])<150 or int(m[1]) > 193 else False
                else:
                    invalid = True if int(m[1])<59 or int(m[1]) > 76 else False
        elif k == 'hcl':
            m = re.match('^#[abcdef0-9]{6,6}$', p[k])
            if m is None:
                invalid = True
        elif k == 'ecl':
            valid = ('amb','blu','brn','gry','grn','hzl','oth')
            invalid = p[k] not in valid
        elif k == 'pid':
            m = re.match('^\d{9,9}$',p[k])
            if m is None:
                invalid=True
        if invalid is True:
            break
    else:
        valid_p2.append(p)
        

print(f'Part1: valid:{len(valid_p1)}, total:{len(passports)}')
print(f'Part2: valid:{len(valid_p2)}, total:{len(passports)}')