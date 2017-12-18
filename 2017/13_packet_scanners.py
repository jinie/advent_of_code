#!/usr/#bin/env python3
from itertools import count


def get_input():
    with open('input13.txt', 'rt') as f:
        lines = f.readlines()
        lines = [l.split(': ') for l in lines]
    ret = {int(l[0]): int(l[1]) for l in lines}
    return ret


def scanner_pos(depth, step):
    offset = step % ((depth - 1) * 2)
    return 2 * (depth - 1) - offset if offset > depth - 1 else offset


def part1():
    input = get_input()
    print(sum(i * input[i] for i in input.keys()
              if scanner_pos(input[i], i) == 0))


def part2():
    input = get_input()
    for delay in count(1):
        if any(scanner_pos(input[d], d + delay) == 0 for d in input):
            continue
        else:
            print(delay)
            return


part1()
part2()
