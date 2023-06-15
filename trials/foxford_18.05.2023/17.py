with open("data/17.txt", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    sums = []
    for i in range(len(data) - 1):
        value = sum(data[i : i + 2])
        if value % 3 == 0 and value % 6:
            sums.append(value)
    print(len(sums), max(sums))
