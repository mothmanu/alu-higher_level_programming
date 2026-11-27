#!/usr/bin/python3
"""This module defines a function that lists an object's attributes."""


def lookup(obj):
    """Return a list of the available attributes and methods of obj."""
    return dir(obj)
