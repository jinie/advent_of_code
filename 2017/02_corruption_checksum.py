with open('input02.txt','rt') as f:
	rows=f.readlines()
	rows=[row.strip('\n').split('\t') for row in rows]
	for i,r in enumerate(rows):
		rows[i]=[int(d) for d in r]

sums = sum([max(r)-min(r) for r in rows])
print(sums)

sums=0
for i,row in enumerate(rows):
		sums+= sum([x/y for x in row for y in row if y >0 and y!=x and x%y==0])
print(sums)

