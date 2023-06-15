from itertools import product

print(len([i for i in set(product("АПКМР", repeat=4)) if i.count("А") == 1]))