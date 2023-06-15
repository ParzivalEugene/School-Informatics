def check(line: str) -> bool:
    line = line.replace("N", "1").replace("O", "1").replace("P", "1")
    return "11" not in line


def main():
    with open("data/24.txt", encoding="utf-8") as file:
        text = file.read()
        line, lines = text[0], []
        for i in range(1, len(text)):
            if check(line + text[i]):
                line += text[i]
            else:
                lines.append(line)
                line = text[i]
        lines.append(line)
        print(max(len(i) for i in lines))


main()
