data = """1	8	0
2	6	0
3	8	2
4	5	3
5	8	0
6	9	1;5
7	6	1;6
8	9	6;7
9	5	5
10	7	9
11	5	1;10
12	5	0
13	8	3
14	6	8
15	8	3;7"""

data = [i.split() for i in data.splitlines()]
data = [[int(i[0]), int(i[1]), [int(j) for j in i[2].split(";")]] for i in data]
counter = {0: 0}
gap = 0

while len(counter) != len(data) + 1:
    for line in data:
        if all(ids in counter for ids in line[2]):
            counter[line[0]] = max(counter[i] for i in line[2]) + line[1] + gap
print(max(counter.values()))
