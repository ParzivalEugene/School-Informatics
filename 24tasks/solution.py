def f(s, m):
    if s >= 54:
        return m % 2 == 0
    if not m:
        return False
    arr = [f(s + 2, m - 1), f(s * 2, m - 1)]
    return any(arr) if (m - 1) % 2 == 0 else all(arr)


