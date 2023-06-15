data = [i**2 for i in range(10, 20)]
for i in range(100):
    s = ">" + "0" * 25 + "1" * i + "2" * 17
    while ">0" in s or ">1" in s or ">2" in s:
        if ">1" in s:
            s = s.replace(">1", "12>", 1)
        if ">2" in s:
            s = s.replace(">2", "22>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    s = s.replace(">", "")
    if sum(map(int, s)) in data:
        print(i)
        print(sum(map(int, s)))
