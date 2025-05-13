from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draw the player on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    # Rotate the player
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # Move the player
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Shoot a shot
    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position[0], self.position[1])  # Create a shot object (x, y, radius)

            start = pygame.Vector2(0, 1).rotate(self.rotation)  # Set the shots starting vector with rotation
            
            shot.velocity = start * PLAYER_SHOOT_SPEED  # Calculate velocity by multiplying the vector by speed

            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Set the shot shoot_timer to the max cooldown

    # Update the position of the player
    def update(self, dt):
        keys = pygame.key.get_pressed()  # Get the keys being pressed

        if keys[pygame.K_a]:  # If the a key is pressed
            self.rotate((-dt))  # Rotate the player to the left
        if keys[pygame.K_d]:  # If the d key is pressed
            self.rotate(dt)  # Rotate the player to the right

        if keys[pygame.K_w]:  # If the w key is pressed
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:  # If the s key is pressed
            self.move(-dt)  # Move backwards

        if keys[pygame.K_SPACE]:  # If the spacebar is pressed
            self.shoot()  # Shoot

        self.shoot_timer -= dt  # Reduce the shoot shoot_timer