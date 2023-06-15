num = 49**20 - 7**19 + 95
count = 0
while num:
    if num % 7 == 6:
        count += 1
    num //= 7
print(count)
