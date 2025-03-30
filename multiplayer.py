import pygame, random
from time import *
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 600
TITLE = "Space Shooter"
SW, SH = 50, 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)

ship1 = pygame.image.load("ship1")
ship1 = pygame.transform.rotate(pygame.transform.scale(ship1, (SW, SH)), 90)
ship2  = pygame.image.load("ship2")
ship2 = pygame.transform.rotate(pygame.transform.scale(ship2, (SW, SH)), 270)
background = pygame.transform.scale(pygame.image.load("spaceBackground"), (WIDTH, HEIGHT))

def main():
    yellowShip = pygame.Rect(100, 100, SW, SH)
    redShip = pygame.Rect(WIDTH-100, HEIGHT-100)
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, "black", BORDER)
    screen.blit(ship1, 100, 100)
    screen.blit(ship2, WIDTH-100, HEIGHT-100)
    
main()    