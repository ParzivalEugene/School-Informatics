def f(line):
    if line[2] == [0]:
        return line[1]
    local_max = 0
    for j in line[2]:
        local_max = max(local_max, f(local_data[j - 1]))
    return local_max + line[1] + 0


with open("data/22-33.csv", encoding="utf-8") as file:
    data = [
        [int(i) for i in line.replace(",", " ").replace(";", " ").split()]
        for line in file.readlines()[1:]
    ]
    data = [[i[0], i[1], i[2:]] for i in data]
    for t in range(50):
        local_data = data[:]
        local_data[2][1] = t
        print("****")
        print(*local_data, sep="\n")
        result = [f(i) for i in local_data]
        print(max(result))
