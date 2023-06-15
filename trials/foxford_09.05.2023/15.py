def check(n):
    for x in range(1, 100):
        for y in range(1, 100):
            if (6 * y - 2 * x > n) or (x + 4 * y < 80) or (2 * y - 3 * x < -72):
                continue
            else:
                return False
    return True


def main():
    for i in range(1000, 0, -1):
        if check(i):
            print(i)
            return


main()
