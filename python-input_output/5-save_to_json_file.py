#!/usr/bin/python3
"""This module defines a function that saves an object as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write my_obj to a text file using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
