#!/usr/bin/python3
"""This module defines a Square class with a size and a position."""


class Square:
    """Represents a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position.

        Args:
            size (int): The length of one side of the square.
            position (tuple): The (x, y) offset used when printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after checking it is valid.

        Args:
            value (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #, shifted by its position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
