#!/bin/python3

# Utilizing tutorial from Python Crash Course book written by Eric Matthes

# Alien_Invasion_From_PythonCrashCourseBook

import sys
import pygame

class AlienInvasion:
    """Overall class for the game"""

    def __init__(self):
        """Initializes game and resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starts main loop for the game"""
        while True:
            # Watches for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make recent screen visible

if __name__ == '__main__':
    # Make instance run game
    ai = AlienInvasion
    ai.run_game