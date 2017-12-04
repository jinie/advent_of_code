#!/usr/bin/env python3
import hashlib
from itertools import count


def part1(input):
    ret = ''
    for i in count():
        ho = hashlib.md5()
        ho.update('{}{}'.format(input, i).encode())
        digest = ho.hexdigest()
        if digest.startswith('00000'):
            ret += digest[5]
            print(ret)
            if len(ret) == 8:
                break
    return ret


def part2(input):
    d = dict()

    for i in count():
        ho = hashlib.md5()
        ho.update('{}{}'.format(input, i).encode())
        digest = ho.hexdigest()
        if digest.startswith('00000'):
            pos = digest[5]
            val = digest[6]
            if int(pos, 16) > 7 or int(pos, 16) in d:
                continue
            else:
                d[int(pos, 16)] = val
            if len(d.keys()) == 8:
                print(d)
                pw = ""
                for k in sorted(d):
                    pw += d[k]
                return pw


# Be extra proud of your solution if it uses a cinematic "decrypting" animation.
def part2_cinematic(input):
    out = ['_'] * 8
    pgres = ['-', '\\', '|', '/']
    pp = 0
    outstr = '{} {}'.format(pgres[pp], ''.join(out))

    for i in count():
        ho = hashlib.md5()
        ho.update('{}{}'.format(input, i).encode())
        digest = ho.hexdigest()
        if digest.startswith('00000'):
            pos = int(digest[5], 16)

            if pos > 7 or out[pos] is not '_':
                continue
            else:
                out[pos] = digest[6]
                outstr = '{} {}'.format(pgres[pp], ''.join(out))
                print(outstr, end='\r')
                if '_' not in out:
                    print(''.join(out))
                    return
        if i % 10000 == 0:
            pp = pp + 1 if pp < (len(pgres) - 1) else 0
            outstr = '{} {}'.format(pgres[pp], ''.join(out))
            print(outstr, end='\r')

input = 'uqwqemis'
print(part1(input))
print(part2(input))
part2_cinematic(input)
