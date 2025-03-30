import pygame, time
from pygame.locals import *
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ghost = pygame.image.load("ghost.png")
background = pygame.image.load("backgroundGhost.jpg")

background = pygame.transform.scale(background, (800, 800))
wd
ghostX = 300
ghostY = 505

while ghostY < HEIGHT:
    screen.blit(background, (0, 0))
    screen.blit(ghost, (ghostX, ghostY))
    
    pygame.display.update()
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif i.type == pygame.KEYUP:
            if i.key == K_UP:
                if ghostY > 0:
                    ghostY -= 20
            elif i.key == K_DOWN:
                if ghostY < HEIGHT-200:
                    ghostY += 20
            elif i.key == K_LEFT:
                if ghostX > 0:
                    ghostX -= 20
            elif i.key == K_RIGHT:
                if ghostX < WIDTH - 200:
                    ghostX += 20
                    
    ghostY += 1
    time.sleep(0.05)                                