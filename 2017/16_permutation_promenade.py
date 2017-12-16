#!/usr/bin/env python3

def get_input():
    with open('input16.txt','rt') as f:
        input = f.read().split(',')
    return input

def dance(input, programs):
    p = programs
    for m in input:
        if m[0] == 's':
            n = int(m[1:])
            p = p[-n:] + p[:-n]
        elif m[0] == 'x':
            p1, p2 = map(int,m[1:].split('/'))
            swap = p[p1]
            p[p1] = p[p2]
            p[p2] = swap
        elif m[0] == 'p':
            p1, p2 = m[1:].split('/')
            pi1, pi2 = p.index(p1), p.index(p2)
            swap = p[pi1]
            p[pi1] = p[pi2]
            p[pi2] = swap
    return p

def part1():
    programs = list('abcdefghijklmnop')
    input = get_input()
    return ''.join(dance(input,programs))

def part2():
    programs = list('abcdefghijklmnop')
    positions = []
    input = get_input()
    while ''.join(programs) not in positions:
        positions.append(''.join(programs))
        programs = dance(input,programs)

    return ''.join(positions[1000000000 % len(positions)])

print(part1())
print(part2())