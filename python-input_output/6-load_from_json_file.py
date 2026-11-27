#!/usr/bin/python3
"""This module defines a function that loads an object from JSON."""
import json


def load_from_json_file(filename):
    """Create and return a Python object from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
