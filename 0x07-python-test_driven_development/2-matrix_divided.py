#!/usr/bin/python3
def matrix_divided(matrix, div):
	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div is 0:
		raise ZeroDivisionError("division by zero")
	if not isinstance(matrix, list):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	else:
		new = []
		length = -1
		for row in range(len(matrix)):
			if not isinstance(matrix[row], list):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
			else:
				if length is not -1 and length is not len(matrix[row]):
					raise TypeError("Each row of the matrix must have the same size")
				else:
					length = len(matrix[row])
				temp = []
				for colomun in range(len(matrix[row])):
					if not isinstance(matrix[row][colomun], (int, float)):
						raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
					temp.append(round(matrix[row][colomun] / div, 2))
				new.append(temp)
		return new
