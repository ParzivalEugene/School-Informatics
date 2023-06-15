# -4 //2  74 -> 2  y10

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 4, y) + f(x // 2, y)


print(f(74, 10) * f(10, 2))