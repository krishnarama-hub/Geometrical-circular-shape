import turtle as t
from turtle import Screen
import random
timmy=t.Turtle()

t.colormode(255)
def color():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    color=(r,b,g)
    return color

for i in range(72):
    timmy.speed("fastest")
    timmy.pencolor(color())
    timmy.circle(100)
    timmy.right(5)
screen=Screen()
screen.exitonclick()
