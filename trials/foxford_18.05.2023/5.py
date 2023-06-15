def f(n):
    r = list(map(int, str(n)))
    data = sorted([str(r[0] * r[1]), str(r[1] * r[2])])
    return int(data[0] + data[1])


def main():
    for i in range(100, 1000):
        if f(i) == 123:
            print(i)
            return


main()
