with open("data/1.txt", encoding="utf-8") as file:
    data = file.readlines()
    size, n = (int(i) for i in data[0].split())
    data = sorted([int(i) for i in data[1:]])
    files = []
    for i in data:
        if sum(files) + i < size:
            files.append(i)
        else:
            break
    max_file_size = max(files)
    gap = size - sum(files)
    result = 0
    for i in range(max_file_size + gap, max_file_size, -1):
        if i in data:
            result = i
            break
    print(len(files), result)
    