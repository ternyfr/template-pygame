import random
import time
import pygame

# переменные с размерами экрана и фпс
WIDTH = 360
HEIGHT = 480
FPS = 30
# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# игру и экран делаем
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("my game")
clock = pygame.time.Clock()

# запускаем 
running = True

# цвет экрана
screencolor = (0, 0, 0)

# координаты и цвет яблочка
y = 0
x = 0
colorap = (255, 150, 100)
xap = 100
yap = 200
width = 50
height = 25
# держими всё в цикле на норм скорости
while running:
    clock.tick(FPS)
    # цветом заполняем
    screen.fill(screencolor)
    # рисуем фигуры
    pygame.draw.rect(screen, (100,50,200), [x, y, width, height])
    # 15 это радиус.
    pygame.draw.circle(screen, (colorap), [xap, yap], 15)
    # проверяем столкновение с яблоком
    if ((x < xap+15 and xap-15 < x+ width) and (y < yap+15 and yap-15 < y+ height)):
        xap = random.randint(0, 340)
        yap = random.randint(0, 460)
        pygame.draw.circle(screen, (colorap), [xap, yap], 15)
        width = width+10
        pygame.draw.rect(screen, (100,50,200), [x, y, width, height])  
    # кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = y - 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        y = y + 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x = x - 10
    if keys[pygame.K_d]:
        x = x + 10
    # проверяем столковение с границами
    if (x<0 or x > WIDTH - width):
        running = False
    # проверяем нажатие на крестик
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            running = False
        
    
    pygame.display.flip()
        
pygame.quit()
