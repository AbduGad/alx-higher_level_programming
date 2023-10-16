#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Class constructor
            Args:
                width: first size
                height: second size
                x: first position
                y: second position
                id: identification
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """git width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, width):
        """set width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """set x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """set y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calculates rectangle area"""
        return self.width * self.height

    def display(self):
        """ prints Rectangle instance with character # """
        print(('#' * self.width + '\n') * self.height, end="")

    def __str__(self):
        """__str__"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
            {self.width}/{self.height}"

    def display(self):
        """display"""
        print(("" + '\n') * self.y, end="")
        print(((self.x * " ") + ('#' * self.width + '\n'))
              * self.height, end="")

    def update(self, *args, **kwargs):
        """update"""
        if args:
            atr_list = ["id", "width", "height",
                        "x", "y"]
            for i, each in enumerate(args):
                setattr(self, atr_list[i], each)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
