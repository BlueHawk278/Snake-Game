from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-20,260)

    def show_score(self, score):
        self.write("Score: " + str(score) , align="center", font=("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))
