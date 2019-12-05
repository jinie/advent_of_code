#!/usr/bin/env python3
input=["109165","576723"]

decrease = lambda w: all(c1<=c2 for c1,c2 in zip(w, w[1:]))
multi = lambda p: any((p.count(c) == 2 for c in p))
double = lambda w: any(c1==c2 for c1,c2 in zip(w, w[1:]))
poss = set((p for p in (str(x) for x in range(int(input[0]), int(input[1]))) if decrease(p) and double(p)))
p2 = sum([multi(p) for p in poss])

print(len(poss))
print(p2)
