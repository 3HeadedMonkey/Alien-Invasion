class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialise statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #High Score should never be reset
        self.high_score = self.read_high_score()

        # Start Alien Invasion in an inanctive state
        self.game_active = False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        with open('docs\high_score.txt', 'r') as file:
            self.saved_score = int(file.read())
            return self.saved_score

    def write_high_score(self):
        with open('docs\high_score.txt', 'w') as file:
            file.write(str(self.high_score))
