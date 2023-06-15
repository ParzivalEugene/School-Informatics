from fnmatch import fnmatch

data = [273 * i for i in range(1, 10**7) if 273 * i < 10**8]
for i in data:
    if fnmatch(str(i), "12??36*1"):
        print(i, i // 273)
