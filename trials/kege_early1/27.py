with open("data/27B.txt", encoding="utf-8") as file:
    amount_of_measurements, gap, *data = list(map(int, file.readlines()))
    max_val = max(data)
    index = data.index(max_val)
    available_data = data[: index - gap] + data[index + gap :]
    print(max_val + max(available_data))
