#!/usr/bin/env python3


def hash(input, elements, repeat=1):
    cpos = 0
    skip = 0
    for _ in range(repeat):
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
    return elements


def part1(orginput):
    input = [int(i) for i in orginput.split(',')]
    elements = hash(input, list(range(256)))
    return(elements[0] * elements[1])


def part2(orginput):
    input = [ord(a) for a in orginput] + [17, 31, 73, 47, 23]
    sparse = hash(input, list(range(256)), 64)
    block = []
    for i in range(0, 256, 16):
        value = sparse[i]
        for j in sparse[i + 1:i + 16]:
            value ^= j
        block.append(value)
    return ''.join('{:02x}'.format(b) for b in block)


def test():
    assert (part2("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

if __name__ == '__main__':
    orginput = "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"
    print("Part 1:", part1(orginput))
    test()
    print("Part 2:", part2(orginput))
