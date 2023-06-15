def f(x, y, z, w):
    return z or (not ((x <= y) <= (w and x)))



print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w)


# w x z y
# 0 _ 0 _
# 1 _ _ 0
# _ _ _ 1
