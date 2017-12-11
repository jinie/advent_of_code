#!/usr/bin/env python3


def part1(input, elements):
    cpos = 0
    skip = 0
    for i in input:
        six = cpos
        eix = cpos + i
        if eix < len(elements):
            subs = elements[six:eix]
            elements[six:eix] = subs[::-1]
        else:
            rlen = len(elements) - cpos
            subs = elements[six:] + elements[:i - rlen]
            subs = subs[::-1]
            elements = subs[rlen:] + elements[i - rlen:six] + subs[:rlen]
        cpos = (cpos + i + skip) if (cpos + i + skip) < len(elements) else (cpos + i + skip) % len(elements)
        skip += 1
    return(elements[0] * elements[1])

if __name__ == '__main__':
    input = [int(i) for i in "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167".split(',')]
    elements = list(range(256))

    print(part1(input, elements))
