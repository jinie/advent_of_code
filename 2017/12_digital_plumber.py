#!/usr/bin/env python3
pipes = dict()
visited = set()


def get_input():
    with open('input12.txt', 'rt') as f:
        input = [l.strip().split('<->') for l in f.readlines()]
    return input


def create_pipes(input):
    for prog in input:
        pipes[int(prog[0])] = [int(i) for i in prog[1].strip().split(',')]

def get_group(p):
	ret = set()
	to_visit = [p]
	while len(to_visit) > 0:
		pp = to_visit.pop()
		ret.add(pp)
		to_visit += [pipe for pipe in pipes[pp] if pipe not in ret]
	return ret

def part1(search):
    return len(get_group(0))

def part2():
	ret = []
	to_visit = set(pipes.keys())
	while len(to_visit) > 0:
		g = get_group(to_visit.pop())
		to_visit = to_visit.difference(g)
		ret.append(g)
	return ret


create_pipes(get_input())
print("Part 1:", part1(0))
print("Part 2:",len(part2()))