#!/usr/bin/env python3


def get_input():
    with open('input07.txt', 'rt') as f:
        input = [l.strip() for l in f]
    return input


def build_tree(input):
    nodes = {}
    for n in input:
        arr = n.split(' ')
        k = arr[0].strip(',')
        nodes[k] = {} if k not in nodes else nodes[k]
        nodes[k]['weight'] = int(arr[1][1].strip('(').strip(')').strip())

        if '->' in arr:
            arr = [v.strip(',') for v in arr]
            for cn in arr[3:]:
                nodes[cn] = {} if cn not in nodes else nodes[cn]
                nodes[cn]['parent'] = k

            nodes[k]['children'] = arr[3:]

    return nodes


def part1(nodes):
    return [n for n in nodes.keys() if 'parent' not in nodes[n].keys() and 'children' in nodes[n].keys()]


def part2(nodes, root):
    # TODO:
    pass


if __name__ == '__main__':
    nodes = build_tree(get_input())
    root = part1(nodes)[0]
    print("root =", root)
