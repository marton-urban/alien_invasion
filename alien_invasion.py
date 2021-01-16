import sys
import pygame
from settings import Settings

"""Overall class to manage game assets and behavior."""
class AlienInvasion:
    """Initialize the game, and create game resources."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    """Start the main loop for the game."""
    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during eah pass through the loop.
            self.screen.fill(self.settings.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()


# Make a game instance, and run the game.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
