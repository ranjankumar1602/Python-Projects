import random
from turtle import Turtle, Screen

screen=Screen()
screen.bgcolor("black")
screen.setup(700,400)
userBet = screen.textinput(title="Make your BET",prompt="Which Turtle will WIN")
colours=["Blue","violet","green","red","purple","orange","cyan"]
y_position=[-150, -100, -50, 0, 50, 100, 150]
allTurtles = []

for i in range(0,7):
  kachua=Turtle("turtle")
  kachua.color(colours[i])
  kachua.penup()
  kachua.goto(x=-330,y=y_position[i])
  allTurtles.append(kachua)

if userBet:
    isRaceOn=True

while isRaceOn:
    for kachua in allTurtles:
        if kachua.xcor() > 330:
            isRaceOn=False
            winningcolour=kachua.pencolor()
            if winningcolour==userBet.lower():
                print(f"You've WON! The {winningcolour} kachua is the Winner")
            else:
                print(f"You've LOST! The {winningcolour} kachua is the Winner")

        distance = random.randint(0,10)
        kachua.forward(distance)

screen.exitonclick()