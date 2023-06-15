with open("data/24.txt", encoding="utf-8") as file:
    data = (
        file.read()
        .replace("A", "1")
        .replace("E", "1")
        .replace("B", "0")
        .replace("C", "0")
        .replace("D", "0")
    )
    pattern = "10"
    while pattern in data:
        pattern += "10"
    print(pattern in data)
    print(len(pattern) / 2)
