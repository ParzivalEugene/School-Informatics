with open("data/26.txt", encoding="utf-8") as file:
    raw = [i for i in file.readlines()]
    size, n = map(int, raw[0].split())
    data = list(map(int, raw[1:]))

    sorted_data = sorted(data)
    files = []
    for i in sorted_data:
        if sum(files) + i < size:
            files.append(i)
        else:
            break

    max_size = max(files)
    gap = size - sum(files)
    for i in range(max_size + gap, max_size, -1):
        if i in data:
            max_size = i
            break

    print(len(files), max_size)
