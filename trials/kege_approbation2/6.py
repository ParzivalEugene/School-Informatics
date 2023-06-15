import math

counter = 0

for x in range(-9, 0):
    for y in range(0, 15):
        if -math.sin(math.pi / 4) * 12 < x < 0:
            if abs(x) < y < abs(x) + 6:
                counter += 1
                print(x, y)
print(counter)