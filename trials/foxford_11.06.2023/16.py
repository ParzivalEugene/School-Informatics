count = 0


def F(n):
    global count
    count += 1
    if n >= 1:
        count += 1
        F(n - 1)
        F(n - 2)
        count += 1


F(35)
print(count)
