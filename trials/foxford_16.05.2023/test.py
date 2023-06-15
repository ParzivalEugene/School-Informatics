num = 1100000
parts = 100
part = num // parts
data = [(part * i, part * (i + 1)) for i in range(parts)]
data[-1] = (data[-1][0], data[-1][1] + 1)
print(data)
