#!/usr/bin/python3
"""This module defines BaseGeometry with an integer validator."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name (str): The name of the value, used in error messages.
            value: The value to check.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
