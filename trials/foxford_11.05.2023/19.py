# 1 <= S <= 69  win: >= 79  batchs: 9 S  moves: +2 *3


def f(x, y, m):
    if x + y >= 79 and m == 3:
        return True
    if x + y < 79 and m == 3:
        return False

    return (
        f(x + 2, y, m + 1)
        or f(x, y + 2, m + 1)
        or f(x * 3, y, m + 1)
        or f(x, y * 3, m + 1)
    )


values = [S for S in range(1, 70) if f(9, S, 1)]
print(values)