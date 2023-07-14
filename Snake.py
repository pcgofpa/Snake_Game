from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITION_BOUNDRY = 280


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]
        self.wall_collision()

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        snake_segment = Turtle("circle")
        snake_segment.color("#DE7218")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake.append(snake_segment)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            snake_x = self.snake[segment - 1].xcor()
            snake_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(snake_x, snake_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def wall_collision(self):
        if self.snake_head.xcor() > POSITION_BOUNDRY or self.snake_head.xcor() < -POSITION_BOUNDRY:
            return True
        elif self.snake_head.ycor() > POSITION_BOUNDRY or self.snake_head.ycor() < -POSITION_BOUNDRY:
            return True
        else:
            return False

    def snake_collision(self):
        for segment in self.snake[1:]:
            if self.snake_head.distance(segment) < 10:
                return True
