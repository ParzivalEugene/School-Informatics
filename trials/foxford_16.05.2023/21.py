# +1 +5 *2 | win >= 235 | 1 <= s <= 234


def f(x, m):
    if x >= 235 and (m == 5 or m == 3):
        return True
    if x < 235 and m == 5 or x >= 235:
        return False
    if m % 2 == 1:
        return f(x + 1, m + 1) and f(x + 5, m + 1) and f(x * 2, m + 1)
    else:
        return f(x + 1, m + 1) or f(x + 5, m + 1) or f(x * 2, m + 1)


def extend(x, m):
    if x >= 235 and m == 3:
        return True
    if x < 235 and m == 3 or x >= 235:
        return False
    if m % 2 == 1:
        return extend(x + 1, m + 1) and extend(x + 5, m + 1) and extend(x * 2, m + 1)
    else:
        return extend(x + 1, m + 1) or extend(x + 5, m + 1) or extend(x * 2, m + 1)


for i in range(1, 235):
    if f(i, 1):
        print(i)

print()

for i in range(1, 235):
    if extend(i, 1):
        print(i)
