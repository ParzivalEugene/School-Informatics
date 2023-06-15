from turtle import *


speed(0)
left(90)
k = 10
for i in range(4):
    forward(16 * k)
    right(45)
    forward(8 * k)
    right(135)
up()
area = 20 * k
for x in range(0, 7 * k, k):
    for y in range(0, 18 * k, k):
        goto(x, y)
        dot(5, "red")
done()
