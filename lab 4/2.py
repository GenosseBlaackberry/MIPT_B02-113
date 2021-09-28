import pygame
from pygame.draw import *

pygame.init()

def whiteball(cd):
    ellipse(screen, (0, 0, 0), (cd[0], cd[1], cd[2], cd[3]))
    ellipse(screen, (255, 255, 255), (cd[0] + 1, cd[1] + 2, cd[2] - 2, cd[3] - 4))

def fibsh(cd):
    polygon(screen, (255, 150, 0), ((cd[0] + 10, cd[1]), (cd[0] + 8, cd[1] - 6), (cd[0] + 30, cd[1] - 6), (cd[0] + 28, cd[1])))
    ellipse(screen, (50, 180, 50), (cd[0], cd[1], 40, 20))
    polygon(screen, (50, 180, 50), ((cd[0], cd[1] + 8), (cd[0] - 7, cd[1] + 15), (cd[0] - 7, cd[1])))
    ellipse(screen, (0, 0, 200), (cd[0]+30, cd[1] + 5, 5, 5))
    polygon(screen, (255, 150, 0), ((cd[0] + 24, cd[1] + 10), (cd[0] + 20, cd[1] + 6), (cd[0] + 20, cd[1] + 14)))

FPS = 30
screen = pygame.display.set_mode((650, 1000))

rect(screen, (100, 100, 255), (0, 0, 650, 500))
rect(screen, (255, 255, 255), (0, 500, 650, 500))
line(screen, (0, 0, 0), (190, 600), (340, 300), 5)
ellipse(screen, (70, 70, 100), (290, 610, 120, 50))
ellipse(screen, (50, 50, 200), (300, 620, 100, 40))
line(screen, (0, 0, 0), (340, 300), (340, 640), 1)
whiteball((30, 400, 150, 300))
whiteball((100, 640, 120, 80))
whiteball((180, 690, 60, 40))
whiteball((150, 480, 100, 60))
whiteball((130, 370, 100, 70))
whiteball((125, 376, 20, 20))
ellipse(screen, (0, 0, 0), (220, 390, 10, 10))
ellipse(screen, (0, 0, 0), (170, 380, 5, 5))
fibsh((350, 700))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
