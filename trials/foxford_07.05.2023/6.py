from turtle import *

speed(0)
k = 10

up()
right(180)
forward(10 * k)
right(90)
forward(20 * k)
right(90)
down()

for _ in range(2):
    forward(15 * k)
    right(90)
    forward(20 * k)
    right(90)

up()
forward(5 * k)
right(90)
forward(10 * k)
left(90)
down()

for _ in range(2):
    forward(30 * k)
    right(90)
    forward(40 * k)
    right(90)

up()
counter = 0
for x in range(-50, 60, k):
    for y in range(0, 110, k):
        # goto(x, y)
        # dot(5, "red")
        counter += 1
print(counter)

done()
