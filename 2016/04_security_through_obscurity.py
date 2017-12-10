#/usr/bin/env python
import string

def real_rooms(rooms):
  i = 0
  for room in rooms:
    *name, remain = room.split('-')
    id, check = remain.split('[')
    res = sorted({*''.join(name)}, key=lambda x: (-''.join(name).count(x), x))
    #print(l[:5],[*check.rstrip(']')])
    if res[:5] == [*check.strip(']')]:
      i += int(id)
  return i
  
def north_pole_rooms(arg):
  ret=[]
  for x in arg:
    *name, remain = x.split('-')
    id = int(remain.split('[')[0])
    for w in name:
      s = ''.join(string.ascii_lowercase[(ord(c) - ord('a') + id) % 26] for c in w)
      if s.find('north') != -1:
        ret.append((x,s,id))
  return ret

rooms = []
with open('input04.txt','rt') as f:
  rooms = f.readlines()
  for i,room in enumerate(rooms):
    rooms[i] = room.strip('\n')

print('Valid Rooms:{}'.format(real_rooms(rooms)))
print('North Pole rooms:{}'.format(north_pole_rooms(rooms)))
