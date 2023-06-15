def f(n):
    if n < 3:
        return 1
    if n % 2 == 0:
        return 2 * n + f(n - 2)
    return f(n - 1) - 2


print(f(54) - f(44))
