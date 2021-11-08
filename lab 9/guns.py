# python3 gun.py

import math
from random import choice
from random import randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRAVITY_TENSION = 1


class Object:
    def __init__(self, screen: pygame.Surface, x: int, y: int, vx: int, vy: int):
        """ Конструктор класса Object

        Args:
            screen - экран, на котором отрисовывается объект
            x - начальное положение объекта по горизонтали
            y - начальное положение объекта по вертикали
            vx - стартовая скорость по горизонтальной оси
            vy - стартовая скорость по вертикальной оси
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.collisions = 0

    def move(self, gravity=0):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).

        Args:
            gravity - условный параметр, опредедляющий ускорение свободного падения
        """
        if (self.x - self.r) <= 0 or (self.x + self.r) >= SCREEN_WIDTH:
            self.vx = -self.vx
            self.x += self.vx
            self.collisions += 1
        if (self.y - self.r) <= 0 or (self.y + self.r) >= SCREEN_HEIGHT:
            self.vy = -self.vy
            self.y -= self.vy
            self.collisions += 1
        self.vy -= gravity
        self.x += self.vx
        self.y -= self.vy
        self.x += self.vx


class Bullet(Object):
    def __init__(self, screen: pygame.Surface, x: int, y: int, r: int, vx: int, vy: int, owner: object, samostrel):
        """ Конструктор класса Bullet

        Args:
            screen - экран, на котором отрисовывается объект
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
            vx - стартовая скорость по горизонтальной оси
            vy - стартовая скорость по вертикальной оси
        """
        super().__init__(screen, x, y, vx, vy)
        self.r = r
        self.owner = owner
        self.samostrel = samostrel

    def move_bullet(self):
        super().move(GRAVITY_TENSION)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2 and (self.owner != obj
                or self.samostrel):
            obj.hit(self.owner)
            self.hit()
        if self.collisions >= 1:
            if self.samostrel == 0:
                self.samostrel = 1
            elif self.collisions >= self.live:
                self.hit()

    def draw(self):
        """Процедура отрисовки мобъекта на экране"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Target(Object):
    def __init__(self, screen: pygame.Surface, x: int, y: int, vx: int, vy: int, live: int):
        """ Конструктор класса Target

        Args:
            screen - экран, на котором отрисовывается объект
            x - начальное положение объекта по горизонтали
            y - начальное положение объекта по вертикали
            vx - стартовая скорость по горизонтальной оси
            vy - стартовая скорость по вертикальной оси
            live - количество жизней мишени
        """
        super().__init__(screen, x, y, vx, vy)
        self.live = live
        self.screen = screen

    def hit(self, obj):
        """Метод запускается при попадании пули в цель"""
        global points
        if obj == guns[0]:
            points[0] += 1
        elif obj== guns[1]:
            points[1] += 1
        self.live -= 1
        if self.live == 0:
            self.new_target()


class Ball(Target):
    def __init__(self, screen: pygame.Surface, x: int, y: int, r: int, vx: int, vy: int, live: int):
        """ Конструктор класса Ball (обычный противник)

        Args:
            screen - экран, на котором отрисовывается объект
            x - начальное положение объекта по горизонтали
            y - начальное положение объекта по вертикали
            r - радиус шара
            vx - стартовая скорость по горизонтальной оси
            vy - стартовая скорость по вертикальной оси
            live - количество жизней мишени
        """
        super().__init__(screen, x, y, vx, vy, live)
        self.r = r
        self.color = RED

    def new_target(self):
        """Метод, порождающий новую цель вместо уничтоженной"""
        new_target = Ball(screen,
                          randint(600, SCREEN_WIDTH - 100),
                          randint(300, SCREEN_HEIGHT - 100),
                          randint(20, 60),
                          randint(-1, 1),
                          randint(-1, 1),
                          1)
        targets.append(new_target)
        targets.remove(self)

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Bomber(Target):
    def __init__(self, screen: pygame.Surface, x: int, y: int, vx: int, vy: int, live: int):
        """ Конструктор класса Bomber (стреляющий противник)

        Args:
            screen - экран, на котором отрисовывается объект
            x - начальное положение объекта по горизонтали
            y - начальное положение объекта по вертикали
            vx - стартовая скорость по горизонтальной оси
            vy - стартовая скорость по вертикальной оси
            live - количество жизней мишени
        """
        super().__init__(screen, x, y, vx, vy, live)
        self.r = 20
        self.color = BLACK

    def move(self):
        """
        Метод, отвечающийй за перемещение и стрельбу бомбера
        """
        super().move()
        chance = randint(1, 10)
        if chance == 10:
            angle = randint(-6, 6) * math.pi / 6
            new_bullet = Idle(self.screen,
                              self.x,
                              self.y,
                              10,
                              self.vx - 25 * math.sin(angle),
                              self.vy + 25 * math.cos(angle),
                              self,
                              0)
            bullets.append(new_bullet)

    def new_target(self):
        """Метод, порождающий новую цель вместо уничтоженной"""
        new_target = Bomber(screen,
                          randint(600, SCREEN_WIDTH - 100),
                          randint(300, SCREEN_HEIGHT - 100),
                          randint(-1, 1),
                          randint(-1, 1),
                          1)
        targets.append(new_target)
        targets.remove(self)

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Simple(Bullet):
    """
    Пуля с рикошетом (отражается от стенок до 9 раз), при попадании в противника исчезает
    """
    def __init__(self, screen: pygame.Surface, x: int, y: int, r: int, vx: int, vy: int, owner, samostrel):
        """
            Args:
                screen - экран, на котором отрисовывается объект
                x - начальное положение объекта по горизонтали
                y - начальное положение объекта по вертикали
                r - радиус объекта
                vx - стартовая скорость по горизонтальной оси
                vy - стартовая скорость по вертикальной оси
                owner - объект, испустивший снаряд
                samostrel - флаг, проверяющий, может ли снаряд навредить owner'у
        """
        super().__init__(screen, x, y, r, vx, vy, owner, samostrel)
        self.color = CYAN
        self.live = 10

    def hit(self):
        if bullets.count(self) != 0:
            bullets.remove(self)


class Idle(Bullet):
    """
    Простой осколок. Не рикошетит, при попадании в противника исчезает
    """
    def __init__(self, screen: pygame.Surface, x: int, y: int, r: int, vx: int, vy: int, owner, samostrel):
        """
            Args:
                screen - экран, на котором отрисовывается объект
                x - начальное положение объекта по горизонтали
                y - начальное положение объекта по вертикали
                r - радиус объекта
                vx - стартовая скорость по горизонтальной оси
                vy - стартовая скорость по вертикальной оси
                owner - объект, испустивший снаряд
                samostrel - флаг, проверяющий, может ли снаряд навредить owner'у
        """
        super().__init__(screen, x, y, r, vx, vy, owner, samostrel)
        self.color = YELLOW
        self.live = 1

    def hit(self):
        """Событие на уничтожение"""
        if bullets.count(self) != 0:
            bullets.remove(self)


class Bomb(Bullet):
    """
    Осколочная граната, при попадании в цель или в стену разрывается, порождая осколки
    """
    def __init__(self, screen: pygame.Surface, x: int, y: int, r: int, vx: int, vy: int, owner, samostrel):
        """
            Args:
                screen - экран, на котором отрисовывается объект
                x - начальное положение объекта по горизонтали
                y - начальное положение объекта по вертикали
                r - радиус объекта
                vx - стартовая скорость по горизонтальной оси
                vy - стартовая скорость по вертикальной оси
                owner - объект, испустивший снаряд
                samostrel - флаг, проверяющий, может ли снаряд навредить owner'у
        """
        super().__init__(screen, x, y, r, vx, vy, owner, samostrel)
        self.color = GREEN
        self.live = 1

    def hit(self):
        """Событие на разрыв"""
        for i in range(15):
            angle = randint(-6, 6) * math.pi / 6
            new_bullet = Idle(self.screen,
                              self.x,
                              self.y,
                              10,
                              self.vx - 3 * math.sin(angle),
                              self.vy + 3 * math.cos(angle),
                              self.owner,
                              1)
            bullets.append(new_bullet)
        if bullets.count(self) != 0:
            bullets.remove(self)


class Gun:
    """Собственно, сам игрок

    Управление для 1/2 игрока:

    w(ц) / p(з) - поднять башню наверх
    s(ы) / ;(ж) - опустить башню вниз
    a(ф) / l(д) - двигаться влево
    d(в) / '(э) - двигаться вправо
    l. Shift / r. Shift - смена типа снаряда (по умолчанию рикошетящий, есть разрывной)
    Space / Enter - усиление выстрела (удержание), выстрел (отпускание)
    """
    def __init__(self, screen: pygame.Surface, colors = [GREY, RED], an = -1, x = 20, y = SCREEN_HEIGHT - 20):
        """
            Args:
                screen - экран, на котором отрисовывается объект
                colors - массив из базового цвета танка и его цвета при усилении
                an - начальный угол поворота пушки танка (от вертикали, положительное направление - против часовой)
                x - начальное положение объекта по горизонтали
                y - начальное положение объекта по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.f2_power = 10
        self.f2_on = 0
        self.an = an
        self.length = 20
        self.colors = colors
        self.color = self.colors[0]
        self.r = 20
        self.ammotype = 0
        self.live = 5

    def change_ammo(self, event):
        """Метод, осуществляющий смену типа патронов"""
        if self.ammotype == 0:
            self.ammotype = 1
        elif self.ammotype == 1:
            self.ammotype = 0

    def fire2_start(self, event):
        """Начало выстрела при нажатии на Space / Enter"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом при отпускании Space / Enter.
        """
        global bullets, bullet
        bullet += 1
        if self.ammotype == 0:
            new_bullet = Simple(self.screen,
                                self.x - self.length * math.sin(self.an),
                                self.y - self.length * math.cos(self.an),
                                10,
                                - self.f2_power * math.sin(self.an) // 3,
                                self.f2_power * math.cos(self.an) // 3,
                                self,
                                0)
        elif self.ammotype == 1:
            new_bullet = Bomb(self.screen,
                              self.x - self.length * math.sin(self.an),
                              self.y - self.length * math.cos(self.an),
                              10,
                              - self.f2_power * math.sin(self.an) // 3,
                              self.f2_power * math.cos(self.an) // 3,
                              self,
                              0)
        bullets.append(new_bullet)
        self.f2_on = 0
        self.f2_power = 10

    def targetting_up(self, event):
        """Поднятие башни"""
        if event:
            if self.an > 0:
                self.an -= 0.02
            if self.an < 0:
                self.an += 0.02

    def targetting_down(self, event):
        """Опускание башни"""
        if event:
            if self.an > 0 and self.an < math.pi / 2:
                self.an += 0.02
            if self.an < 0 and self.an > -math.pi / 2:
                self.an -= 0.02

    def move_right(self, event):
        """Движение вправо"""
        if event and self.x < SCREEN_WIDTH:
            self.x += 1
            if self.an > 0:
                self.an = - self.an

    def move_left(self, event):
        """Движение влево"""
        if event and self.x > 0:
            self.x -= 1
            if self.an < 0:
                self.an = - self.an

    def draw(self):
        """Метод, рисующий пушку"""
        pygame.draw.polygon(
            self.screen,
            self.color,
            ((self.x - 5 * math.cos(self.an),
              self.y + 5 * math.sin(self.an)),
            (self.x - self.length * math.sin(self.an) - 5 * math.cos(self.an),
             self.y - self.length * math.cos(self.an) + 5 * math.sin(self.an)),
            (self.x - self.length * math.sin(self.an) + 5 * math.cos(self.an),
             self.y - self.length * math.cos(self.an) - 5 * math.sin(self.an)),
             (self.x + 5 * math.cos(self.an),
              self.y - 5 * math.sin(self.an))
             )
        )
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)
        pygame.draw.polygon(
            self.screen,
            self.color,
            ((self.x - 10, self.y),
             (self.x + 10, self.y),
             (self.x + 20, self.y + 5),
             (self.x + 20, self.y + 15),
             (self.x - 20, self.y + 15),
             (self.x - 20, self.y + 5))
        )

    def power_up(self):
        """Процесс усиления выстрела при удерживании кнопки"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.length += 1
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]
            self.length = 20

    def hit(self, obj):
        """Событие на получение урона"""
        self.live -= 1



def score_points(points: list):
    """
    Выводит на экран количество набранных очков

    Args:
        points - массив количества очков у игроков
    """
    f = pygame.font.Font(None, 36)
    text = f.render('Score: ' + str(points[0]*(hp[0] + 1) / 6), 1, (180, 0, 0))
    screen.blit(text, (24, 18))
    text = f.render('Score: ' + str(points[1]*(hp[1] + 1) / 6), 1, (0, 0, 180))
    screen.blit(text, (424, 18))


def health_points(hp):
    f = pygame.font.Font(None, 36)
    text = f.render('Health: ' + str(hp[0]), 1, (180, 0, 0))
    screen.blit(text, (24, 60))
    text = f.render('Health: ' + str(hp[1]), 1, (0, 0, 180))
    screen.blit(text, (424, 60))


def leaderboards(score: list):
    """
    Процедура, которая заносит результаты в таблицу лидеров

    Args:
         score - массив количества очков у игроков
    """
    name1 = input('Введите имя первого игрока ')
    name2 = input('Введите имя второго игрока ')
    with open('leaderboards.txt', 'a') as board:
        board.write(name1+'/'+name2+': '+str(score[0])+'/'+str(score[1])+'\n')


def pause(defeat):
    """Процедура вызовы паузы

    Esc / крестик - приостановка игры на паузу
    Esc (в паузе) - возобновление игры
    крестик (в паузе) - закрытие окна игры
    """
    global finished
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                finished = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and defeat == False:
                flag = False


# Инициализация мира
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bullet = 0
points = [0, 0]
bullets = []
targets = []
guns = []

# Создание пушки и целей
clock = pygame.time.Clock()
guns.append(Gun(screen))
guns.append(Gun(screen, [GREEN, BLUE], 1, SCREEN_WIDTH - 20))
targets.append(Ball(screen,
                              randint(100, SCREEN_WIDTH - 100),
                              randint(300, SCREEN_HEIGHT - 100),
                              randint(20, 60),
                              randint(-1, 1),
                              randint(-1, 1),
                    1))


targets.append(Bomber(screen,
                              randint(100, SCREEN_WIDTH - 100),
                              randint(300, SCREEN_HEIGHT - 100),
                              randint(-1, 1),
                              randint(-1, 1),
                    1))

# Основной цикл программы
finished = False

while not finished:
    screen.fill(WHITE)
    for g in guns:
        g.draw()
    for t in targets:
        t.draw()
    for b in bullets:
        b.draw()

    hp = [guns[0].live, guns[1].live]
    score_points(points)
    health_points(hp)
    pygame.display.update()
    for g in guns:
        if g.live <= 0:
            pause(1)

    clock.tick(FPS)
    # Цикл, отвечающий за обработку управления
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pause(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                guns[0].fire2_start(event)
            elif event.key == pygame.K_RETURN:
                guns[1].fire2_start(event)
            elif event.key == pygame.K_RETURN:
                print('vh')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                guns[0].fire2_end(event)
            elif event.key == pygame.K_RETURN:
                guns[1].fire2_end(event)
        if pygame.key.get_pressed()[pygame.K_w]:
            guns[0].targetting_up(event)
        if pygame.key.get_pressed()[pygame.K_s]:
            guns[0].targetting_down(event)
        if pygame.key.get_pressed()[pygame.K_d]:
            guns[0].move_right(event)
        if pygame.key.get_pressed()[pygame.K_a]:
            guns[0].move_left(event)
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            guns[0].change_ammo(event)
            print(8)

        if pygame.key.get_pressed()[pygame.K_p]:
            guns[1].targetting_up(event)
        if pygame.key.get_pressed()[59]:
            guns[1].targetting_down(event)
        if pygame.key.get_pressed()[39]:
            guns[1].move_right(event)
        if pygame.key.get_pressed()[pygame.K_l]:
            guns[1].move_left(event)
        if pygame.key.get_pressed()[pygame.K_RSHIFT]:
            guns[1].change_ammo(event)

    # Цикл, отвечающий за перемещение объектов и обработку столкновений
    for b in bullets:
        b.move_bullet()
        for t in targets:
            b.hittest(t)
        for g in guns:
            b.hittest(g)
    for t in targets:
        t.move()
    guns[0].power_up()
    guns[1].power_up()

# Закрытие игрового окошка и запись в базу лидеров
pygame.quit()
leaderboards(points)