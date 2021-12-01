with open('2020/input09.txt','rt') as f:
    lines = [int(l.strip()) for l in f.readlines()]

vfound = lambda x,testvalues: any(True for i in range(len(testvalues)) if x-testvalues[i] in testvalues[i+1:])
bad = None
#Part 1
for i in range(25,len(lines)):
    if not vfound(lines[i],lines[i-25:i]):
        print(f'{lines[i]} not found')
        bad=lines[i]

#Part 2
total = []
for l in lines:
    total.append(l)
    while sum(total) > bad: total.pop(0)
    if len(total) > 1 and sum(total) == bad: break
print(f'Part2: {min(total)}+{max(total)}={min(total)+max(total)}')