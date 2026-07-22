import turtle as t
from turtle import Screen
import random
timmy=t.Turtle()

list_of_number=[90,180,270,360]
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "navy",
    "sky blue",
    "deep sky blue",
    "light blue",
    "steel blue",
    "royal blue",
    "dodger blue",
    "midnight blue",
    "turquoise",
    "aquamarine",
    "teal",
    "forest green",
    "lime green",
    "sea green",
    "spring green",
    "olive",
    "olive drab",
    "khaki",
    "goldenrod",
    "dark green",
    "dark blue",
    "dark red",
    "dark orange",
    "dark violet",
    "dark cyan",
    "violet",
    "plum",
    "orchid",
    "lavender",
    "indigo",
    "coral",
    "salmon",
    "tomato",
    "crimson",
    "firebrick",
    "hot pink",
    "deep pink",
    "light pink",
    "light coral",
    "light salmon",
    "beige",
    "ivory",
    "wheat",
    "chocolate",
    "sienna",
    "peru",
    "maroon",
    "tan",
    "mint cream",
    "honeydew",
    "snow"
]
count=0
while True:

    rand=random.choice(list_of_number)
    timmy.width(10)
    timmy.color(random.choice(colors))
    
    timmy.setheading(rand)#setheading is nothing it is same as the right and left but it just give the direction directly instead of right and left

    timmy.forward(20)
    
    timmy.speed("fastest")
screen=Screen()
screen.exitonclick()
