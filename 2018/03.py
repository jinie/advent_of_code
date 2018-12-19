import re
import collections

Pattern = collections.namedtuple('Pattern', 'id x y w h')
patterns = list()

rep = re.compile("#(\d+)\s*@\s*(\d+),(\d+):\s*(\d+)x(\d+)")
with open("03_input.txt", "rt") as f:
    lines = f.readlines()
for l in lines:
    m = rep.match(l)
    if m:
        patterns.append(Pattern(id=int(m.group(1)), x=int(m.group(2)), y=int(m.group(3)), w=int(m.group(4)), h=int(m.group(5))))


cloth = [0 for i in range(1000 * 1000)]
rowoffset = 1000

#Part 1
for p in patterns:
    for h in range(p.y, p.y + p.h):
        for w in range(p.x, p.x + p.w):
            pos = (rowoffset * h) + w
            cloth[pos] += 1
print(len([x for x in cloth if x > 1]))


#Part 2
for p in patterns:
    acs = 0  # Actual Sum of the cloth squares
    for h in range(p.y, p.y + p.h):
        acs += sum(cloth[(rowoffset * h) + p.x:(rowoffset * h) + p.x + p.w])

    if (p.w*p.h) == acs:
        print(p.id)
        break
