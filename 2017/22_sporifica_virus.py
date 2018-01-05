from collections import defaultdict


def get_input():
    with open('input22.txt') as f:
        return [l.strip() for l in f.readlines()]


class Sporifica:

    def defaultvalue(self):
        return 'C'

    def load_initial(self, inp):
        infected = defaultdict(self.defaultvalue)
        for y, row in enumerate(inp):
            for x, c in enumerate(row):
                if c == '#':
                    infected[(x, y)] = 'I'
        return infected

    def simulate(self, bursts, inp, simple=True):
        # States
        # (C)lean -> (I)nfected
        simple_states = {'C': 'I', 'I': 'C'}
        # (C)lean -> (W)eakened -> (I)nfected -> (F)lagged
        evolved_states = {'C': 'W', 'W': 'I', 'I': 'F', 'F': 'C'}
        dir_states = {'I': 'R', 'F': 'T', 'C': 'L', 'W': None}
        ttable = {
            'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
            'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
            'T': {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
        }        
        infected = self.load_initial(inp)
        x, y = len(inp) // 2, (len(inp) // 2)
        heading = 'N'
        states = simple_states if simple else evolved_states
        ict = 0
        for _ in range(bursts):
            idx = (x,y)
            v = infected[idx]
            direction = dir_states[v]
            nv = states[v]

            infected[idx] = nv

            if direction is not None:
                heading = ttable[direction][heading]

            if heading == 'S': y+=1
            elif heading == 'N': y-=1
            elif heading == 'E': x+=1
            else: x-=1

            if nv == 'I':
                ict += 1
        return(ict)


if __name__ == '__main__':
    inp = get_input()
    v = Sporifica()
    print(v.simulate(10000, inp))
    print(v.simulate(10000000, inp, simple=False))
