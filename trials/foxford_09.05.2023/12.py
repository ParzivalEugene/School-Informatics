s = ">" + "1" * 20 + "2" * 20 + "3" * 10
while any(x in s for x in (">1", ">2", ">3")):
    s = s.replace(">1", "22>3", 1)
    s = s.replace(">2", "33>", 1)
    s = s.replace(">3", "11>2", 1)

print(s)
print(sum(map(int, s.replace(">", ""))))
