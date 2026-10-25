#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    num = 0
    if ord(roman_string[0]) < ord(roman_string[1]):
        num = numerals[roman_string[1]] - numerals[roman_string[0]]
    else:
        for char in roman_string:
            num += numerals[char]
    return num
