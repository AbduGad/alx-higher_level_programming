#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # len(matrix) of an empty matrix is always 1
    if len(matrix) == 1:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=' ')
            print("{:d}".format(matrix[i][j + 1]))
