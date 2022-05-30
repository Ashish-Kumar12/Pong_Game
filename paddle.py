
from turtle import Turtle 
from pong_game_constants import *

class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=PADDLE_HEIGHT, stretch_wid=PADDLE_WIDTH)
        self.penup()
        self.goto(x=xpos, y=ypos)

    def paddle_up(self):
        new_y = self.ycor() + 20
        if new_y > HEIGHT//2 - 50: 
            new_y = HEIGHT//2 - 50
        self.goto(self.xcor(), new_y)
        
    def paddle_down(self):
        new_y = self.ycor() - 20
        if new_y < -HEIGHT//2 + 50: 
            new_y = -HEIGHT//2 + 50
        self.goto(self.xcor(), new_y)
