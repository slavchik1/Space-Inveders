import pygame
import sys
import settings
from spaceship import Spaceship


pygame.display.set_caption("Space Invadors")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
screen = pygame.display.set_mode((settings.width, settings.height))
surface = pygame.Surface((settings.width, settings.height))
Spaceship = Spaceship(surface)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(surface, (0, 0))
    pygame.display.flip()

    Spaceship.draw()
