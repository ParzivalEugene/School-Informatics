data = [int(i) for i in open('data/17-4.txt')]
avg_data = sum(data) / len(data)
counter, max_sum = 0, 0

for i in range(len(data) - 1):
    if data[i] < avg_data and data[i + 1] < avg_data and (data[i] % 100 == 19 or data[i + 1] % 100 == 19):
        counter += 1
        sum_of_pair = sum(data[i: i + 2])
        if max_sum < sum_of_pair:
            max_sum = sum_of_pair

print(counter, max_sum)
# 14 9500
