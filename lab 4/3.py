import pygame as pg
import sys


YELLOW = (255,255,0)
FIBSH_PLAVNIK = (255, 150, 0)
FIBSH_BODY = (50, 180, 50)
FIBSH_EYE = (0, 0, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEBRA_BODY = (230, 230, 230)
ICE = (70, 70, 100)
WATER = (50, 50, 200)
SUN = (255, 255, 0)
SKY = (100, 100, 255)

Width = 1200
Height = 800

sc = pg.display.set_mode((Width, Height))
sc.fill(SKY)
"""
Пользовательский экран
Width это ширина окна
Height это высота окна200
"""

Sky = pg.Surface((Width, Height//2))
Sky.fill(SKY)
rect = Sky.get_rect(topleft = (0,0))
sc.blit(Sky, rect)
"""
Поверхность на которой будет отображено небо
занимает верхнюю половину пользовательского экрана
Цвет Sky
"""

Ice = pg.Surface((Width, Height//2))
Ice.fill(WHITE)
rect = Ice.get_rect(bottomleft = (0, Height))
sc.blit(Ice, rect)
"""
Поверхность на которой будет отображена земля
занимает нижнюю половину пользовательского экрана
Цвет WHITE
"""

Picture = pg.Surface((Width//2, 3*Height//5))
Picture.fill(WHITE)
Picture.set_colorkey(WHITE)
"""
Поверхность на которой будет отображена картинка бэбры
занимает треть пользовательского экрана
для дальнейшей возможности сжатия
Цвет WHITE
Координатами является положение центра картинки
Прозрачна относительно неба
"""

Sun = pg.Surface((Width//4, Height//4))
Sun.fill(SKY)
Sun.set_colorkey(SKY)
rect = Sun.get_rect(center = (Width//2, Height//4))
Sun.set_alpha(10)
sc.blit(Sun, rect)
def whiteball(cd):
    """
    Рисует основной овал из которого состоит бэбра.
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата по x крайней левой точки
    param: cd[1] это координата по y крайней верхней точки
    param: cd[2] это высота эллипса
    param: cd[3] это ширина эллипса
    Отображается на поверхности Picture
    """
    ori = cd[2]/abs(cd[2])
    #КОНТУР БЕЛОГО ЭЛЛИПСА
    pg.draw.ellipse(Picture, BLACK, (cd[0], cd[1], cd[2], cd[3]))
    #БЕЛЫЙ ЭЛЛИПС
    pg.draw.ellipse(Picture, BEBRA_BODY, (cd[0] + 1*ori, cd[1] + 2, cd[2] - 2*ori, cd[3] - 4))

def fibsh(cd):
    """
    Рисует рыбу.
    Цвет тела - FIBSH_BODY,
    Цвет плавников - FIBSH_PLAVNIK,
    Цвет глаза - FIBSH_EYE,
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата по x крайней левой точки
    param: cd[1] это координата по y крайней верхней точки
    param: cd[2] это модуль коэффициента увеличения
    param: cd[3] это знак коэффициента увеличения, равен +-1.
    Возможно отображение относительно вертикальной оси
    Отображается на поверхности Picture
    """   
    cd = (cd[0] / cd[2], cd[1] / abs(cd[2]), abs(cd[2]), cd[2]/abs(cd[2]))
    #КОНТУР ВЕРХНЕГО ПЛАВНИКА
    pg.draw.polygon(Picture, BLACK,
            ((((cd[0] + 10) * cd[2] - 1) * cd[3], (cd[1] + 4) * cd[2] + 1), (((cd[0] + 8) * cd[2] - 1) * cd[3], (cd[1] - 3) * cd[2] - 1),
            (((cd[0] + 30) * cd[2] + 1) * cd[3], (cd[1] - 3) * cd[2] - 1), (((cd[0] + 28) * cd[2] + 1) * cd[3], (cd[1] + 4) * cd[2] + 1)))
    #ВЕРХНИЙ ПЛАВНИК
    pg.draw.polygon(Picture, FIBSH_PLAVNIK, (((cd[0] + 10)*cd[2]*cd[3], (cd[1] + 4)*cd[2]), ((cd[0] + 8)*cd[2]*cd[3], (cd[1] - 3)*cd[2]),
                                    ((cd[0] + 30)*cd[2]*cd[3], (cd[1] - 3)*cd[2]), ((cd[0] + 28)*cd[2]*cd[3], (cd[1]+4)*cd[2])))
    #КОНТУР ТЕЛА
    pg.draw.ellipse(Picture, BLACK, ((cd[0] * cd[2] -1) * cd[3] , cd[1] * cd[2] - 1, (40 * cd[2] + 2) * cd[3], 20 * cd[2] + 2))
    #ТЕЛО
    pg.draw.ellipse(Picture, FIBSH_BODY, (cd[0] * cd[2] * cd[3], cd[1] * cd[2], 40 * cd[2] * cd[3], 20 * cd[2]))
    #КОНТУР ЗАДНЕГО ПЛАВНИКА
    pg.draw.polygon(Picture, BLACK,
            (((cd[0] * cd[2] + 1)* cd[3], (cd[1] + 8) * cd[2]), (((int(cd[0] - 7) * cd[2] - 1)* cd[3]), (cd[1] + 15) * cd[2] + 1),
             ((int((cd[0] - 7) * cd[2] - 1)* cd[3]), cd[1] * cd[2] - 1)))
    #ЗАДНИЙ ПЛАВНИК
    pg.draw.polygon(Picture, FIBSH_BODY, ((cd[0]*cd[2]*cd[3], (cd[1] + 8)*cd[2]), (int((cd[0] - 7)*cd[2]*cd[3]), (cd[1] + 15)*cd[2]),
                                    (int((cd[0] - 7)*cd[2]*cd[3]), cd[1]*cd[2])))
    #ГЛАЗ
    pg.draw.ellipse(Picture, (FIBSH_EYE), ((cd[0] + 30)*cd[2]*cd[3], (cd[1] + 5)*cd[2], 5*cd[2]*cd[3], 5*cd[2]))
    #БОКОВОЙ ПЛАВНИК
    pg.draw.polygon(Picture, (FIBSH_PLAVNIK ), (((cd[0] + 24)*cd[2]*cd[3], (cd[1] + 10)*cd[2]),
                                    ((cd[0] + 20)*cd[2]*cd[3], (cd[1] + 6)*cd[2]),
                                    ((cd[0] + 20)*cd[2]*cd[3], (cd[1] + 14)*cd[2])))

def fibshes(cd):  
    """
    Рисует Улов рыб.
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата по x крайней левой точки
    param: cd[1] это координата по y крайней верхней точки
    param: cd[2] это модуль коэффициента увеличения
    param: cd[3] это знак коэффициента увеличения, равен +-1.
    cd[2] * cd[3] = abs(cd[2])
    """
    fibsh(((cd[0] + 320) * cd[2] * cd[3], (cd[1] + 300) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 400) * cd[2] * cd[3], (cd[1] + 305) * cd[2], cd[2] * cd[3] * (-1)))
    fibsh(((cd[0] + 360) * cd[2] * cd[3], (cd[1] + 290) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 380) * cd[2] * cd[3], (cd[1] + 295) * cd[2], cd[2] * cd[3] * (-1)))
    fibsh(((cd[0] + 240) * cd[2] * cd[3], (cd[1] + 200) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 280) * cd[2] * cd[3], (cd[1] + 180) * cd[2], cd[2] * cd[3]))
    fibsh(((cd[0] + 330) * cd[2] * cd[3], (cd[1] + 190) * cd[2], cd[2] * cd[3]))

def bebr(cd):
    """
    Рисует бэбру с удочкой и лункой.
    Цвет удочки, лески, глаза, носа, улыбки  - BLACK,
    Цвет льда - ICE,
    Цвет воды - WATER,
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата по x крайней левой точки
    param: cd[1] это координата по y крайней верхней точки
    param: cd[2] это модуль коэффициента увеличения
    param: cd[3] это знак коэффициента увеличения, равен +-1.
    Возможно отображение относительно вертикальной оси
    Отображается на поверхности Picture.
    """
    cd = (cd[0] / cd[2], cd[1] / abs(cd[2]), abs(cd[2]), cd[2]/abs(cd[2]))
    #УЛОВ
    fibshes(cd)
    #ЛУНКА
    pg.draw.ellipse(Picture, ICE, ((cd[0] + 260)*cd[2]*cd[3], (cd[1] + 210)*cd[2], 120*cd[2]*cd[3], 50*cd[2]))
    pg.draw.ellipse(Picture, WATER, ((cd[0] + 270)*cd[2]*cd[3], (cd[1] + 220)*cd[2], 100*cd[2]*cd[3], 40*cd[2]))
    #УДОЧКА
    pg.draw.line(Picture, BLACK, ((cd[0] + 160)*cd[2]*cd[3], (cd[1] + 200)*cd[2]),
         ((cd[0] + 310)*cd[2]*cd[3], (cd[1] - 100)*cd[2]), max(int(5*cd[2]), 1))
    #ЛЕСКА
    pg.draw.line(Picture, BLACK, ((cd[0] + 310)*cd[2]*cd[3], (cd[1] - 100)*cd[2]),
         ((cd[0] + 310)*cd[2]*cd[3], (cd[1] + 240)*cd[2]), 1)
    #BEBRA'S BODY
    whiteball((cd[0]*cd[2]*cd[3], cd[1]*cd[2], 150*cd[2]*cd[3], 300*cd[2]))
    #BEBRA'S LEG
    whiteball(((cd[0] + 70)*cd[2]*cd[3], (cd[1] + 240)*cd[2], 120*cd[2]*cd[3], 80*cd[2]))
    #BEBRA'S FOOT
    whiteball(((cd[0] + 150)*cd[2]*cd[3], (cd[1] + 290)*cd[2], 60*cd[2]*cd[3], 40*cd[2]))
    #BEBRA'S ARM
    whiteball(((cd[0] + 120)*cd[2]*cd[3], (cd[1] + 80)*cd[2], 100*cd[2]*cd[3], 60*cd[2]))
    #BEBRA'S HEAD
    whiteball(((cd[0] + 100)*cd[2]*cd[3], (cd[1] - 30)*cd[2], 100*cd[2]*cd[3], 70*cd[2]))
    #BEBRA'S EAR
    whiteball(((cd[0] + 95)*cd[2]*cd[3], (cd[1] - 24)*cd[2], 20*cd[2]*cd[3], 20*cd[2]))
    #BEBRA'S SMILE
    pg.draw.line(Picture, BLACK, ((cd[0] + 180)*cd[2]*cd[3], (cd[1] + 5)*cd[2]),
         ((cd[0] + 200)*cd[2]*cd[3], (cd[1] + 10)*cd[2]))
    #BEBRA'S NOSE
    pg.draw.ellipse(Picture, BLACK, ((cd[0] + 190)*cd[2]*cd[3], (cd[1] - 10)*cd[2], 10*cd[2]*cd[3], 10*cd[2]))
    #BEBRA'S EYE
    pg.draw.ellipse(Picture, BLACK, ((cd[0] + 120)*cd[2]*cd[3], (cd[1] - 20)*cd[2], 5*cd[2]*cd[3], 5*cd[2]))

bebr((50, 100, 1))
rect = Picture.get_rect(topleft = (Width*2, 4*Height))    
sc.blit(Picture, rect)
"""
Кладем на поверхность Picture рисунок бэбры
Прячем ее за экраном
"""

def picture(cd):
    """
    Рисует прямую бэбру с удочкой, лункой и уловом
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата центра по x
    param: cd[1] это координата центра по y
    param: cd[2] это коэффициент уменьшения размеров
    """
    scale = pg.transform.scale(Picture,
    (Picture.get_width() // cd[2], Picture.get_height() //cd[2]))
    scale_rect = scale.get_rect(center = (cd[0], cd[1]))
    sc.blit(scale, scale_rect)
    
def antipicture(cd):
    """
    Рисует отраженную бэбру с удочкой, лункой и уловом
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата центра по x
    param: cd[1] это координата центра по y
    param: cd[2] это коэффициент уменьшения размеров
    """
    Picture_mirror = pg.transform.flip(Picture, 1, 0)
    scale_mirror = pg.transform.scale(Picture_mirror,
    (Picture_mirror.get_width() // cd[2], Picture_mirror.get_height() //cd[2]))
    rect_mirror = scale_mirror.get_rect(center = (cd[0], cd[1]))
    sc.blit(scale_mirror, rect_mirror)

def galo(R):
    """
    Задаёт рисунок солнца и гало
    param: R задает радиус солнца и радиус гало
    """
    pg.draw.circle(Sun, YELLOW, [Width//8, Height//8], R)
    pg.draw.circle(Sun, YELLOW, [Width//8, Height//8], 2*R, 8)

def sun(cd):
    """
    Рисует солнце и гало
    param: cd это кортеж переменных вводимых в качестве параметров
    param: cd[0] это координата центра картики солнца и гало по x
    param: cd[1] это координата центра картики солнца и гало по y
    param: cd[2] это яркость изображения
    param: cd[3] это радиус кругов
    """
    galo(cd[3])
    for i in range(1, cd[2]):
        scale = pg.transform.scale(
        Sun, ((i+1)*Sun.get_width() // i+3, (i+1)*Sun.get_height() // i+3))
        Sun.set_alpha(20+i*2)
        rect = scale.get_rect(center = (cd[0], cd[1]))
        sc.blit(scale, rect)



sun((600, 200, 70, 40))
picture((210, 410, 2))
picture((600, 500, 1))
antipicture((900, 450, 1))


pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYUP \
                and i.key == pygame.K_f: 
            pg.display.update(rect)
 
    pg.time.delay(20)
