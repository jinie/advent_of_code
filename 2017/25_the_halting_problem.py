#!/usr/bin/env python3
from collections import defaultdict

states = {
    'A': ((1,  1, 'B'), (0, -1, 'B')),
    'B': ((0,  1, 'C'), (1, -1, 'B')),
    'C': ((1,  1, 'D'), (0, -1, 'A')),
    'D': ((1, -1, 'E'), (1, -1, 'F')),
    'E': ((1, -1, 'A'), (0, -1, 'D')),
    'F': ((1,  1, 'A'), (1, -1, 'E')),
}

tape = defaultdict(int)
steps = 12586542
cursor = 0
state = 'A'

for _ in range(steps):
	value = tape[cursor]
	wr,move,state = states[state][value]
	tape[cursor] = wr
	cursor += move

print(sum(tape.values()))