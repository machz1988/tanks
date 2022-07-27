from game.casting.actor import Actor
from game.casting.label import Label

class Meter(Actor):
    """A meter for variables like tank's health or tank's shooting power
    
    The responsibility of Meter is to keep track of the variable's value
    Attributes:
        _value (integer): the variable's value
        _kind (string): the meter's kind
        _min_value (integer): the variable's min value
        _max_value (integer): the variable's max value
        _size (Point): the rectangle's size, the visible representation of the meter
    """

    def __init__(self, label, holder, value_holder, value, kind, min_value, max_value, color):
        """
            Constructor for a Meter instance
        """
        super().__init__()

        self._label = label
        self._value = value
        self._kind = kind
        self._min_value = min_value
        self._max_value = max_value
        self._holder = holder
        self._value_holder = value_holder
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

    def update_max_value(self, max_value):
        """Updates max value

        Args:
            max_value (integer): The given value.
        """
        self._max_value = max_value