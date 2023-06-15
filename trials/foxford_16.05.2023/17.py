with open("data/17.txt", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    some_const = len([i for i in data if str(i)[-1] == "8"])
    sums = []
    for i in range(len(data) - 1):
        pair = data[i : i + 2]
        if any(x < 0 for x in pair) and sum(pair) ** 2 >= some_const:
            sums.append(sum(pair))
    print(len(sums), max(sums))
