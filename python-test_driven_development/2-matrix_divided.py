#!/usr/bin/python3
"""This module defines a function that divides every element of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div.

    Each result is rounded to 2 decimal places.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of numbers, if the
            rows are not all the same size, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) and len(row) > 0
                    for row in matrix)):
        raise TypeError(msg)
    for row in matrix:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
