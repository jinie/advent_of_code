from collections import defaultdict


def get_input():
    with open('input22.txt') as f:
        return [l.strip() for l in f.readlines()]


class Sporifica:
    # States
    # (C)lean -> (I)nfected
    simple_states = {'C': 'I', 'I': 'C'}
    # (C)lean -> (W)eakened -> (I)nfected -> (F)lagged
    evolved_states = {'C': 'W', 'W': 'I', 'I': 'F', 'F': 'C'}
    states = simple_states
    dir_states = {'I': 'R', 'F': 'T', 'C': 'L', 'W': None}
    ttable = {
        'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
        'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
        'T': {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
    }

    def defaultvalue(self):
        return 'C'

    def load_initial(self, inp):
        infected = defaultdict(self.defaultvalue)
        for y, row in enumerate(inp):
            for x, c in enumerate(row):
                if c == '#':
                    infected[(x, y)] = 'I'
        return infected

    def turn(self, heading, direction):
        return self.ttable[direction][heading]

    def move(self, x, y, heading):
        if heading == 'S':
            return (x, y + 1)
        elif heading == 'N':
            return (x, y - 1)
        elif heading == 'E':
            return (x + 1, y)
        else:
            return (x - 1, y)

    def burst(self, x, y, heading, infected):
        v = infected[(x,y)]
        direction = self.dir_states[v]
        nv = self.states[v]
        
        infected[(x, y)] = nv

        if direction is not None:
            heading = self.turn(heading, direction)
        x, y = self.move(x, y, heading)

        return x, y, heading, nv == 'I'

    def simulate(self, bursts, inp, simple=True):
        infected = self.load_initial(inp)
        x, y = len(inp) // 2, (len(inp) // 2)
        heading = 'N'
        self.states = self.simple_states if simple else self.evolved_states
        ict = 0
        for _ in range(bursts):
            x, y, heading,inf = self.burst(x, y, heading, infected)
            if inf:
                ict+=1
        return(ict)


if __name__ == '__main__':
    inp = get_input()
    v = Sporifica()
    print(v.simulate(10000, inp))
    print(v.simulate(10000000, inp, simple=False))
