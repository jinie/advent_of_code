import math
target = 361527

#part 1
i = math.ceil(math.sqrt(target))
if i % 2 == 0:
  i += 1 
  
corners = [i**2 - ((i-1) * j) - math.floor(i/2) for j in range(4)]
steps = ((i-1)/2) + min([abs(corner - target) for corner in corners])
print(steps)


#part 2
#https://oeis.org/A141481
