with open("data/24.txt", encoding="utf-8") as file:
    text = file.read()
    lines, line = [], text[0]
    for i in range(1, len(text)):
        if text[i] >= text[i - 1]:
            line += text[i]
        else:
            lines.append(line)
            line = text[i]
    lines.append(line)
    max_len = max(len(i) for i in lines)
    res = [i for i in lines if len(i) == max_len][0]
    print(f"{len(res)} {res[0]} {res[-1]}")
