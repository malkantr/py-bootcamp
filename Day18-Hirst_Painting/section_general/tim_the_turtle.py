# from turtle import Turtle
# import turtle as t
#
# tim = t.Turtle()
# tom = t.Turtle()


from turtle import Turtle, Screen


def turn_and_go(timmy_the_turtlex):
    timmy_the_turtlex.right(90)
    timmy_the_turtlex.forward(100)


tim = Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# turn_and_go(tim)
# turn_and_go(tim)
# turn_and_go(tim)
# turn_and_go(tim)

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
