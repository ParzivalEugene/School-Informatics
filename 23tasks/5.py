# 2 -> 40  y13 n17


def f(x, y):
    if x == 17 or x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(2, 13) * f(13, 40))
