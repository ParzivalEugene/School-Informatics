with open("data/24.txt", encoding="utf-8") as file:
    data = file.read()
    # data = "AABBCCAB"
    lines, line = [], data[0]
    for i in range(1, len(data)):
        if data[i - 1] != data[i]:
            line += data[i]
        else:
            lines.append(line)
            line = data[i]
    lines.append(line)
    lines = [len(i) for i in lines]
    print(max(lines))
