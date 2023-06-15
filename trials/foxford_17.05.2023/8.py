from itertools import product

data = sorted("".join(i) for i in set(product("ФОКС", repeat=4)))
for i, value in enumerate(data, 1):
    if value == "ФОКС":
        print(i, value)
