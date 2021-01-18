import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

"""Overall class to manage game assets and behavior."""
class AlienInvasion:

    """Initialize the game, and create game resources."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    """Start the main loop for the game."""
    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    """Respond to keypresses and mouse events."""
    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """Update position of bullets and get rid of old bullets."""
    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    """Create the fleet of aliens."""
    def _create_fleet(self):
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width = alien.rect.x
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    """Create an alien and place it in the row."""
    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.x
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    """Update images on the screen, and flip to the new screen."""
    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the first row of aliens # pygame.sprite.Group.draw(self.aliens, self.screen)
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    """Create a new bullet and add it to the bullets group."""
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """Respond to keypresses."""
    def _check_keydown_events(self, event):
        # Move the ship to the left
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Move the ship to the right
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Quit the game
        elif event.key == pygame.K_q:
            sys.exit()
        # Fire a bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    """Respond to key releases."""
    def _check_keyup_events(self, event):
        # Stop moving the ship to the left
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # Stop moving the ship to the right
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


# Make a game instance, and run the game.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
