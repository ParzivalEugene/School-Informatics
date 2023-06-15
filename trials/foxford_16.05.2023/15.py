def check(A: int) -> bool:
    for x in range(1, 100):
        for y in range(1, 100):
            if (x + y < 54) or (x <= y - 3) or (x > A):
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
