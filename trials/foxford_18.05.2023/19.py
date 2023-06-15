# +2 *3 | win >= 79 | 1 <= s <= 69 | 9 s


def f(x, y, m):
    if m == 3 and x + y >= 79:
        return True
    if m == 3 and x + y < 79 or x + y >= 79:
        return False

    return (
        f(x + 2, y, m + 1)
        or f(x, y + 2, m + 1)
        or f(x * 3, y, m + 1)
        or f(x, y * 3, m + 1)
    )


for s in range(1, 70):
    if f(9, s, 1):
        print(s)
