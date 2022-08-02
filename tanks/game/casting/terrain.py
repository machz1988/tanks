import constants
from game.casting.actor import Actor
from game.casting.rectangle import Rectangle
from game.casting.point import Point
from game.casting.image import Image

class Terrain(Actor):
    """The playing area the tanks will have available to play against each other.
    
    The responsibility of Terrain is to place the Tanks correctly and show the play field.
    
    Attributes:
        _surface (list<Rectangle>): the list of rectangles which conforms the terrain
    """

    def __init__(self, surface, filename):
        """Constructs a new instance of Terrain"""
        super().__init__()
        self._surface = []
        self._position_tank1 = Point(0, 0)
        self._position_tank2 = Point(0, 0)
        self._image = Image(filename, 0.1)
        self._initialize_surface(surface)

    def _initialize_surface(self, surface):
        rows = len(surface)
        cols = len(surface[0])
        row_size = int(constants.SCREEN_HEIGHT / rows)
        col_size = int(constants.SCREEN_WIDTH / cols)
        
        x = 0
        for i in range(rows):
            y = 0
            for j in range(cols):
                if surface[i][j] == 1:
                    position = Point(y, x)
                    size = Point(col_size, row_size)
                    self._surface.append(Rectangle(position,size))
                elif surface[i][j] == 2:
                    self._position_tank1 = Point(y, x)
                elif surface[i][j] == 3:
                    self._position_tank2 = Point(y, x)
                y += row_size
            x += col_size  

    def get_image(self):
        """Gets the image for the terrain

        Returns:
            Image: the image for the terrain
        """
        return self._image

    def get_surface(self):
        """Gets the list of rectangles

        Returns:
            list<Rectangle>: the list of Rectangles
        """
        return self._surface
    
    def set_surface(self, surface):
        """Updates the surface to the given one.

        Args:
            surface (list<Line>): The given surface.
        """
        self._surface = surface

    def get_tank1_position(self):
        """Returns the tank1's position
        Returns:
            position (Point): the tank1's position
        """
        return self._position_tank1
        
    def get_tank2_position(self):
        """Returns the tank2's position
        Returns:
            position (Point): the tank2's position
        """
        return self._position_tank2