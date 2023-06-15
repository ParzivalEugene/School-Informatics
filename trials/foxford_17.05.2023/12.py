s = ">" + "1" * 20 + "2" * 20 + "3" * 10
while any(f">{x}" in s for x in range(1, 4)):
    s = s.replace(">1", "22>3", 1).replace(">2", "33>", 1).replace(">3", "11>2", 1)
print(sum(int(x) for x in s.replace(">", "")))
