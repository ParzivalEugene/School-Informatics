with open("data/22.txt", encoding="utf-8") as file:
    raw = [i.split() for i in file.readlines()]
    data = [[int(i[0]), int(i[1]), list(map(int, i[2].split(";")))] for i in raw]
    counter = {0: 0}
    while len(counter) != len(data) + 1:
        for _id, _time, _ids in data:
            if all(x in counter for x in _ids):
                counter[_id] = _time + max([counter[x] for x in _ids])
    print(max(counter.values()))