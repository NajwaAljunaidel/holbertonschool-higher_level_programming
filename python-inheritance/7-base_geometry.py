#!/usr/bin/python3
"""Module that contains BaseGeometry class with validation."""


class BaseGeometry:
    """A geometry class with area method and integer validation."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always, as area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the value
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
