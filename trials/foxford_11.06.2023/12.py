s = ">" + "1" * 17 + "2" * 30 + "3" * 28
while any(f">{x}" in s for x in range(1, 4)):
    if ">1" in s:
        s = s.replace(">1", "22>", 1)
    if ">2" in s:
        s = s.replace(">2", "2>1", 1)
    if ">3" in s:
        s = s.replace(">3", "1>", 1)
print(sum(map(int, s[:-1])))
