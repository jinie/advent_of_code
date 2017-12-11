#!/usr/bin/env python


def get_input():
    with open('input09.txt', 'rt') as f:
        input = f.read().strip()
    return input


def test_examples():
    examples = [
        ['{<{}}>}', 1],
        ['{}', 1],
        ['{{{}}}', 6],
        ['{{},{}}', 5],
        ['{{{},{},{{}}}}', 16],
        ['{<a>,<a>,<a>,<a>}', 1],
        ['{{<ab>},{<ab>},{<ab>},{<ab>}}', 9],
        ['{{<!!>},{<!!>},{<!!>},{<!!>}}', 9],
        ['{{<a!>},{<a!>},{<a!>},{<ab>}}', 3]
    ]

    for e in examples:
        input = e[0]
        assert (part1(input)[0] == e[1])


def part1(input):
    escape = False
    garbage = False
    total = 0
    group_ct = 0
    garbage_ct = 0
    i = 0
    for i, c in enumerate(input):
        if garbage:
            if escape:
                escape = False
            elif c == '>':
                garbage = False
            elif c == '!':
                escape = True
            else:
                garbage_ct += 1
        elif c == '{':
            group_ct += 1
            total += group_ct
        elif c == '}':
            group_ct -= 1
        elif c == '<':
            garbage = True

    return total, garbage_ct


test_examples()
input = get_input()
print(part1(input))
