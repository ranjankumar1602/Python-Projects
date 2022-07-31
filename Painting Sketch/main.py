from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()


def move_forwards():
    pencil.forward(10)

def move_backwards():
    pencil.backward(10)

def turn_left():
    new_heading = pencil.heading() + 10
    pencil.setheading(new_heading)

def turn_right():
    new_heading = pencil.heading() - 10
    pencil.setheading(new_heading)

def clear():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()

def down():
    pencil.pendown()

def up():
    pencil.penup()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(up, "u")
screen.onkey(down, "d")

screen.exitonclick()
