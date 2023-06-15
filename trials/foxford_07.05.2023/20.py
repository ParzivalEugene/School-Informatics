def f(x, y, move):
    if x + y >= 71 and move == 4:
        return True
    if x + y < 71 and move == 4:
        return False
    if x + y >= 71:
        return False
    if move % 2 == 0:
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


for s in range(1, 57):
    if f(13, s, 1):
        print(s)
