import pygame
from config import WIDTH, HEIGHT


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIDTH/2, -t+HEIGHT/2

    l = min(0, l)
    l = max(-(camera.width-WIDTH), l)
    t = max(-(camera.height-HEIGHT), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)


def camera_creator(level):
    total_level_width = len(level[0]) * 50
    total_level_height = len(level) * 50

    camera = Camera(camera_configure, total_level_width, total_level_height)
    return camera
