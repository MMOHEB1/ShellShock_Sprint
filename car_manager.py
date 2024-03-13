import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3)
        self.color(COLORS[random.randint(0, 5)])
        self.setx(200)
        self.sety(random.randint(-260, 260))
        self.setheading(180)


