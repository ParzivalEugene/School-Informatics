# 200-220 | max quantity
with open("data/26.txt", encoding="utf-8") as file:
    raw = file.readlines()
    n, drive_size, data = *list(map(int, raw[0].split())), list(map(int, raw[1:]))
    vip_cargos = list(filter(lambda x: 200 <= x <= 220, data))
    data = sorted(filter(lambda x: 200 > x or x > 220, data))
    drive = vip_cargos[:]
    for cargo in data:
        if sum(drive) + cargo <= drive_size:
            drive.append(cargo)
        else:
            break
    max_cargo = max(drive)
    gap = drive_size - sum(drive)
    max_cargo = max([max_cargo + i for i in range(gap + 1) if max_cargo + i in data])
    print(len(drive), max_cargo)
