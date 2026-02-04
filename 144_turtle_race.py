from turtle import Turtle, Screen
import random

is_race_on = False
screen=Screen()
screen.setup(width=500, height=400)     #keyword argument
user_bet=screen.textinput(title="Make your move", prompt="Which colored turtle you want to bet on?")
colors=["red", "orange", "yellow", "green", "blue", "violet", "purple"]
all_turtles=[]

y_position= [-150,-100,-50,0,50,100,150]
for index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.goto(-230, y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:     #turtle is 40 by 40
            is_race_on = False
            winning_color= turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The {winning_color} turtle is the winner.")
            else:
                print(f"You Lose! The {winning_color} turtle is the winner.")

        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()