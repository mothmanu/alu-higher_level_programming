#!/usr/bin/python3
"""This module defines a Student class that can be saved and reloaded."""


class Student:
    """Represents a student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with a first name, last name and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        Args:
            attrs (list): If a list of strings, only these attributes
                are included. Otherwise all attributes are included.
        """
        if (type(attrs) is list and
                all(type(a) is str for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the student's attributes with values from a dictionary.

        Args:
            json (dict): Attribute names mapped to their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
