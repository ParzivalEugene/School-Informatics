from itertools import product


data = [i for i in set(product("АПКМР", repeat=4)) if i.count("А") == 1]
print(len(data))
