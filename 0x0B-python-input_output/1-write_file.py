#!/usr/bin/python3
""" write to file"""


def write_file(filename="", text=""):
    """writes to a utf-8 encoded text file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)
