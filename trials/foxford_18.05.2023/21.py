# +2 *3 | win >= 79 | 1 <= s <= 69 | 9 s


def f(x, y, m):
    if m in (3, 5) and x + y >= 79:
        return True
    if m == 5 and x + y < 79 or x + y >= 79:
        return False
    if m % 2:
        return (
            f(x + 2, y, m + 1)
            and f(x, y + 2, m + 1)
            and f(x * 3, y, m + 1)
            and f(x, y * 3, m + 1)
        )
    return (
        f(x + 2, y, m + 1)
        or f(x, y + 2, m + 1)
        or f(x * 3, y, m + 1)
        or f(x, y * 3, m + 1)
    )


def exclude(x, y, m):
    if m == 3 and x + y >= 79:
        return True
    if m == 3 and x + y < 79 or x + y >= 79:
        return False
    if m % 2:
        return (
            exclude(x + 2, y, m + 1)
            and exclude(x, y + 2, m + 1)
            and exclude(x * 3, y, m + 1)
            and exclude(x, y * 3, m + 1)
        )
    return (
        exclude(x + 2, y, m + 1)
        or exclude(x, y + 2, m + 1)
        or exclude(x * 3, y, m + 1)
        or exclude(x, y * 3, m + 1)
    )


for s in range(1, 70):
    if f(9, s, 1):
        print(s)


for s in range(1, 70):
    if exclude(9, s, 1):
        print(s)
