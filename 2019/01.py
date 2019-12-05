#!/usr/bin/env python
from math import floor
input = []
with open('input01.txt') as f:
	input = [float(l) for l in f]

def get_fuel(mass):
	fuel = (floor(mass/3)-2)
	return 0 if fuel < 0 else fuel

fuels = [get_fuel(m) for m in input]
total = sum(fuels)
print(f"Part1 : {total}")

afuels = []
for f in fuels:
	while f > 0:
		f = get_fuel(f)
		afuels.append(f)

total = total + sum(afuels)
print(f'Part2: {total}')