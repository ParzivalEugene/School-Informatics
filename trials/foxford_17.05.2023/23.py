# +1 *2 *3 | 4 => 38 | x18 y11


def f(x, y):
    if x > y or x == 18:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(4, 11) * f(11, 38))
