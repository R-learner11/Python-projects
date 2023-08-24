from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_pos = 10
        self.y_pos = 10
        self.set_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() +  self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pos *= -1
        self.set_speed *= 0.9

    def bounce_x(self):
        self.x_pos *= -1
        self.set_speed *= 0.9

    def reset(self):
        self.set_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

