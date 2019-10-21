# Comp120-Contract4
# David Brown
# Last Updated: 21/10/2019.

# Pygame and sys are imported for further use in the program.
import sys

import pygame


pygame.init()   # Pygame is initialised, all its functions are now usable.
screen = pygame.display.set_mode((400, 400))    # Sets the size of the screen.
pygame.display.set_caption("Contract-4-Program")


def addImage():
    entity = pygame.image.load("Ground.png").convert()
    screen.blit(entity, (0, 0))


def entityColourChanger(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r), int(pixel.g * 0.1), int(pixel.b))
            )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    addImage()
    entityColourChanger(screen)
    pygame.display.flip()

pygame.quit()