import time
from turtle import Screen
from Snake import *
from Snake_Food import Food
from Snake_Score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increment_score()

    if snake.wall_collision():
        scoreboard.game_over()
        game_on = False

    if snake.snake_collision():
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
