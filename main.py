# import colorgram
# colors=colorgram.extract('image.jpg',30)
# color=[]
# for i in range(0,30):
#     r=colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     color.append((r,g,b))
# print(color)

import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
timmy=Turtle()
color_list=[(221, 157, 105), (238, 220, 229), (238, 217, 199), (97, 169, 213), (234, 65, 80), (218, 231, 225), (229, 118, 144), (238, 201, 97), (125, 189, 164), (29, 121, 164), (234, 73, 59), (178, 182, 215), (36, 115, 70), (24, 38, 79), (168, 210, 179), (234, 158, 179), (104, 63, 85), (169, 55, 39), (26, 133, 233), (240, 158, 148), (39, 153, 196), (27, 93, 63), (54, 169, 135), (76, 73, 27), (31, 72, 37), (4, 81, 109), (20, 60, 113), (153, 206, 217), (186, 157, 64)]
timmy.hideturtle()
timmy.speed(10)
timmy.penup()
timmy.goto(-200,-200)
for _ in range(0,10):
    for _ in range(0,10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50*10)
    timmy.right(180)
    timmy.pendown()



my_screen=Screen()
my_screen.exitonclick()