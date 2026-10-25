#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best_score = None
        for k, v in a_dictionary.items():
            if best_score is None or v > a_dictionary[best_score]:
                best_score = k
        return best_score
