#!/usr/bin/env python3
from itertools import count

def part1(input):
	ip = 0
	for i in count():
		oip = ip
		ip = ip + input[ip]
		if ip < 0 or ip >= len(input):
			return i+1
		input[oip] += 1

def part2(input):
	ip = 0
	for i in count():
		oip = ip
		ip = ip + input[ip]
		if ip < 0 or ip >= len(input):
			return i+1
		input[oip] = input[oip] + 1 if input[oip] < 3 else input[oip]-1


input = []
with open('input05.txt','rt') as f:
	for l in f:
		input.append(int(l.strip('\r\n ')))

print(part1(input[:]))
print(part2(input[:]))