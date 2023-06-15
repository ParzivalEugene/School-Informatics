with open("data/27b.txt", encoding="utf-8") as file:
    raw = file.readlines()
    n, data = int(raw[0]), list(map(lambda x: list(map(int, x.split())), raw[1:]))
    max_sum = sum(max(i) for i in data)
    gaps = sorted(i for i in set(max(i) - min(i) for i in data) if i)
    max_sum = max(max_sum - i for i in gaps if max_sum - i % 4)
    print(max_sum)
