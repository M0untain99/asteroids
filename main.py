import pygame
import sys
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()  # Initialise PyGame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Define the screen
    clock = pygame.time.Clock()  # Game Clock for controlling fps
    dt = 0  # Delta Time

    asteroids = pygame.sprite.Group()  # Create a group for all the asteroids
    updateable = pygame.sprite.Group()  # Create a group for all updateable entities
    drawable = pygame.sprite.Group()  # Create a group for all drawable sprites
    shots = pygame.sprite.Group()  # Create a group for all shots

    Player.containers = (updateable, drawable)  # Add the updateable and drawable containers to the Player class
    Shot.containers = (updateable, drawable)  # Add the updateable and drawable containers to the Shot class
    Asteroid.containers = (asteroids, updateable, drawable)  # Add the containers to the Asteroid class
    AsteroidField.containers = (updateable)  # Add the updateable container to the AsteroidField class

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))  # Create a player object
    asteroid_field = AsteroidField()  # Create the asteroid field
    
    while True:  # Initialise Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the game
                return  # Kill the game

        updateable.update(dt)  # Update all the entities in the updateable group

        for asteroid in asteroids:  # For every asteroid
            if asteroid.collision_check(player):  # If it's collided with the player
                print('Game over!')
                sys.exit()  # Close the game

        screen.fill('black')  # Make the screen black

        for sprite in drawable:  # For every drawable entity
            sprite.draw(screen)  # Draw the entity

        player.draw(screen)  # Draw Player
        pygame.display.flip()  # Display the screen
        
        time_passed = clock.tick(60)  # Set FPS to 60
        dt = time_passed/1000


if __name__ == "__main__":
    main()