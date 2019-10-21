import sys

import pygame

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Contract-4-Program")

xPosBox = 200
yPosBox = 200

pygame.draw.rect(screen, WHITE, (xPosBox, yPosBox, 20, 20))
pygame.display.update()

while 1:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
