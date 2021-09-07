from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle((375, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# Create another paddle
# Create the ball and make it move
    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the left and the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 395:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # Detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

# Keep score
































screen.exitonclick()
