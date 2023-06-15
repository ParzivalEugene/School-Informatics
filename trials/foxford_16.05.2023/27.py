from math import ceil, inf


with open("data/27_B.txt", encoding="utf-8") as file:
    n, *data = list(map(lambda x: list(map(int, x.split())), file.readlines()))
    n = n[0]
    data = [[i, ceil(v / 30)] for i, v in data]

    lab = sum((i - data[0][0]) * value for i, value in data)
    right_sum = sum(value for _, value in data)
    left_sum = 0
    min_sum = inf
    for i in range(len(data) - 1):
        r = data[i + 1][0] - data[i][0]
        left_sum += data[i][1]
        right_sum -= data[i][1]
        lab += r * (left_sum - right_sum)
        min_sum = min(min_sum, lab)
    print("b:", min_sum)
