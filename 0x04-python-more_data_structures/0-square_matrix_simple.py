#!/usr/bin/python3

def square_matrix(matrix=[]):
    squares = []
    for mat in matrix:
        squares.append([n**2 for n in mat])
    return squares
