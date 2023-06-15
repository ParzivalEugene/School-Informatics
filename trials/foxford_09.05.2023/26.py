with open("data/26.txt", encoding="utf-8") as file:
    raw = file.readlines()
    n, drive_size = map(int, raw[0].split())
    data = list(map(int, raw[1:]))
    cargos = [i for i in data if 200 <= i <= 220]
    data = sorted([i for i in data if i > 220 or i < 200], reverse=True)
    i = 0
    while sum(cargos) + data[i] < drive_size:
        cargos.append(data[i])
        i += 1
    print(cargos)
    print(len(cargos), max(cargos))
