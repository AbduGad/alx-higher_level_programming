#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # len(matrix) of an empty matrix is always 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print()
