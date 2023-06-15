from turtle import *

k = 10

left(90)
speed(0)
color("black", "red")
begin_fill()

for _ in range(3):
    forward(14 * k)
    right(120)

end_fill()

canvas = getcanvas()
counter, area = 0, 100 * k

for x in range(-area, area, k):
    for y in range(-area, area, k):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            counter += 1
print(counter)
