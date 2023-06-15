def main():
    for x in range(1, 1000000):
        value = 216**8 + 36**2 - x
        count = 0
        while value:
            if value % 6 == 5:
                count += 1
            value //= 6
        if count == 20:
            print(x)
            return


main()
