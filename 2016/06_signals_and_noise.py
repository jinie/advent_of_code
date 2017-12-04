#!/usr/bin/env python3
from collections import Counter

def part1(input):
	return ''.join(Counter(c).most_common(1)[0][0] for c in zip(*input))


def part2(input):
	return ''.join(Counter(c).most_common()[-1][0] for c in zip(*input))

with open('input06.txt','rt') as f:
	input = f.readlines()
	input = [l.strip('\r\n') for l in input]

print('part 1:{}'.format(part1(input)))
print('part 2:{}'.format(part1(input)))

