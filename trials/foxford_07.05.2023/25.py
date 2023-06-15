# 1?3124*6
from fnmatch import fnmatch


def main():
    counter = 0
    for i in range(0, 10**10, 1983):
        if fnmatch(str(i), "1?3124*6"):
            print(i, i // 1983)
            counter += 1
        if counter == 2:
            return


main()
