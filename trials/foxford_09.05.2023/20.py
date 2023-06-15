def f(x, y, m):
    if x + y >= 71 and m == 4:
        return True
    if x + y < 71 and m == 4:
        return False
    if x + y >= 71:
        return False

    if m % 2 == 0:
        return (
            f(x + 3, y, m + 1)
            and f(x, y + 3, m + 1)
            and f(x * 2, y, m + 1)
            and f(x, y * 2, m + 1)
        )
    return (
        f(x + 3, y, m + 1)
        or f(x, y + 3, m + 1)
        or f(x * 2, y, m + 1)
        or f(x, y * 2, m + 1)
    )


for s in range(1, 57):
    if f(13, s, 1):
        print(s)
