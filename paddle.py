from turtle import Turtle

MAX_LEFT = -350
MAX_RIGHT = 350

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -275)

    def go_left(self):
        if self.xcor() > MAX_LEFT:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())


    def go_right(self):
        if self.xcor() < MAX_RIGHT:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
