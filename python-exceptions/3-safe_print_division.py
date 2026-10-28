#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You are trying to divide by 0")
    finally:
        print("{}".format(result))
        return result
