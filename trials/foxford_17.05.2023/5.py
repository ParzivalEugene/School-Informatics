def f(n):
    r = list(bin(n)[2:])
    r[3], r[4] = r[4], r[3]
    r[4], r[5] = r[5], r[4]
    return int("".join(r), 2) - n


print(len(set([f(i) for i in range(128, 256)])))
