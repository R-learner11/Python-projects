# import colorgram
# colors = colorgram.extract('hirst.jpg',10)
# color_list = []
# for _ in colors:
#     # rgb = _.rgb
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     tup = (r, g, b)
#     color_list.append(tup)

print(color_list)

import turtle as t
from random import choice
hirst = t.Turtle()
t.colormode(255)
hirst.speed('fastest')

color_list = [(230, 223, 226), (207, 72, 90), (158, 6, 55), (252, 223, 0), (226, 233, 228), (238, 133, 43), (14, 60, 143), (94, 204, 187)]


# creating small dots
# hirst.fillcolor('violet')
# hirst.circle(10)

# def draw_rows():
#     for _ in range(10):
#         # hirst.pendown()
#         hirst.dot(20, choice(color_list))
#         hirst.penup()
#         hirst.forward(30)
#         hirst.pendown()
#
# hirst.penup()
# # hirst.shape('turtle')
# hirst.setheading(225)
# hirst.forward(200)
# hirst.setheading(0)
#
# for i in range(10):
#     draw_rows()
#     hirst.penup()
#     pos = list(hirst.position())
#     # print(pos[0]+pos[1])
#     print(pos[0], pos[1])
#     hirst.setx(-pos[0]+20)
#     hirst.sety(pos[1]+30)

hirst.penup()
hirst.hideturtle()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
no_of_dots = 100
for dot_count in range(1, no_of_dots+1):
    hirst.dot(20, choice(color_list))
    hirst.forward(50)

    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)


s = t.Screen()
s.exitonclick()