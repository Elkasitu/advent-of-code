def parse(buf):
    rows = buf.split('\n')
    matrix = [c.split('\t') for c in rows if c]
    return [[int(c) for c in r] for r in matrix]


def main():
    with open("input.txt", "r") as f:
        buf = f.read()

    matrix = parse(buf)
    
    res1 = sum([max(row) - min(row) for row in matrix])

    res2 = 0

    for row in matrix:
        l = len(row)
        for i in range(1, l):
            shifted = row[-i:] + row[:l - i]
            val = [n/m for n, m in zip(row, shifted) if n % m == 0]
            if val:
                res2 += val[0]
                break

    print("The checksum for part1 is %d" % res1)
    print("The checksum for part2 is %d" % res2)


if __name__ == '__main__':
    main()
