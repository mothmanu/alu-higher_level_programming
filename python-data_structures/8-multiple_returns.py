#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    first_char = new_tuple[0]
    if sentence is None:
        first_char = None
    for char in sentence:
        new_tuple += (char, )
    return len(new_tuple), first_char
