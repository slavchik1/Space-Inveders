import settings
from random import randint


class Ufo:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def draw(self):
        self.surface.blit(settings.UfoImg, (self.x, self.y))

    def shot(self):
        if randint(1, settings.UfoShotChancePerFrame) == 1:
            return True

