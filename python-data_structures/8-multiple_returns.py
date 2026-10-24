#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if sentence is None:
        first_char = None
    else:
        for char in sentence:
            new_tuple += (char, )
        first_char = new_tuple[0]
    return len(new_tuple), first_char
