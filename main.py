from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()


def move_forward():
    draw.forward(10)


def move_backward():
    draw.backward(10)


def clock():
    draw.setheading(draw.heading() - 10)


def anti_clock():
    draw.setheading(draw.heading() + 10)


def reset():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkeypress(anti_clock, "a")
screen.onkeypress(clock, "d")
screen.onkey(reset, "c")

screen.exitonclick()
