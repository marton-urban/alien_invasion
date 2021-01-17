import sys
import pygame
from settings import Settings
from ship import Ship

"""Overall class to manage game assets and behavior."""
class AlienInvasion:

    """Initialize the game, and create game resources."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    """Start the main loop for the game."""
    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    """Respond to keypresses and mouse events."""
    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                # Move the ship to the right
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

            elif event.type == pygame.KEYUP:

                # Stop moving the ship to the right
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    """Update images on the screen, and flip to the new screen."""
    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# Make a game instance, and run the game.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
