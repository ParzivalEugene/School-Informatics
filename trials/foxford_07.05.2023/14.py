def main():
    for x in "0123456789ABCDEF":
        value = int(f"153{x}4", 16) + int(f"1{x}325", 16)
        if value % 15 == 0:
            print(x, value // 15)


main()
