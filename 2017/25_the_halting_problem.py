#!/usr/bin/env python3
from collections import defaultdict

def state_machine(tape, cursor, state):
	if state == 'A':
		if tape[cursor] == 0:
			tape[cursor] = 1
			cursor += 1
		else:
			del tape[cursor]
			cursor -= 1
		state = 'B'
	elif state == 'B':
		if tape[cursor] == 0:
			del tape[cursor]
			cursor += 1
			state = 'C'
		else:
			tape[cursor] = 1
			cursor -= 1
			state = 'B'
	elif state == 'C':
		if tape[cursor] == 0:
			tape[cursor] = 1
			cursor += 1
			state = 'D'
		else:
			del tape[cursor]
			cursor -= 1
			state = 'A'
	elif state == 'D':
		if tape[cursor] == 0:
			state = 'E'
		else:
			state = 'F'
		tape[cursor] = 1
		cursor -= 1
	elif state == 'E':
		if tape[cursor] == 0:
			tape[cursor] = 1
			state = 'A'
		else:
			tape[cursor] = 0
			state = 'D'
		cursor -= 1
	elif state == 'F':
		if tape[cursor] == 0:
			tape[cursor] = 1
			cursor += 1
			state = 'A'
		else:
			tape[cursor] = 1
			cursor -= 1
			state = 'E'
	return cursor,state


tape = defaultdict(int)
steps = 12586542
cursor = 0
state = 'A'

for i in range(steps):
	cursor, state = state_machine(tape, cursor, state)
print(sum(tape.values()))