import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Contract-4-Program")
screen.fill((255, 255, 255))


def addImage():
    entity = pygame.image.load("Ground.png").convert_alpha()
    screen.blit(entity, (0, 0))
    pygame.display.flip()


def entityColourChanger(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r * 0.5), pixel.g, pixel.b)
            )


while 1:
    addImage()
    pygame.display.flip()
    entityColourChanger(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
