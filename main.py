import pygame
from constants import *

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()  # Initialise PyGame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Define the screen
    
    while True:  # Initialise Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the game
                return  # Kill the game

        screen.fill('black')  # Make the screen black
        pygame.display.flip()  # Display the screen


if __name__ == "__main__":
    main()