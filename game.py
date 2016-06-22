import pygame
from sys import exit
from pygame.locals import *










pygame.init()
screen = pygame.display.set_mode((1000, 500), 0, 32) 
pygame.display.set_caption("Snake!")

background =  pygame.Surface((1000,500),flags=SRCALPHA, depth=32)

background.fill((100,100,100))


while True:
    screen.fill((0,255,100))
##    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    
