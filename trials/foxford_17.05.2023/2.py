def f(x, y, z, w):
    return ((x <= y) == (y <= (not w))) or ((not z) and w)


def main():
    print("x y z w")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not f(x, y, z, w):
                        print(x, y, z, w)


main()
# w x z y
# . . . 0
# 0 . . 0
# 0 . 0 0
