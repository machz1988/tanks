from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
        self._health = MAXIMUM_HEALTH
        self._projectile_power = PROJECTILE_DEFAULT_POWER
        self._shooting_power = PROJECTILE_DEFAULT_V0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def add_health(self, value):
        """Adds the given value to health."""
        new = self._health + value
        if new > MAXIMUM_HEALTH:
            self._health = MAXIMUM_HEALTH 
        else:
            self._health = new

    def add_projectile_power(self, value, value_max):
        """Adds the given value to projectile power."""
        new = self._projectile_power + value
        if new > value_max:
            self._projectile_power = value_max 
        else:
            self._projectile_power = new

    def add_shooting_power(self, value, value_max):
        """Adds the given value to shooting power."""
        new = self._shooting_power + value
        if new > value_max:
            self._shooting_power = value_max 
        else:
            self._shooting_power = new

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score
    
    def get_health(self):
        """Gets the health.

        Returns:
            integer: A number representing the health.
        """
        return self._health

    def get_projectile_power(self):
        """Gets the projectile power

        Returns:
            integer: A number representing the projectile power.
        """
        return self._projectile_power

    def get_shooting_power(self):
        """Gets the shooting power

        Returns:
            integer: A number representing the shooting power.
        """
        return self._shooting_power

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1

    def lose_health(self, value):
        """Rests the given value to health."""
        new = self._health - value
        if new < 0:
            self._health = 0 
        else:
            self._health = new

    def lose_projectile_power(self, value, value_min):
        """Rests the given value to projectile power."""
        new = self._projectile_power - value
        if new < value_min:
            self._projectile_power = value_min 
        else:
            self._projectile_power = new

    def lose_shooting_power(self, value, value_min):
        """Rests the given value to shooting power."""
        new = self._shooting_power - value
        if new < value_min:
            self._shooting_power = value_min 
        else:
            self._shooting_power = new
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
        self._health = 100
        self._projectile_power = PROJECTILE_DEFAULT_POWER
        self._shooting_power = PROJECTILE_DEFAULT_V0