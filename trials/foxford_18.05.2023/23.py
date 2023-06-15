# +3 +2 *2 | 10 -> 36 y 18
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 2, y) + f(x * 2, y)


print(f(10, 18) * f(18, 36))
