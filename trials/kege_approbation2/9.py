with open("data/9.csv", encoding="utf-8") as file:
    data = [list(map(int, x.split(","))) for x in file.readlines()]
    counter = 0
    for line in data:
        if len(set(line)) == len(line):
            a, *other, b = sorted(line)
            if (a + b) * 3 >= sum(other) * 2:
                counter += 1
    print(counter)
