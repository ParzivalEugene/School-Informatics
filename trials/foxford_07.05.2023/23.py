# 5 -> 22  y11 n14  +1 +3 +4

def f(x, y):
    if x == 14 or x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x + 4, y)

print(f(5, 11) * f(11, 22))