#!/usr/bin/python3
"""This module defines a function that turns an object into a dict."""


def class_to_json(obj):
    """Return the dictionary of obj's attributes for JSON serialization."""
    return obj.__dict__
