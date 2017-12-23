#!/usr/bin/env python
# -*- coding: utf-8 -*-


def redist(banks):
    snapshots = [banks[:]]

    while True:
        to_redist = max(banks)
        i = banks.index(to_redist)
        banks[i] = 0

        while to_redist:
            i = (i + 1) % len(banks)
            banks[i] += 1
            to_redist -= 1

        if banks in snapshots:
            break

        snapshots.append(banks[:])

    return len(snapshots)


def test():
    assert redist([0, 2, 7, 0]) == 5, "Test input failed"


def main():
    with open("input.txt", "r") as f:
        buf = f.read()

    banks = list(map(int, buf.split("\t")))
    print("Memory redistribution completed in %d cycles" % redist(banks))
    return


if __name__ == '__main__':
    test()
    main()
