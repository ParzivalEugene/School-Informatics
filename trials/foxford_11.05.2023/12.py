s = "7" * 123
while "7777" in s or "1111" in s:
    if "7777" in s:
        s = s.replace("7777", "11", 1)
    else:
        s = s.replace("1111", "77", 1)
print(s)
