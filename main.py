from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n red, orange, yellow, green, blue or purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

popup_message = Turtle()
popup_message.penup()
popup_message.hideturtle()
popup_message.goto(0, 0)

i = 0
for _ in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[_])
    tim.goto(x=-230, y=-100 + i)
    i += 40
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                popup_message.write(f"You've won! The {winning_color} is the winner!", align="center",
                                    font=("Arial", 16, "normal"))
            else:
                popup_message.write(f"You've lost! The {winning_color} is the winner!", align="center",
                                    font=("Arial", 16, "normal"))
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)
screen.exitonclick()