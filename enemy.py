import pygame


class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.image = pygame.Surface((20, 20))
        self.image.fill((127, 95, 0))
        self.gravity = 0.05
        self.vely = 0
        self.velx = 1
        self.onground = False

    def update(self, platforms):
        if not self.onground:
            self.vely += self.gravity
        if self.onground:
            self.vely = 0
        self.onground = False

        self.rect.x += self.velx
        self.collide_check(self.velx, 0, platforms)
        self.rect.y += self.vely
        self.collide_check(0, int(self.vely), platforms)

    def collide_check(self, velx, vely, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if velx > 0 or velx < 0:
                    self.velx = -self.velx
                if vely > 0:
                    self.rect.bottom = platform.rect.top
                    self.onground = True
                    self.vely = 0
                if vely < 0:
                    self.rect.top = platform.rect.bottom
                    self.vely = 0
