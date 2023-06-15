# +2 *3 | win >= 79 | 1 <= S <= 69 | 9 S


def f(x, y, m):
    if x + y >= 79 and m == 4:
        return True
    if x + y < 79 and m == 4 or x + y >= 79:
        return False

    if m % 2:
        return (
            f(x + 2, y, m + 1)
            or f(x * 3, y, m + 1)
            or f(x, y + 2, m + 1)
            or f(x, y * 3, m + 1)
        )
    return (
        f(x + 2, y, m + 1)
        and f(x * 3, y, m + 1)
        and f(x, y + 2, m + 1)
        and f(x, y * 3, m + 1)
    )


for S in range(1, 70):
    if f(9, S, 1):
        print(S)
