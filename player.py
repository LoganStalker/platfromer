import pygame
import time

from config import HEIGHT


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.gravity = 0.05
        self.vely = 0
        self.velx = 0
        self.onground = False
        self.big_before = 0

    def boost_size(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 60, 60)
        self.image = pygame.Surface((60, 60))
        self.image.fill((0, 255, 0))
        self.big_before = time.time() + 7

    def stop_boost(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))

    def update(self, left, right, up, platforms):
        if time.time() > self.big_before:
            self.stop_boost()

        if left:
            self.velx = -1
        if right:
            self.velx = 1
        if not left and not right:
            self.velx = 0

        if self.onground:
            self.vely = 0
        if not self.onground:
            self.vely += self.gravity
        if up and self.onground:
            self.vely = -4

        self.onground = False

        self.rect.x += self.velx
        self.collide_check(self.velx, 0, platforms)
        self.rect.y += self.vely
        self.collide_check(0, self.vely, platforms)

    def collide_check(self, velx, vely, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if velx > 0:
                    self.rect.right = platform.rect.left
                if velx < 0:
                    self.rect.left = platform.rect.right
                if vely > 0:
                    self.rect.bottom = platform.rect.top
                    self.onground = True
                    self.vely = 0
                if vely < 0:
                    self.rect.top = platform.rect.bottom
                    self.vely = 0
                platform.collided_with_player(self)

    def start_thorns(self):
        self.thorns_before = time.time() + 2
        self.image.fill((105, 131, 57))


