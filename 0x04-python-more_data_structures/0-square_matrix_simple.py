#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            new[i][j] = matrix[i][j] ** 2
            j += 1
        i += 1
    return new
