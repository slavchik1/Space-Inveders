import pygame
import settings


class Spaceship:
    def __init__(self, surface):
        self.surface = surface

    def draw(self):
        surface.blit(settings.SpaceShipImg, (settings.SpaceShipStartX, settings.SpaceShipStartY))
