
from turtle import Turtle 
from pong_game_constants import * 

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, HEIGHT//2-100)
        self.write(self.left_score, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        self.goto(+100, HEIGHT//2-100)
        self.write(self.right_score, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
