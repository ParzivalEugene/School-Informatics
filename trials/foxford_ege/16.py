import sys

sys.setrecursionlimit(10000000)


def f(n):
    if n == 1:
        return 2
    return (2 * n + f(n - 1)) * n


print(int(f(2001) / f(1998)))
