#!/usr/bin/env python3
from collections import defaultdict, deque


def get_input():
    with open('input18.txt', 'rt') as f:
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
        reg['freq'] = get(x)
        reg['part2'] += 1
    elif op == 'jgz':
        if get(x) > 0:
            return ip + y, True
    return ip + 1, True


def part1(input):
    reg = defaultdict(int)
    ip = 0
    while ip >= 0 and ip < len(input):
        ip, _ = execute(reg, ip, input[ip])
        if 'part1_freq' in reg:
            return reg['part1_freq']


def part2(input):
    reg0, reg1 = defaultdict(int), defaultdict(int)
    reg1['p'] = 1
    ip0, ip1 = 0, 0
    q0, q1 = deque(), deque()

    while True:
        if ip1 >= 0 and ip1 < len(input):
            ip1, s1 = execute(reg1, ip1, input[ip1], iq=q0, oq=q1, pid=1)
        if ip0 >= 0 and ip0 < len(input):
            ip0, s0 = execute(reg0, ip0, input[ip0], iq=q1, oq=q0, pid=0)
        if s0 is False and s1 is False:
            return reg1['part2']

print('Part 1:',part1(get_input()))
print('Part 2:',part2(get_input()))
