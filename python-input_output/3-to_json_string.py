#!/usr/bin/python3
"""This module defines a function that converts an object to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of my_obj."""
    return json.dumps(my_obj)
