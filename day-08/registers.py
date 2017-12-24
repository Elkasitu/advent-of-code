#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


def process(instructions):
    vars = defaultdict(int)
    for instruction in instructions:
        if eval(instruction[3]):
            val = instruction[2]
            if instruction[1] == 'inc':
                vars[instruction[0]] += val
            else:
                vars[instruction[0]] -= val

    return max(vars.values())


def parse(raw):
    lines = raw.split('\n')[:-1]
    parsed = []
    for line in lines:
        line = line.split()
        parsed.append((line[0], line[1], int(line[2]),
                       ' '.join(["vars['%s']" % line[4], line[5], line[6]])))
    return parsed


def test():
    instructions = [
        ('b', 'inc', 5, "vars['a'] > 1"),
        ('a', 'inc', 1, "vars['b'] < 5"),
        ('c', 'dec', -10, "vars['a'] >= 1"),
        ('c', 'inc', -20, "vars['c'] == 10")
    ]
    assert process(instructions) == 1, "Test failed!"


def main():
    test()

    with open("input.txt", "r") as f:
        buf = f.read()
    instructions = parse(buf)

    print("The highest registry value is %d" % process(instructions))


if __name__ == '__main__':
    main()
