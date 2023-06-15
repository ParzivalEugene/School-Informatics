def main():
    for i in range(4, 100):
        s = "3" + "5" * i
        while "25" in s or "355" in s or "555" in s:
            if "25" in s:
                s = s.replace("25", "3", 1)
            if "355" in s:
                s = s.replace("355", "52", 1)
            if "555" in s:
                s = s.replace("555", "23", 1)
        num = sum(map(int, s))
        if num == 27:
            print(i)
            return


main()
