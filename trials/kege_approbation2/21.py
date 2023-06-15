# +1 +4 *3 | win >= 55 | 1 <= S <= 54


def f(x, m):
    if x >= 55 and (m == 5 or m == 3):
        return True
    if x < 55 and m == 5 or x >= 55:
        return False

    if m % 2 == 0:
        return f(x + 1, m + 1) or f(x + 4, m + 1) or f(x * 3, m + 1)
    return f(x + 1, m + 1) and f(x + 4, m + 1) and f(x * 3, m + 1)


def e(x, m):
    if x >= 55 and m == 3:
        return True
    if x < 55 and m == 3 or x >= 55:
        return False

    if m % 2 == 0:
        return e(x + 1, m + 1) or e(x + 4, m + 1) or e(x * 3, m + 1)
    return e(x + 1, m + 1) and e(x + 4, m + 1) and e(x * 3, m + 1)


vals, ext = [], []
for S in range(1, 55):
    if f(S, 1):
        vals.append(S)
for S in range(1, 55):
    if e(S, 1):
        if S in vals:
            ext.append(S)
print([i for i in vals if i not in ext])
