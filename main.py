import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
# timmy.fd(100)
# timmy.rt(90)
# timmy.fd(100)
# timmy.rt(90)
# timmy.fd(100)
# timmy.rt(90)
# timmy.fd(100)
# timmy.rt(90)
# for i in range(50):
#     timmy.pd()
#     timmy.fd(10)
#     timmy.pu()
#     timmy.fd(10)

# for a in range(3):
#     timmy.fd(100)
#     timmy.rt(120)
# for a in range(4):
#     timmy.fd(100)
#     timmy.rt(90)
# for a in range(5):
#     timmy.fd(100)
#     timmy.rt(72)
# for a in range(6):
#     timmy.fd(100)
#     timmy.rt(60)
# for a in range(7):
#     timmy.fd(100)
#     timmy.rt(51.4)
# for a in range(8):
#     timmy.fd(100)
#     timmy.rt(45)
# for a in range(9):
#     timmy.fd(100)
#     timmy.rt(40)
# for a in range(10):
#     timmy.fd(100)
#     timmy.rt(36)

import random

# faces = []
# angle = []
# for n in range(3, 11):
#     shape = 360 / n
#     angle.append(shape)
#     faces.append(n)
# print(angle)
#
# for a in range(len(faces)):
#     for n in range(faces[a]):
#         timmy.fd(100)
#         timmy.rt(angle[a])
#     timmy.color(random.choice(color))


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# direction = [0, 90, 180, 270]
# timmy.width(10)
# timmy.speed("fastest")
# for a in range(300):
#     timmy.color(color())
#     timmy.fd(50)
#     timmy.setheading(random.choice(direction))
for i in range(int(360 / 5)):
    timmy.speed(0)
    timmy.color(color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)




screen = Screen()
screen.exitonclick()
