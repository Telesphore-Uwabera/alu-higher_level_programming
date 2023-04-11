#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number and return a new matrix.

    Parameters:
    matrix (list of lists): A matrix represented as a list of lists of integers or floats.
    div (int or float): The number to divide all elements of the matrix by.

    Returns:
    list of lists: A new matrix where all elements of the input matrix are divided by div and rounded to 2 decimal places.
    """
    # Check that matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check that each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check that div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check that div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)
    
    return new_matrix
