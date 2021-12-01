def part1():
    with open('2020/input06.txt','rt') as f:
        groups = []
        group = set()
        for l in f.readlines():
            l = l.strip()
            if l=='':
                groups.append(group)
                group=set()
            else:
                for c in l: group.add(c)

    gsum = sum([len(set(g)) for g in groups])
    print(f'Part 1: {gsum}')

def part2():
    with open('2020/input06.txt','rt') as f:
        input = [l.strip() for l in f.readlines() ]

    ct = 0
    group = list()
    for l in input:
        if l == '':
            common = group[0].intersection(*group[1:])
            ct+=len(common)
            group = list()
        else:
            group.append(set(l))
    print(f'Part 2: {ct}')

part1()
part2()
