from turtle import Turtle, Screen
from random import randint

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
user_bet = ""
racing = True

screen.setup(width=500, height=400)
while not user_bet in colors:
    user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")

for color in colors:
    # Create turtle and set color
    next_turtle = Turtle(shape="turtle")
    next_turtle.color(color)
    next_turtle.penup()

    # Send turtle to starting coords
    y_cor = -150 + colors.index(color) * 50
    next_turtle.goto(x=-230, y=y_cor)

    # Add turtle to array
    turtles.append(next_turtle)

# Run the race
while racing:
    for turt in turtles:
        step = randint(1, 10)
        turt.forward(step)
        if turt.xcor() >= 230:
            racing = False
            winner = turt.color()[0]
            break

# Announce winner
if user_bet == winner:
    print(f"You win! The {winner} turtle is the winner.")
else:
    print(f"You lose. The {winner} turtle is the winner.")

screen.exitonclick()