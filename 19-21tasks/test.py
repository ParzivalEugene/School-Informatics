def divisors(num: int) -> set:
    a, b = [], []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            a.append(i)
            b.append(num // i)
    return set(a + b)


def main():
    with open("data.txt", encoding="utf-8") as f:
        data = f.read().splitlines()
        max_size, n = map(int, data[0].split())
        data = sorted([int(i) for i in data[1:]])
        i = 1
        while sum(data[:i]) <= max_size:
            i += 1
        print(len(data[:i - 1]), max(data[:i - 1]))


if __name__ == "__main__":
    main()
