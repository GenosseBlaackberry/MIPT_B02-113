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

def stepseek(n, t=2):
    temp = []
    for i in range(1, n//2+1):
        if n%i==0:
            pass
        else:
            temp.append(i)
    return max(temp)
    
    
def star(n):
    turtle.pencolor('white')
    data = polygon(n, 30, n, -1, 0, 0)
    turtle.pencolor('black')
    step = stepseek(n)
    for i in range(n+1):
        c = n-1-(i*step%n)
        turtle.goto(data[c])

def ex14():
    turtle.penup()
    turtle.goto(-40, 0)
    turtle.pendown()
    star(5)
    turtle.penup()
    turtle.goto(40, 0)
    turtle.pendown()
    star(7)

ex14()

