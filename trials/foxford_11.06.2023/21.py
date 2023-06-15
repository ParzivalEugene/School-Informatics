# +2 *3 | win >= 79 | 1 <= S <= 69 | 9 S


def f(x, y, m):
    if x + y >= 79 and m == 5:
        return True
    if x + y < 79 and m == 5 or x + y >= 79:
        return False

    if m % 2 == 0:
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


def e(x, y, m):
    if x + y >= 79 and m == 3:
        return True
    if x + y < 79 and m == 3 or x + y >= 79:
        return False

    if m % 2 == 0:
        return (
            e(x + 2, y, m + 1)
            or e(x * 3, y, m + 1)
            or e(x, y + 2, m + 1)
            or e(x, y * 3, m + 1)
        )
    return (
        e(x + 2, y, m + 1)
        and e(x * 3, y, m + 1)
        and e(x, y + 2, m + 1)
        and e(x, y * 3, m + 1)
    )


for S in range(1, 70):
    if f(9, S, 1):
        print(S)


print("--")

for S in range(1, 70):
    if e(9, S, 1):
        print(S)
