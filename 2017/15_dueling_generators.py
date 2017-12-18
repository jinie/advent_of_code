#!/usr/bin/env python3


def generate(seed, multiplier, divisor=1):
    pval = seed
    while True:
        pval = (pval * multiplier) % 2147483647
        if pval % divisor == 0:
            yield pval


def get_samples(genA, genB, count):
    ct = 0
    for _ in range(count):
        if (next(genA) & 0xffff) == (next(genB) & 0xffff):
            ct += 1
    return ct


def part1():
    genA = generate(873, 16807)
    genB = generate(583, 48271)
    return get_samples(genA, genB, 40000000)


def part2():
    genA = generate(873, 16807, 4)
    genB = generate(583, 48271, 8)
    return get_samples(genA, genB, 5000000)


print('part 1:', part1())
print('part 2:', part2())
