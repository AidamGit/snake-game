from modules import *
import turtle as t
import time

# start game prompt
prompt = Turtle()
prompt.hideturtle()
prompt.pencolor("white")
prompt.write(arg="PRESS SPACE TO START", font=("arial", 20, "normal"), align="center")

# display
display = t.Screen()
display.setup(height=625, width=650)
display.title("Aidam Snake Game")
display.bgcolor("black")
display.listen()
display.tracer(False)

# score
score_display = Score()
score_display.setposition(-290, 280)
high_score_display = Score()
high_score_display.setposition(200, 280)
with open("high_score.txt", mode="r") as import_high_score:
    high_score = int(import_high_score.read())

# creating the wall/border
border = t.Turtle()
border.color("gold")
border.pensize(10)
border.hideturtle()
border.penup()
border.setposition(-288, 268)
border.pendown()
border.setheading(0)
border.forward(288 * 2)
border.setheading(270)
border.forward(268 * 2)
border.setheading(180)
border.forward(288 * 2)
border.setheading(90)
border.forward(268 * 2)


def play_snake():

    prompt.clear()

    score_display.clear()
    score = 0
    global high_score

    # declaring snake and food
    snake = [Snake((0, 0)), Snake((0, 0)), Snake((0, 0))]
    food = Food()
    food.random_position()

    # logic: imagine the snake as a list
    #        the index 0 is its head while all the indexes after that are the segments of it's body
    #        every time the snake head comes into contact with food, we append the snake "list"
    #        with a new segment of it's body thus making it longer

    snake[0].setposition(0, 0)
    snake[0].turtlesize(1, 1, 6)  # this is the head (snake[0])
    snake[0].showturtle()
    snake[0].setheading(90)

    # the code below makes it possible for snake head (snake[0]) to be controlled with WASD
    display.onkey(key="w", fun=snake[0].face_up)
    display.onkey(key="a", fun=snake[0].face_left)
    display.onkey(key="s", fun=snake[0].face_down)
    display.onkey(key="d", fun=snake[0].face_right)

    alive = True
    while alive:

        score_display.write(f"Score: {score}", font=("arial", 12, "normal"))
        high_score_display.write(f"High Score: {high_score}", font=("arial", 12, "normal"))

        display.update()

        time.sleep(0.05)
        snake[0].forward(10)

        # when snake eats food, the code below adds a new segment is added to the snake's body
        if snake[0].distance(food) <= 20:

            # the new segments will spawn in the last segment of the snake before they get added
            # the reasoning behind this is to prevent them from appearing at (0,0) for a split second
            snake.append(Snake(snake[len(snake)-1].position()))
            snake.append(Snake(snake[len(snake)-1].position()))

            score += 1
            score_display.clear()
            if score >= high_score:
                high_score_display.clear()
                high_score = score
                with open("high_score.txt", mode="w") as update_high_score:
                    update_high_score.write(str(high_score))

            food.random_position()

        # updated_position stores the updated positions of the snake segments after the head moves
        updated_position = []
        for index in range(1, len(snake)):  # also possible = for segment in snake[:len(snake)]
            updated_position.append(snake[index - 1].position())

        for index in range(1, len(snake)):

            # checks if the snake head collided with the tail
            if int(snake[0].distance(snake[index])) == 0:
                alive = False
                score = 0
                for segment in snake:
                    segment.hideturtle()
                food.hideturtle()
                prompt.write(arg="PRESS SPACE TO PLAY AGAIN", font=("arial", 20, "normal"), align="center")

            # if snake did not collide, then the code below updates the position of the segments
            snake[index].setposition(updated_position[index - 1])

        # the code below checks if snake head hit the wall (280, 260) and ends the game if it does
        if int(snake[0].xcor()) >= 280 or int(snake[0].xcor()) <= -280 or \
                int(snake[0].ycor()) >= 260 or int(snake[0].ycor()) <= -260:
            alive = False
            score = 0
            for segment in snake:
                segment.hideturtle()
            food.hideturtle()
            prompt.write(arg="PRESS SPACE TO PLAY AGAIN", font=("arial", 20, "normal"), align="center")


display.onkey(key="space", fun=play_snake)
t.done()
