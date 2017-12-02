def parse(buf):
    return [int(c) for c in buf.strip()]

def sum_it(inpt, step=0):
    i = 1
    l = len(inpt)
    res = 0

    while i <= l:
        prev = inpt[i-1]
        cur = inpt[(i + step) % l]

        res += prev if prev == cur else 0
        i += 1
    return res


def main():

    with open("input.txt", "r") as f:
        buf = f.read()

    inpt = parse(buf)
    total1 = sum_it(inpt)
    step = len(inpt) // 2 - 1
    total2 = sum_it(inpt, step)

    print("The total for part 1 is %d !" % total1)
    print("The total for part 2 is %d !" % total2)


if __name__ == '__main__':
    main()
