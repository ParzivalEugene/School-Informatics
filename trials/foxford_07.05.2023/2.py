def f(x, y, z, w):
    return ((x == (not w)) <= (z and (not x))) or ((y and w) and z)


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w)


# x w y z
# 1 x 1 1
# 0 1 1 0
# x 0 0 0
