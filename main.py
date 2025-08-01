import time
from turtle import Screen
from snake import Snake
from food import  Food
from scoreboard import  Scoreboard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game = True

while game is True:
    screen.update()
    time.sleep(0.1)
    snake.move()



    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            game = False
            scoreboard.game_over()






screen.exitonclick()
