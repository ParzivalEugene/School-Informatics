def f(x, y, z, w):
    return x and ((not y) and z and (not w) or y and (not z))


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w)

# w x z y
# 0 1 0 1
# 0 1 1 0
# 1 1 0 1
