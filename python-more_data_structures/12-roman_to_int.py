#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    num = 0
    for i in range(len(roman_string)):
        if roman_string[i] < roman_string[i+1]:
            num = numerals[roman_string[i+1]] - numerals[roman_string[i]]
        else:
            num += numerals[roman_string[i]]
    return num
