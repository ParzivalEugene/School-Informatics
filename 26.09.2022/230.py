data = [int(i) for i in open('data/17-1.txt')]
avg_data = sum(data) / len(data)
counter, max_sum = 0, -10000 * 3 - 1

for i in range(len(data) - 2):
    triplet = data[i: i + 3]
    if any(x < avg_data for x in triplet) and any(x % 10 == 6 for x in triplet):
        counter += 1
        sum_of_triplet = sum(triplet)
        if max_sum < sum_of_triplet:
            max_sum = sum_of_triplet

print(counter, max_sum)
# 2432 17979
