import re

rex = re.compile('(\d+)\-(\d+)\s+(\S)\:\s+(.*)')
with open('2020/input02.txt','rt') as f:
    passwords = tuple(((int(m[1]), int(m[2]), m[3], m[4]) for m in (rex.match(l) for l in f.readlines())))

invalid_position = lambda o: (o[3].count(o[2]) < o[0] or o[3].count(o[2]) > o[1])
either_position = lambda o: f'{o[3][o[0]-1]}{o[3][o[1]-1]}'.count(o[2])==1

print(f'Part 1: {len(passwords)-sum(invalid_position(o) for o in passwords)}')
print(f'Part 2: {sum(either_position(o) for o in passwords)}')
    