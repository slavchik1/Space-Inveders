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

for i in range(15):
    ufos.append(Ufo(surface, i * 90 + 50, 100))

for i in range(10):
    ufos.append(Ufo(surface, i * 90 + 300, 200))


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
        i.move()
        if i.shot():
            bullets.append(Bullet(surface, i.x, i.y, "ufo"))

    bullets_to_remove = []
    ufos_to_remove = []

    for i in range(len(ufos) - 1, -1, -1):
        for j in range(len(bullets) - 1, -1, -1):
            if bullets[j].belonging == "spaceship" and ufos[i].isColided(bullets[j].x, bullets[j].y):
                ufos_to_remove.append(i)
                bullets_to_remove.append(j)

    for i in bullets_to_remove:
        bullets.pop(i)
    for i in ufos_to_remove:
        ufos.pop(i)

    for i in range(len(bullets)):
        if bullets[i].belonging == "ufo" and Spaceship.isColided(bullets[i].x, bullets[i].y):
            pygame.quit()
            sys.exit(f"Game Over! UFOs destoyed: {25 - len(ufos)}")

    if len(ufos) == 0:
        pygame.quit()
        sys.exit("You win!")





    Clock.tick(settings.fps)
