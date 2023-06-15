from itertools import product


data = sorted(map("".join, set(product("АВЛОР", repeat=4))))
for i, v in enumerate(data, 1):
    print(i, v)
