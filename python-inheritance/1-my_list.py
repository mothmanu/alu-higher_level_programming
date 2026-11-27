#!/usr/bin/python3
"""This module defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A subclass of list with a method to print its items in order."""

    def print_sorted(self):
        """Print the list sorted in ascending order without changing it."""
        print(sorted(self))
