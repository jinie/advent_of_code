#!/usr/bin/env python

with open('input02.txt') as f:
	opcodes = [int(c) for c in f.read().split(',')]

def part1(noun, verb):
	program = [x for x in opcodes]
	program[1] = noun
	program[2] = verb
	pos = 0
	while True:
		if program[pos] in [1,2]:
			if program[pos] == 1:
				program[program[pos+3]] = program[program[pos+1]]+program[program[pos+2]]
			elif program[pos] == 2:
				program[program[pos+3]] = program[program[pos+1]]*program[program[pos+2]]
			pos+=4
		elif program[pos] == 99:
			return program[0]


print(part1(12,2))

for i in range(99):
	for j in range(99):
		if part1(i,j) == 19690720:
			print(f'{i},{j}')
			break