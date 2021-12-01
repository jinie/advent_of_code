with open('2020/input12.txt','rt') as f:
    directions = [(l[0],int(l[1:])) for l in f.readlines()]

def turn(heading, direction, degrees):
    ct = degrees//90
    ch = {'N':0, 'E': 90, 'S': 180, 'W':270}[heading]
    for i in range(ct):
        ch = ch-90 if direction == 'L' else ch+90
        if ch > 270: ch = 0
        elif ch < 0: ch = 270
    return "NESW"[ch//90]

moves = {
    'N': lambda x, heading, position: (heading, complex(position.real, position.imag+x)),
    'S': lambda x, heading, position: (heading, complex(position.real, position.imag-x)),
    'E': lambda x, heading, position: (heading, complex(position.real+x, position.imag)),
    'W': lambda x, heading, position: (heading, complex(position.real-x, position.imag)),
    'F': lambda x, heading, position: moves[heading](x,heading,position),
    'L': lambda x, heading, position: (turn(heading, 'L', x), position),
    'R': lambda x, heading, position: (turn(heading, 'R', x), position),
}

heading='E'
position = 0+0j

for d in directions:
    heading, position = moves[d[0]](d[1], heading, position)

print(f'Part 1: {abs(abs(0)-abs(position.real) + abs(0) - abs(position.imag))}')