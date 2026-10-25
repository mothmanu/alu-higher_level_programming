#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            max = 0
            if v > max:
                max = k
        return max
