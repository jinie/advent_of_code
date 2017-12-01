#!/usr/bin/env python
with open('input03.txt','rt') as f:
  input = f.read()

tr = []

for x in input.split('\n'):
	x = x.strip('\r').strip(' ')
	v =  [int(y) for y in x.split()]
	if len(v) > 0:
		tr.append(v)

print(sum(a + b > c and b + c > a and a + c > b for column in zip(*tr) for a, b, c in zip(*[iter(column)]*3)))
