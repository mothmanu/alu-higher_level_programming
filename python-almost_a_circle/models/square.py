#!/usr/bin/python3
"""This module defines the Square class, which inherits from Rectangle."""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square: a rectangle whose width and height are equal."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The length of each side.
            x (int): The horizontal offset used when displaying.
            y (int): The vertical offset used when displaying.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and then the height of the square to value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the square as [Square] (id) x/y - size."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square's attributes.

        Args:
            *args: In order: id, size, x, y.
            **kwargs: Attribute names mapped to new values. Skipped when
                args is given and not empty.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            pairs = zip(attrs, args)
        else:
            pairs = ((k, v) for k, v in kwargs.items() if k in attrs)
        for key, value in pairs:
            if key == "id" and value is None:
                Base.__init__(self)
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
