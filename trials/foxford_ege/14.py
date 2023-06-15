def main():
    for i in "0123456789ABCDEF":
        value = int(f"153{i}4", 16) + int(f"1{i}325", 16)
        print(value, value % 15 == 0, i)
        if value % 15 == 0:
            print(value // 15)
            return


main()
