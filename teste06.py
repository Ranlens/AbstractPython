import turtle
turtle.bgcolor('black')
turtle.pensize(5)
turtle.speed(-10)


for i in range(70):
    for colours in ['orange','red',]:
        turtle.color(colours)
        turtle.circle(200)
        turtle.left(10)
turtle.hideturtle()