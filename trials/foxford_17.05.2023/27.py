with open("data/27b.txt", encoding="utf-8") as file:
    raw = list(map(lambda x: list(map(int, x.split())), file.readlines()))
    n, data = raw[0][0], raw[1:]
    max_sum = sum(max(i) for i in data)
    gaps = sorted([abs(a - b) for a, b in data])
    print(max_sum, max_sum % 5 == 0)
    for i in gaps:
        value = max_sum - i
        if value % 5 == 0:
            print(value)
            break
