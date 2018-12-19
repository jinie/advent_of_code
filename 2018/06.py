#!/usr/bin/env python3
from collections import namedtuple
from operator import attrgetter
import sys
def get_input():
	with open('06_input.txt','rt') as f:
		return [(int(x), int(y)) for (x,y) in [l.strip().split(',') for l in f.readlines()]]

def dt(x1, y1, x2, y2):
    return abs((abs(x1) - abs(x2)) + (abs(y1) - abs(y2)))

def part1():
	lines = get_input()
	Coord = namedtuple('Coord','x,y,distance,nxplus,nxminus,nyplus,nyminus,area')
	ycords = sorted([y for (x,y) in lines])
	xcords = sorted([x for (x,y) in lines])

	ll = [(x,y) for (x,y) in lines if x < maxx and x > minx and y < maxy and y > miny]
	for (x,y) in ll:
		xindex = xcords.index(x)
		yindex = ycords.index(y)
		nxp = xcords[xindex+1]
		nxm = xcords[xindex-1]
		nyp = ycords[yindex+1]
		nym = ycords[yindex-1]

		for mx in range(x,nxp):
			if dt(x,y,nxp,)


part1()