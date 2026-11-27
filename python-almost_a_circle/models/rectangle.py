#!/usr/bin/python3
"""This module defines the Rectangle class, which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a width, height, position (x, y) and id."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal offset used when displaying.
            y (int): The vertical offset used when displaying.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __validate(name, value, allow_zero):
        """Check that value is an integer within the allowed range.

        Args:
            name (str): The attribute name, used in error messages.
            value: The value to check.
            allow_zero (bool): True for x and y, which may be 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if allow_zero and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not allow_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking it is a positive integer."""
        self.__validate("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking it is a positive integer."""
        self.__validate("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Return the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x offset after checking it is an integer >= 0."""
        self.__validate("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Return the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y offset after checking it is an integer >= 0."""
        self.__validate("y", value, True)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with # characters, shifted by x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the rectangle as [Rectangle] (id) x/y - width/height."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes.

        Args:
            *args: In order: id, width, height, x, y.
            **kwargs: Attribute names mapped to new values. Skipped when
                args is given and not empty.
        """
        attrs = ["id", "width", "height", "x", "y"]
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
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
