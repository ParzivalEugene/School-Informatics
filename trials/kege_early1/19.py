# +1 +4 *4 | win >= 78 | 1 <= S <= 77 | S


def f(x, m):
    if x >= 78 and m == 3:
        return True
    if x < 78 and m == 3 or x >= 78:
        return False
    if m % 2 == 0:
        return f(x + 1, m + 1) or f(x + 4, m + 1) or f(x * 4, m + 1)
    return f(x + 1, m + 1) and f(x + 4, m + 1) and f(x * 4, m + 1)


for S in range(1, 78):
    if f(S, 1):
        print(S)
