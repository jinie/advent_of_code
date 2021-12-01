import re

def get_input():
    with open('2020/input07.txt','rt') as f:
        lines = [l.strip() for l in f.readlines()]

    rpat = re.compile('\s*(\d?)\s*(\w*\s?\w*?)\s*(?:bag)\s*(?:contain)?')
    rules = dict()
    for l in lines:
        l = l.replace(",","").replace('bags','bag').replace('contains','contain').replace('.','')
        #print(l)
        matches = rpat.findall(l)
        prev = None
        for g in matches:
            pr = prev
            if g[1] not in rules:
                rules[g[1]] = [{'ct':int(g[0]) if g[0] != '' else 1, 'prev':pr},]
            else:
                rules[g[1]].append({'ct':int(g[0]) if g[0] != '' else 1, 'prev':pr})
            prev = g[1]

    return rules

def get_bags(color, rules):
    ct = 0
    if color == 'no other':
        return ct
    for (k,va) in rules.items():
        for v in va:
            if color == v['prev']:
                ct+=v['ct']
                ct += get_bags(k,rules)
            elif v['prev'] == None:
                continue
    return ct
        
rules = get_input()
#gold = [k for (k,v) in rules.items() if v['prev']=='shiny gold']
ct = get_bags('shiny gold', rules)
print(ct)