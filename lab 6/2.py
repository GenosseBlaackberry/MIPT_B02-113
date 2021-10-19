#  python3 2.py

import pygame
from pygame.draw import *
from random import randint
from math import log2
pygame.init()

# Некоторые базовые константы
FPS = 30
SCREEN_LENGTH = 1366
SCREEN_WIDTH = 768
BALL_NUMBER = 5
FACE_NUMBER = 1
MAX_SPEED = 0
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

# Константы цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Переменные, ответственные за подсчёт очков
prev_score = 0
score = 0

# Масстивы, в которые будут помещаться экземпляры классов
BALLS = []
FACES = []


class Ball:
    def __init__(self):
        self.x = randint(100, SCREEN_LENGTH - 100)
        self.vx = randint(-MAX_SPEED, MAX_SPEED)
        self.y = randint(100, SCREEN_WIDTH - 100)
        self.vy = randint(-MAX_SPEED, MAX_SPEED)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    def erase(self):
        """
        Закрашивает наш круг чёрным
        """
        circle(screen, BLACK, (self.x, self.y), self.r)

    def move(self):
        """
        Метод перемещения лица
        """
        circle(screen, BLACK, (self.x, self.y), self.r)
        if (self.x - self.r) <= 0 or (self.x + self.r) >= SCREEN_LENGTH:
            self.vx = -self.vx
        if (self.y - self.r) <= 0 or (self.y + self.r) >= SCREEN_WIDTH:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        circle(screen, self.color, (self.x, self.y), self.r)


class Face:
    def __init__(self):
        self.x = randint(100, SCREEN_LENGTH - 100)
        self.vx = randint(-10, 11)
        self.y = randint(100, SCREEN_WIDTH - 100)
        self.vy = randint(-10, 11)
        self.draw_face()

    def draw_face(self):
        """
        Метод рисования лица
        """
        circle(screen, (200, 200, 0), (self.x, self.y), 100)
        rect(screen, (0, 0, 0), (self.x - 25, self.y + 55, 50, 10))
        circle(screen, (255, 0, 0), (self.x - 40, self.y - 35), 20)
        circle(screen, (0, 0, 0), (self.x - 40, self.y - 35), 8)
        circle(screen, (255, 0, 0), (self.x + 40, self.y - 35), 15)
        circle(screen, (0, 0, 0), (self.x + 40, self.y - 35), 6)
        polygon(screen, (0, 0, 0), ((self.x - 60, self.y - 70), (self.x - 20, self.y - 50), (self.x - 20, self.y - 60),
                                    (self.x - 60, self.y - 80)))
        polygon(screen, (0, 0, 0), ((self.x + 20, self.y - 50), (self.x + 60, self.y - 70), (self.x + 60, self.y - 80),
                                    (self.x + 20, self.y - 60)))

    def erase(self):
        """
        Метод, закрашивающий лицо тёмным кругом
        """
        circle(screen, BLACK, (self.x, self.y), 110)

    def move(self):
        """
        Метод, осуществляющий перемещение лица
        """
        self.vx = self.vx + randint(-randint(1, 7), randint(1, 7))
        self.vy = self.vy + randint(-randint(1, 7), randint(1, 7))
        if (self.x - 100) <= 10 or (self.x + 100) >= SCREEN_LENGTH - 10:
            self.vx = -self.vx
        if (self.y - 100) <= 10 or (self.y + 100) >= SCREEN_WIDTH - 10:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        self.draw_face()


def click(event):
    """
    Процедура-обработчик события щелчка мыши
    :param event: Параметр, принимающий на вход событие
    """
    global score
    global prev_score

    # Проверка попадания по шарам
    for i in range(len(BALLS)):
        if (event.pos[0] - BALLS[i].x)**2 + (event.pos[1] - BALLS[i].y)**2 <= BALLS[i].r**2:
            BALLS[i].erase()
            BALLS[i] = Ball()
            prev_score = score
            score += 1

    # Проверка попадания по лицам
    for i in range(len(FACES)):
        if (event.pos[0] - FACES[i].x)**2 + (event.pos[1] - FACES[i].y)**2 <= 100**2:
            FACES[i].erase()
            FACES[i] = Face()
            prev_score = score
            score += 2


def score_points(score: int):
    """
    Выводит на экран количество набранных очков
    :param score:
    """
    f = pygame.font.Font(None, 36)
    text = f.render('Score: ' + str(prev_score), 1, (0, 0, 0))
    screen.blit(text, (24, 18))
    text = f.render('Score: ' + str(score), 1, (180, 0, 0))
    screen.blit(text, (24, 18))


def leaderboards(score: int):
    """
    Процедура, которая заносит результаты в таблицу лидеров
    :param score: Число очков
    """
    name = input('Введите своё имя ')
    with open('leaderboards.txt', 'a') as board:
        board.write(name+': '+str(score)+'\n')


def target_generator(type, TARGETS, TARGET_NUMBER):
    """
    Процедура генерации мишений
    :param type: Тип мишени (Ball/Face)
    :param TARGETS: Массив в который эти мишени добавлять
    :param TARGET_NUMBER: Необходимое количество мишеней в массиве
    """
    while len(TARGETS) < TARGET_NUMBER:
        TARGETS.append(eval(type+'()'))

def frame():
    """
    Процедура, отрисовывающая новый кадр
    """
    for ball in BALLS:
        ball.erase()
    for face in FACES:
        face.erase()
    for ball in BALLS:
        ball.move()
    for face in FACES:
        face.move()


def development(MAX_SPEED):
    """
    Меняет скорость в зависимости от числа заработанных очков
    :param MAX_SPEED: Полученная максимальная скорость
    :return: Высчитанная максимальная скорость
    """
    if score == 0:
        MAX_SPEED = 3
    else:
        MAX_SPEED = 3 + int(log2(score))
    return MAX_SPEED


# Генерация начальных условий игры
pygame.display.update()
clock = pygame.time.Clock()
finished = False
target_generator('Ball', BALLS, BALL_NUMBER)
target_generator('Face', FACES, FACE_NUMBER)

# Основной цикл, обрабатывающий события
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    frame()
    MAX_SPEED = development(MAX_SPEED)
    score_points(score)
    pygame.display.update()

# Завершение игры и запись резултатов
pygame.quit()
leaderboards(score)