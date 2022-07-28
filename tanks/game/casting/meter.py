from turtle import position, update
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.rectangle import Rectangle
from game.casting.label import Label

class Meter(Actor):
    """A meter for variables like tank's health or tank's shooting power
    
    The responsibility of Meter is to keep track of the variable's value
    Attributes:
        _label (Label): the meter's label
        _value (integer): the meter's value to keep track of
        _min_value (integer): the variable's min value
        _max_value (integer): the variable's max value
        _holder (Rectangle): a rectangular shape, the visible representation of the meter
        _value_holder (Rectangle): a rectangular shape, the visible representation of the value
        _color (Color): the color of the value holder
    """

    def __init__(self, label, holder, value, min_value, max_value, color):
        """
            Constructor for a Meter instance
        """
        super().__init__()
        self._label = label
        self._value = value
        self._min_value = min_value
        self._max_value = max_value
        self._holder = holder
        self._value_holder = Rectangle(Point(0,0), Point(0,0))
        self._update_value_holder()
        self._color = color

    def get_color(self):
        """It returns the meter's color
        Returns:
            Color: the meter's color
        """
        return self._color

    def get_value(self):
        """It returns the variable's value
        Returns:
            integer: the variable's value
        """
        return self._value
    
    def get_kind(self):
        """It returns the meter's kind
        Returns:
            string: the meter's kind
        """
        return self._kind

    def get_min_value(self):
        """It returns the variable's min value
        Returns:
            integer: the variable's min value
        """
        return self._min_value

    def get_max_value(self):
        """It returns the variable's max value
        Returns:
            integer: the variable's max value
        """
        return self._max_value

    def get_holder(self):
        """It returns the meter's holder, which its 
            the visible representation for the meter
        Returns:
            Body: the meter's holder
        """
        return self._holder

    def get_label(self):
        """It returns the meter's label
        Returns:
            Text: the meter's label
        """
        return self._label

    def get_value_holder(self):
        """It returns the meter's value holder
        Returns:
            Body: the meter's value holder
        """
        return self._value_holder

    def update_value(self, value):
        """Updates the health's value

        Args:
            value (integer): The given value.
        """
        self._value = value
        self._update_value_holder()
        
    def update_min_value(self, min_value):
        """Updates min value

        Args:
            min_value (integer): The given value.
        """
        self._max_value = min_value

    def update_max_value(self, max_value):
        """Updates max value

        Args:
            max_value (integer): The given value.
        """
        self._max_value = max_value
    
    def _update_value_holder(self):
        positionh = self._holder.get_position()
        sizeh = self._holder.get_size()
        wh = sizeh.get_x()
        hh = sizeh.get_y()
        measure = (self._max_value - self._min_value) / wh
        x = int((self._value - self._min_value) / measure)
        y = hh
        position = positionh
        size = Point(x, y)
        self._value_holder = Rectangle(position, size)