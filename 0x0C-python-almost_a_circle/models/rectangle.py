#!/usr/bin/python3
"""Rectangle module"""

from base import Base



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
	
