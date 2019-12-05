#!/usr/bin/env python3

dirmap = {'U':0+1j, 'D':0+-1j, 'L':-1+0j, 'R':1+0j}

with open('input03.txt') as f:
	wires = [w for w in f.read().split('\n')]
	for i in range(len(wires)):
		wires[i] = [p for p in wires[i].split(',')]

def map_wire(wire):
	grid = {}
	pos = 0 + 0j
	steps = 0

	for p in wire:
		dir = p[0]
		dist = int(p[1:])

		ndir = dirmap[dir]
		for _ in range(dist):
			pos += ndir
			steps += 1
			if pos not in grid.keys():
				grid[pos] = steps

	return grid


w1 = map_wire(wires[0])
w2 = map_wire(wires[1])
bw = set(w1.keys()).intersection(set(w2.keys()))

part1 = min([abs(x.real)+abs(x.imag) for x in bw])
print(part1)
part2 = min([w1[pos]+w2[pos] for pos in bw])
print(part2)