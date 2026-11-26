#!/usr/bin/python3
"""This module defines a Square class that can print itself."""


class Square:
    """Represents a square that stores and validates its size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after checking it is valid.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using the # character."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
