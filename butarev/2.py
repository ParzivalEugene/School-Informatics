def main():
    path = "data/data.txt"  # path to the file
    with open(path, encoding="utf-8") as file:
        n, *data = [int(i) for i in file.readlines()]
        data = sorted(data, reverse=True)

        # solution for client
        client_sum = 0
        client_data = data.copy()
        for _ in range(n // 3):
            trace = client_data.pop(0), client_data.pop(), client_data.pop()
            client_sum += sum(trace[1:])
        client_sum += sum(client_data)

        # solution for machine
        machine_sum = sum(
            [0 if (i + 1) % 3 == 0 else value for i, value in enumerate(data)]
        )

        print(client_sum, machine_sum)


if __name__ == "__main__":
    main()
