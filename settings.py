"""A class to store all settings for Alien Invasion."""
class Settings:

    """Initialize the game's settings."""
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_color = (60, 60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3