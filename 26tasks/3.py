with open("data/3.txt", encoding="utf-8") as file:
    raw = file.readlines()
    size, n = map(int, raw[0].split())
    data = sorted(map(int, raw[1:]))

    files = []
    for i in data:
        if sum(files) + i < size:
            files.append(i)
        else:
            break

    max_file_size, gap = max(files), size - sum(files)
    result = max_file_size
    for i in range(max_file_size + gap, max_file_size, -1):
        if i in data:
            result = i
            break

    print(len(files), result)
