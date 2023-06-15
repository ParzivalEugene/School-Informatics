def f(n: int) -> int:
    nums = list(map(int, str(n)))
    nums = [nums[0] * nums[1], nums[1] * nums[2]]
    return int("".join(str(i) for i in sorted(nums, reverse=True)))


def main():
    values = []
    for i in range(100, 1000):
        if f(i) == 123:
            print(i, f(i))


main()
