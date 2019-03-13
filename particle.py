from math import sin, cos
import pygame

class Particle:
    def __init__(self, x, y, screen_obj):
        self.pos = (x, y)
        self.x = x
        self.y = y
        self.offset_x = (x) * 70
        self.offset_y = (y) * 70
        self.screen = screen_obj

    def update(self, ticks):
        self.x = int(sin(ticks / (20 * sum(self.pos))) * 25 + self.offset_x)
        self.y = int(cos(ticks / (20 * sum(self.pos))) * 25 + self.offset_y)

    def show(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 2)
