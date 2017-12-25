#!/usr/bin/env python3

from collections import defaultdict, deque
from math import sqrt,floor

def get_input():
    with open('input23.txt', 'rt') as f:
        input = f.readlines()
    return [l.strip().split(' ') for l in input]


def execute(reg, ip, inst, iq=deque(), oq=deque(), pid=0):

    def get(v):
        try:
            return int(v)
        except ValueError:
            return reg[v]

    op = inst[0]
    x = inst[1]
    y = get(inst[2]) if len(inst) > 2 else None

    if op == 'set':
        reg[x] = y
    elif op == 'sub':
        reg[x] -= y
    elif op == 'add':
        reg[x] += y
    elif op == 'mul':
        reg[x] *= y
    elif op == 'mod':
        reg[x] %= y
    elif op == 'rcv':
        if reg[x] != 0:
            reg['part1_freq'] = reg['freq']
        if len(iq) == 0:  # "wait" for next value
            return ip, False
        else:
            reg[x] = iq.popleft()
    elif op == 'snd':
        oq.append(get(x))
    elif op == 'jgz':
        if get(x) > 0:
            return ip + y, True
    elif op == 'jnz':
        if get(x) != 0:
            return ip + y, True
    return ip + 1, True

def part1(input):
    reg = defaultdict(int)
    ip = 0
    ct = 0
    while ip >= 0 and ip < len(input):
        if input[ip][0] == 'mul':
            ct += 1
        ip, _ = execute(reg, ip, input[ip])
    return ct

def part2(input):   
    ct = 0
    for x in range(106500,123500 + 1,17):
        for i in range(2,x):
            if x % i == 0:
                ct += 1
                break
    return ct

print(part1(get_input()))
print(part2(get_input()))
