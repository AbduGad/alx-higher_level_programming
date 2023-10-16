#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, size):
        """size"""
        self.width = size
        self.height = size

    def __str__(self):
        """str"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ update a class square with
            args o kwargs
            Args:
                *args: no keyworded args
                **kwargs: keyworded args
        """

        setter = ['id',
                  'size',
                  'x',
                  'y']
        if args and len(args) > 0:
            for counter, arg in enumerate(args):
                setattr(self, setter[counter], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
