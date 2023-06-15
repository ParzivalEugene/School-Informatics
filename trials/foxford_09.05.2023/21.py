def f(x, y, m):
    if x + y >= 71 and m in (3, 5):
        return True
    if x + y < 71 and m == 5:
        return False
    if x + y >= 71:
        return False

    if m % 2 == 1:
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

def exclude(x, y, m):
    if x + y >= 71 and m == 3:
        return True
    if x + y < 71 and m == 3:
        return False
    if x + y >= 71:
        return False

    if m % 2 == 1:
        return (
            exclude(x + 3, y, m + 1)
            and exclude(x, y + 3, m + 1)
            and exclude(x * 2, y, m + 1)
            and exclude(x, y * 2, m + 1)
        )
    return (
        exclude(x + 3, y, m + 1)
        or exclude(x, y + 3, m + 1)
        or exclude(x * 2, y, m + 1)
        or exclude(x, y * 2, m + 1)
    )


for s in range(1, 57):
    if f(s, 13, 1):
        print(s)

print()

for s in range(1, 57):
    if exclude(s, 13, 1):
        print(s)