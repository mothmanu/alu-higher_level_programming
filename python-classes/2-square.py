#!/usr/bin/python3
"""This module is for size validation"""


class Square:
    def __init__(self, __size=0):
        try:
            if __size < 0:
                raise ValueError('size must be >=0')
        except TypeError:
            print('size must be an integer')
