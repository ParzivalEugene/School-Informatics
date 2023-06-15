def main():
    nums = []
    for i in range(1033, 7738):
        if i % 5 == 0 and all(i % x for x in (11, 17, 19, 23)):
            nums.append(i)
    print(len(nums), max(nums))


main()
