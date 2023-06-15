with open("data/22.csv", encoding="utf-8") as file:
    raw = list(map(lambda x: x.split(","), file.readlines()))
    data = [[int(i[0]), int(i[1]), list(map(int, i[2].split(";")))] for i in raw]

    counter = {0: 0}
    while len(counter) != len(data) + 1:
        for _id, time, ids in data:
            if all(x in counter for x in ids):
                counter[_id] = time + max([counter[x] for x in ids])

    print(max(counter.values()))
    print(counter)
