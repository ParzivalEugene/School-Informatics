def main():
    for x in "0123456789ABCDE"[::-1]:
        num = int(f"99658{x}29", 15) + int(f"102{x}023", 15)
        if num % 14 == 0:
            print(num // 14)
            return


main()
