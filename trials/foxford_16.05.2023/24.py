with open("data/24.txt", encoding="utf-8") as file:
    text = file.read()
    triples = ("GFE", "EGF")
    counter_gfe, counter_egf = 0, 0

    line = triples[0]
    while line + triples[0] in text:
        line += triples[0]
    print(line, len(line), f"| line in text: {line in text}")

    line = triples[1]
    while line + triples[1] in text:
        line += triples[1]
    print(line, len(line), f"| line in text: {line in text}")

    patterns = triples[:]
    while any(x in text for x in patterns):
        patterns = [i + j for i in patterns for j in triples if i + j in text]
    patterns = [
        "GFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFE",
        "EGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGFEGF",
    ]
    for line in patterns:
        print(line, len(line), f"| line in text: {line in text}")
