import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (200, 200, 200), (0, 0, 400, 400))
circle(screen, (200, 200, 0), (200, 175), 100)
rect(screen, (0, 0, 0), (175, 230, 50, 10))
circle(screen, (255, 0, 0), (160, 140), 20)
circle(screen, (0, 0, 0), (160, 140), 8)
circle(screen, (255, 0, 0), (240, 140), 15)
circle(screen, (0, 0, 0), (240, 140), 6)
polygon(screen, (0, 0, 0), ((140, 105), (180, 125), (180, 115), (140, 95)))
polygon(screen, (0, 0, 0), ((220, 125), (260, 105), (260, 95), (220, 115)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()