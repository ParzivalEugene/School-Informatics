with open("22.csv", encoding="utf-8") as file:
    data = [i.strip().split() for i in file.readlines()]
    data = [[int(i[0]), int(i[1]), list(map(int, i[2].split(";")))] for i in data]

    counter = {0: 0}
    gap = 0

    while len(counter) != len(data) + 1:
        for line in data:
            if all(ids in counter for ids in line[2]):
                counter[line[0]] = max(counter[i] for i in line[2]) + line[1] + gap
    print(max(counter.values()))

    counter = {0: 0}
    while len(counter) != len(data) + 1:
        for line in data:
            if all(ids in counter for ids in line[2]):
                counter[line[0]] = max(counter[i] for i in line[2]) + line[1]
    print(max(counter.values()))
