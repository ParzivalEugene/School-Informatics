def f(x, y, z, w):
    return ((w <= y) <= (x == y)) or (not z)


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w)
# x y z w
# _ 0 1 0
# 0 _ _ 0
# _ 1 1 _
