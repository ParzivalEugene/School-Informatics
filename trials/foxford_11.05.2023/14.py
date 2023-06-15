num = 36 ** 28 + 6 ** 19 - 39
counter = 0
while num:
    if num % 6 == 5:
        counter += 1
    num //= 6
print(counter)