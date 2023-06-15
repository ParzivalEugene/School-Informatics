def f(n: int) -> int:
    r = bin(n)[2:]
    r += "10" if r[-1] == "1" else "01"
    r += str(sum(map(int, r)) % 2)
    return int(r, 2)


values = [f(i) for i in range(100) if f(i) > 147]
print(min(values))
