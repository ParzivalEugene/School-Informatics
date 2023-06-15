def f(n):
    r = list(bin(n)[2:])
    r[3], r[4] = r[4], r[3]
    r[4], r[5] = r[5], r[4]
    r = int("".join(r), 2) - n
    return r


values = []
for i in range(127, 257):
    values += [f(i)]
print(len(set(values)))
