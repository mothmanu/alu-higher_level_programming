#!/usr/bin/python3
"""This module defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")
