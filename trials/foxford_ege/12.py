def main():
    sums = [i**2 for i in range(20)]
    for i in range(100):
        s = ">" + "0" * 25 + "1" * i + "2" * 17
        while any(x in s for x in (">1", ">2", ">0")):
            if ">1" in s:
                s = s.replace(">1", "12>", 1)
            if ">2" in s:
                s = s.replace(">2", "22>", 1)
            if ">0" in s:
                s = s.replace(">0", "1>", 1)
        line_sum = sum(int(i) for i in s if i in "012")
        if line_sum in sums:
            return i


print(main())
