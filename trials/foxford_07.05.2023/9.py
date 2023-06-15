with open("data/9.csv", encoding="utf-8") as file:
    data = list(map(lambda x: list(map(int, x.split(";"))), file.readlines()))
    data = list(
        filter(
            lambda x: len(set(x)) == 5
            and sum([i ** 2 for i in x if x.count(i) == 1])
            >= [i for i in x if x.count(i) == 2][0] ** 3,
            data,
        )
    )
    print(len(data))
