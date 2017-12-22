#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_valid(data):
    counter = 0
    for phrase in data:
        phrase = [w for w in phrase.split(' ') if w]

        if len(set(phrase)) == len(phrase):
            counter += 1
    return counter


def main():
    with open("input.txt", "r") as f:
        buf = f.read()

    data = [p for p in buf.split('\n') if p]
    print("There are %d valid passphrases!" % count_valid(data))
    return


if __name__ == '__main__':
    main()
