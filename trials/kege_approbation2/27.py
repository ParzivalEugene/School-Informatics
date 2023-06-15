with open("data/27b.txt", encoding="utf-8") as file:
    gap, n, *data = list(map(int, file.readlines()))
    max_val = max(data)
    vals = []
    l_index = data.index(max_val)
    try:
        r_index = data.index(max_val, l_index + 1)
    except ValueError:
        r_index = l_index

    for i in [l_index, r_index]:
        available_data = data[:l_index] + data[l_index + 1 :]
        vals.append(max(available_data) + max_val)
    print(max(vals))
