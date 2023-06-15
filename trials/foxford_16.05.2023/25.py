from fnmatch import fnmatch


mask = "10*04?23"
for i in range(0, 10**8 + 1, 51):
    if fnmatch(str(i), mask):
        print(i, i // 51)

