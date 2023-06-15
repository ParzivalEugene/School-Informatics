def main():
    gap = 56  # gap between rings
    path = "data/data.txt"  # path to the file
    with open(path, encoding="utf-8") as file:
        n, *data = [int(i) for i in file.readlines()]
        data = sorted(data, reverse=True)
        colors, color = [0] * n, 0
        combintaions = []
        for i in range(n):
            if not colors[i]:
                color += 1
                colors[i] = color
                combintaion = [data[i]]
                for j in range(i, n):
                    if not colors[j] and combintaion[-1] - gap >= data[j]:
                        colors[j] = color
                        combintaion.append(data[j])
                combintaions.append(combintaion)
    max_combination = max(combintaions, key=len)
    print(len(max_combination), min(max_combination))


if __name__ == "__main__":
    main()
