# +1 +4 *3 | win >= 55 | 1 <= S <= 54


def f(x, m):
    if x >= 55 and m == 4:
        return True
    if x < 55 and m == 4 or x >= 55:
        return False

    if m % 2:
        return f(x + 1, m + 1) or f(x + 4, m + 1) or f(x * 3, m + 1)
    return f(x + 1, m + 1) and f(x + 4, m + 1) and f(x * 3, m + 1)


for S in range(1, 55):
    if f(S, 1):
        print(S)
