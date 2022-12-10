from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time

sc = Screen()
sc.setup(width=1.0, height=1.0)
sc.bgcolor("black")

sc.tracer(0)
sc.listen()
food = Food()
snake = Snake()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")
score = ScoreBoard()
is_game = True

try:
    while(is_game):
        sc.update()
        time.sleep(0.1)
        snake.move()
        if(snake.head.distance(food) < 15):
            food.refresh()
            score.inc_score()
            snake.extend()

        if(snake.head.xcor() > 620 or snake.head.xcor() < -620 or snake.head.ycor() > 330 or snake.head.ycor() < -330):
            score.game_over()
            is_game = False

        for block in snake.blocks:
            if(block != snake.head and snake.head.distance(block) < 10):
                score.game_over()
                is_game = False
                break

except:
    pass

sc.exitonclick()


