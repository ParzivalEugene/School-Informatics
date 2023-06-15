with open("data/27b.txt", encoding="utf-8") as file:
    n, *data = list(map(int, file.readlines()))
    sums = []
    for i, value in enumerate(data):
        for j in range(i + 1, n):
            if value > data[j]:
                sub_value = value + data[j]
                if sub_value % 1011 == 40:
                    sums.append(((value, data[j]), sub_value))
    min_sum = min(i[1] for i in sums)
    print([i for i in sums if i[1] == min_sum])
