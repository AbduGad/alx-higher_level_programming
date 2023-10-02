#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rectangle class with priv height and width"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        """geeter for width"""
        return self.__width

    def height(self):
        """getter for height"""
        return self.__height

    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
