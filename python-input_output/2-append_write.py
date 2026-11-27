#!/usr/bin/python3
"""This module defines a function that appends a string to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
