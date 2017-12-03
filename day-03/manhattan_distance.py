from math import ceil, sqrt

def get_ring(n):
    return ceil((sqrt(n) - 1) / 2)


def get_coords(n):
    r = get_ring(n)  # ring number
    l = 2 * r + 1  # segment length
    m = l**2  # max

    l -= 1

    if n >= m - l:
        return (r - (m - n), -r)

    m -= l

    if n >= m - l:
        return (-r, -r + (m - n))

    m -= l

    if n >= m - l:
        return (-r + (m - n), r)

    return (r, r - (m - n - l))


def mhd(p):
    o = (0, 0)
    return abs(p[0] - o[0]) + abs(p[1] - o[1])


def main():
    part1 = mhd(get_coords(347991))
    print("Part #1: square 347991: %d" % part1)


if __name__ == '__main__':
    main()
