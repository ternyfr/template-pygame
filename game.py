import random
import time
import pygame

# переменные с размерами экрана и фпс
WIDTH = 800
HEIGHT = 800
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

img = pygame.image.load("./sunny.png")
scale = pygame.transform.scale(img, (img.get_width(),img.get_height()))
scale_rect = scale.get_rect(center=(WIDTH//2,HEIGHT//2))


omori_img = pygame.image.load("./omori.png")
scale_omori = pygame.transform.scale(omori_img, (64,64))
omori_rect = scale_omori.get_rect()
omori_rect.center = 100,100

font_style = pygame.font.SysFont("Times New Roman", 25)
fs = pygame.font.SysFont("Times New Roman", 100)
och = 0
msg = font_style.render(f"score: {och}", True, (200, 100, 100),(100, 40 ,200))
go = fs.render("ГЕЙМ ОВЕР", True, (255, 255, 255))

# pygame.time.wait(5000)

# держими всё в цикле на норм скорости
while running:
    clock.tick(FPS)
    # цветом заполняем
    screen.fill(screencolor)
    screen.blit(scale, scale_rect)
    screen.blit(scale_omori, omori_rect)
    screen.blit(msg, [20,20])

    # рисуем фигуры
    pygame.draw.rect(screen, (100,50,200), [x, y, width, height])
    # 15 это радиус.
    pygame.draw.circle(screen, (colorap), [xap, yap], 15)
    # проверяем столкновение с яблоком
    if ((x < xap+15 and xap-15 < x+ width) and (y < yap+15 and yap-15 < y+ height)):
        och = och+1
        msg = font_style.render(f"score: {och}", True, (200, 100, 100),(100, 40 ,200))
        width = width+10
        xap = random.randint(0, WIDTH)
        yap = random.randint(0, HEIGHT)
        scale_rect.center = xap, yap
        pygame.draw.circle(screen, (colorap), [xap, yap], 15)
        
        pygame.draw.rect(screen, (100,50,200), [x, y, width, height])  
    # кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = y - 15
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        y = y + 15
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x = x - 15
    if keys[pygame.K_d]:
        x = x + 15
    # проверяем столковение с границами
    if (x<0 or x > WIDTH - width):
        screen.blit(go, [100, 200])
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
        
        
    # проверяем нажатие на крестик
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()

        
pygame.quit()
