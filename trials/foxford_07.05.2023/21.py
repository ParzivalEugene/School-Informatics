def f(x, y, move):
    if x + y >= 71 and move in (3, 5):
        return True
    if x + y < 71 and move == 5:
        return False
    if x + y >= 71:
        return False

    if move % 2 == 1:
        return (
            f(x + 3, y, move + 1)
            and f(x, y + 3, move + 1)
            and f(x * 2, y, move + 1)
            and f(x, y * 2, move + 1)
        )
    return (
        f(x + 3, y, move + 1)
        or f(x, y + 3, move + 1)
        or f(x * 2, y, move + 1)
        or f(x, y * 2, move + 1)
    )


def exclude(x, y, move):
    if x + y >= 71 and move == 3:
        return True
    if x + y < 71 and move == 3:
        return False
    if x + y >= 71:
        return False

    if move % 2 == 1:
        return (
            exclude(x + 3, y, move + 1)
            and exclude(x, y + 3, move + 1)
            and exclude(x * 2, y, move + 1)
            and exclude(x, y * 2, move + 1)
        )
    return (
        exclude(x + 3, y, move + 1)
        or exclude(x, y + 3, move + 1)
        or exclude(x * 2, y, move + 1)
        or exclude(x, y * 2, move + 1)
    )


for s in range(1, 57):
    if f(13, s, 1):
        print(s)

print()

for s in range(1, 57):
    if exclude(13, s, 1):
        print(s)
