#!/usr/bin/env python
import operator


def part1(input):
    results = [input]
    ca = input[:]
    while True:
        c2 = ca[:]
        i, v = max(enumerate(ca), key=operator.itemgetter(1))
        i2 = i
        c2[i] = 0
        while v > 0:
            i2 = i2 + 1 if i2 + 1 < len(c2) else 0
            c2[i2] += 1
            v -= 1
        if c2 in results:
            return len(results), c2
        else:
            results.append(c2)
        ca = c2

input = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'.split()
input = [int(i) for i in input]

# Part 1
i, input = part1(input)
print(i)

# Part 2
i, _ = part1(input)
print(i)
