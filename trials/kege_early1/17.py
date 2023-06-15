with open("data/17.txt", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    min_val = min([i for i in data if len(str(i)) == 3 and i % 10 == 5])
    sums = []
    for i in range(len(data) - 1):
        pair = data[i : i + 2]
        if sum(len(str(x)) == 3 for x in pair) == 1 and sum(pair) % min_val == 0:
            sums.append(sum(pair))
    print(len(sums), min(sums))
