import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((650, 1000))

rect(screen, (100, 100, 255), (0, 0, 650, 500))
rect(screen, (255, 255, 255), (0, 500, 650, 500))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()