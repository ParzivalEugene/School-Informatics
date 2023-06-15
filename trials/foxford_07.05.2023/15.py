def check(A):
    for x in range(100):
        if (x % 7 == 0) <= (not (x % 6) or (x + A >= 54)):
            continue
        else:
            return False
    return True


def main():
    for A in range(1000):
        if check(A):
            print(A)
            break


main()
