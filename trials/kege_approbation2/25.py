from fnmatch import fnmatch


data = [253 * i for i in range(10**8) if 253 * i < 10**8]
for i in data:
    if fnmatch(str(i), "12??15*6"):
        print(i, i // 253)
