import pygame

from player import Player
from platforms import Brick, Question, Red, Portal, FirePlatform
from config import WIDTH, HEIGHT
from enemy import Enemy
from camera import camera_creator

window = pygame.display.set_mode((WIDTH, HEIGHT))

hero = Player(150, HEIGHT-150)

run = True
right, left, up = False, False, False
clock = pygame.time.Clock()

level = [
    '-    ------  -------------------',
    '--   -                     0   -',
    '------                         -',
    '-          ??                  -',
    '-                              -',
    '-                          --  -',
    '-                -             -',
    '-   ~~                         -',
    '-                              -',
    '-     +   ---?       -??-      -',
    '-                              -',
    '-               --             -',
    '-                              -',
    '-   fff                  --    -',
    '-           ---                -',
    '-       ~          -        -- -',
    '-                          -   -',
    '-                 ???-   -     -',
    '-  -?-                         -',
    '-       ---                    -',
    '-                        ?-    -',
    '-                              -',
    '--------------------------------',
]
platforms = []
x, y = 0, 0
portals = []

enemy = None
for row in level:
    for sim in row:
        if sim == '-':
            brick = Brick(x, y)
            platforms.append(brick)
        if sim == "?":
            question = Question(x, y)
            platforms.append(question)
        if sim == "~":
            red = Red(x, y)
            platforms.append(red)
        if sim == "0":
            portal = Portal(x, y, (155, -100))
            portals.append(portal)
        if sim == "+":
            enemy = Enemy(x, y)
        if sim == "f":
            fire = FirePlatform(x, y)
            platforms.append(fire)
        x += 50
    y += 50
    x = 0

camera = camera_creator(level)
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                up = True
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                up = False
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
    clock.tick(250)
    window.fill((50, 50, 50))

    enemy.update(platforms)
    hero.update(left, right, up, platforms)
    for p in platforms:
        # p.draw(window)
        window.blit(p.image, camera.apply(p))

    for p in portals:
        if p.rect.colliderect(hero.rect):
            p.collided_with_player(hero)
        # p.draw(window)
        window.blit(p.image, camera.apply(p))

    # window.blit(hero.image, (hero.rect.x, hero.rect.y))
    # window.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
    window.blit(hero.image, camera.apply(hero))
    window.blit(enemy.image, camera.apply(enemy))

    camera.update(hero)

    pygame.display.flip()
pygame.quit()
