#!/usr/bin/env python


class taxi:
    prevloc = set()
    eblocation = None

    def turn(self, direction, nd):
        if direction == '+y':
            return '-x' if nd == 'L' else '+x'
        elif direction == '-y':
            return '+x' if nd == 'L' else '-x'
        elif direction == '+x':
            return '+y' if nd == 'L' else '-y'
        elif direction == '-x':
            return '-y' if nd == 'L' else '+y'

    def dt(self, x1, y1, x2, y2):
        return abs((abs(x1) - abs(x2)) + (abs(y1) - abs(y2)))

    def check_ebl(self, pos):
        if pos in self.prevloc:
            self.eblocation = pos
        else:
            self.prevloc.add(pos)

    def logmove(self, x, y, direction, distance):
        if direction[1] == 'x':
            if direction[0] == '+':
                for i in range(x, x + distance, 1):
                    self.check_ebl((i, y))
            elif direction[0] == '-':
                for i in range(x, x - distance, -1):
                    self.check_ebl((i, y))
        if direction[1] == 'y':
            if direction[0] == '+':
                for i in range(y, y + distance, 1):
                    self.check_ebl((x, i))
            elif direction[0] == '-':
                for i in range(y, y - distance, -1):
                    self.check_ebl((x, i))

    def run(self, directions):
        curx, cury = 0, 0
        direction = '+y'

        for d in directions:
            head, dist = d[0], int(d[1:])
            ox, oy = curx, cury
            direction = self.turn(direction, head)
            if direction[0] == '+':
                if direction[1] == 'x':
                    curx += dist
                else:
                    cury += dist
            else:
                if direction[1] == 'y':
                    cury -= dist
                else:
                    curx -= dist

            if self.eblocation is None:
                self.logmove(ox, oy, direction, dist)

        x, y = self.eblocation
        print("distance from 0,0 -> {},{} = {}".format(curx, cury, self.dt(0, 0, curx, cury)))
        print("Easter bunny location is at {},{}, distance from {},{} is {}".format(
            x, y, 0, 0, self.dt(0, 0, x, y)))


directions = [x.strip() for x in "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3".split(",")]
taxi().run(directions)
