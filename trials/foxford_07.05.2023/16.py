import sys

sys.setrecursionlimit(1000000)


def f(n):
    if n == 1:
        return 2
    if n > 1:
        return (2 * n + f(n - 1)) * n


print(f(2001) / f(1998) == 7999998000)
