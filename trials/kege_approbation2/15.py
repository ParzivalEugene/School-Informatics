def f(A):
    for x in range(100):
        if (((x & 52) != 0) and ((x & 36) == 0)) <= (not ((x & A) == 0)):
            continue
        else:
            return False
    return True


def main():
    for i in range(100):
        if f(i):
            print(i)
            return


main()
