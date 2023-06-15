from itertools import product


data = sorted(map("".join, set(product("АВОРТ", repeat=6))))
for i, v in enumerate(data, 1):
    if v == "ВОРОТА":
        print(i, v)
