#!/usr/bin/python3
"""This module defines a function that splits text after . ? and :."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    No printed line starts or ends with a space.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")
