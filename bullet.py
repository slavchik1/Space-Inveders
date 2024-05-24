import pygame
import settings


class Bullet():
    def __init__(self, surface, x, y, belonging):
        self.surface = surface
        self.x = x
        self.y = y
        self.belonging = belonging
        if belonging == "spaceship":
            self.a = -1
        elif belonging == "ufo":
            self.a = 1

    def fly(self):
        if self.y <= settings.height:
            self.y += settings.BulletSpeed * self.a
            pygame.draw.rect(self.surface, (255, 255, 255), (self.x, self.y, settings.BulletWidth, settings.BulletHeight))
