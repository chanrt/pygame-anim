from math import cos, pi, sin
from random import random

import pygame as pg


class Particle:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

        self.random_mode = True

    def start_targetting(self, target_x, target_y, time_left):
        self.random_mode = False

        self.dx = (target_x - self.x) / time_left
        self.dy = (target_y - self.y) / time_left

    def update(self):
        if self.random_mode:
            noise = 1 * random() - 0.5
            self.x += cos(self.theta + noise)
            self.y += sin(self.theta + noise)
        else:
            noise_x, noise_y = 5 * random() - 2.5, 5 * random() - 2.5
            self.x += self.dx + noise_x
            self.y += self.dy + noise_y


class DirectedExplosion:
    def __init__(self, start_x, start_y, target_x, target_y, explosion_radius, color, screen):
        self.start_x = start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y

        self.radius = explosion_radius
        self.color = color
        self.screen = screen

        self.display = True
        self.num_particles = 100
        self.max_particle_size = 5

        self.current_step = 0
        self.targeting_start = 100
        self.final_step = 200

        self.make_particles()

    def make_particles(self):
        self.particles = []

        for i in range(self.num_particles):
            theta = 2 * pi * random()
            r = self.radius * random()
            x = self.start_x + r * cos(theta)
            y = self.start_y + r * sin(theta)

            self.particles.append(Particle(x, y, theta))

    def update(self):
        for particle in self.particles:
            particle.update()

        self.current_step += 1
        if self.current_step == self.targeting_start:
            for particle in self.particles:
                particle.start_targetting(self.target_x, self.target_y, self.final_step - self.targeting_start)
        if self.current_step >= self.final_step:
            self.display = False

    def render(self):
        if self.display:
            for particle in self.particles:
                pg.draw.circle(self.screen, self.color, (particle.x, particle.y), self.max_particle_size * (1 - self.current_step / self.final_step), 0)