def main():
    for x in range(10000):
        num = 216**8 + 36**2 - x
        counter = 0
        while num:
            if num % 6 == 5:
                counter += 1
            num //= 6
        if counter == 20:
            print(x)
            return


main()
