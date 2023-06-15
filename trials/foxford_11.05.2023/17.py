with open("data/17.txt", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    sums = []
    for i in range(len(data) - 1):
        pair = data[i : i + 2]
        if sum(pair) % 3 == 0 and sum(pair) % 6:
            sums.append(sum(pair))
    print(len(sums), max(sums))
