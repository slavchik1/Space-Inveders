import pygame
import sys


pygame.display.set_caption("Space Invadors")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
width = 1425
height = 750
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
