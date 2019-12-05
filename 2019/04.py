#!/usr/bin/env python3

input=["109165","576723"]

def check_multi(p):
    return any((p.count(c) == 2 for c in p))

def check_double(w):
	return any(c1==c2 for c1,c2 in zip(w, w[1:]))

def check_decrease(w):
	return all(c1<=c2 for c1,c2 in zip(w, w[1:]))

poss = set((p for p in [str(x) for x in range(int(input[0]), int(input[1]))] if check_decrease(p) and check_double(p)))
p2 = sum([check_multi(p) for p in poss])

print(len(poss))
print(p2)
