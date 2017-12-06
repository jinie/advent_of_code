#!/usr/bin/env python3
#from collections import defaultdict

def part1(input):
	valid_ct = 0
	
	for line in input:
		words = line.split(' ')
		cc = set(words)
		if len(cc) == len(words):
			valid_ct +=1
	return valid_ct

def part2(input):
	valid_ct = 0

	for line in input:
		words = line.split(' ')
		wl = []
		for w in words:
			ll = sorted(list(w))
			wl.append(ll)

		for i,w in enumerate(wl):
			if w in wl[i+1:]:
				break
		else:
			valid_ct+=1
	return valid_ct

with open('input04.txt','rt') as f:
	input = f.readlines()
	input = [l.strip('\r\n') for l in input]


print("Valid passwords : {}".format(part1(input)))
print("Valid passwords : {}".format(part2(input)))

with open('input04.txt') as f:
	input = f.read()
res = [len({(*sorted(w),) for w in ws}) == len(ws) for ws in map(str.split, input.splitlines()) if len({*ws}) == len(ws)]
print('Number of valid passphrases:', len(res))
print('Number of valid passphrases (no anagrams):', sum(res))