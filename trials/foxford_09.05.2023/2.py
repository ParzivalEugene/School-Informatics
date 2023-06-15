def f(x, y, z, w):
    return ((x <= y) == (y <= (not z))) or ((not z) and w)


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w)

# w x z y
# x x x 0
# 0 x x 0
# 0 x 0 0
