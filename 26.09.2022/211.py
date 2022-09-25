data = [int(i) for i in open('data/17-4.txt')]
avg_data = sum(data) / len(data)
counter, min_sum = 0, 10000 * 2 + 1

for i in range(len(data) - 1):
    sum_of_pair = sum(data[i: i + 2])
    if (data[i] > avg_data or data[i + 1] > avg_data) and sum_of_pair % 7 == 0:
        counter += 1
        if sum_of_pair < min_sum:
            min_sum = sum_of_pair

print(counter, min_sum)
# 202 6916
