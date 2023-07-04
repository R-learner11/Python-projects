# import colorgram
# color = colorgram.extract('hirst.jpg')
# color_list = []
# for _ in color:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     tup = (r,g,b)
#     color_list.append(tup)

color_list = [(230, 223, 226), (207, 72, 90), (158, 6, 55), (252, 223, 0), (226, 233, 228), (238, 133, 43), (14, 60, 143), (94, 204, 187)]

import turtle as t
from random import choice
t.colormode(255)
X = -200
Y = -200

for _ in range(10):
    tim = t.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.dot(20, choice(color_list))



screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("My self hirst painting")

screen.exitonclick()
