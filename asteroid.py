from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def split(self):
        self.kill()  # Remove the existing asteroid

        if self.radius < ASTEROID_MIN_RADIUS:  # If it's just a small asteroid
            return  # Do nothing

        angle = random.uniform(20, 50)  # Get a new angle for the asteroids to move at

        # Generate angles in two directions
        new_angles1 = pygame.Vector2(self.velocity).rotate(angle)
        new_angles2 = pygame.Vector2(self.velocity).rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS  # Set a smaller radius

        # Create two new asteroid objects
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)

        # Set the direction of two new asteroids
        asteroid1.velocity = new_angles1 * 1.2
        asteroid2.velocity = new_angles2 * 1.2



    # Move the asteroid forward
    def update(self, dt):
        self.position += (self.velocity * dt)