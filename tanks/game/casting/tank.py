from turtle import position
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
    
    def __init__(self, position, size, velocity, filename, scale, rotation, image_position):
        """Constructs an instance of tank
        """
        super().__init__()
        self._body = Body(position, size, velocity)
        self._image = Image(filename, scale, rotation)
        self._image_position = image_position
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

    def get_image_position(self):
        """Gets the position of tank's image.

        Returns:
            Image: the position of tank's image.
        """
        return self._image_position

    def move_next(self):
        """Moves the tank to its next position."""
        velocity = self._body.get_velocity()
        position = self._body.get_position()
        x = position.get_x() + velocity.get_x()
        y = position.get_y() + velocity.get_y()
        new_position = Point(x, y)
        self._body.set_position(new_position)
        ix  = self._image_position.get_x() + velocity.get_x()
        iy  = self._image_position.get_y() + velocity.get_y()
        self._image_position = Point(ix, iy)

    def set_can_move(self, can_move):
        self._can_move = can_move