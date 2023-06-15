# 4 -> 38  y11 n18  +1 *2 *3
def f(x, y):
    if x == 18 or x > y:
        return False
    if x == y:
        return True
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(4, 11) * f(11, 38))
