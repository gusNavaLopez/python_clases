from turtle import *
from time import *
color('blue', 'white')
begin_fill()
for i in range(10):
    forward(20)
    penup()
    forward(5)
    pendown()
left(180)
penup()
forward(250)
left(90)
forward(100)
left(90)
pendown()
x=5
for i in range(10):
    forward(x*i)
    penup()
    forward(5)
    pendown()    

end_fill()
done()