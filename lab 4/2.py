import pygame
from pygame.draw import *

pygame.init()

def whiteball(cd):
    ellipse(screen, (0, 0, 0), (cd[0], cd[1], cd[2], cd[3]))
    ellipse(screen, (255, 255, 255), (cd[0] + 1, cd[1] + 2, cd[2] - 2, cd[3] - 4))

def fibsh(cd):
    cd = (cd[0] / cd[2], cd[1] / cd[2], cd[2])
    polygon(screen, (255, 150, 0), ((cd[0]*cd[2] + 10*cd[2], (cd[1] + 4)*cd[2]), (cd[0]*cd[2] + 8*cd[2], cd[1]*cd[2] - 2*cd[2]),
                                    (cd[0]*cd[2] + 30*cd[2], cd[1]*cd[2] - 2*cd[2]), (cd[0]*cd[2] + 28*cd[2], (cd[1]+4)*cd[2])))
    ellipse(screen, (50, 180, 50), (cd[0]*cd[2], cd[1]*cd[2], 40*cd[2], 20*cd[2]))
    polygon(screen, (50, 180, 50), ((cd[0]*cd[2], cd[1]*cd[2] + 8*cd[2]), (cd[0]*cd[2] - int(7*cd[2]), cd[1]*cd[2] + 15*cd[2]),
                                    (cd[0]*cd[2] - int(7*cd[2]), cd[1]*cd[2])))
    ellipse(screen, (0, 0, 200), (cd[0]*cd[2] + 30*cd[2], cd[1]*cd[2] + 5*cd[2], 5*cd[2], 5*cd[2]))
    polygon(screen, (255, 150, 0), ((cd[0]*cd[2] + 24*cd[2], cd[1]*cd[2] + 10*cd[2]),
                                    (cd[0]*cd[2] + 20*cd[2], cd[1]*cd[2] + 6*cd[2]),
                                    (cd[0]*cd[2] + 20*cd[2], cd[1]*cd[2] + 14*cd[2])))

def bebr(cd):
    cd = (cd[0]/cd[2], cd[1]/cd[2], cd[2])
    line(screen, (0, 0, 0), (cd[0]*cd[2] + 160*cd[2], cd[1]*cd[2] + 200*cd[2]),
         (cd[0]*cd[2] + 310*cd[2], cd[1]*cd[2] - 100*cd[2]), max(int(5*cd[2]), 1))
    ellipse(screen, (70, 70, 100), (cd[0]*cd[2] + 260*cd[2], cd[1]*cd[2] + 210*cd[2], 120*cd[2], 50*cd[2]))
    ellipse(screen, (50, 50, 200), (cd[0]*cd[2] + 270*cd[2], cd[1]*cd[2] + 220*cd[2], 100*cd[2], 40*cd[2]))
    line(screen, (0, 0, 0), (cd[0]*cd[2] + 310*cd[2], cd[1]*cd[2] - 100*cd[2]),
         (cd[0]*cd[2] + 310*cd[2], cd[1]*cd[2] + 240*cd[2]), 1)
    whiteball((cd[0]*cd[2], cd[1]*cd[2], 150*cd[2], 300*cd[2]))
    whiteball((cd[0]*cd[2] + 70*cd[2], cd[1]*cd[2] + 240*cd[2], 120*cd[2], 80*cd[2]))
    whiteball((cd[0]*cd[2] + 150*cd[2], cd[1]*cd[2] + 290*cd[2], 60*cd[2], 40*cd[2]))
    whiteball((cd[0]*cd[2] + 120*cd[2], cd[1]*cd[2] + 80*cd[2], 100*cd[2], 60*cd[2]))
    whiteball((cd[0]*cd[2] + 100*cd[2], cd[1]*cd[2] - 30*cd[2], 100*cd[2], 70*cd[2]))
    whiteball((cd[0]*cd[2] + 95*cd[2], cd[1]*cd[2] - 24*cd[2], 20*cd[2], 20*cd[2]))
    line(screen, (0, 0, 0), (cd[0]*cd[2] + 180*cd[2], cd[1]*cd[2] + 5*cd[2]),
         (cd[0]*cd[2] + 200*cd[2], cd[1]*cd[2] + 10*cd[2]))
    ellipse(screen, (0, 0, 0), (cd[0]*cd[2] + 190*cd[2], cd[1]*cd[2] - 10*cd[2], 10*cd[2], 10*cd[2]))
    ellipse(screen, (0, 0, 0), (cd[0]*cd[2] + 120*cd[2], cd[1]*cd[2] - 20*cd[2], 5*cd[2], 5*cd[2]))

    fibsh((cd[0]*cd[2] + 320*cd[2], cd[1]*cd[2] + 300*cd[2], cd[2]))


FPS = 30
screen = pygame.display.set_mode((650, 1000))

rect(screen, (100, 100, 255), (0, 0, 650, 500))
rect(screen, (255, 255, 255), (0, 500, 650, 500))


bebr((100, 400, 1))

ellipse(screen, (255, 255, 0), (305, 130, 60, 60))
ellipse(screen, (100, 100, 255), (310, 135, 50, 50))
ellipse(screen, (255, 255, 0), (325, 150, 20, 20))







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
