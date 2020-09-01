import pygame
from color import *


class WindowSize(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def initDisplay(self):
        pygame.init()

        size = self.width, self.height
        screen = pygame.display.set_mode(size)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill(black)
            pygame.display.flip()

    def returnScreen(self):
        return screen


class Ray(object):
    def __init__(self, magnitude, angle, x, y):
        self.magnitude = magnitude
        self.angle = angle
        self.x = x
        self.y = y


class Camera(object):
    def __init__(self, x, y, screen, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color

    def draw(self):
        surface.set_at((self.x, self.y), self.color)


class Obstacles(object):
    def __init__(self, x, y, type):
        pass
