import pygame
import settings


class Spaceship:
    def __init__(self, surface):
        self.surface = surface
        self.x = settings.SpaceShipStartX
        self.y = settings.SpaceShipStartY

    def draw(self):
        self.surface.blit(settings.SpaceShipImg, (self.x, self.y))

    def isColided(self, x, y):
        if x >= self.x and x <= self.x + settings.UfoWidth and y >= self.y and y <= self.y + settings.UfoHeight:
            return True
