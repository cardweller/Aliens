class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (150,123,182)

        #ship settings
        self.ship_speed_factor = 1.5
        