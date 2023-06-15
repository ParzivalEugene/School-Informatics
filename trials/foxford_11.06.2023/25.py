def get_divisors(num):
    divisors = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors


def main():
    for i in range(194465, 194551):
        divisors = get_divisors(i)
        if len(divisors) == 4:
            print(i, *divisors)


main()
