#!/usr/bin/env python3
import re


def get_input():
    with open('input08.txt', 'rt') as f:
        input = [l.strip() for l in f.readlines()]
    return input


def parse_line(line):
    return re.match("(\S+)\s(\S+)\s([-]?\d+)\s(\S+)\s(\S+)\s(\S+)\s(\S+).*", line).groups()


def parse_condition(op, cmp, val):
    if op not in registers:
        registers[op] = 0
    ret = False

    if cmp == '==':
        ret = (registers[op] == val)
    elif cmp == '<':
        ret = (registers[op] < val)
    elif cmp == '>':
        ret = (registers[op] > val)
    elif cmp == '<=':
        ret = (registers[op] <= val)
    elif cmp == '>=':
        ret = (registers[op] >= val)
    elif cmp == '!=':
        ret = (registers[op] != val)
    else:
        raise "Unknown operator" + cmp
    print("{} {} {} == {}".format(registers[op], cmp, val, ret))
    return ret


registers = {}
max_value = 0


def part1():
    global registers
    global max_value
    for line in get_input():
        opts = parse_line(line)
        if opts[0] not in registers:
            registers[opts[0]] = 0
        if parse_condition(opts[4], opts[5], int(opts[6])):
            if opts[1] == 'inc':
                registers[opts[0]] += int(opts[2])
            elif opts[1] == 'dec':
                registers[opts[0]] -= int(opts[2])
            if registers[opts[0]] > max_value:
                max_value = registers[opts[0]]
    mk = max(registers, key=registers.get)
    print(registers[mk])


def part2():
    global registers
    global max_value

    print(max_value)


if __name__ == '__main__':
    part1()
    part2()
