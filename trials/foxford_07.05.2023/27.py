# with open("data/27a.txt", encoding="utf-8") as file:
#     n = int(file.readline())
#     data = sorted(map(lambda x: list(map(int, x.split())), file.readlines()))
#     res = sum(max(i) for i in data)
#     print(res, res % 4 != 0)


with open("data/27b.txt", encoding="utf-8") as file:
    n = int(file.readline())
    data = sorted(map(lambda x: list(map(int, x.split())), file.readlines()))
    res = sum(max(i) for i in data)
    print(res, res % 4 != 0)
