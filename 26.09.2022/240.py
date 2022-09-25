data = [int(i) for i in open('data/17-1.txt')]
avg_data = sum(data) / len(data)
counter, max_sum = 0, -10000 * 3 - 1

for i in range(len(data) - 2):
    triplet = data[i: i + 3]
    if [x < avg_data for x in triplet].count(True) > 1 and any('6' in str(x) for x in triplet):
        counter += 1
        sum_of_triplet = sum(triplet)
        if sum_of_triplet > max_sum:
            max_sum = sum_of_triplet

print(counter, max_sum)
# 3617 8416
