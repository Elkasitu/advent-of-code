#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(raw):
    lines = [line for line in raw.split('\n') if line.find('->') > 0]
    supporting = []
    supported = []

    for line in lines:
        splitted = line.split('->')
        supporting.append(splitted[0].split()[0])
        supported += splitted[1].strip().split(', ')

    return supporting, supported


def find_root(supporting, supported):
    for node in supporting:
        if node not in supported:
            return node


def test():
    data = [
        ['fwft', 'padx', 'tknk', 'ugml'],
        ['ktlj', 'cntj', 'xhth', 'pbga', 'havc', 'qoyq', 'ugml', 'padx',
         'fwft', 'gyxo', 'ebii', 'jptl']
    ]
    assert find_root(*data) == 'tknk', "Test input failed!"


def main():
    test()

    with open("input.txt", "r") as f:
        buf = f.read()

    print("Bottom program is %s" % find_root(*parse(buf)))


if __name__ == '__main__':
    main()
