import pygame
from pygame.sprite import Sprite

"""A class to manage bullets fired from the ship"""
class Bullet(Sprite):

    """Create a bullet object at the ship's current position."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.speed = self.settings.bullet_speed
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store te bullet's position as a decimal value.
        self.y = float(self.rect.y)

    """Move the bullet up the screen."""
    def update(self):
        # Update the decimal position of the bullet.
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

    """Draw the bullet to the screen."""
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
