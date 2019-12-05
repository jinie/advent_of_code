#!/usr/bin/env python
from collections import deque

class ModeIter:
    def __init__(self, n: int):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        value = self.n % 10
        self.n //= 10
        return value

class Intcode:
	_ptr = 0
	_running = False
	_output = []

	def __init__(self):
		self._instructions = {
			1: self.add,
			2: self.multiply,
			3: self.input,
			4: self.output,
			5: self.jump_if_true,
			6: self.jump_if_false,
			7: self.cmp_lt,
			8: self.cmp_eq,
			99: self.halt
		}

	def run(self, program, input=[]):
		self._running = True
		self._program = program
		self._ptr=0
		self._input = iter(input)
		while self._running is True:
			self.step()
		return self._output

	def get_instruction(self):
		instruction = self._program[self._ptr]
		self._ptr+=1
		return instruction

	def step(self):
		instruction = self.get_instruction()
		modes = ModeIter(instruction // 100)
		opcode = instruction % 100
		try:
			self._instructions[opcode](modes)
		except Exception as e:
			print(f'Error running instruction : {instruction} => {opcode}({modes}), output = {self._output}')
			raise(e)

	def get_param(self, mode):
		pos = self.get_instruction()
		if mode == 0:
			p = self._program[pos]
		else:
			p = pos
		return(p)

	def put_param(self, value):
		pos = self.get_instruction()
		self._program[pos] = value

	def add(self,modes):
		x1 = self.get_param(next(modes))
		x2 = self.get_param(next(modes))
		self.put_param(x1+x2)

	def multiply(self,modes):
		x1 = self.get_param(next(modes))
		x2 = self.get_param(next(modes))
		self.put_param(x1*x2)

	def input(self, modes):
		pos = self.get_instruction()
		i = next(self._input)
		self._program[pos] = i

	def output(self, modes):
		self._output.append(self.get_param(next(modes)))

	def jump_if_true(self, modes):
		cmp = self.get_param(next(modes))
		pos = self.get_param(next(modes))
		if cmp != 0:
			self._ptr=pos
	
	def jump_if_false(self, modes):
		cmp = self.get_param(next(modes))
		pos = self.get_param(next(modes))
		if cmp == 0:
			self._ptr=pos

	def cmp_lt(self, modes):
		c1 = self.get_param(next(modes))
		c2 = self.get_param(next(modes))
		pos = self.get_instruction()
		self._program[pos] = int(c1 < c2)

	
	def cmp_eq(self, modes):
		c1 = self.get_param(next(modes))
		c2 = self.get_param(next(modes))
		pos = self.get_instruction()
		self._program[pos] = int(c1 == c2)

	def halt(self,_):
		self._running = False

with open("input05.txt") as f:
	program = [int(c) for c in f.read().split(',')]

ic = Intcode()
print(ic.run(program.copy(),(1,)))
print(ic.run(program.copy(),(5,)))