import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.movement, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    if turtle.ycor() >= FINISH_LINE_Y:
        screen.update()
        scoreboard.add_score()
        turtle.reset()
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            print("hit")
            game_is_on = False
    #     need to increase moving increment


screen.exitonclick()