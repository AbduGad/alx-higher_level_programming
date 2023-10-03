#!/usr/bin/python3
def print_square(size):
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		if isinstance(size, float):
			raise TypeError("size must be an integer")
		else:
			raise ValueError("size must be >= 0")
	string = ""
	for i in range (size):
		string += '#' * size + '\n'
	print(string, end = '')
