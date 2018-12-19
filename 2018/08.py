#!/usr/bin/env python3
import sys
from collections import namedtuple

#sys.setrecursionlimit(1500)
Node = namedtuple('Node',['children','metadata'])

nodeinput = []
with open('08_input.txt','rt') as f:
	nodeinput = [int(i) for i in f.read().strip().split(' ')]



print(len(nodeinput))

def read_node(idx, input):
	
	n = Node(children=[], metadata=[])
	nchild = input[idx]
	idx+=1
	nmeta = input[idx]
	idx += 1
	for i in range(nchild):
		(idx, cn) = read_node(idx, input)
		n.children.append(cn)
	for i in input[idx:idx+nmeta]:
		n.metadata.append(i)
	idx+=nmeta
	#print(f'{idx} - nchildren={nchild}, nmeta={nmeta} : {n}')
	return (idx,n)

def sum_meta(node):
	msum = 0
	for n in node.children:
		msum += sum_meta(n)
	msum += sum(node.metadata)
	return msum

def sum_indexed(node):
	if len(node.children) == 0:
		return sum(node.metadata)
	else:
		msum = 0
		for m in node.metadata:
			if m > len(node.children) or m == 0:
				continue
			else:
				msum += sum_indexed(node.children[m-1])
		return msum

root = []
idx=0
while idx < len(nodeinput):
	idx, tree = read_node(idx,nodeinput)
	root.append(tree)
print(len(root))

msum = 0
for n in root:
	msum += sum_meta(n)
print(msum)

msum = 0
for n in root:
	msum += sum_indexed(n)
print(msum)