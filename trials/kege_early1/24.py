def check(line: str) -> bool:
    return "11" not in line.replace("Q", "1").replace("R", "1").replace("S", "1")


def main():
    with open("data/24.txt", encoding="utf-8") as file:
        text = file.read()
        line = text[0]
        lengths = []
        for i in range(1, len(text)):
            if check(line + text[i]):
                line += text[i]
            else:
                lengths.append(len(line))
                line = text[i]
        lengths.append(len(line))
        print(max(lengths))


main()
