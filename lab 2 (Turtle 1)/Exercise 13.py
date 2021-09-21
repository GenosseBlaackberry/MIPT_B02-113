import turtle
turtle.shape('turtle')
import math
turtle.speed(10)

def polygon(n, r, alpha, spin=1, par=True, T=True):
    pos =[]
    if par:
        a=r
    else:
        a=r*(2*math.sin(math.pi/n))
    if T:
        turtle.penup()
        turtle.forward(a/(2*math.sin(math.pi/n)))
        turtle.left(spin*180-90*(n-2)/n)
        turtle.pendown()
    for i in range(alpha):
        turtle.forward(a)
        turtle.left(spin*360/n)
        pos.append(turtle.position())
    if T:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.right(spin*180-90*(n-2)/n)
    return pos

def kruzhok(r, c):
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    polygon(360, r, 360, -1, 0, 0)
    turtle.end_fill()
    turtle.penup()

def ex13():
    kruzhok(100, 'yellow')
    turtle.goto(-30, -30)
    kruzhok(10, 'blue')
    turtle.goto(30, -30)
    kruzhok(10, 'blue')
    turtle.goto(0, -40)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor('brown')
    turtle.forward(70)
    turtle.penup()
    turtle.goto(-30, -90)
    turtle.pendown()
    turtle.pencolor('red')
    polygon(360, 30, 180, 1, 0, 0)
            
ex13()
