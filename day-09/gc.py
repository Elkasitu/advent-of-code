#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_closing(subraw):
    j = 0
    while j < len(subraw):
        if subraw[j] == '!':
            j += 2
            continue
        elif subraw[j] == '>':
            return j
        j += 1


def parse(raw):
    score = 0
    level = 0
    i = 0

    while i < len(raw):
        c = raw[i]
        if c == '{':
            level += 1
        elif c == '!':
            i += 2
            continue
        elif c == '<':
            i += find_closing(raw[i:]) + 1
            continue
        elif c == '}':
            score += level
            level -= 1
        i += 1

    return score


def test():
    raws = [
        '{}',
        '{{{}}}',
        '{{}, {}}',
        '{{{}, {}, {{}}}}',
        '{<a>, <a>, <a>, <a>}',
        '{{<ab>}, {<ab>}, {<ab>}, {<ab>}}',
        '{{<!!>},{<!!>},{<!!>},{<!!>}}',
        '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    ]

    assert parse(raws[0]) == 1, "Raws 0 Failed"
    assert parse(raws[1]) == 6, "Raws 1 Failed"
    assert parse(raws[2]) == 5, "Raws 2 Failed"
    assert parse(raws[3]) == 16, "Raws 3 Failed"
    assert parse(raws[4]) == 1, "Raws 4 Failed"
    assert parse(raws[5]) == 9, "Raws 5 Failed"
    assert parse(raws[6]) == 9, "Raws 6 Failed"
    assert parse(raws[7]) == 3, "Raws 7 Failed"


def main():
    test()
    with open("input.txt", "r") as f:
        buf = f.read()
    print("The total score is %d" % parse(buf))


if __name__ == '__main__':
    main()
