import pygame as pg


class Highlight:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

        self.display = True

        self.highest_thickness = 5
        self.lowest_thickness = 1
        self.thickness_velocity = 0.2

        self.thickness = self.lowest_thickness

        self.screen = screen

    def update(self):
        self.thickness += self.thickness_velocity
        self.transient_radius = self.radius + self.thickness // 2
        if self.thickness > self.highest_thickness:
            self.thickness = self.highest_thickness
            self.thickness_velocity *= -1
        elif self.thickness < self.lowest_thickness:
            self.thickness = self.lowest_thickness
            self.thickness_velocity *= -1

    def render(self):
        if self.display:
            pg.draw.circle(self.screen, self.color, (self.x, self.y), self.transient_radius, int(self.thickness))