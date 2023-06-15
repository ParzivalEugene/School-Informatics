def chunk(s):
    n = 1
    while s < 31:
        s = s + 3
        n = n * 2
    return n


def main():
    for i in range(1000):
        if chunk(i) == 128:
            print(i)
            return


main()
