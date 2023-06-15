def chunk(x):
    L = 2 * x - 20
    M = 2 * x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


def main():
    for i in range(200, 1000):
        if chunk(i) == 50:
            print(i)
            return


main()
