#!/usr/bin/env python3

dirx = {'U':0, 'D':0, 'L':-1, 'R':1}
diry = {'U':1, 'D':-1, 'L':0, 'R':0}

with open('input03.txt') as f:
	wires = [w for w in f.read().split('\n')]
	for i in range(len(wires)):
		wires[i] = [p for p in wires[i].split(',')]

def map_wire(wire):
	grid = {}
	y = 0
	x = 0
	steps = 0
	
	for p in wire:
		dir = p[0]
		dist = int(p[1:])

		for _ in range(dist):
			x += dirx[dir]
			y += diry[dir]
			steps += 1
			if (x,y) not in grid.keys():
				grid[(x,y)] = steps

	return grid


w1 = map_wire(wires[0])
w2 = map_wire(wires[1])
bw = set(w1.keys()) & set(w2.keys())

part1 = min([abs(x)+abs(y) for (x,y) in bw])
print(part1)
part2 = min([w1[pos]+w2[pos] for pos in bw])
print(part2)