num = 3 * 292**1031 - 3 * 244**1032 + 16**1033 - 3 * 28**1034 - 1052

counter = 0
while num:
    if num % 4 == 1:
        counter += 1
    num //= 4
print(counter)
