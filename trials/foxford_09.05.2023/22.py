with open("data/22.csv", encoding="utf-8") as file:
    raw = list(map(lambda x: x.split(","), file.readlines()))
    data = [[int(i[0]), int(i[1]), list(map(int, i[2].split(";")))] for i in raw]
    counter = {0: 0}
    while len(counter) - 1 != len(data):
        for _id, _time, _ids in data:
            if all(id in counter for id in _ids):
                counter[_id] = _time + max(counter[id_] for id_ in _ids)
    print(max(counter.values()))
