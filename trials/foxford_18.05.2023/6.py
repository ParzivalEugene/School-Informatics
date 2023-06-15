from turtle import *

left(90)
speed(0)
k = 25
color("black", "red")

begin_fill()
for _ in range(3):
    forward(14 * k)
    right(120)
end_fill()

area = 30 * k
canvas = getcanvas()
counter = 0
for x in range(-area, area, k):
    for y in range(-area, area, k):
        data = canvas.find_overlapping(x, y, x, y)
        if len(data) == 1 and data[0] == 5:
            counter += 1
print(counter)
