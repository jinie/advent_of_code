#!/usr/bin/env python3
import re
from collections import defaultdict


pat = re.compile(r'Step ([a-zA-Z]) must be finished before step ([a-zA-Z]) can begin.')
steps = set()
dependencies = defaultdict(set)

with open('07_input.txt','rt') as f:
    for l in f.readlines():
        l.strip()
        mat = pat.match(l)
        sv = (mat.group(1), mat.group(2))
        steps |= {sv[0],sv[1]}
        dependencies[sv[1]].add(sv[0])

done = list()
for _ in steps:
    done.append(min(x for x in steps if x not in done and dependencies[x] <= set(done)))
print(''.join(done))


def addtime(task):
    return ord(task) - ord('A') + 61

times = 0
done = set()
nworkers = 5
workers=[0] * nworkers
worker_tasks =[''] * nworkers
idx = 0
sec = 0

steps=list(steps)
while True:
    for widx in range(len(workers)):
        if workers[widx] > 0 :
            if workers[widx]-1 ==0:
                done.add(worker_tasks[widx])
                worker_tasks[widx] = ''
                workers[widx] = 0
                #print(f'{sec}: {widx} -> done')
            else:
                workers[widx]-=1
                continue


        if workers[widx] == 0 and len(steps):
            tasks = [t for t in steps if dependencies[t] <= set(done)]
            if len(tasks) == 0:
                continue
            else:
                task = min(tasks)
            steps.remove(task)
            workers[widx] = addtime(task)
            worker_tasks[widx] = task
            idx+=1
    if sum(workers) == 0:
        break
    print(f'{sec}: {workers} {worker_tasks} - {done}')
    sec+=1
print(sec)