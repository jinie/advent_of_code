#!/usr/bin/env python3
import re
from collections import defaultdict

def get_input():
    input = {}
    with open('input20.txt', 'rt') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        input[i] = [(int(m[1]), int(m[2]), int(m[3])) for m in re.findall(r'(\w)=\<(-?\d+),\s*(-?\d+),\s*(-?\d+)\>', l)]
    return input


def collide(input):
    for tic in range(100):
        places = defaultdict(set)
        for i, (p,v,a) in input.items():
            places[tuple(p)].add(i)
            v = [x+y for x,y in zip(v, a)]
            p = [x+y for x,y in zip(p, v)]
            input[i] = [p,v,a]
        collided = {i for g in places.values() for i in g if len(g) > 1}
        input = {k:v for k,v in input.items() if k not in collided}
    return len(input)


# Part 1
input = get_input()
   
dt = lambda k: [x**2 + y**2 + z**2 for x, y, z in input[k][::-1]]
print(min(input, key=dt))

# Part 2
print(collide(get_input()))
