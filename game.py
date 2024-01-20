import random
import time
import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("my game")
clock = pygame.time.Clock()

running = True
red = 0
green = 0
blue = 0
isredmax = False
isgr = False
isbl = False

y = 0
x = 0
colorap = (255, 150, 100)
xap = 0
yap = 0
#460 340
while running:
    clock.tick(FPS)
    screen.fill((red, green, blue))
    # if isgr == True:
    #     blue = blue + 1
    #     if blue == 255:
    #         blue = 0
    #         ifbl = True
    # else:
    #     if isredmax == True:
    #         green = green + 1
    #         if green == 255:
    #             green = 0
    #             isgr = True
    #     else:
    #         red = red+1
    #     if red == 255:
    #         red = 0
    #         isredmax = True

    #проверка нажатия на клавиши движения
    pygame.draw.rect(screen, (100,50,200), [x, y, 25, 25])
    pygame.draw.circle(screen, (colorap), [xap, yap], 10)
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y - 10
            if event.key == pygame.K_a:
                x = x - 10
            if event.key == pygame.K_s:
                y = y + 10
                print(y)
            if event.key == pygame.K_d:
                x = x + 10
                print(x)
            if event.key == pygame.K_SPACE:
                print("space nachal")
    pygame.display.flip()
        
pygame.quit()
