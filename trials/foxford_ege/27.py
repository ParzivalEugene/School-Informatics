# a
with open("data/27b.txt", encoding="utf-8") as file:
    raw = file.readlines()
    n, data = (
        int(raw[0]),
        sorted(sorted(map(int, i.split()))[::-1] for i in raw[1:])[::-1],
    )
    value = sum(max(i) for i in data)
    print(value, value % 4 != 0)
