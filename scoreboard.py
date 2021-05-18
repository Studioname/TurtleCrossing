from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-150, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",align= "center",font= FONT)
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over", align="center", font=FONT)
