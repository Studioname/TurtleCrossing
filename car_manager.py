from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        turtle.color(random.choice(COLORS))
        turtle.goto(320, (random.randint(-12,12) * 20))
        turtle.shape("square")
        self.cars.append(turtle)


    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_speed, car.ycor())

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
        self.hideturtle()