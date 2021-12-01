with open('2020/input03.txt','rt') as f:
    slope = [l.strip() for l in f.readlines()]

def run_slope(xmov, ymov):
    sp = (0+0j)
    np = lambda pos,move,max: pos+move if pos+move < max else (pos+move)-max
    trees = []
    while(sp.imag < len(slope)):
        if slope[int(sp.imag)][int(sp.real)] == '#':
            trees.append(sp)
        ny = sp.imag + ymov if sp.imag + ymov < len(slope) else len(slope) #np(sp.imag, ymov, len(slope))
        nx = np(sp.real, xmov, len(slope[int(sp.imag)]))
        sp = complex(nx,ny)
    return(len(trees))

p1 = run_slope(3,1)
print(f'Part 1: {p1}')

patterns = ((1,1), (5,1), (7,1), (1,2))
res = p1
for p in patterns:
    res = res * run_slope(p[0],p[1])
print(f'Part 2: {res}')

