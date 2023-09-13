#!/usr/bin/python3
"""if key in a_dictionary (will work) 
&& update updates it if it exists or 
creates the new one"""
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if i == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary.update({key : value})
    return a_dictionary
