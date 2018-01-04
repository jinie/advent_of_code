def get_input():
    with open('input22.txt') as f:
        return [l.strip() for l in f.readlines()]


class Sporifica:
    x = 0
    y = 0
    ict = 0
    infected = dict()

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

    def turn(self, heading, direction):
        return self.ttable[direction][heading]

    def move(self):
        if self.heading == 'S':
            self.y += 1
        elif self.heading == 'N':
            self.y -= 1
        elif self.heading == 'E':
            self.x += 1
        else:
            self.x -= 1

    def burst(self, simple=True):

        if (self.x, self.y) not in self.infected.keys():
            self.infected[(self.x, self.y)] = 'C'

        direction = self.dir_states[self.infected[(self.x, self.y)]]
        self.infected[(self.x, self.y)] = self.states[self.infected[(self.x, self.y)]]

        if self.infected[(self.x, self.y)] == 'I':
            self.ict += 1

        if direction is not None:
            self.heading = self.turn(self.heading, direction)
        self.move()

    def simulate(self, bursts, inp, simple=True):
        self.infected = dict()
        self.ict = 0
        for y, row in enumerate(inp):
            for x, c in enumerate(row):
                if c == '#':
                    self.infected[(x, y)] = 'I'
        self.x, self.y = len(inp) // 2, (len(inp) // 2)
        self.heading = 'N'
        self.states = self.simple_states if simple else self.evolved_states
        for _ in range(bursts):
            self.burst(simple=simple)
        return(self.ict)


if __name__ == '__main__':
    inp = get_input()
    v = Sporifica()
    print(v.simulate(10000, inp))
    print(v.simulate(10000000, inp, simple=False))
