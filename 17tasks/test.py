with open("data/17-3.txt", encoding="utf-8") as file:
    data = [int(i) for i in file.readlines()]
    avg = sum(data) / len(data)
    sums = []
    for i in range(len(data) - 2):
        triple = data[i : i + 3]
        if any(x > avg for x in triple) and sum(x % 7 == 0 for x in triple) >= 2:
            sums.append(sum(triple))
    print(len(sums), max(sums))
