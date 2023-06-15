from itertools import product


data = sorted(set(product("ФОКС", repeat=4)))
for i, value in enumerate(data, 1):
    if "".join(value) == "ФОКС":
        print(i, "".join(value))
