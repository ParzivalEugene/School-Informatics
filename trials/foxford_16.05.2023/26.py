from math import ceil

with open("data/26.txt", encoding="utf-8") as file:
    n, *data = list(map(int, file.readlines()))
    expected_price = sum(data)
    counter = {i: ceil(data.count(i) / 2) for i in data}
    items, final_price = sum(counter.values()), sum(i * v for i, v in counter.items())
    print(expected_price - final_price, n - items)
    print(expected_price, final_price)
