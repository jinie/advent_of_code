with open('02_input.txt','rt') as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

c2 = list()
c3 = list()

for l in lines:
    for le in list(l):
        if l not in c2 and l.count(le) == 2:
           c2.append(l)
        if l not in c3 and l.count(le) == 3:
            c3.append(l)
print(len(c2) * len(c3))

for b1i in range(len(c2)):
    for b2i in range(b1i+1,len(c2)):
        ndif = 0
        dpos = -1

        b1 = c2[b1i]
        b2 = c2[b2i]
        for li in range(len(list(b1))):
            if b1[li] != b2[li]:
                ndif += 1
                dpos = li
                if ndif > 1:
                    break
        else:
            print("only one char difference (idx={})\n\t{} [{}] {}\n\t{} [{}] {}".format(dpos,b1[:dpos],b1[dpos],b1[dpos+1:],b2[:dpos],b2[dpos],b2[dpos+1:]))
                
            
