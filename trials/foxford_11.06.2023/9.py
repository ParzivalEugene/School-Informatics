with open("data/9.csv", encoding="utf-8") as file:
    data = [float(i) for line in file.read().replace(",", ".").splitlines() for i in line.split()]
    _avg, _min = sum(data) / len(data), min(data)
    print(_avg - _min)
