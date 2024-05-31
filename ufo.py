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

    def move(self):
        if self.x < settings.width - 50 and self.y == 100:
            self.x += settings.UfoSpeedInX
        elif self.y < 200 and self.x >= settings.width - 50:
            self.y += settings.UfoSpeedInY
        elif self.x > 100 and self.y >= 200:
            self.x -= settings.UfoSpeedInX
        else:
            self.y -= settings.UfoSpeedInY


    def isColided(self, x, y):
        if x >= self.x and x <= self.x + settings.UfoWidth and y >= self.y and y <= self.y + settings.UfoHeight:
            return True
