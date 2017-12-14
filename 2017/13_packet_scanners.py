#!/usr/#bin/env python3
def get_input():
    with open('input13.txt', 'rt') as f:
        lines = f.readlines()
        lines = [l.split(': ') for l in lines]
    # return lines
    ret = {int(l[0]): {'l': int(l[1])} for l in lines}
    return ret


def scanner_pos(depth, step):
    return step if step <= depth else (step - (step * depth)) % depth


input = get_input()
print(sum(i * input[i]['l'] for i in input.keys() if scanner_pos(input[i]['l'] - 1, i) == 0))
