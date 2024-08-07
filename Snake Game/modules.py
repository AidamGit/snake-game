from turtle import Turtle
import random


class Snake(Turtle):

    def __init__(self, coordinates):
        # the coordinates argument is necessary to avoid a new segment from appearing for a split second at (0, 0)
        super().__init__()
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shape("square")
        self.setheading(90)
        self.setposition(coordinates)

    def move_forward(self):
        self.forward(5)

    def face_up(self):
        self.setheading(90) if int(self.heading()) != 270 else False

    def face_down(self):
        self.setheading(270) if int(self.heading()) != 90 else False

    def face_left(self):
        self.setheading(180) if int(self.heading()) != 0 else False

    def face_right(self):
        self.setheading(0) if int(self.heading()) != 180 else False

    def restart(self):
        self.penup()
        self.setposition(0, 0)
        self.setheading(90)
        self.pendown()


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.speed("fastest")
        self.shape("circle")
        self.turtlesize(0.5, 0.5, 0)
        self.setheading(90)
        self.penup()

    def random_position(self):
        self.setposition(random.randint(-270, 270), random.randint(-250, 250))


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("silver")
        self.penup()
        self.hideturtle()
