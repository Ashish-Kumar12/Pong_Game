
from turtle import Turtle 
from pong_game_constants import * 

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.move_speed = INIT_BALL_SPEED
        self.x_move = 10
        self.y_move = 10

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_axis()
        self.move_speed = INIT_BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x= new_x, y= new_y)

    def bounce_y_axis(self):
        # reverse y-axis direction
        self.y_move *= -1

    def bounce_x_axis(self):
        # reverse x-axis direction
        self.x_move *= -1
        self.move_speed *= 0.9
