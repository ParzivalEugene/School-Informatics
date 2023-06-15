def main():
    with open("data/27b.txt", encoding="utf-8") as file:
        n, *data = list(map(lambda x: list(map(int, x.split())), file.readlines()))
        n = n[0]
        res = [0]
        for pair in data:
            res = [x + y for x in res for y in pair]
            res = list({i % 5: i for i in sorted(res)}.values())
        print(max(i for i in res if i % 5 == 0))


main()
