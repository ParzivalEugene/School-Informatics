with open("data/26.txt", encoding="utf-8") as file:
    raw = file.readlines()
    drive_size, n = map(int, raw[0].split())
    data = sorted(map(int, raw[1:]))
    counter, users = 0, []
    for i in data:
        if i % 3 == 0:
            counter += 1
            if sum(users) + i < drive_size and counter > 10:
                users.append(i)

    max_size, gap = max(users), drive_size - sum(users)
    while max_size in data and max_size % 3 == 0 and max_size < gap:
        max_size += 1

    print(len(users), max_size)
