def check(i):
    for x in range(500):
        if ((x % 7 == 0) <= (not (x % 6 == 0))) or ((x + i) >= 54):
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
