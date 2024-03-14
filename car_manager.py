import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        all_cars = []
        # super(CarManager, self).__init__()
        # self.shape("square")
        # self.penup()
        # self.shapesize(stretch_len=3)
        # self.color(random.choice(COLORS))
        # self.setx(300)
        # self.sety(random.randint(-260, 260))
        # self.setheading(180)

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)