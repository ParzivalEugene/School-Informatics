from itertools import product


data = sorted(map("".join, set(product("ЛОТКИ", repeat=4))))
for i, value in enumerate(data, 1):
    if value.startswith("О"):
        print(i, value)
        break