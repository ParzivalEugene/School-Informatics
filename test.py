def f(n):
    if n <= 5:
        return 2 + n
    if n % 2:
        return f(n - 1) + f(n - 2) + n
    return f(n - 2) + 2 * f(n / 2) - n


print(f(97) - f(88))
