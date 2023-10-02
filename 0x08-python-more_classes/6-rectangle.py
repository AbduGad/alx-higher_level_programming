#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rectangle class with priv height and width"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """geeter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height is 0 or self.width is 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)

    def __str__(self):
        if self.width is 0 or self.height is 0:
            return ""
        str_rect = ""
        for i in range(self.height):
            str_rect += ('#' * self.width) + '\n'
        return str_rect[:-1]

    def __repr__(self):
        str_rect = "Rectangle("
        str_rect += str(self.width) + ", " + str(self.height)
        return str_rect + ')'

    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
