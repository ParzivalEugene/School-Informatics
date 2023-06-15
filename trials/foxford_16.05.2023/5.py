def f(n: int) -> int:
    r = bin(n)[2:]
    if n % 2:
        r = "10" + r
        r = r[:-1] + "0"
    else:
        r = "11" + r
        r = r[:-1] + "1"
    return int(r, 2)


print(min([f(i) for i in range(20, 100)]))
