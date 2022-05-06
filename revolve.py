from math import cos, pi, sin
import pygame as pg

class Revolve:
    def __init__(self, x, y, orbit_radius, particle_radius, color, screen):
        self.x = x
        self.y = y
        self.orbit_radius = orbit_radius
        self.particle_radius = particle_radius
        self.color = color
        self.screen = screen

        self.set_num_particles(3)
        self.orbit_thickness = 3

        self.display = True
        self.speed = 0.05

        self.angle = 0

    def set_num_particles(self, num_particles):
        self.num_particles = num_particles
        self.calculate_separation()

    def calculate_separation(self):
        self.separation = 2 * pi / self.num_particles

    def update(self):
        self.angle += self.speed
        while self.angle > 2 * pi:
            self.angle -= 2 * pi
        
    def render(self):
        if self.display:
            pg.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.orbit_radius, self.orbit_thickness)
            for i in range(self.num_particles):
                x = self.x + self.orbit_radius * cos(self.angle + i * 2 * self.separation)
                y = self.y + self.orbit_radius * sin(self.angle + i * 2 * self.separation)
                pg.draw.circle(self.screen, self.color, (int(x), int(y)), self.particle_radius)