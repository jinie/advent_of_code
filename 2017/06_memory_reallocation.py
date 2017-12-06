#!/usr/bin/env python
import operator


def part1(input):
    results = [input]
    c2 = input
    while True:
        c2 = c2[:]
        i, v = max(enumerate(c2), key=operator.itemgetter(1))
        c2[i] = 0
        while v > 0:
            i = i + 1 if i + 1 < len(c2) else 0
            c2[i] += 1
            v -= 1
        if c2 in results:
            return len(results), c2
        else:
            results.append(c2)

input = [int(i) for i in '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'.split()]

# Part 1
i, input = part1(input)
print(i)

# Part 2
i, _ = part1(input)
print(i)
