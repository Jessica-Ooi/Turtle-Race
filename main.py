"""
Programmer: Jessica Ooi
Project: Turtle Racer
Date: 11/17/2022
"""
import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'orange', 'green', 'black', 'purple', 'cyan', 'yellow', 'pink', 'brown', 'grey']


def get_number_of_racers():
    racers = 3


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racers')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the {winner} turtle!")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color(f'{winner}')
turtle.write(f"The winner is {winner}!", font=("Verdana", 18, 'italic'), align='center')
time.sleep(10)
