from itertools import product


data = sorted(set(product("ЗАЧЯЮ", repeat=4)))
for i, value in enumerate(data, 1):
    print(i, "".join(value))
