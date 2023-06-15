with open("data/9.txt", encoding="utf-8") as file:
    data = [float(i.replace(",", ".")) for i in file.read().split()]
    avg = sum(data) / len(data)
    print(avg - min(data))
