import pyray
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image

class Tank(Actor):
    """A tank entity represeting the player.

    The responsibility of Tank is to move itself.

    Attributes:
        _size (Point): the tank's size 
        _rotation (float): the tank's rotation
    """
    
    def __init__(self, position, size, velocity, filename, scale, rotation):
        """Constructs an instance of tank
        """
        super().__init__()
        self._body = Body(position, size, velocity)
        self._image = Image(filename, scale, rotation)
        self._can_move = False

    def get_body(self):
        """Gets the tank's body.

        Returns:
            Body: The tank's body.
        """
        return self._body

    def get_image(self):
        """Gets the tank's image.

        Returns:
            Image: The tank's image.
        """
        return self._image

    def move_next(self):
        """Moves the tank to its next position."""
        pass

    def set_can_move(self, can_move):
        self._can_move = can_move