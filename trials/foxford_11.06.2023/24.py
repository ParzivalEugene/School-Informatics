with open("data/24.txt", encoding="utf-8") as file:
    text = file.read()
    s = "S"
    while s + "S" in text:
        s += "S"
    print(len(s))
