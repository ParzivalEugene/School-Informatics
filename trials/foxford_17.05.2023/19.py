# +3 * 2 | win >= 71 | 1 <= s <= 56 | s 13


def f(x, y, m):
    if m == 3 and x + y >= 71:
        return True
    if m == 3 and x + y < 71 or x + y >= 71:
        return False

    return (
        f(x + 3, y, m + 1)
        or f(x, y + 3, m + 1)
        or f(x * 2, y, m + 1)
        or f(x, y * 2, m + 1)
    )


for s in range(1, 57):
    if f(13, s, 1):
        print(s)
