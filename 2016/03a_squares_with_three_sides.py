#!/usr/bin/env python

with open('input03.txt','rt') as f:
  input = f.read()
sides = [list(map(int, line.split())) for line in input.strip('\r').strip(' ').split('\n') if len(line) > 0]
print("Possible : {}".format([sum(i) > 2 * max(i) for i in sides].count(True)))