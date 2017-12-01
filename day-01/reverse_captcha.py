def sum_if_next_match(buf):

    res = 0
    inted = [int(c) for c in buf]
    prev = inted[0]

    for cur in inted[1:]:
        if prev == cur:
            res += prev

        prev = cur

    if inted[0] == inted[-1]:
        res += inted[-1]

    return res


def main():

    with open("input.txt", "r") as f:
        buf = f.read().strip()

    total = sum_if_next_match(buf)

    print("The total is %d !" % total)


if __name__ == '__main__':
    main()
