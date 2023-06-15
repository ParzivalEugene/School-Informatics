def main():
    for x in "0123456789ABCDE":
        num = int(f"97968{x}13", 15) + int(f"7{x}213", 15)
        if num % 14 == 0:
            print(num // 14)
            return


main()
