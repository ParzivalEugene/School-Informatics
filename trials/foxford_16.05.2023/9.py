with open("data/9.csv", encoding="utf-8") as file:
    data = list(map(lambda x: list(map(int, x.split(","))), file.readlines()))
    counter = 0
    for i in data:
        _min, *other, _max = sorted(i)
        if _max + _min >= sum(other):
            counter += 1
    print(counter)
