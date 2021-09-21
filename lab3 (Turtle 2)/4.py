import turtle as tu

ax = 0
ay = -10
vx = 10
vy = 30
x = 0
y = 0
t = 0
t_end = 100
tick = 0.1
tu.shape('turtle')
tu.goto(500, 0)
tu.goto(-50, 0)
tu.goto(0, 0)
for i in range(int(t_end/tick)):
    if y>0:
        tu.goto(x, y)
    else:
        vy = 0.95*abs(vy)
        vx = 0.95*vx
    x+= vx*tick+ ax*tick**2/2
    y+= vy*tick + ay*tick**2/2
    vx+= ax*tick
    vy+= ay*tick
    tu.goto(x, y)
