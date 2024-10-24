from turtle import Turtle, Screen

# Create a Turtle object to draw
draw = Turtle()
# Create a Screen object to handle the drawing window
screen = Screen()


def move_forward():
    """Function to move the turtle forward by 10 units"""
    draw.forward(10)


def move_backward():
    """Function to move the turtle backward by 10 units"""
    draw.backward(10)


def clock():
    """Function to rotate the turtle clockwise by 10 degrees"""
    draw.setheading(draw.heading() - 10)


def anti_clock():
    """Function to rotate the turtle counterclockwise by 10 degrees"""
    draw.setheading(draw.heading() + 10)


def reset():
    """Function to clear the drawing and reset the turtle's position"""
    draw.clear()  # Clear the drawing on the screen
    draw.penup()  # Lift the pen so it doesn't draw while moving
    draw.home()   # Return the turtle to the home position (0, 0)
    draw.pendown()  # Put the pen down to resume drawing


# Listen for keyboard inputs
screen.listen()
# Bind the 'w' key to move the turtle forward
screen.onkey(move_forward, "w")
# Bind the 's' key to move the turtle backward
screen.onkey(move_backward, "s")
# Bind the 'a' key to rotate the turtle counterclockwise
screen.onkeypress(anti_clock, "a")
# Bind the 'd' key to rotate the turtle clockwise
screen.onkeypress(clock, "d")
# Bind the 'c' key to reset the turtle's position and clear the screen
screen.onkey(reset, "c")

# Allow the program to exit when the screen is clicked
screen.exitonclick()
