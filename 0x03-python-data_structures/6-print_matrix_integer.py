#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = '\n'.join([''.join(['{:d} '.format(item)
                  for item in row]) for row in matrix])
    print(x)
