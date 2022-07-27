from game.casting.point import Point


class Circle:
    """A circular shape."""

    def __init__(self, center, radius, color):
        """Constructs a new Circle."""
        self._center = center
        self._radius = radius
        self._color = color

    def get_center(self):
        """Gets the center point of the circle.
        
        Returns:
            Point: An instance of Point containing the center coordinates.
        """
        return self._center

    def get_radius(self):
        """Gets the radius of the circle.
        
        Returns:
            float: A number which represents the radius of the circle
        """
        return self._radius
    
    def get_color(self):
        """Gets the color of the circle.
        
        Returns:
            Color: An instance of Color containing the circle's color
        """
        return self._color