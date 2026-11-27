#!/usr/bin/python3
"""This module defines a function that checks for a subclass instance."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class, not a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
