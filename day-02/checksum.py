def parse(buf):
    rows = buf.split('\n')
    matrix = [c.split('\t') for c in rows if c]
    return [[int(c) for c in r] for r in matrix]


def main():
    with open("input.txt", "r") as f:
        buf = f.read()

    matrix = parse(buf)
    res = 0

    for row in matrix:
        res += max(row) - min(row)

    print("The checksum is %d" % res)


if __name__ == '__main__':
    main()
