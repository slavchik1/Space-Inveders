import pygame
import sys
import settings
from spaceship import Spaceship
from bullet import Bullet
from ufo import Ufo


pygame.display.set_caption("Space Invadors")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
screen = pygame.display.set_mode((settings.width, settings.height))
surface = pygame.Surface((settings.width, settings.height))
Spaceship = Spaceship(surface)
Clock = pygame.time.Clock()

bullets = []
ufos = []
del_bullet_index = None
del_ufo_index = None

for i in range(10):
    ufos.append(Ufo(surface, i * 100 + 50, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(surface, Spaceship.x, Spaceship.y, "spaceship"))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Spaceship.x -= settings.SpaceShipSpeed
    elif keys[pygame.K_d]:
        Spaceship.x += settings.SpaceShipSpeed

    screen.blit(surface, (0, 0))
    pygame.display.flip()

    surface.fill((0, 0, 0))
    Spaceship.draw()

    for i in bullets:
        i.fly()

    for i in ufos:
        i.draw()
        if i.shot():
            bullets.append(Bullet(surface, i.x, i.y, "ufo"))

    def function():
        for i in range(len(ufos)):
            for j in range(len(bullets)):
                if bullets[j].belonging == "spaceship" and ufos[i].isColided(bullets[j].x, bullets[j].y):
                    return (i, j)





    Clock.tick(settings.fps)
