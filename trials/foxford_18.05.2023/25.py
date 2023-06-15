def divisors(n):
    divs = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def main():
    for i in range(185348, 185399 + 1):
        value = divisors(i)
        if len(value) == 2:
            print(*value)


main()