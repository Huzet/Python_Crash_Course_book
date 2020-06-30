# Utilizing tutorial from Python Crash Course book written by Eric Matthes

# Alien_Invasion_From_PythonCrashCourseBook

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class for the game"""

    def __init__(self):
        """Initializes game and resources"""
        pygame.init()
        
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Starts main loop for the game"""
        while True:
            # Watches for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
             # Redraw screen
            self.screen.fill(self.bg_color)
            self.ship.blitme()

             # Make recent screen visible
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make instance run game
    ai = AlienInvasion()
    ai.run_game()