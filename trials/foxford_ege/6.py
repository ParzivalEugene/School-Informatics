from turtle import *

speed(0)
k = 5

for i in range(2):
    forward(15 * k)
    right(90)
    forward(20 * k)
    right(90)

up()

forward(5 * k)
right(90)
forward(10)
left(90)

down()

for i in range(2):
    forward(30 * k)
    right(90)
    forward(40 * k)
    right(90)

up()
speed(1)
for x in range(k * 5, 200, k):
    for y in range(-k * 2, -102, -k):
        goto(x, y)
        dot()

done()
