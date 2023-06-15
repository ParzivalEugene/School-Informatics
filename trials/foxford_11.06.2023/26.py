with open("data/26.txt", encoding="utf-8") as file:
    raw = file.readlines()
    drive_size, users_amount = map(int, raw[0].split())
    users = sorted(map(int, raw[1:]))
    users_in_drive, i = [], 0
    while sum(users_in_drive) + users[i] < drive_size:
        users_in_drive.append(users[i])
        i += 1
    gap = drive_size - sum(users_in_drive)
    max_user = max(users_in_drive)
    max_user = max(max_user + i for i in range(1, gap + 1) if max_user + i in users)
    print(len(users_in_drive), max_user)
