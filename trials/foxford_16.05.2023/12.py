s = "7" * 178 + "5" * 45
while "5555" in s or "7777" in s:
    if "7777" in s:
        s = s.replace("7777", "5", 1)
    if "5555" in s:
        s = s.replace("5555", "7", 1)
print(s)