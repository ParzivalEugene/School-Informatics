from turtle import *

speed(0)
left(90)

k = 10
for _ in range(8):
    left(45)
    forward(12 * k)

up()
right(90)
backward(8 * k)
down()

for _ in range(4):
    forward(33)
    right(90)

up()
area = 10 * k
for x in range(-area, area, k):
    for y in range(-area, area, k):
        goto(x, y)
        dot(3, "red")

done()
