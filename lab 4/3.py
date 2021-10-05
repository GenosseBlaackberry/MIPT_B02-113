import pygame
from pygame.draw import *

pygame.init()

def screenfill(cd):
    global screen
    screen = pygame.display.set_mode((cd))
    rect(screen, (100, 100, 255), (0, 0, cd[0], cd[1]//2))
    rect(screen, (255, 255, 255), (0, cd[1]//2, cd[0], cd[1]//2))

def whiteball(cd):
    ori = cd[2]/abs(cd[2])
    ellipse(screen, (0, 0, 0), (cd[0], cd[1], cd[2], cd[3]))
    ellipse(screen, (255, 255, 255), (cd[0] + 1*ori, cd[1] + 2, cd[2] - 2*ori, cd[3] - 4))

def fibsh(cd):
    cd = (cd[0] / cd[2], cd[1] / abs(cd[2]), abs(cd[2]), cd[2]/abs(cd[2]))
    polygon(screen, (0, 0, 0),
            ((((cd[0] + 10) * cd[2] - 1) * cd[3], (cd[1] + 4) * cd[2] + 1), (((cd[0] + 8) * cd[2] - 1) * cd[3], (cd[1] - 3) * cd[2] - 1),
             (((cd[0] + 30) * cd[2] + 1) * cd[3], (cd[1] - 3) * cd[2] - 1), (((cd[0] + 28) * cd[2] + 1) * cd[3], (cd[1] + 4) * cd[2] + 1)))
    polygon(screen, (255, 150, 0), (((cd[0] + 10)*cd[2]*cd[3], (cd[1] + 4)*cd[2]), ((cd[0] + 8)*cd[2]*cd[3], (cd[1] - 3)*cd[2]),
                                    ((cd[0] + 30)*cd[2]*cd[3], (cd[1] - 3)*cd[2]), ((cd[0] + 28)*cd[2]*cd[3], (cd[1]+4)*cd[2])))
    ellipse(screen, (0, 0, 0), ((cd[0] * cd[2] -1) * cd[3] , cd[1] * cd[2] - 1, (40 * cd[2] + 2) * cd[3], 20 * cd[2] + 2))
    ellipse(screen, (50, 180, 50), (cd[0] * cd[2] * cd[3], cd[1] * cd[2], 40 * cd[2] * cd[3], 20 * cd[2]))
    polygon(screen, (0, 0, 0),
            (((cd[0] * cd[2] + 1)* cd[3], (cd[1] + 8) * cd[2]), (((int(cd[0] - 7) * cd[2] - 1)* cd[3]), (cd[1] + 15) * cd[2] + 1),
             ((int((cd[0] - 7) * cd[2] - 1)* cd[3]), cd[1] * cd[2] - 1)))
    polygon(screen, (50, 180, 50), ((cd[0]*cd[2]*cd[3], (cd[1] + 8)*cd[2]), (int((cd[0] - 7)*cd[2]*cd[3]), (cd[1] + 15)*cd[2]),
                                    (int((cd[0] - 7)*cd[2]*cd[3]), cd[1]*cd[2])))
    ellipse(screen, (0, 0, 200), ((cd[0] + 30)*cd[2]*cd[3], (cd[1] + 5)*cd[2], 5*cd[2]*cd[3], 5*cd[2]))
    polygon(screen, (255, 150, 0), (((cd[0] + 24)*cd[2]*cd[3], (cd[1] + 10)*cd[2]),
                                    ((cd[0] + 20)*cd[2]*cd[3], (cd[1] + 6)*cd[2]),
                                    ((cd[0] + 20)*cd[2]*cd[3], (cd[1] + 14)*cd[2])))

def fibshes(cd):
    fibsh(((cd[0] + 320) * cd[2] * cd[3], (cd[1] + 300) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 400) * cd[2] * cd[3], (cd[1] + 305) * cd[2], cd[2] * cd[3] * (-1)))
    fibsh(((cd[0] + 360) * cd[2] * cd[3], (cd[1] + 290) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 380) * cd[2] * cd[3], (cd[1] + 295) * cd[2], cd[2] * cd[3] * (-1)))
    fibsh(((cd[0] + 240) * cd[2] * cd[3], (cd[1] + 200) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 280) * cd[2] * cd[3], (cd[1] + 180) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 330) * cd[2] * cd[3], (cd[1] + 190) * cd[2], cd[2] * cd[3]))

