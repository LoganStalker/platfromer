import pygame


class BasePlatform:
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def collided_with_player(self, player):
        pass


class Brick(BasePlatform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.image.load("images/brick.png")


class Question(BasePlatform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 1, y - 1, 52, 52)
        self.image = pygame.image.load("images/question.png")

    def collided_with_player(self, player):
        player.vely = -2
        player.onground = False


class Red(BasePlatform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 1, y - 1, 52, 52)
        self.image = pygame.Surface((52, 52))
        self.image.fill((255, 0, 0))

    def collided_with_player(self, player):
        player.boost_size()


class Portal(BasePlatform):
    def __init__(self, x, y, pos):
        self.rect = pygame.Rect(x + 12, y + 12, 25, 25)
        self.goal = pos
        self.image = pygame.Surface((50, 50))
        pygame.draw.circle(self.image, (255, 189, 46), center=(25, 25), radius=20, width=7)
        self.image.set_colorkey((0, 0, 0))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x - 12, self.rect.y - 12))

    def collided_with_player(self, player):
        player.rect.x = self.goal[0]
        player.rect.y = self.goal[1]


class FirePlatform(BasePlatform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 123, 0))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def collided_with_player(self, player):
        player.start_burn()


class FrozenPlatform(BasePlatform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.image.load("images/ice.png")

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def collided_with_player(self, player):
        player.start_iced()
