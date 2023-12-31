#!/usr/bin/python3
"""Square class"""


class Square:
    """square attr: size some attributes are protected from input. """
    def __init__(self, size=0):
        """ The __init__ method  used to initialize the object """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
