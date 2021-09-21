import turtle as tu

ax = 0
ay = -10
vx = 10
vy = -10
for t in range(100):
    print(vy)
    tu.goto(tu.position()[0]+vx, tu.position()[1]+vy)
    vx+=ax
    vy+=ay
    if tu.position()[1]<=0:
        vy = abs(vy)
