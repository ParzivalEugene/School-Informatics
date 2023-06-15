# 1?3124*6


def check(i):
    number = str(i)
    return number[0] == "1" and number[2:6] == "3124" and number[-1] == "6"


def main():
    count = 0
    values = [1983 * i for i in range(10000000) if 1983 * i < 10 ** 10]
    for i in values:
        if check(i):
            count += 1
            print(i, i // 1983)
            if count == 2:
                return


main()
