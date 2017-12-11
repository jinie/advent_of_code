#!/usr/bin/env python3


def get_input():
    with open('input07.txt', 'rt') as f:
        input = [l.strip() for l in f]
    return input


def sum_children(nodes, node):
    total = nodes[node]['weight']
    if 'children' in nodes[node]:
        for n in nodes[node]['children']:
            total += sum_children(nodes, n)
    return total


def build_tree(input):
    nodes = {}
    for n in input:
        arr = n.split(' ')
        k = arr[0].strip(',')
        nodes[k] = {} if k not in nodes else nodes[k]
        nodes[k]['weight'] = int(arr[1].strip('(').strip(')').strip())
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
    ret = None
    if 'children' in nodes[root]:
        sums = {}
        for ch in nodes[root]['children']:
            csum = sum_children(nodes, ch)
            if csum not in sums:
                sums[csum] = [ch]
            else:
                sums[csum].append(ch)

        odds = [sums[k][0] for k in sums if len(sums[k]) == 1]
        if len(odds) == 1:
            ret = part2(nodes, odds[0])
    if ret is None:
        children = nodes[nodes[root]['parent']]['children']
        chsums = [sum_children(nodes, ch) for ch in children]
        rootsum = sum_children(nodes, root)
        if max(chsums) == rootsum:
            diff = nodes[root]['weight'] - (rootsum - min(chsums))
        else:
            diff = nodes[root]['weight'] + (max(chsums) - rootsum)
        ret = root,diff
    return ret


if __name__ == '__main__':
    nodes = build_tree(get_input())
    root = part1(nodes)[0]
    print("root =", root)
    print(part2(nodes, root))
