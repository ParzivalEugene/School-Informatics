from turtle import *

speed(0)
left(90)


k = 30
for _ in range(3):
    forward(13 * k)
    right(120)
up()
area = 20 * k
for x in range(0, area, k):
    for y in range(0, area, k):
        goto(x, y)
        dot(5, "red")

done()
