#!/usr/bin/python3
"""geometry continued """


class BaseGeometry():
    """for use with shapes. Super class.
    """

    def area(self):
        """instance method to calculate area of shape
        """
        raise Exception("area() is not implemented")
