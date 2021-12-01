
def get_input(fname):
    with open(fname,'rt') as f:
        lines = [int(l.strip()) for l in f.readlines()]
    return lines

lines = get_input('2020/input01.txt')
for i in range(0,len(lines)):
    for j in range(i+1,len(lines)):
        if lines[i]+lines[j] == 2020:
            print(f'Part 1: {lines[i]*lines[j]}')
        for k in range(j+1,len(lines)):
            if lines[i]+lines[j]+lines[k] == 2020:
                print(f'Part 2: {lines[i]*lines[j]*lines[k]}')

