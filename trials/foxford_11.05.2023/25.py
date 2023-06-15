def divisors(n):
    counter = 0
    _divisors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            counter += 1
            _divisors.append(i)
            if counter > 2:
                return False
    return _divisors if counter == 2 else False


def main():
    for i in range(185348, 185399 + 1):
        value = divisors(i)
        if value:
            print(i, f"{value[0]},{value[1]}")


main()
