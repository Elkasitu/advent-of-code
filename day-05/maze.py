#!/usr/bin/env python
# -*- coding: utf-8 -*-


def escape(maze):
    steps = 0
    i = 0
    while i < len(maze):
        cur = maze[i]
        maze[i] += 1
        i += cur
        steps += 1
    return steps


def main():
    with open("input.txt", "r") as f:
        buf = f.read()

    data = [int(x) for x in buf.split('\n') if x]
    print("Escaped the maze in %d steps!" % escape(data))
    return


if __name__ == '__main__':
    main()
