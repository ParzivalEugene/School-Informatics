with open("data/9.txt", encoding="utf-8") as file:
    data = [float(i) for i in file.read().replace(",", ".").split()]
    print(sum(data) / len(data) - min(data))
