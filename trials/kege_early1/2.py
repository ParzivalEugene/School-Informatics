def f(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w)

# x w z y
# 0 _ _ 0
# 0 1 0 1
# _ 1 0 _