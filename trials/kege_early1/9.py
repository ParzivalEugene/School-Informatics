with open("data/9.csv", encoding="utf-8") as file:
    data = list(map(lambda x: list(map(int, x.split())), file.readlines()))
    counter = 0
    for line in data:
        if len(set(line)) == len(line):
            a, *other, b = sorted(line)
            if 3 * (a + b) <= 2 * sum(other):
                counter += 1
    print(counter)
