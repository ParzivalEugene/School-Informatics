def f(A):
    for x in range(1000):
        if ((x % A) and (x % 21 == 0)) <= (x % 14 == 0):
            continue
        else:
            return False
    return True


def main():
    for i in range(1000, 0, -1):
        if f(i):
            print(i)
            return


main()
