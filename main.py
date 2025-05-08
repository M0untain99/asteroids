import pygame
from constants import *
from player import Player

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()  # Initialise PyGame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Define the screen
    clock = pygame.time.Clock()  # Game Clock for controlling fps
    dt = 0  # Delta Time
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    while True:  # Initialise Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the game
                return  # Kill the game

        screen.fill('black')  # Make the screen black
        player.draw(screen)  # Draw Player
        pygame.display.flip()  # Display the screen
        
        time_passed = clock.tick(60)  # Set FPS to 60
        dt = time_passed/1000


if __name__ == "__main__":
    main()