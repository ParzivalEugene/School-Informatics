with open("data/24.txt", encoding="utf-8") as file:
    data = file.read()
    lines, line = [], ""
    for i in range(1, len(data)):
        if data[i] >= data[i - 1]:
            line += data[i - 1]
        else:
            line += data[i - 1]
            lines.append(line)
            line = ""
    line += data[-1]
    lines.append(line)
    max_len = max([len(i) for i in lines])
    print([i for i in lines if len(i) == max_len])
