from itertools import product

data = sorted(set(product("ЗАЧЮЯ", repeat=4)))
for i, value in enumerate(data):
    if value[0] == "Я":
        print(i + 1)
        break
