def f(n):
    if n == 1:
        return 1
    return f(n - 1) - g(n - 1)


def g(n):
    if n == 1:
        return 0
    return f(n - 1) + g(n - 1)


print(-4294967296 == -4294967296)
