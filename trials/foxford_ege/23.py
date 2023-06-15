# 5 -> 22  y11 x14

def f(x, y):
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x + 4, y)


print(f(5, 11) * f(11, 22))
