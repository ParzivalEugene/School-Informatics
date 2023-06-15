from itertools import product


data = [
    (i, "".join(v))
    for i, v in enumerate(sorted(set(product("РУЧКА", repeat=5))), 1)
    if v.count("Ч") <= 1
]
for i, v in data:
    if "УУ" not in v:
        print(i, v)
