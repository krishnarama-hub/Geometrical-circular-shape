import turtle as t
from turtle import Screen
import random
timmy=t.Turtle()
timmy.shape("classic")


def traingle():
    for _ in range(3):   
        timmy.color("green")        
        timmy.forward(100)
        
        
        timmy.right(120)
traingle()

def square():
    for _ in range(4):
        timmy.color("blue")
        timmy.forward(100)
        
        timmy.right(90)
        
square()

def pentagon():
    timmy.forward(100)
    for _ in range(5):
        
        timmy.right(72)
        timmy.color("red")
        timmy.forward(100)
        
pentagon()

def hexagon():
    
    for _ in range(6):
        timmy.right(60)
        timmy.color("yellow")
        timmy.forward(100)
        
hexagon()  

def heptagon():

    for _ in range(7):
        timmy.right(51.43)
        timmy.color("brown")
        timmy.forward(100)
        
heptagon()

def octagon():

    for _ in range(8):
        timmy.right(45)
        timmy.color("orange")
        timmy.forward(100)
        
octagon()

def nongon():

    for _ in range(9):
        timmy.right(40)
        timmy.color("pink")
        timmy.forward(100)
        
nongon()

def decagon():

    for _ in range(10):
        timmy.right(36)
        timmy.color("purple")
        timmy.forward(100)
        
decagon()
screen=Screen()
screen.exitonclick()
