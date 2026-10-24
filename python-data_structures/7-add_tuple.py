#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple=()
    if len(tuple_a) < 2:
        for i in range(2):
            if tuple_a[i] is None:
                tuple_a[i] = 0
    elif len(tuple_b) < 2:
        for i in range(2):
            if tuple_b[i] is None:
                   tuple_b[i] = 0
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_a[:2]
    new_tuple[0] = tuple_a[0] + tuple_b[0]
    new_tuple[1] = tuple_a[1] + tuple_b[1]
    return new_tuple
