central_line = Turtle()
central_line.color('white')
central_line.penup()
central_line.pensize(5)
central_line.goto(0, 300)
central_line.setheading(270)
central_line.pendown()


def create_dotted_line():
    for _ in range(10):
        central_line.forward(30)
        central_line.penup()
        central_line.forward(30)
        central_line.pendown()


create_dotted_line()
central_line.hideturtle()
