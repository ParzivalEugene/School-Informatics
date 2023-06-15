def f(x, y):
    if x == 12:
        return 0
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)


print(f(2, 11) * f(11, 24))
