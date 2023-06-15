with open("data/9.csv", encoding="utf-8") as file:
    data = [
        float(i.replace(",", "."))
        for line in file.readlines()
        for i in line.split(" , ")
    ]
    gaps = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    print(max(gaps))
