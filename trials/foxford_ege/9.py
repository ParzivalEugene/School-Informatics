with open("9.csv", encoding="utf-8") as file:
    data = [[int(i) for i in line.split(";")] for line in file.readlines()]
    count = 0
    for line in data:
        counter = {i: line.count(i) for i in line}
        values = list(counter.values())
        if values.count(2) == 1 and values.count(1) == 4 and len(values) == 5:
            unique = [i for i, value in counter.items() if value == 2][0]
            others = [i**2 for i, value in counter.items() if value == 1]
            if not (sum(others) < unique**3):
                count += 1
    print(count)
