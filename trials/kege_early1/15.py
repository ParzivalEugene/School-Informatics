def check(A):
    for x in range(100):
        if (x & 39 == 0) or ((x & 11 == 0) <= (not (x & A == 0))):
            continue
        else:
            return False
    return True


def main():
    for i in range(100):
        if check(i):
            print(i)
            return


main()
