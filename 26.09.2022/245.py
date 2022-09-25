data = [int(i) for i in open('data/17-243.txt')]
max_data = max(data)
counter, min_sum = 0, 10000 * 2 + 1

for i in range(len(data) - 1):
    pair = data[i: i + 2]
    if all(x < max_data for x in pair) and all(x % 71 == 0 for x in pair) and any(x % 13 == 0 for x in pair):
        print(pair)
        counter += 1
        sum_of_pair = sum(pair)
        if min_sum > sum_of_pair:
            min_sum = sum_of_pair

print(counter, min_sum)
# 1 10224
