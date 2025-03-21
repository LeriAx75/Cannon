"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199

	#Estos son los valores que controlan la velocidad del proyectil. Entre mas pequeño el numero por el que dividimos mas rapido sera
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
    #Este valor controla la velocidad de los balones. Entre mas grande sea el valor mayor sera la velocidad de los balones
        target.x -= 0.75

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    else:
        """Reposiciona las pelotas en caso de que salgan de la pantalla"""
        ball.x = -199
        ball.y = -199
        speed.x = 0
        speed.y = 0

    dupe = targets.copy()
    targets.clear()

    for target in dupe:       
        if abs(target - ball) > 13:
            targets.append(target)


    draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