def bebr(cd):
    cd = (cd[0] / cd[2], cd[1] / abs(cd[2]), abs(cd[2]), cd[2]/abs(cd[2]))
    fibshes(cd)
    line(screen, (0, 0, 0), ((cd[0] + 160)*cd[2]*cd[3], (cd[1] + 200)*cd[2]),
         ((cd[0] + 310)*cd[2]*cd[3], (cd[1] - 100)*cd[2]), max(int(5*cd[2]), 1))
    ellipse(screen, (70, 70, 100), ((cd[0] + 260)*cd[2]*cd[3], (cd[1] + 210)*cd[2], 120*cd[2]*cd[3], 50*cd[2]))
    ellipse(screen, (50, 50, 200), ((cd[0] + 270)*cd[2]*cd[3], (cd[1] + 220)*cd[2], 100*cd[2]*cd[3], 40*cd[2]))
    line(screen, (0, 0, 0), ((cd[0] + 310)*cd[2]*cd[3], (cd[1] - 100)*cd[2]),
         ((cd[0] + 310)*cd[2]*cd[3], (cd[1] + 240)*cd[2]), 1)
    whiteball((cd[0]*cd[2]*cd[3], cd[1]*cd[2], 150*cd[2]*cd[3], 300*cd[2]))
    whiteball(((cd[0] + 70)*cd[2]*cd[3], (cd[1] + 240)*cd[2], 120*cd[2]*cd[3], 80*cd[2]))
    whiteball(((cd[0] + 150)*cd[2]*cd[3], (cd[1] + 290)*cd[2], 60*cd[2]*cd[3], 40*cd[2]))
    whiteball(((cd[0] + 120)*cd[2]*cd[3], (cd[1] + 80)*cd[2], 100*cd[2]*cd[3], 60*cd[2]))
    whiteball(((cd[0] + 100)*cd[2]*cd[3], (cd[1] - 30)*cd[2], 100*cd[2]*cd[3], 70*cd[2]))
    whiteball(((cd[0] + 95)*cd[2]*cd[3], (cd[1] - 24)*cd[2], 20*cd[2]*cd[3], 20*cd[2]))
    line(screen, (0, 0, 0), ((cd[0] + 180)*cd[2]*cd[3], (cd[1] + 5)*cd[2]),
         ((cd[0] + 200)*cd[2]*cd[3], (cd[1] + 10)*cd[2]))
    ellipse(screen, (0, 0, 0), ((cd[0] + 190)*cd[2]*cd[3], (cd[1] - 10)*cd[2], 10*cd[2]*cd[3], 10*cd[2]))
    ellipse(screen, (0, 0, 0), ((cd[0] + 120)*cd[2]*cd[3], (cd[1] - 20)*cd[2], 5*cd[2]*cd[3], 5*cd[2]))

def sun(cd):
    ellipse(screen, (255, 255, 0), (cd[0], cd[1], 60, 60))
    ellipse(screen, (100, 100, 255), (cd[0] + 5, cd[1] + 5, 50, 50))
    ellipse(screen, (255, 255, 0), (cd[0] + 20, cd[1] + 20, 20, 20))

def FPS(FPS, finished = False, clock = pygame.time.Clock()):
    pygame.display.update()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()

def bebras():
    bebr((400, 500, -0.5))
    bebr((500, 400, -0.25))
    bebr((20, 600, 0.75))
    bebr((650, 800, -1))

def __Main__():
    screenfill((650, 850))
    bebras()
    sun((300, 80))
    FPS(10)

__Main__()


