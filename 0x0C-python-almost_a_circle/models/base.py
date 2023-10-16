#!/usr/bin/python3
"""base class"""
import json



class Base():
	"""Base Class for inheritance."""
	
	__nb_objects = 0

	def __init__(self, id=None):
		""" instance constructor
        """
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = self.__nb_objects
	
	@staticmethod
	def to_json_string(list_dictionaries):
		""" Write a Json file with list_objs
            Args:
                cls: class name
                list_objs: list of instances
        """
		if list_dictionaries in (None, []):
			return "[]"
		else:
			return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		""" Save the content into a JSON file"""
		save = []
		if list_objs:
			for obj in list_objs:
				save.append(obj.to_dictionary())
		with open(cls.__name__ + ".json", 'w') as file:
			file.write(Base.to_json_string(save))
	
	@staticmethod
	def from_json_string(json_string):
		""" Read a Json string and return a list of objects"""
		if json_string is None:
			return []
		return json.loads(json_string)
	
	@classmethod
	def create(cls, **dictionary):
		""" Create and set a new instance
            Args:
                **dictionary: kwargs of class
        """
		if cls.__name__ == "Rectangle":
			dummy = cls(0)
		elif cls.__name__ == "Square":
			dummy = cls(0)
		dummy.update(**dictionary)
		return dummy

	@classmethod
	def load_from_file(cls):
		""" Instantiate and return a list of
            instances from json file
        """
		inst_list = []
		try:
			with open(cls.__name__ + ".json", 'r') as file:
				data = file.read()
				list = Base.from_json_string(data)
				for kwargs in list:
					inst_list.append(cls.create(**kwargs))
				return inst_list
		except FileNotFoundError:
			return []
