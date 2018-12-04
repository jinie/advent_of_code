#!/usr/bin/env python
from pprint import pprint

def hash(input, elements=list(range(256)), repeat=1):
    cpos = 0
    skip = 0
    for _ in range(repeat):
        for i in input:
            six = cpos
            eix = cpos + i
            if eix < len(elements):
                subs = elements[six:eix]
                elements[six:eix] = subs[::-1]
            else:
                rlen = len(elements) - cpos
                subs = elements[six:] + elements[:i - rlen]
                subs = subs[::-1]
                elements = subs[rlen:] + elements[i - rlen:six] + subs[:rlen]
            cpos = (cpos + i + skip) if (cpos + i + skip) < len(elements) else (cpos + i + skip) % len(elements)
            skip += 1
    return elements


def hexhash(orginput):
    input = [ord(a) for a in orginput] + [17, 31, 73, 47, 23]
    sparse = hash(input, list(range(256)), 64)
    block = []
    for i in range(0, 256, 16):
        value = sparse[i]
        for j in sparse[i + 1:i + 16]:
            value ^= j
        block.append(value)
    return ''.join('{:02x}'.format(b) for b in block)


def part1(input):
    grid = []
    for i in range(128):
        inp = '{}-{}'.format(input, i)
        h = hexhash(inp)
        grid.append(''.join(['{:04b}'.format(int(str(c), 16)) for c in h]))

    print('used', grid.count('1'))
    return grid


visited = set()
grid = None


def search(x, y):
    if (x, y) in visited:
        return
    if y >= len(grid) or x >= len(grid[y]):
        return
    if grid[y][x] != '1':
        return
    visited.add((x, y))
    if x > 0:
        search(x - 1, y)
    if x < len(grid[y]):
        search(x + 1, y)
    if y > 0:
        search(x, y - 1)
    if y < len(grid):
        search(x, y + 1)


def part2():
    groups = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '1' and (x, y) not in visited:
                groups += 1
                search(x, y)
    pprint(groups)


input = 'uugsqrei'
grid = part1(input)
part2()
