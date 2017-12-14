#!/usr/bin/env python3


def get_input():
    with open('input11.txt', 'rt') as f:
        input = f.read().strip().split(',')
    return input


def hexdistance(x, y):
    x, y = abs(x), abs(y)

    if y > x:
        return x + (y - x) / 2
    elif y < x:
        return y + (x - y) / 2
    else:
        return x


def part1(input):
    x, y = 0, 0
    furthestdistance = 0

    for dir in input:
        if dir == 'n':
            y += 2
        elif dir == 's':
            y -= 2
        elif dir == 'se':
            x += 1
            y -= 1
        elif dir == 'sw':
            x -= 1
            y -= 1
        elif dir == 'nw':
            x -= 1
            y += 1
        elif dir == 'ne':
            x += 1
            y += 1
        dist = hexdistance(x, y)
        if dist > furthestdistance:
            furthestdistance = dist
    return hexdistance(x, y), furthestdistance

input = get_input()
dist, furthest = part1(input)
print("Part 1:", dist)
print("Furthest Distance:", furthest)
