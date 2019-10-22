# Comp120-Contract4
# David Brown
# Last Updated: 21/10/2019.

# Pygame and sys are imported for further use in the program.
import sys
import pygame


# Pygame is initialised, all its functions are now usable.
pygame.init()
# Sets the size of the screen.
screen = pygame.display.set_mode((400, 400))
# Sets the tag on the top bar of the window to say Contract-4-Program
pygame.display.set_caption("Contract-4-Program")


# This loads in the original image and ensures that it is casted onto the screen.
def AddImage():
    entity = pygame.image.load("Ground.png").convert()
    screen.blit(entity, (0, 0))


# This function changes the colour of pixels depending on the values on line 33.
def EntityColourChanger(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r * 2), int(pixel.g * 0.1), int(pixel.b))
            )


# Main game loop, continues until the user presses the exit button.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # This calls the functions needed to change the colour of the asset and saves the picture.

    screen.fill((255, 255, 255))
    AddImage()
    EntityColourChanger(screen)
    pygame.display.flip()
    pygame.image.save(screen, 'newImage.png')

pygame.quit()
