# +1 +2 *3 | 3 -> 18 | y8 n 13


def f(x, y):
    if x > y or x == 13:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(3, 8) * f(8, 18))
