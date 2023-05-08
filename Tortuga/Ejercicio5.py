from turtle import *
from time import *
color('blue', 'white')
begin_fill()
penup()
left(180)
forward(200)
pendown()
for i in range(3):
    forward(100)
    right(120)
right(180)
penup()
forward(100)
pendown()
for i in range(4):
    forward(100)
    left(90)
penup()
forward(200)
pendown()
for i in range(5):
    forward(100)
    left(72)
end_fill()
done()