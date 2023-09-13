#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    max_key = None
    for i, j in a_dictionary.items():
        if j > max_score:
            max_key = i
            max_score = j
    return max_key
