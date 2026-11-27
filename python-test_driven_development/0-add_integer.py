#!/usr/bin/python3
"""
This module defines the add_integer function.
It adds two numbers after casting them to integers.
Only integers and floats are accepted.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer.

    Floats are cast to integers before they are added."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
