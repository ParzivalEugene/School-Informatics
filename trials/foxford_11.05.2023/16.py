def G(n):
    print(n)
    if n % 3 != 0:
        G(n - 1)
        G(n // 2)


G(14)
