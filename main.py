import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.title("Tortor")

screen.listen(xdummy=None, ydummy=None)
screen.onkeypress(fun=player.move_up, key = "w")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    odds = 4
    if random.randint(0, odds) == odds:
        car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() > 280:
        player.level_up()
        car_manager.level_up()
        scoreboard.level_up()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()







