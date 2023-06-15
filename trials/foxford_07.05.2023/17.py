with open("data/17.txt", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    min_3_ending = abs(min([i for i in data if str(i)[-1] == "3"]))
    sums = []
    for i in range(len(data) - 1):
        pair = data[i : i + 2]
        if (
            sum([str(x)[-1] == "3" for x in pair]) == 1
            and sum(pair) ** 2 >= min_3_ending
        ):
            sums.append(sum(pair) ** 2)
    print(len(sums), max(sums))
