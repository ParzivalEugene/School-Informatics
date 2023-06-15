def f(n):
    r = bin(n)[2:]
    r += r[-3:] if n % 3 == 0 else bin(3 * (n % 3))[2:]
    return int(r, 2)


def main():
    for i in range(1000, 0, -1):
        if f(i) < 100:
            print(i)
            return


main()
