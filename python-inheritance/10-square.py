#!/usr/bin/python3
"""This module defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize the square after validating its size.

        Args:
            size (int): The length of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
