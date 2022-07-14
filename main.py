from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import winsound

screen = Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake_speed = 0
user_choice = screen.textinput(title="CHOOSE GAME LEVEL", prompt="Enter 'e' for EASY MODE.\n\nEnter 'm' for MEDIUM MODE.\n\nEnter 'h' for HARD MODE.").lower()
if user_choice=='e':
    snake_speed=0.1
elif user_choice =='m':
    snake_speed=0.07
elif user_choice =='h':
    snake_speed=0.05
else:
    print("Invalid Choice")
    screen.bye()

if user_choice == 'e' or user_choice == 'm' or user_choice == 'h':
    snake=Snake()
    snake.walls()
    food=Food()
    score = Scoreboard()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(snake_speed)
        snake.move()
        
        if snake.head.distance(food) < 15: 
            winsound.PlaySound("eat.wav",winsound.SND_ASYNC)
            food.refresh()
            snake.extend()
            score.update_scoreboard()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
            winsound.PlaySound("bi.wav",winsound.SND_ASYNC)
            score.reset()
            snake.reset()

        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                winsound.PlaySound("bi.wav",winsound.SND_ASYNC)
                score.reset()
                snake.reset()

    screen.exitonclick()
