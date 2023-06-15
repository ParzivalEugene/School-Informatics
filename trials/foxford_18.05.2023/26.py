with open("data/26.txt", encoding="utf-8") as file:
    raw = file.readlines()
    drive_size, n = map(int, raw[0].split())
    data = sorted(map(int, raw[1:]))

    users = []
    i = 0
    while sum(users) + data[i] < drive_size:
        users.append(data[i])
        i += 1
    gap = drive_size - sum(users)
    max_size = max(users)
    while gap + max_size not in data:
        gap -= 1
    max_size += gap
    print(users)
    print(len(users), max_size)
