
import time 
from turtle import Screen
from paddle import Paddle
from ball import Ball 
from scoreboard import Scoreboard
from pong_game_constants import *

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.listen()
screen.tracer(0)

game_is_on = True 

left_paddle = Paddle(xpos=-PADDLE_X_POS, ypos=PADDLE_Y_POS)
right_paddle = Paddle(xpos=PADDLE_X_POS, ypos=PADDLE_Y_POS)

ball = Ball()
score_board = Scoreboard()

screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

while game_is_on : 

    # Detection with wall and bounce
    if ball.ycor() > HEIGHT//2 - 20 or ball.ycor() < -HEIGHT//2 + 20:
        ball.bounce_y_axis()

    # Detecttion with left or right paddle
    if ( ball.xcor() < left_paddle.xcor()+20 and ball.distance(left_paddle)<50 ) or ( ball.xcor() > right_paddle.xcor()-20 and ball.distance(right_paddle)<50 ):
        ball.bounce_x_axis()

    # Detect when right paddle misses the ball
    if ball.xcor() > WIDTH//2 - 20:
        ball.reset_position()
        score_board.left_point()

    # Detect when left paddle misses the ball
    if ball.xcor() < -WIDTH//2 + 20:
        ball.reset_position()
        score_board.right_point()

    ball.move()
    time.sleep(ball.move_speed)
    screen.update() 

screen.exitonclick()
