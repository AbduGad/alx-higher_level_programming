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

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
