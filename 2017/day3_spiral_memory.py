import math
from collections import defaultdict
target = 361527

#part 1
i = math.ceil(math.sqrt(target))
if i % 2 == 0:
  i += 1 
  
corners = [i**2 - ((i-1) * j) - math.floor(i/2) for j in range(4)]
steps = ((i-1)/2) + min([abs(corner - target) for corner in corners])
print('part 1:',steps)


#part 2
#https://oeis.org/A141481

def sum_table(table,x,y):
  return sum(table[i,j] for i in range(x-1, x+2) for j in range(y-1, y+2))
  
def spiral_table(target):
  table = defaultdict(int)
  side=1
  x,y = 0,0
  table[0,0] = 1
  csum = 1
  
  while csum < target:
    for _ in range(side): #increment x
      x+=1
      table[x,y] = sum_table(table,x,y)
      if table[x,y] > target: return table[x,y]
    for _ in range(side): #increment y
      y+=1
      table[x,y] = sum_table(table,x,y)
      if table[x,y] > target: return table[x,y]
    for _ in range(side+1): #decrement x
      x-=1
      table[x,y] = sum_table(table,x,y)
      if table[x,y] > target: return table[x,y]
    for _ in range(side+1): #decrement y
      y-=1
      table[x,y] = sum_table(table,x,y)
      if table[x,y] > target: return table[x,y]
    side+=2
    
print('part 2:',spiral_table(target))
