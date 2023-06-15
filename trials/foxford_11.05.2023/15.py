def check(A):
    for x in range(100):
        for y in range(100):
            if ((x <= 3) <= (x**2 <= A)) and ((y**2 <= A) <= (y <= 3)):
                continue
            else:
                return False
    return True


def main():
    for i in range(1000, 0, -1):
        if check(i):
            print(i)
            return


main()
