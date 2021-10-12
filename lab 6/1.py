#  python3 1.py

import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
SCREEN_LENGTH = 1920
SCREEN_WIDTH = 1080
BALL_NUMBER = 5
FACE_NUMBER = 1
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ball_x = [0 for i in range(BALL_NUMBER)]
ball_y = [0 for i in range(BALL_NUMBER)]
ball_r = [0 for i in range(BALL_NUMBER)]
ball_vx = [0 for i in range(BALL_NUMBER)]
ball_vy = [0 for i in range(BALL_NUMBER)]
ball_color = [0 for i in range(BALL_NUMBER)]

face_x = [0 for i in range(FACE_NUMBER)]
face_y = [0 for i in range(FACE_NUMBER)]
face_vx = [0 for i in range(FACE_NUMBER)]
face_vy = [0 for i in range(FACE_NUMBER)]

prev_score = 0
score = 0


def new_ball(i):
    '''рисует новый шарик '''
    ball_x[i] = randint(100, SCREEN_LENGTH - 100)
    ball_vx[i] = randint(-10, 11)
    ball_y[i] = randint(100, SCREEN_WIDTH - 100)
    ball_vy[i] = randint(-10, 11)
    ball_r[i] = randint(10, 100)
    ball_color[i] = COLORS[randint(0, 5)]
    circle(screen, ball_color[i], (ball_x[i], ball_y[i]), ball_r[i])


def draw_face(x, y):
    circle(screen, (200, 200, 0), (x, y), 100)
    rect(screen, (0, 0, 0), (x - 25, y + 55, 50, 10))
    circle(screen, (255, 0, 0), (x - 40, y - 35), 20)
    circle(screen, (0, 0, 0), (x - 40, y - 35), 8)
    circle(screen, (255, 0, 0), (x + 40, y - 35), 15)
    circle(screen, (0, 0, 0), (x + 40, y - 35), 6)
    polygon(screen, (0, 0, 0), ((x - 60, y - 70), (x - 20, y - 50), (x - 20, y - 60), (x - 60, y - 80)))
    polygon(screen, (0, 0, 0), ((x + 20, y - 50), (x + 60, y - 70), (x + 60, y - 80), (x + 20, y - 60)))


def new_face(i):
    face_x[i] = randint(100, SCREEN_LENGTH - 100)
    face_vx[i] = randint(-10, 11)
    face_y[i] = randint(100, SCREEN_WIDTH - 100)
    face_vy[i] = randint(-10, 11)
    draw_face(face_x[i], face_y[i])


def click(event):
    global score
    global prev_score
    for i in range(BALL_NUMBER):
        if (event.pos[0] - ball_x[i])**2 + (event.pos[1] - ball_y[i])**2 <= ball_r[i]**2:
            circle(screen, BLACK, (ball_x[i], ball_y[i]), ball_r[i])
            new_ball(i)
            prev_score = score
            score+=1
    for i in range(FACE_NUMBER):
        if (event.pos[0] - face_x[i])**2 + (event.pos[1] - face_y[i])**2 <= 100**2:
            circle(screen, BLACK, (face_x[i], face_y[i]), 110)
            new_face(i)
            prev_score = score
            score+=2


def move_ball(i):
    circle(screen, BLACK, (ball_x[i], ball_y[i]), ball_r[i])
    if (ball_x[i] - ball_r[i])<=0 or (ball_x[i] + ball_r[i])>=SCREEN_LENGTH:
        ball_vx[i]=-ball_vx[i]
    if (ball_y[i] - ball_r[i])<=0 or (ball_y[i] + ball_r[i])>=SCREEN_WIDTH:
        ball_vy[i]=-ball_vy[i]
    ball_x[i]+=ball_vx[i]
    ball_y[i]+=ball_vy[i]
    circle(screen, ball_color[i], (ball_x[i], ball_y[i]), ball_r[i])


def move_face(i):
    circle(screen, BLACK, (face_x[i], face_y[i]), 110)
    face_vx[i]=face_vx[i]+randint(-randint(1, 7), randint(1, 7))
    face_vy[i]=face_vy[i]+randint(-randint(1, 7), randint(1, 7))
    if (face_x[i] - 100)<=0 or (face_x[i] + 100)>=SCREEN_LENGTH:
        face_vx[i]=-face_vx[i]
    if (face_y[i] - 100)<=0 or (face_y[i] + 100)>=SCREEN_WIDTH:
        face_vy[i]=-face_vy[i]
    face_x[i]+=face_vx[i]
    face_y[i]+=face_vy[i]
    draw_face(face_x[i], face_y[i])


def score_points(score):
    f = pygame.font.Font(None, 36)
    text = f.render('Score: ' +str(prev_score), 1, (0, 0, 0))
    screen.blit(text, (24, 18))
    text = f.render('Score: ' +str(score), 1, (180, 0, 0))
    screen.blit(text, (24, 18))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
for i in range(BALL_NUMBER):
    new_ball(i)
for i in range(FACE_NUMBER):
    new_face(i)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    for i in range(BALL_NUMBER):
        move_ball(i)
    for i in range(FACE_NUMBER):
        move_face(i)
    score_points(score)
    pygame.display.update()

pygame.quit()
