with open("data/9.csv", encoding="utf-8") as file:
    raw = list(
        map(lambda x: list(map(float, x.replace(",", ".").split())), file.readlines())
    )
    data = []
    for i in raw:
        data += i

    pairs = []
    for i in range(len(data) - 1):
        a, b = data[i : i + 2]
        pairs.append(abs(a - b))
    print(max(pairs))
