#!/usr/bin/env python3


def spin(step, spinct):
    cbuf = [0]
    cpos = 0
    for nval in range(1, spinct + 1):
        cpos = ((cpos + step) % nval) + 1
        cbuf.insert(cpos, nval)
    return cbuf


def spin2(step, spinct):
    # 0 is always at the front of the list, so we only need to check if something is
    # inserted at position 1 and save that.
    cpos = 0
    ret = None
    for nval in range(1, spinct + 1):
        cpos = ((cpos + step) % nval) + 1
        if cpos == 1:
            ret = nval
    return ret


# Part 1
buf = spin(349, 2017)
print('Part 1:', buf[buf.index(2017) + 1:buf.index(2017) + 2])

# Part 2
buf = spin2(349, 50000000)
print('Part 2:', buf)
