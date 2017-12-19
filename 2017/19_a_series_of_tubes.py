#!/usr/bin/env python3

def get_input():
	with open('input19.txt','rt') as f:
		input = f.read().split('\n')
	return input

def navigate(input):
	ret = ''
	d = 'd'
	y = 0
	x = (input[0].index('|'))
	stp = 0
	while input[y][x] != ' ':
		if d == 'd':
			y+=1
		elif d == 'u':
			y-=1
		elif d == 'l':
			x-=1
		elif d == 'r':
			x+=1
		stp+=1
		if input[y][x] == '+':
			if d in ('l','r'):
				d = 'u' if input[y-1][x] != ' ' else 'd'
			elif d in ('u','d'):
				d = 'l' if input[y][x-1] != ' ' else 'r'

		elif input[y][x] not in ('|','-'):
			ret+=input[y][x]

	return ret,stp


input = get_input()
print(navigate(input))